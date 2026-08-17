"""
OptiManager Pro
----------------
Entité : PatientPhoto
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientPhoto(BaseModel):
    """
    Photo associée à un patient.
    """

    __tablename__ = "patient_photos"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    chemin: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    prise_le: Mapped[datetime | None] = mapped_column(
        nullable=True,
    )

    patient = relationship(
        "Patient",
        back_populates="photos",
    )

    def __repr__(self) -> str:
        return (
            f"PatientPhoto("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"type='{self.type}', "
            f"chemin='{self.chemin}')"
        )