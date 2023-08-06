from __future__ import annotations

import collections as co
import functools as ft
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Sequence,
    Tuple,
    Type,
    TYPE_CHECKING,
    TypeVar,
    Union,
)

import sympy
import torch


ExprType = TypeVar("ExprType", bound=sympy.Expr)
T = TypeVar("T")

if TYPE_CHECKING:
    # Because there are methods of our class objects below called `sympy` that
    # implicitly override the `sympy` name in the global namespace while defining other
    # methods, our type checker needs to know that we're referring to the sympy module
    # in our type annotations.
    import sympy as sympy_


def _reduce(fn: Callable[..., T]) -> Callable[..., T]:
    def fn_(*args: Any) -> T:
        return ft.reduce(fn, args)

    return fn_


def _I(*args: Any) -> torch.Tensor:
    return torch.tensor(1j)


_global_func_lookup: Dict[
    Union[Type[sympy.Basic], Callable[..., Any]], Callable[..., torch.Tensor]
] = {
    sympy.Mul: _reduce(torch.mul),
    sympy.Add: _reduce(torch.add),
    sympy.div: torch.div,
    sympy.Abs: torch.abs,
    sympy.sign: torch.sign,
    # Note: May raise error for ints.
    sympy.ceiling: torch.ceil,
    sympy.floor: torch.floor,
    sympy.log: torch.log,
    sympy.exp: torch.exp,
    sympy.sqrt: torch.sqrt,
    sympy.cos: torch.cos,
    sympy.acos: torch.acos,
    sympy.sin: torch.sin,
    sympy.asin: torch.asin,
    sympy.tan: torch.tan,
    sympy.atan: torch.atan,
    sympy.atan2: torch.atan2,
    # Note: May give NaN for complex results.
    sympy.cosh: torch.cosh,
    sympy.acosh: torch.acosh,
    sympy.sinh: torch.sinh,
    sympy.asinh: torch.asinh,
    sympy.tanh: torch.tanh,
    sympy.atanh: torch.atanh,
    sympy.Pow: torch.pow,
    sympy.re: torch.real,
    sympy.im: torch.imag,
    sympy.arg: torch.angle,
    # Note: May raise error for ints and complexes
    sympy.erf: torch.erf,
    sympy.loggamma: torch.lgamma,
    sympy.Eq: torch.eq,
    sympy.Ne: torch.ne,
    sympy.StrictGreaterThan: torch.gt,
    sympy.StrictLessThan: torch.lt,
    sympy.LessThan: torch.le,
    sympy.GreaterThan: torch.ge,
    sympy.And: torch.logical_and,
    sympy.Or: torch.logical_or,
    sympy.Not: torch.logical_not,
    sympy.Max: torch.max,
    sympy.Min: torch.min,
    # Matrices
    sympy.MatAdd: torch.add,
    sympy.HadamardProduct: torch.mul,
    sympy.Trace: torch.trace,
    # Note: May raise error for integer matrices.
    sympy.Determinant: torch.det,
    sympy.core.numbers.ImaginaryUnit: _I,
    sympy.conjugate: torch.conj,
}

number_symbols = [cls for cls in sympy.NumberSymbol.__subclasses__()]


def number_symbol_to_torch(symbol: sympy.NumberSymbol, *args: Any) -> torch.Tensor:
    return torch.tensor(float(symbol))


_global_func_lookup.update(
    {s: ft.partial(number_symbol_to_torch, s()) for s in number_symbols}
)


class _Node(torch.nn.Module, Generic[ExprType]):
    def __init__(
        self,
        *,
        expr: ExprType,
        _memodict: Dict[sympy.Basic, torch.nn.Module],
        _func_lookup,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self._sympy_func: Type[ExprType] = expr.func

        self._torch_func: Callable[..., torch.Tensor]
        self._args: Union[
            torch.nn.ModuleList,
            Tuple[Callable[[Dict[str, torch.Tensor]], torch.Tensor], ...],
        ]
        self._value: Any

        if issubclass(expr.func, sympy.Float):
            self._value = torch.nn.Parameter(torch.tensor(float(expr)))
            self._torch_func = lambda: self._value
            self._args = ()
        elif issubclass(expr.func, sympy.Integer):
            self._value = torch.tensor(int(expr))
            self._torch_func = lambda: self._value
            self._args = ()
        elif issubclass(expr.func, sympy.Rational):
            self._numerator: torch.Tensor
            self._denominator: torch.Tensor
            assert isinstance(expr, sympy.Rational)
            self.register_buffer(
                "_numerator", torch.tensor(expr.p, dtype=torch.get_default_dtype())
            )
            self.register_buffer(
                "_denominator", torch.tensor(expr.q, dtype=torch.get_default_dtype())
            )
            self._torch_func = lambda: self._numerator / self._denominator
            self._args = ()
        elif issubclass(expr.func, sympy.UnevaluatedExpr):
            if len(expr.args) != 1 or not issubclass(expr.args[0].func, sympy.Float):
                raise ValueError("UnevaluatedExpr should only be used to wrap floats.")
            assert isinstance(expr.args[0], sympy.Float)
            self.register_buffer("_value", torch.tensor(float(expr.args[0])))
            self._torch_func = lambda: self._value
            self._args = ()
        elif issubclass(expr.func, sympy.Symbol):
            assert isinstance(expr, sympy.Symbol)
            self._name = expr.name
            self._torch_func = lambda value: value
            self._args = ((lambda memodict: memodict[expr.name]),)
        else:
            self._torch_func = _func_lookup[expr.func]
            args: List[torch.nn.Module] = []
            for arg in expr.args:
                try:
                    arg_ = _memodict[arg]
                except KeyError:
                    arg_ = type(self)(
                        expr=arg,  # type: ignore
                        _memodict=_memodict,
                        _func_lookup=_func_lookup,
                        **kwargs,
                    )
                    _memodict[arg] = arg_
                args.append(arg_)
            self._args = torch.nn.ModuleList(args)

    def sympy(self, _memodict: Dict[_Node, sympy_.Expr]) -> ExprType:
        if issubclass(self._sympy_func, sympy.Float):
            assert isinstance(self._value, torch.nn.Parameter)
            return self._sympy_func(self._value.item())
        elif issubclass(self._sympy_func, sympy.UnevaluatedExpr):
            assert isinstance(self._value, torch.Tensor)
            return self._sympy_func(self._value.item())
        elif issubclass(
            self._sympy_func,
            (type(sympy.S.NegativeOne), type(sympy.S.One), type(sympy.S.Zero)),
        ):
            return self._sympy_func()
        elif issubclass(self._sympy_func, sympy.Integer):
            return self._sympy_func(self._value)
        elif issubclass(self._sympy_func, sympy.Rational):
            if issubclass(self._sympy_func, type(sympy.S.Half)):
                return sympy.S.Half
            else:
                return self._sympy_func(
                    self._numerator.item(), self._denominator.item()
                )
        elif issubclass(self._sympy_func, sympy.Symbol):
            return self._sympy_func(self._name)
        elif issubclass(self._sympy_func, sympy.core.numbers.ImaginaryUnit):
            return sympy.I
        elif issubclass(self._sympy_func, sympy.core.numbers.NumberSymbol):
            return self._sympy_func()
        else:
            if issubclass(self._sympy_func, (sympy.Min, sympy.Max)):
                evaluate = False
            else:
                evaluate = True
            args = []
            for arg in self._args:
                assert isinstance(arg, _Node)
                try:
                    arg_ = _memodict[arg]
                except KeyError:
                    arg_ = arg.sympy(_memodict)
                    _memodict[arg] = arg_
                args.append(arg_)
            return self._sympy_func(*args, evaluate=evaluate)  # type: ignore

    def forward(self, memodict) -> torch.Tensor:
        args = []
        for arg in self._args:
            try:
                arg_ = memodict[arg]
            except KeyError:
                arg_ = arg(memodict)
                memodict[arg] = arg_
            args.append(arg_)
        return self._torch_func(*args)


class SymPyModule(torch.nn.Module):
    def __init__(self, *, expressions, extra_funcs=None, **kwargs):
        super().__init__(**kwargs)

        expressions = tuple(expressions)

        if extra_funcs is None:
            extra_funcs = {}
        _func_lookup = co.ChainMap(_global_func_lookup, extra_funcs)

        _memodict = {}
        self._nodes: Sequence[_Node] = torch.nn.ModuleList(  # type: ignore
            [
                _Node(expr=expr, _memodict=_memodict, _func_lookup=_func_lookup)
                for expr in expressions
            ]
        )
        self._expressions_string = str(expressions)

    def __repr__(self):
        return f"{type(self).__name__}(expressions={self._expressions_string})"

    def sympy(self) -> List[sympy.Expr]:
        _memodict: Dict[_Node, sympy.Expr] = {}
        return [node.sympy(_memodict) for node in self._nodes]

    def forward(self, **symbols: Any) -> torch.Tensor:
        out = [node(symbols) for node in self._nodes]
        out = torch.broadcast_tensors(*out)
        return torch.stack(out, dim=-1)
