"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : produit.py
Description : Modèle Produit
=========================================================
"""

from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import TypeProduit
from models.base import BaseModel


class Produit(BaseModel):
    """
    Produit du magasin.
    """

    __tablename__ = "produits"

    reference: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    code_barres: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True,
        index=True,
    )

    designation: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )

    categorie: Mapped[TypeProduit] = mapped_column(
        Enum(TypeProduit),
        nullable=False,
    )

    marque: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    fournisseur_id: Mapped[int | None] = mapped_column(
        ForeignKey("fournisseurs.id"),
        nullable=True,
        index=True,
    )

    prix_achat: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    prix_vente: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    stock: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    stock_minimum: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ==========================================
    # Relations
    # ==========================================

    fournisseur = relationship(
        "Fournisseur",
        back_populates="produits",
    )

    mouvements_stock = relationship(
        "MouvementStock",
        back_populates="produit",
        cascade="all, delete-orphan",
    )

    lignes_vente = relationship(
        "LigneVente",
        back_populates="produit",
    )

    lignes_commande = relationship(
        "LigneCommande",
        back_populates="produit",
    )

    reparations = relationship(
        "Reparation",
        back_populates="produit",
    )