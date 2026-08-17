"""
OptiManager Pro
----------------
Entité : PatientInsurance
"""

from __future__ import annotations

from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientInsurance(BaseModel):
    """
    Couverture d'assurance d'un patient.
    """

    __tablename__ = "patient_insurances"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    organisme: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    numero_assure: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    numero_contrat: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    type_couverture: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    date_debut: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    date_fin: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    observations: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    patient = relationship(
        "Patient",
        back_populates="insurances",
    )

    def __repr__(self) -> str:
        return (
            f"PatientInsurance("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"organisme='{self.organisme}', "
            f"numero_assure='{self.numero_assure}')"
        )