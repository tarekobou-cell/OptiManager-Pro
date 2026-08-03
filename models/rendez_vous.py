"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : rendez_vous.py
Description : Modèle Rendez-vous
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from config.constantes import StatutRendezVous
from models.base import BaseModel


class RendezVous(BaseModel):
    """
    Rendez-vous d'un patient.
    """

    __tablename__ = "rendez_vous"

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
        index=True,
    )

    date_heure: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        index=True,
    )

    motif: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    commentaire: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    statut: Mapped[StatutRendezVous] = mapped_column(
        Enum(StatutRendezVous),
        default=StatutRendezVous.PREVU,
        nullable=False,
    )

    # =====================================================
    # Relations
    # =====================================================

    patient = relationship(
        "Patient",
        back_populates="rendez_vous",
    )