from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database import Base


class Consultation(Base):

    __tablename__ = "consultations"

    # ==================================================
    # Clé primaire
    # ==================================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # ==================================================
    # Patient
    # ==================================================

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
        index=True,
    )

    # ==================================================
    # Consultation
    # ==================================================

    date_consultation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    motif: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    observations: Mapped[str] = mapped_column(
        String(1000),
        nullable=True,
    )

    # ==================================================
    # Relations
    # ==================================================

    patient = relationship(
        "Patient",
        back_populates="consultations",
    )

    prescription = relationship(
        "Prescription",
        back_populates="consultation",
        uselist=False,
        cascade="all, delete-orphan",
    )