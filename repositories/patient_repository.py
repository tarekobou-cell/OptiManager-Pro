"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : patient_repository.py
Description : Repository des patients.
Auteur : Mohamed Tarek & ChatGPT
Version : 3.0.0
=========================================================
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from models.patient import Patient
from repositories.base_repository import BaseRepository


class PatientRepository(BaseRepository[Patient]):
    """
    Repository dédié aux patients.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session,
            Patient,
        )

    # =====================================================
    # Recherches simples
    # =====================================================

    def rechercher_par_numero(
        self,
        numero: str,
    ) -> Patient | None:

        return (
            self.session.query(Patient)
            .filter(
                Patient.numero_dossier == numero
            )
            .first()
        )

    def rechercher_par_telephone(
        self,
        telephone: str,
    ) -> Patient | None:

        return (
            self.session.query(Patient)
            .filter(
                Patient.telephone == telephone
            )
            .first()
        )

    def rechercher_par_email(
        self,
        email: str,
    ) -> Patient | None:

        return (
            self.session.query(Patient)
            .filter(
                Patient.email == email
            )
            .first()
        )

    # =====================================================
    # Recherche générale
    # =====================================================

    def rechercher(
        self,
        texte: str,
    ) -> list[Patient]:

        texte = f"%{texte}%"

        return (
            self.session.query(Patient)
            .filter(
                or_(
                    Patient.numero_dossier.ilike(
                        texte
                    ),
                    Patient.nom.ilike(
                        texte
                    ),
                    Patient.prenom.ilike(
                        texte
                    ),
                    Patient.telephone.ilike(
                        texte
                    ),
                    Patient.email.ilike(
                        texte
                    ),
                )
            )
            .order_by(
                Patient.nom,
                Patient.prenom,
            )
            .all()
        )

    def rechercher_actifs(
        self,
    ) -> list[Patient]:

        return (
            self.session.query(Patient)
            .filter(
                Patient.actif.is_(True)
            )
            .order_by(
                Patient.nom,
                Patient.prenom,
            )
            .all()
        )

    # =====================================================
    # Vérifications
    # =====================================================

    def numero_existe(
        self,
        numero: str,
    ) -> bool:

        return (
            self.rechercher_par_numero(
                numero
            )
            is not None
        )

    def telephone_existe(
        self,
        telephone: str,
    ) -> bool:

        return (
            self.rechercher_par_telephone(
                telephone
            )
            is not None
        )

    def email_existe(
        self,
        email: str,
    ) -> bool:

        return (
            self.rechercher_par_email(
                email
            )
            is not None
        )

    # =====================================================
    # Numéro de dossier
    # =====================================================

    def dernier_numero_dossier(
        self,
    ) -> str | None:
        """
        Retourne le dernier numéro
        de dossier enregistré.
        """

        patient = (
            self.session.query(Patient)
            .order_by(
                Patient.numero_dossier.desc()
            )
            .first()
        )

        if patient is None:
            return None

        return patient.numero_dossier