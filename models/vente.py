"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : vente.py
Description : Vente
=========================================================
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Numeric,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import BaseModel


class Vente(BaseModel):

    __tablename__ = "ventes"

    patient_id: Mapped[int | None] = mapped_column(
        ForeignKey("patients.id"),
        nullable=True,
        index=True,
    )

    utilisateur_id: Mapped[int | None] = mapped_column(
        ForeignKey("utilisateurs.id"),
        nullable=True,
        index=True,
    )

    date_vente: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
        index=True,
    )

    total_ht: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    remise: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    total_ttc: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    patient = relationship(
        "Patient",
        back_populates="ventes",
    )

    utilisateur = relationship(
        "Utilisateur",
        back_populates="ventes",
    )

    lignes = relationship(
        "LigneVente",
        back_populates="vente",
        cascade="all, delete-orphan",
    )

    paiements = relationship(
        "Paiement",
        back_populates="vente",
        cascade="all, delete-orphan",
    )