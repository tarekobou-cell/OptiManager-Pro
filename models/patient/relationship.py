"""
OptiManager Pro
----------------
Entité : PatientRelationship
"""

from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientRelationship(BaseModel):
    """
    Relation entre deux patients.

    Exemples :
    - parent / enfant
    - tuteur légal
    - conjoint
    - autre relation familiale
    """

    __tablename__ = "patient_relationships"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    related_patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    relation: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    responsable_legal: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    patient = relationship(
        "Patient",
        foreign_keys=[patient_id],
        back_populates="relationships",
    )

    related_patient = relationship(
        "Patient",
        foreign_keys=[related_patient_id],
    )

    def __repr__(self) -> str:
        return (
            f"PatientRelationship("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"related_patient_id={self.related_patient_id}, "
            f"relation='{self.relation}')"
        )