import pytest

from app.operations.factory import get_operation, normalize_calculation_type


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("Add", "add"),
        ("addition", "add"),
        ("+", "add"),
        ("Sub", "sub"),
        ("subtract", "sub"),
        ("-", "sub"),
        ("Multiply", "multiply"),
        ("multiplication", "multiply"),
        ("*", "multiply"),
        ("Divide", "divide"),
        ("division", "divide"),
        ("/", "divide"),
    ],
)
def test_normalize_calculation_type(raw, expected):
    assert normalize_calculation_type(raw) == expected


def test_normalize_calculation_type_invalid():
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        normalize_calculation_type("modulus")


def test_normalize_calculation_type_requires_string():
    with pytest.raises(ValueError, match="type must be a string"):
        normalize_calculation_type(None)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "type_,a,b,expected",
    [
        ("add", 10, 5, 15),
        ("sub", 10, 5, 5),
        ("multiply", 10, 5, 50),
        ("divide", 10, 2, 5),
    ],
)
def test_get_operation_executes(type_, a, b, expected):
    op = get_operation(type_)
    assert op(a, b) == expected
