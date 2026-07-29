from database import SessionLocal

from models.patient import Patient


def ajouter_patient(
    nom,
    prenom,
    telephone,
    date_naissance,
    adresse,
    date_visite,
    od_sphere,
    od_cylindre,
    od_axe,
    og_sphere,
    og_cylindre,
    og_axe,
    type_verre,
    traitement,
    notes
):

    db = SessionLocal()


    patient = Patient(

        nom=nom,
        prenom=prenom,
        telephone=telephone,

        date_naissance=date_naissance,
        adresse=adresse,

        date_derniere_visite=date_visite,

        od_sphere=od_sphere,
        od_cylindre=od_cylindre,
        od_axe=od_axe,

        og_sphere=og_sphere,
        og_cylindre=og_cylindre,
        og_axe=og_axe,

        type_verre=type_verre,
        traitement_verre=traitement,

        notes=notes
    )


    db.add(patient)

    db.commit()

    db.refresh(patient)

    db.close()


    return patient