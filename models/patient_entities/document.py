"""
OptiManager Pro
----------------
Entité : PatientDocument
"""

from __future__ import annotations

from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientDocument(BaseModel):
    """
    Document associé à un patient.
    """

    __tablename__ = "patient_documents"

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

    nom_fichier: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    chemin: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    mime_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    taille: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    date_document: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    patient = relationship(
        "Patient",
        back_populates="documents",
    )

    def __repr__(self) -> str:
        return (
            f"PatientDocument("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"type='{self.type}', "
            f"nom_fichier='{self.nom_fichier}')"
        )