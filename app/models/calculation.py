from __future__ import annotations

import uuid

from sqlalchemy import CheckConstraint, Column, Float, String, Uuid

from app.database import Base
from app.operations.factory import get_operation, normalize_calculation_type


class Calculation(Base):
    __tablename__ = "calculations"

    __table_args__ = (
        CheckConstraint(
            "type IN ('add', 'sub', 'multiply', 'divide')",
            name="ck_calculation_type",
        ),
        CheckConstraint(
            "NOT (type = 'divide' AND b = 0)",
            name="ck_calculation_no_divide_by_zero",
        ),
    )

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(String(20), nullable=False, index=True)
    result = Column(Float, nullable=True)

    @classmethod
    def create(cls, *, a: float, b: float, type: str) -> "Calculation":
        canonical_type = normalize_calculation_type(type)
        operation = get_operation(canonical_type)
        result = operation(a, b)
        return cls(a=a, b=b, type=canonical_type, result=result)

    def compute_result(self) -> float:
        operation = get_operation(self.type)
        return operation(self.a, self.b)
