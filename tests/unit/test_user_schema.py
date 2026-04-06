import pytest
from pydantic import ValidationError

from app.schemas.user import UserCreate, UserRead


def test_user_create_validates_email():
    with pytest.raises(ValidationError):
        UserCreate(username="alice", email="not-an-email", password="Password123")


def test_user_create_requires_min_password_length():
    with pytest.raises(ValidationError):
        UserCreate(username="alice", email="alice@example.com", password="123")


def test_user_read_omits_password_hash():
    schema_fields = set(UserRead.model_fields.keys())
    assert "password_hash" not in schema_fields
    assert "password" not in schema_fields
