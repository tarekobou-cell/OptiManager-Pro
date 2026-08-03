"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : prescription.py
Description : Modèle Prescription
=========================================================
"""

from sqlalchemy import (
    Boolean,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import TypeVerre
from models.base import BaseModel


class Prescription(BaseModel):
    """
    Prescription optique.
    """

    __tablename__ = "prescriptions"

    consultation_id: Mapped[int] = mapped_column(
        ForeignKey("consultations.id"),
        unique=True,
        nullable=False,
        index=True,
    )

    # ==========================================
    # Œil droit
    # ==========================================

    od_sphere: Mapped[float | None] = mapped_column(Float)

    od_cylindre: Mapped[float | None] = mapped_column(Float)

    od_axe: Mapped[int | None] = mapped_column(Integer)

    od_addition: Mapped[float | None] = mapped_column(Float)

    od_prisme: Mapped[float | None] = mapped_column(Float)

    # ==========================================
    # Œil gauche
    # ==========================================

    og_sphere: Mapped[float | None] = mapped_column(Float)

    og_cylindre: Mapped[float | None] = mapped_column(Float)

    og_axe: Mapped[int | None] = mapped_column(Integer)

    og_addition: Mapped[float | None] = mapped_column(Float)

    og_prisme: Mapped[float | None] = mapped_column(Float)

    # ==========================================
    # Mesures
    # ==========================================

    distance_pupillaire: Mapped[float | None] = mapped_column(
        Float
    )

    hauteur_montage: Mapped[float | None] = mapped_column(
        Float
    )

    # ==========================================
    # Verres
    # ==========================================

    type_verre: Mapped[TypeVerre | None] = mapped_column(
        Enum(TypeVerre),
        nullable=True,
    )

    indice: Mapped[str | None] = mapped_column(
        String(20)
    )

    traitement: Mapped[str | None] = mapped_column(
        String(100)
    )

    teinte: Mapped[str | None] = mapped_column(
        String(100)
    )

    photochromique: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    blue_cut: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    polarisant: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    remarques: Mapped[str | None] = mapped_column(
        Text
    )

    # ==========================================
    # Relation
    # ==========================================

    consultation = relationship(
        "Consultation",
        back_populates="prescription",
    )