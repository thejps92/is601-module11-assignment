import pytest

from app.auth.security import hash_password, verify_password


def test_hash_password_not_equal_to_plaintext():
    password = "SuperSecret123"
    password_hash = hash_password(password)
    assert password_hash != password


def test_verify_password_accepts_correct_password():
    password = "SuperSecret123"
    password_hash = hash_password(password)
    assert verify_password(password, password_hash) is True


def test_verify_password_rejects_incorrect_password():
    password_hash = hash_password("SuperSecret123")
    assert verify_password("wrong-password", password_hash) is False
