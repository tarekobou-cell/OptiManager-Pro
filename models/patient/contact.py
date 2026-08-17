"""
OptiManager Pro
----------------
Entité : PatientContact
"""

from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientContact(BaseModel):
    """
    Contact associé à un patient.

    Exemples :
    - parent
    - tuteur légal
    - conjoint
    - contact d'urgence
    - autre
    """

    __tablename__ = "patient_contacts"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    prenom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    relation: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    telephone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
        index=True,
    )

    telephone_secondaire: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    adresse: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    contact_principal: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    contact_urgence: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    patient = relationship(
        "Patient",
        back_populates="contacts",
    )

    def __repr__(self) -> str:
        return (
            f"PatientContact("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"nom='{self.nom}', "
            f"prenom='{self.prenom}', "
            f"relation='{self.relation}')"
        )