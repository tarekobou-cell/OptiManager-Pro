"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : mouvement_stock.py
Description : Historique des mouvements de stock
=========================================================
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import TypeMouvementStock
from models.base import BaseModel


class MouvementStock(BaseModel):
    """
    Historique des mouvements de stock.
    """

    __tablename__ = "mouvements_stock"

    produit_id: Mapped[int] = mapped_column(
        ForeignKey("produits.id"),
        nullable=False,
        index=True,
    )

    date_mouvement: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
        index=True,
    )

    type_mouvement: Mapped[TypeMouvementStock] = mapped_column(
        Enum(TypeMouvementStock),
        nullable=False,
    )

    quantite: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    motif: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    produit = relationship(
        "Produit",
        back_populates="mouvements_stock",
    )