from database import SessionLocal
from models.consultation import Consultation


def creer_consultation(patient_id, motif=None, observations=None):

    db = SessionLocal()

    try:
        consultation = Consultation(
            patient_id=patient_id,
            motif=motif,
            observations=observations
        )

        db.add(consultation)
        db.commit()
        db.refresh(consultation)

        return consultation

    finally:
        db.close()


def liste_consultations_patient(patient_id):

    db = SessionLocal()

    try:
        return (
            db.query(Consultation)
            .filter(
                Consultation.patient_id == patient_id
            )
            .all()
        )

    finally:
        db.close()