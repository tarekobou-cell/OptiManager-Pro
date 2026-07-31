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
            .order_by(Patient.nom)
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
            .order_by(Patient.nom)
            .all()
        )

    finally:

        db.close()


# ==================================================
# Ajouter un patient
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

            nom=nom,

            prenom=prenom,

            telephone=telephone,

            date_naissance=date_naissance,

            adresse=adresse,

            notes=notes

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
# Détail d'un patient
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
# Modifier
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

        patient = db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

        if patient is None:

            return None

        patient.nom = nom
        patient.prenom = prenom
        patient.telephone = telephone
        patient.date_naissance = date_naissance
        patient.adresse = adresse
        patient.notes = notes

        db.commit()

        db.refresh(patient)

        return patient

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


# ==================================================
# Supprimer
# ==================================================

def supprimer_patient(patient_id):

    db = SessionLocal()

    try:

        patient = db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

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