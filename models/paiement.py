"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : paiement.py
Description : Paiement d'une vente
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
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import ModePaiement
from models.base import BaseModel


class Paiement(BaseModel):
    """
    Paiement d'une vente.
    """

    __tablename__ = "paiements"

    vente_id: Mapped[int] = mapped_column(
        ForeignKey("ventes.id"),
        nullable=False,
        index=True,
    )

    date_paiement: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    mode: Mapped[ModePaiement] = mapped_column(
        Enum(ModePaiement),
        nullable=False,
    )

    montant: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    reference: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    vente = relationship(
        "Vente",
        back_populates="paiements",
    )