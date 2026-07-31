from __future__ import annotations

from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Prescription(Base):

    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    consultation_id: Mapped[int] = mapped_column(
        ForeignKey("consultations.id"),
        nullable=False,
        unique=True
    )

    # Œil droit
    od_sphere: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    od_cylindre: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    od_axe: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    # Œil gauche
    og_sphere: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    og_cylindre: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    og_axe: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    addition: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    notes: Mapped[str] = mapped_column(
        String(500),
        nullable=True
    )


    consultation = relationship(
        "Consultation",
        back_populates="prescription"
    )