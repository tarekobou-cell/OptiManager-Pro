from database import SessionLocal

from models.rendez_vous import RendezVous


def creer_rendez_vous(
    patient_id,
    date_heure,
    motif
):

    db = SessionLocal()

    try:

        rdv = RendezVous(
            patient_id=patient_id,
            date_heure=date_heure,
            motif=motif,
            statut="Prévu"
        )

        db.add(rdv)
        db.commit()
        db.refresh(rdv)

        return rdv

    except Exception as e:

        db.rollback()
        raise e

    finally:

        db.close()



def liste_rendez_vous():

    db = SessionLocal()

    try:

        return db.query(RendezVous).all()

    finally:

        db.close()



def modifier_statut(rdv_id, statut):

    db = SessionLocal()

    try:

        rdv = db.query(RendezVous).filter(
            RendezVous.id == rdv_id
        ).first()

        if rdv:

            rdv.statut = statut
            db.commit()

        return rdv

    finally:

        db.close()