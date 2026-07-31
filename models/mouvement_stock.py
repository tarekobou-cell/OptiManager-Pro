from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class MouvementStock(Base):

    __tablename__ = "mouvements_stock"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    produit_id: Mapped[int] = mapped_column(
        ForeignKey("produits.id"),
        nullable=False
    )

    type_mouvement: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    # ENTREE / SORTIE

    quantite: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    date_mouvement: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    observation: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )