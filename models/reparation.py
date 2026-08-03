"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : reparation.py
Description : Réparation
=========================================================
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import TypeReparation
from models.base import BaseModel


class Reparation(BaseModel):
    """
    Réparation d'un équipement optique.
    """

    __tablename__ = "reparations"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
        index=True,
    )

    produit_id: Mapped[int | None] = mapped_column(
        ForeignKey("produits.id"),
        nullable=True,
        index=True,
    )

    date_entree: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    date_sortie: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    type_reparation: Mapped[TypeReparation] = mapped_column(
        Enum(TypeReparation),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    statut: Mapped[str] = mapped_column(
        String(50),
        default="En attente",
        nullable=False,
    )

    cout: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    patient = relationship(
        "Patient",
        back_populates="reparations",
    )

    produit = relationship(
        "Produit",
        back_populates="reparations",
    )