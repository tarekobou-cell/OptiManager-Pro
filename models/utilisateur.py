"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : utilisateur.py
Description : Modèle Utilisateur
=========================================================
"""

from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import RoleUtilisateur
from models.base import BaseModel


class Utilisateur(BaseModel):
    """
    Utilisateur du logiciel.
    """

    __tablename__ = "utilisateurs"

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    prenom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    login: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    mot_de_passe: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[RoleUtilisateur] = mapped_column(
        Enum(RoleUtilisateur),
        nullable=False,
    )

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    derniere_connexion: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    consultations = relationship(
        "Consultation",
        back_populates="utilisateur",
    )

    ventes = relationship(
        "Vente",
        back_populates="utilisateur",
    )