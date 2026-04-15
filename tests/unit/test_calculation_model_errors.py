import pytest

from app.models.calculation import Calculation


def test_calculation_compute_result_invalid_type_raises():
    calc = Calculation(a=1, b=2, type="modulus", result=None)
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        calc.compute_result()
