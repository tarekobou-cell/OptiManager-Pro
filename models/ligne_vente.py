"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : ligne_vente.py
Description : Ligne de vente
=========================================================
"""

from decimal import Decimal

from sqlalchemy import (
    ForeignKey,
    Integer,
    Numeric,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import BaseModel


class LigneVente(BaseModel):
    """
    Ligne d'une vente.
    """

    __tablename__ = "ligne_ventes"

    vente_id: Mapped[int] = mapped_column(
        ForeignKey("ventes.id"),
        nullable=False,
        index=True,
    )

    produit_id: Mapped[int] = mapped_column(
        ForeignKey("produits.id"),
        nullable=False,
        index=True,
    )

    quantite: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    prix_unitaire: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    remise: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    vente = relationship(
        "Vente",
        back_populates="lignes",
    )

    produit = relationship(
        "Produit",
        back_populates="lignes_vente",
    )