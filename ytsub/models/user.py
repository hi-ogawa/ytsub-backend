from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.sql.functions import current_timestamp

from .base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, nullable=False)
    password_digest = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=current_timestamp(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        onupdate=datetime.now,
        nullable=False,
    )

    __table_args__ = tuple([UniqueConstraint("username")])
