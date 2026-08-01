from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    Float,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database import Base


class Patient(Base):

    __tablename__ = "patients"

    # ==========================
    # Identité
    # ==========================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )

    prenom: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    telephone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True
    )

    date_naissance: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )

    adresse: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    date_derniere_visite: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )

    # ==========================
    # Correction
    # ==========================

    od_sphere: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    od_cylindre: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    od_axe: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    og_sphere: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    og_cylindre: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    og_axe: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    type_verre: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    traitement_verre: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    notes: Mapped[str] = mapped_column(
        String(500),
        nullable=True
    )

    # ==========================
    # Audit
    # ==========================

    actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

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

    # ==========================
    # Relations
    # ==========================

    consultations = relationship(
        "Consultation",
        back_populates="patient"
    )

    rendez_vous = relationship(
        "RendezVous",
        back_populates="patient"
    )