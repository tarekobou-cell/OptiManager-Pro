"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : patient_service.py
Description : Service métier des patients.
Auteur : Mohamed Tarek & ChatGPT
Version : 3.0.0
=========================================================
"""

from sqlalchemy.orm import Session

from models.patient import Patient
from repositories.patient_repository import PatientRepository


class PatientService:
    """
    Service métier des patients.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self.repository = PatientRepository(
            session
        )

    # =====================================================
    # CRUD
    # =====================================================

    def creer(
        self,
        patient: Patient,
    ) -> Patient:
        """
        Crée un nouveau patient après validation.
        """

        # ---------------------------------------------
        # Téléphone
        # ---------------------------------------------

        if self.telephone_existe(
            patient.telephone
        ):

            raise ValueError(
                "Ce numéro de téléphone existe déjà."
            )

        # ---------------------------------------------
        # E-mail
        # ---------------------------------------------

        if (
            patient.email
            and self.repository.email_existe(
                patient.email
            )
        ):

            raise ValueError(
                "Cette adresse e-mail existe déjà."
            )

        # ---------------------------------------------
        # Numéro de dossier
        # ---------------------------------------------

        patient.numero_dossier = (
            self.generer_numero_dossier()
        )

        return self.repository.ajouter(
            patient
        )

    def modifier(
        self,
        patient: Patient,
    ) -> None:
        """
        Enregistre les modifications d'un patient.
        """

        self.repository.sauvegarder()

    def supprimer(
        self,
        patient: Patient,
    ) -> None:
        """
        Supprime un patient.
        """

        self.repository.supprimer(
            patient
        )

    # =====================================================
    # Recherches
    # =====================================================

    def rechercher(
        self,
        texte: str,
    ) -> list[Patient]:

        return self.repository.rechercher(
            texte
        )

    def rechercher_tous(
        self,
    ) -> list[Patient]:

        return (
            self.repository.rechercher_actifs()
        )

    def rechercher_par_id(
        self,
        identifiant: int,
    ) -> Patient | None:

        return (
            self.repository.rechercher_par_id(
                identifiant
            )
        )

    # =====================================================
    # Génération automatique
    # =====================================================

    def generer_numero_dossier(
        self,
    ) -> str:
        """
        Génère un numéro de dossier unique.
        """

        dernier = (
            self.repository
            .dernier_numero_dossier()
        )

        if dernier is None:
            return "PAT000001"

        numero = int(
            dernier.replace(
                "PAT",
                "",
            )
        )

        numero += 1

        return f"PAT{numero:06d}"

    # =====================================================
    # Validation
    # =====================================================

    def telephone_existe(
        self,
        telephone: str,
    ) -> bool:

        return (
            self.repository.telephone_existe(
                telephone
            )
        )

    def numero_existe(
        self,
        numero: str,
    ) -> bool:

        return (
            self.repository.numero_existe(
                numero
            )
        )

    def email_existe(
        self,
        email: str,
    ) -> bool:

        return (
            self.repository.email_existe(
                email
            )
        )