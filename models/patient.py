"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : patient.py
Description : Modèle Patient
=========================================================
"""

from datetime import date

from sqlalchemy import (
    Boolean,
    Date,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import BaseModel


class Patient(BaseModel):
    """
    Dossier administratif d'un patient.
    """

    __tablename__ = "patients"

    numero_dossier: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=False,
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
    )

    prenom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    telephone: Mapped[str] = mapped_column(
        String(20),
        index=True,
        nullable=False,
    )

    date_naissance: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    adresse: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        index=True,
        nullable=True,
    )

    profession: Mapped[str | None] = mapped_column(
        String(100),
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

    # =====================================================
    # Relations
    # =====================================================
    contacts = relationship(
        "PatientContact",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    addresses = relationship(
        "PatientAddress",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    relationships = relationship(
        "PatientRelationship",
        foreign_keys="PatientRelationship.patient_id",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    insurances = relationship(
        "PatientInsurance",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    documents = relationship(
        "PatientDocument",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    photos = relationship(
        "PatientPhoto",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    alerts = relationship(
        "PatientAlert",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    tags = relationship(
        "PatientTag",
        back_populates="patient",
        cascade="all, delete-orphan",
    )
    consultations = relationship(
        "Consultation",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    rendez_vous = relationship(
        "RendezVous",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    ventes = relationship(
        "Vente",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    reparations = relationship(
        "Reparation",
        back_populates="patient",
        cascade="all, delete-orphan",
    )