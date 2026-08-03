"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : ligne_commande.py
Description : Lignes des commandes fournisseurs
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


class LigneCommande(BaseModel):

    __tablename__ = "ligne_commandes"

    commande_id: Mapped[int] = mapped_column(
        ForeignKey("commandes.id"),
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

    commande = relationship(
        "Commande",
        back_populates="lignes",
    )

    produit = relationship(
        "Produit",
        back_populates="lignes_commande",
    )