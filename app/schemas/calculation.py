from __future__ import annotations

from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from app.operations.factory import normalize_calculation_type


class CalculationType(str, Enum):
    ADD = "add"
    SUB = "sub"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


class CalculationCreate(BaseModel):
    a: float = Field(..., description="Left operand")
    b: float = Field(..., description="Right operand")
    type: CalculationType = Field(..., description="Add, Sub, Multiply, or Divide")

    @field_validator("type", mode="before")
    @classmethod
    def normalize_type(cls, v):
        return normalize_calculation_type(v)

    @model_validator(mode="after")
    def validate_divide_by_zero(self) -> "CalculationCreate":
        if self.type == CalculationType.DIVIDE and self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self

    model_config = ConfigDict(from_attributes=True)


class CalculationRead(BaseModel):
    id: UUID
    a: float
    b: float
    type: CalculationType
    result: float | None = None

    model_config = ConfigDict(from_attributes=True)
