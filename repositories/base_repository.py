"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : base_repository.py
Description : Repository générique.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from typing import Generic
from typing import TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """
    Repository générique.

    Fournit toutes les opérations CRUD communes.
    """

    def __init__(
        self,
        session: Session,
        model: type[T],
    ) -> None:

        self.session = session
        self.model = model

    # =====================================================
    # CREATE
    # =====================================================

    def ajouter(
        self,
        objet: T,
    ) -> T:

        self.session.add(objet)

        self.session.commit()

        self.session.refresh(objet)

        return objet

    # =====================================================
    # READ
    # =====================================================

    def rechercher_par_id(
        self,
        identifiant: int,
    ) -> T | None:

        return self.session.get(
            self.model,
            identifiant,
        )

    def rechercher_tous(self) -> list[T]:

        return (
            self.session.query(self.model)
            .all()
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def sauvegarder(self) -> None:

        self.session.commit()

    # =====================================================
    # DELETE
    # =====================================================

    def supprimer(
        self,
        objet: T,
    ) -> None:

        self.session.delete(objet)

        self.session.commit()

    # =====================================================
    # UTILITAIRES
    # =====================================================

    def compter(self) -> int:

        return (
            self.session.query(self.model)
            .count()
        )

    def existe(
        self,
        identifiant: int,
    ) -> bool:

        return (
            self.rechercher_par_id(
                identifiant
            )
            is not None
        )

    def rollback(self) -> None:

        self.session.rollback()

    def fermer(self) -> None:

        self.session.close()