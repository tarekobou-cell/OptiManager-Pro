from datetime import datetime

from sqlalchemy import Integer, Float, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Vente(Base):

    __tablename__ = "ventes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    client_nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    total: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    date_vente: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    lignes = relationship(
        "LigneVente",
        back_populates="vente",
        cascade="all, delete"
    )
    