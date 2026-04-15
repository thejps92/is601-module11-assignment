from __future__ import annotations

from collections.abc import Callable

from app.operations import add, divide, multiply, subtract


_ALLOWED_TYPES = {"add", "sub", "multiply", "divide"}

_TYPE_ALIASES: dict[str, str] = {
    "add": "add",
    "addition": "add",
    "+": "add",
    "sub": "sub",
    "subtract": "sub",
    "subtraction": "sub",
    "-": "sub",
    "multiply": "multiply",
    "multiplication": "multiply",
    "mul": "multiply",
    "*": "multiply",
    "divide": "divide",
    "division": "divide",
    "div": "divide",
    "/": "divide",
}


def normalize_calculation_type(value: str) -> str:
    if not isinstance(value, str):
        raise ValueError("type must be a string")

    normalized = value.strip().lower()
    canonical = _TYPE_ALIASES.get(normalized)
    if not canonical or canonical not in _ALLOWED_TYPES:
        raise ValueError(f"Unsupported calculation type: {value}")
    return canonical


def get_operation(calculation_type: str) -> Callable[[float, float], float]:
    canonical = normalize_calculation_type(calculation_type)
    operations: dict[str, Callable[[float, float], float]] = {
        "add": add,
        "sub": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    return operations[canonical]
