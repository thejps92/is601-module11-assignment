import pytest
from sqlalchemy.exc import IntegrityError

from app.models.calculation import Calculation


def test_insert_and_read_calculation(db_session):
    calc = Calculation.create(a=10, b=5, type="Add")
    db_session.add(calc)
    db_session.commit()
    db_session.refresh(calc)

    assert calc.id is not None
    assert calc.a == 10
    assert calc.b == 5
    assert calc.type == "add"
    assert calc.result == 15


def test_db_rejects_invalid_type(db_session):
    calc = Calculation(a=1, b=2, type="modulus", result=None)
    db_session.add(calc)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_db_rejects_divide_by_zero(db_session):
    calc = Calculation(a=10, b=0, type="divide", result=None)
    db_session.add(calc)
    with pytest.raises(IntegrityError):
        db_session.commit()
