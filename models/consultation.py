from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

from models.prescription import Prescription


class Consultation(Base):
    __tablename__ = "consultations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False
    )

    date_consultation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    motif: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    observations: Mapped[str] = mapped_column(
        String(1000),
        nullable=True
    )

    patient = relationship(
    "Patient",
    back_populates="consultations",
    foreign_keys=[patient_id]
)

    prescription = relationship(
        "Prescription",
        back_populates="consultation",
        uselist=False,
        cascade="all, delete-orphan"
    )