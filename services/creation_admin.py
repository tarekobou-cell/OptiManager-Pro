"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : creation_admin.py
Description : Création automatique du compte administrateur.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.1.0
=========================================================
"""

from sqlalchemy.orm import Session

from config.constantes import RoleUtilisateur
from database import SessionLocal
from models.utilisateur import Utilisateur
from repositories.utilisateur_repository import UtilisateurRepository
from utils.securite import crypter_mot_de_passe


def creer_admin() -> None:
    """
    Crée automatiquement le compte administrateur
    s'il n'existe pas.
    """

    session: Session = SessionLocal()
    repository = UtilisateurRepository(session)

    try:

        admin = repository.rechercher_par_login("admin")

        if admin is None:

            repository.ajouter(

                Utilisateur(
                    nom="Administrateur",
                    prenom="Principal",
                    login="admin",
                    mot_de_passe=crypter_mot_de_passe("admin123"),
                    role=RoleUtilisateur.ADMIN,
                )

            )

            print("✅ Compte administrateur créé")

    except Exception as erreur:

        session.rollback()

        print(f"Erreur création administrateur : {erreur}")

        raise

    finally:

        session.close()