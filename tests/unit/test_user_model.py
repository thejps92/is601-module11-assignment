from __future__ import annotations

from app.models.user import User


def test_user_create_hashes_and_verify_works():
    user = User.create(username="alice", email="alice@example.com", password="Password123")
    assert user.password_hash != "Password123"
    assert user.verify("Password123") is True
    assert user.verify("wrong-password") is False
