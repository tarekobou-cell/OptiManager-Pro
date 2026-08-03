"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : commande.py
Description : Commande fournisseur
=========================================================
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import EtatCommande
from models.base import BaseModel


class Commande(BaseModel):
    """
    Commande passée à un fournisseur.
    """

    __tablename__ = "commandes"

    fournisseur_id: Mapped[int] = mapped_column(
        ForeignKey("fournisseurs.id"),
        nullable=False,
        index=True,
    )

    date_commande: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
        index=True,
    )

    statut: Mapped[EtatCommande] = mapped_column(
        Enum(EtatCommande),
        default=EtatCommande.EN_ATTENTE,
        nullable=False,
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False,
    )

    fournisseur = relationship(
        "Fournisseur",
        back_populates="commandes",
    )

    lignes = relationship(
        "LigneCommande",
        back_populates="commande",
        cascade="all, delete-orphan",
    )