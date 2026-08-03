"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : utilisateur_repository.py
Description : Repository des utilisateurs.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from sqlalchemy.orm import Session

from models.utilisateur import Utilisateur
from repositories.base_repository import BaseRepository


class UtilisateurRepository(BaseRepository[Utilisateur]):
    """
    Repository dédié aux utilisateurs.
    """

    def __init__(self, session: Session):
        super().__init__(
    session,
    Utilisateur,
)

    def rechercher_par_login(self, login: str) -> Utilisateur | None:
        """
        Recherche un utilisateur par son login.
        """

        return (
            self.session.query(Utilisateur)
            .filter(Utilisateur.login == login)
            .first()
        )

    def utilisateur_existe(self, login: str) -> bool:
        """
        Vérifie si un utilisateur existe.
        """

        return self.rechercher_par_login(login) is not None