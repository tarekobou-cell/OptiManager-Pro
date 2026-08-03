"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : patient_controller.py
Description : Contrôleur des patients.
Auteur : Mohamed Tarek & ChatGPT
Version : 3.0.0
=========================================================
"""

from sqlalchemy.orm import Session

from models.patient import Patient
from services.patient_service import PatientService


class PatientController:
    """
    Contrôleur des patients.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self.service = PatientService(
            session
        )

    # =====================================================
    # CRUD
    # =====================================================

    def creer_patient(
        self,
        patient: Patient,
    ) -> Patient:
        """
        Crée un nouveau patient.
        """

        return self.service.creer(
            patient
        )

    def modifier_patient(
        self,
        patient: Patient,
    ) -> None:
        """
        Enregistre les modifications
        d'un patient.
        """

        self.service.modifier(
            patient
        )

    def supprimer_patient(
        self,
        patient: Patient,
    ) -> None:
        """
        Supprime un patient.
        """

        self.service.supprimer(
            patient
        )

    # =====================================================
    # Recherches
    # =====================================================

    def rechercher(
        self,
        texte: str,
    ) -> list[Patient]:

        return self.service.rechercher(
            texte
        )

    def rechercher_tous(
        self,
    ) -> list[Patient]:

        return self.service.rechercher_tous()

    def rechercher_par_id(
        self,
        identifiant: int,
    ) -> Patient | None:

        return self.service.rechercher_par_id(
            identifiant
        )

    # =====================================================
    # Validation
    # =====================================================

    def numero_existe(
        self,
        numero: str,
    ) -> bool:

        return self.service.numero_existe(
            numero
        )

    def telephone_existe(
        self,
        telephone: str,
    ) -> bool:

        return self.service.telephone_existe(
            telephone
        )

    def email_existe(
        self,
        email: str,
    ) -> bool:

        return self.service.email_existe(
            email
        )