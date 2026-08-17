"""
OptiManager Pro
----------------
Entité : PatientTag
"""

from __future__ import annotations

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class PatientTag(BaseModel):
    """
    Tag associé à un patient.
    """

    __tablename__ = "patient_tags"

    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "tag",
            name="uq_patient_tag",
        ),
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    tag: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    patient = relationship(
        "Patient",
        back_populates="tags",
    )

    def __repr__(self) -> str:
        return (
            f"PatientTag("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"tag='{self.tag}')"
        )