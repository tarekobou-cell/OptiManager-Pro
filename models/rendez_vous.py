from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class RendezVous(Base):

    __tablename__ = "rendez_vous"


    id = Column(
        Integer,
        primary_key=True
    )


    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )


    date_heure = Column(
        DateTime,
        nullable=False
    )


    motif = Column(
        String,
        nullable=False
    )


    statut = Column(
        String,
        default="Prévu"
    )


    patient = relationship(
        "Patient",
        back_populates="rendez_vous"
    )