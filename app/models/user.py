from __future__ import annotations

from datetime import datetime
import uuid

from sqlalchemy import Column, DateTime, String, Uuid

from app.auth.security import hash_password, verify_password
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    @classmethod
    def create(cls, *, username: str, email: str, password: str) -> "User":
        return cls(username=username, email=email, password_hash=hash_password(password))

    def verify(self, password: str) -> bool:
        return verify_password(password, self.password_hash)
