from database import SessionLocal

from models.patient import Patient


# ==================================================
# Liste des patients
# ==================================================

def liste_patients():

    db = SessionLocal()

    try:

        return (
            db.query(Patient)
            .order_by(Patient.nom.asc())
            .all()
        )

    finally:

        db.close()


# ==================================================
# Recherche
# ==================================================

def rechercher_patients(texte):

    db = SessionLocal()

    try:

        return (
            db.query(Patient)
            .filter(
                Patient.nom.ilike(f"%{texte}%")
                |
                Patient.prenom.ilike(f"%{texte}%")
                |
                Patient.telephone.ilike(f"%{texte}%")
            )
            .order_by(Patient.nom.asc())
            .all()
        )

    finally:

        db.close()


# ==================================================
# Détail
# ==================================================

def detail_patient(patient_id):

    db = SessionLocal()

    try:

        return (
            db.query(Patient)
            .filter(Patient.id == patient_id)
            .first()
        )

    finally:

        db.close()


# ==================================================
# Création
# ==================================================

def creer_patient(

    nom,
    prenom,
    telephone,
    date_naissance="",
    adresse="",
    notes=""

):

    db = SessionLocal()

    try:

        patient = Patient(

            nom=nom.strip(),

            prenom=prenom.strip(),

            telephone=telephone.strip(),

            date_naissance=date_naissance.strip(),

            adresse=adresse.strip(),

            notes=notes.strip()

        )

        db.add(patient)

        db.commit()

        db.refresh(patient)

        return patient

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


# ==================================================
# Modification
# ==================================================

def modifier_patient(

    patient_id,

    nom,
    prenom,
    telephone,

    date_naissance,
    adresse,
    notes

):

    db = SessionLocal()

    try:

        patient = (
            db.query(Patient)
            .filter(Patient.id == patient_id)
            .first()
        )

        if patient is None:

            return None

        patient.nom = nom.strip()
        patient.prenom = prenom.strip()
        patient.telephone = telephone.strip()
        patient.date_naissance = date_naissance.strip()
        patient.adresse = adresse.strip()
        patient.notes = notes.strip()

        db.commit()

        db.refresh(patient)

        return patient

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


# ==================================================
# Suppression
# ==================================================

def supprimer_patient(patient_id):

    db = SessionLocal()

    try:

        patient = (
            db.query(Patient)
            .filter(Patient.id == patient_id)
            .first()
        )

        if patient is None:

            return False

        db.delete(patient)

        db.commit()

        return True

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()