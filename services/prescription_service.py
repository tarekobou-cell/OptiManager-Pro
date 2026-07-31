from database import SessionLocal
from models.prescription import Prescription


def creer_prescription(
    consultation_id,
    od_sphere=None,
    od_cylindre=None,
    od_axe=None,
    og_sphere=None,
    og_cylindre=None,
    og_axe=None,
    addition=None,
    notes=None
):

    db = SessionLocal()

    try:
        prescription = Prescription(
            consultation_id=consultation_id,
            od_sphere=od_sphere,
            od_cylindre=od_cylindre,
            od_axe=od_axe,
            og_sphere=og_sphere,
            og_cylindre=og_cylindre,
            og_axe=og_axe,
            addition=addition,
            notes=notes
        )

        db.add(prescription)
        db.commit()
        db.refresh(prescription)

        return prescription

    finally:
        db.close()


def obtenir_prescription(consultation_id):

    db = SessionLocal()

    try:
        return (
            db.query(Prescription)
            .filter(
                Prescription.consultation_id == consultation_id
            )
            .first()
        )

    finally:
        db.close()