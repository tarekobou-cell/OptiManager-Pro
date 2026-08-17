"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : consultation.py
Description : Modèle Consultation
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import BaseModel


class Consultation(BaseModel):
    """
    Consultation d'un patient.
    """

    __tablename__ = "consultations"

    # =====================================================
    # Informations générales
    # =====================================================

    patient_id: Mapped[int] = mapped_column(
        ForeignKey(
            "patients.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    utilisateur_id: Mapped[int | None] = mapped_column(
    ForeignKey(
        "utilisateurs.id",
        ondelete="SET NULL",
    ),
    nullable=True,
    index=True,
)

    date_consultation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    motif: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    observations: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =====================================================
    # Relation Patient
    # =====================================================

    patient = relationship(
        "Patient",
        back_populates="consultations",
    )
    # =====================================================
    # Réfraction - Œil droit (OD)
    # =====================================================

    sphere_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cylindre_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    axe_od: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    addition_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # =====================================================
    # Réfraction - Œil gauche (OG)
    # =====================================================

    sphere_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cylindre_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    axe_og: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    addition_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # =====================================================
    # Écart pupillaire (PD)
    # =====================================================

    ecart_pupillaire_loin: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    ecart_pupillaire_pres: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )
    # =====================================================
    # Acuité visuelle
    # =====================================================

    acuite_loin_od: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    acuite_loin_og: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    acuite_pres_od: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    acuite_pres_og: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    # =====================================================
    # Kératométrie
    # =====================================================

    k1_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    k2_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    k1_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    k2_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # =====================================================
    # Tonométrie
    # =====================================================

    tonometrie_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    tonometrie_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # =====================================================
    # Diagnostic
    # =====================================================

    diagnostic: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    traitement: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    recommandations: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    prochain_controle: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )
    # =====================================================
    # Relations
    # =====================================================

    prescription = relationship(
        "Prescription",
        back_populates="consultation",
        uselist=False,
        cascade="all, delete-orphan",
    )

    utilisateur = relationship(
    "Utilisateur",
    back_populates="consultations",
)
    # =====================================================
    # Représentation
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"Consultation("
            f"id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"date='{self.date_consultation:%d/%m/%Y %H:%M}')"
        )
    # =====================================================
    # Informations professionnelles
    # =====================================================

    type_consultation: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    dominance_oculaire: Mapped[str | None] = mapped_column(
        String(2),
        nullable=True,
    )

    # =====================================================
    # Réfraction objective
    # =====================================================

    sphere_obj_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cylindre_obj_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    axe_obj_od: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    sphere_obj_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cylindre_obj_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    axe_obj_og: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    # =====================================================
    # Réfraction subjective
    # =====================================================

    sphere_subj_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cylindre_subj_od: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    axe_subj_od: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    sphere_subj_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cylindre_subj_og: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    axe_subj_og: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    # =====================================================
    # Prescription des verres
    # =====================================================

    type_verre: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    traitement_verre: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    materiau_verre: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    indice_verre: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    commentaires_verres: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )