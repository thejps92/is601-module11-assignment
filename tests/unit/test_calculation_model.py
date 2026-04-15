import pytest

from app.models.calculation import Calculation


def test_calculation_create_stores_canonical_type_and_result():
    calc = Calculation.create(a=10, b=5, type="Add")
    assert calc.type == "add"
    assert calc.result == 15


def test_calculation_create_invalid_type_raises():
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        Calculation.create(a=1, b=2, type="modulus")


def test_calculation_compute_result_computes_on_demand():
    calc = Calculation(a=10, b=2, type="divide", result=None)
    assert calc.compute_result() == 5
