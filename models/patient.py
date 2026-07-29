from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Patient(Base):

    __tablename__ = "patients"


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


    telephone: Mapped[str] = mapped_column(
        String(20)
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


    # Correction œil droit
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


    # Correction œil gauche
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


    date_creation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )