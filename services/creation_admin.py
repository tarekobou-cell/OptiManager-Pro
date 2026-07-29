from sqlalchemy.orm import Session

from database import SessionLocal
from models.utilisateur import Utilisateur

from utils.securite import crypter_mot_de_passe


def creer_admin():

    db: Session = SessionLocal()

    admin_existe = db.query(Utilisateur).filter(
        Utilisateur.login == "admin"
    ).first()


    if not admin_existe:

        admin = Utilisateur(
            nom="Administrateur",
            prenom="Principal",
            login="admin",
            mot_de_passe=crypter_mot_de_passe(
                "admin123"
            ),
            role="Administrateur"
        )

        db.add(admin)
        db.commit()

        print("Compte administrateur créé")


    db.close()