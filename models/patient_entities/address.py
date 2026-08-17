"""
OptiManager Pro
----------------
Entité : PatientAddress
"""

from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientAddress(BaseModel):
    """
    Adresse associée à un patient.
    """

    __tablename__ = "patient_addresses"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    adresse: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    ville: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    wilaya: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    code_postal: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    pays: Mapped[str] = mapped_column(
        String(100),
        default="Algérie",
        nullable=False,
    )

    principale: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    patient = relationship(
        "Patient",
        back_populates="addresses",
    )

    def __repr__(self) -> str:
        return (
            f"PatientAddress("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"type='{self.type}', "
            f"ville='{self.ville}')"
        )