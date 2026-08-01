from database import SessionLocal

from models.consultation import Consultation


# ==================================================
# Liste des consultations
# ==================================================

def liste_consultations():

    db = SessionLocal()

    try:

        return (
            db.query(Consultation)
            .order_by(
                Consultation.date_consultation.desc()
            )
            .all()
        )

    finally:

        db.close()


# ==================================================
# Liste des consultations d'un patient
# ==================================================

def consultations_patient(patient_id):

    db = SessionLocal()

    try:

        return (
            db.query(Consultation)
            .filter(
                Consultation.patient_id == patient_id
            )
            .order_by(
                Consultation.date_consultation.desc()
            )
            .all()
        )

    finally:

        db.close()


# ==================================================
# Détail d'une consultation
# ==================================================

def detail_consultation(consultation_id):

    db = SessionLocal()

    try:

        return (
            db.query(Consultation)
            .filter(
                Consultation.id == consultation_id
            )
            .first()
        )

    finally:

        db.close()


# ==================================================
# Création
# ==================================================

def creer_consultation(

    patient_id,
    motif="",
    observations=""

):

    db = SessionLocal()

    try:

        consultation = Consultation(

            patient_id=patient_id,

            motif=motif.strip(),

            observations=observations.strip()

        )

        db.add(consultation)

        db.commit()

        db.refresh(consultation)

        return consultation

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


# ==================================================
# Modification
# ==================================================

def modifier_consultation(

    consultation_id,

    motif,

    observations

):

    db = SessionLocal()

    try:

        consultation = (
            db.query(Consultation)
            .filter(
                Consultation.id == consultation_id
            )
            .first()
        )

        if consultation is None:

            return None

        consultation.motif = motif.strip()

        consultation.observations = observations.strip()

        db.commit()

        db.refresh(consultation)

        return consultation

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


# ==================================================
# Suppression
# ==================================================

def supprimer_consultation(consultation_id):

    db = SessionLocal()

    try:

        consultation = (
            db.query(Consultation)
            .filter(
                Consultation.id == consultation_id
            )
            .first()
        )

        if consultation is None:

            return False

        db.delete(consultation)

        db.commit()

        return True

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()