from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nom: Mapped[str] = mapped_column(
        String(100)
    )

    prenom: Mapped[str] = mapped_column(
        String(100)
    )

    login: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    mot_de_passe: Mapped[str] = mapped_column(
        String(255)
    )

    role: Mapped[str] = mapped_column(
        String(50)
    )

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    date_creation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )