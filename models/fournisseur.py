"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : fournisseur.py
Description : Modèle Fournisseur
=========================================================
"""

from sqlalchemy import (
    Boolean,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import BaseModel


class Fournisseur(BaseModel):
    """
    Fournisseur du magasin.
    """

    __tablename__ = "fournisseurs"

    raison_sociale: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    contact: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    telephone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
        index=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        index=True,
    )

    adresse: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ==========================================
    # Relations
    # ==========================================

    produits = relationship(
        "Produit",
        back_populates="fournisseur",
    )

    commandes = relationship(
        "Commande",
        back_populates="fournisseur",
        cascade="all, delete-orphan",
    )