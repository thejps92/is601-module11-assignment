import pytest
from pydantic import ValidationError

from app.schemas.calculation import CalculationCreate, CalculationType


def test_calculation_create_valid_addition():
    calc = CalculationCreate(a=10, b=5, type="Add")
    assert calc.type == CalculationType.ADD


def test_calculation_create_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=5, type="modulus")


def test_calculation_create_divide_by_zero_rejected():
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(a=10, b=0, type="Divide")

    assert "Cannot divide by zero" in str(exc_info.value)
