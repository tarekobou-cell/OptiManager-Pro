"""
OptiManager Pro
----------------
Entité : PatientAlert
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientAlert(BaseModel):
    """
    Alerte associée à un patient.
    """

    __tablename__ = "patient_alerts"

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

    titre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    niveau: Mapped[str] = mapped_column(
        String(30),
        default="INFO",
        nullable=False,
        index=True,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )

    date_debut: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    date_fin: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    patient = relationship(
        "Patient",
        back_populates="alerts",
    )

    def __repr__(self) -> str:
        return (
            f"PatientAlert("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"type='{self.type}', "
            f"niveau='{self.niveau}', "
            f"active={self.active})"
        )