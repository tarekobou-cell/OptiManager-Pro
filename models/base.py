"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : base.py
Description : Classe de base commune à tous les modèles.
=========================================================
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import DateTime
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    """
    Base SQLAlchemy.
    """
    pass


class BaseModel(Base):
    """
    Classe de base commune à tous les modèles.
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    date_creation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    date_modification: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self) -> str:
        valeurs = ", ".join(
            f"{c.name}={getattr(self, c.name)!r}"
            for c in self.__table__.columns
        )
        return f"{self.__class__.__name__}({valeurs})"