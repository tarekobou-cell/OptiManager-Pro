from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Utilisateur(Base):

    __tablename__ = "utilisateurs"

    # ==========================
    # Clé primaire
    # ==========================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # ==========================
    # Informations personnelles
    # ==========================

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    prenom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # ==========================
    # Authentification
    # ==========================

    login: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False
    )

    mot_de_passe: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # ==========================
    # Autorisations
    # ==========================

    role: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="OPTICIEN"
    )

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    # ==========================
    # Audit
    # ==========================

    date_creation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False
    )

    date_modification: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False
    )

    dernier_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )