"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : consultation_service.py
Description : Service métier des consultations.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from sqlalchemy.orm import Session

from models.consultation import Consultation
from repositories.consultation_repository import (
    ConsultationRepository,
)


class ConsultationService:
    """
    Service métier des consultations.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self.repository = ConsultationRepository(
            session
        )

    # =====================================================
    # CRUD
    # =====================================================

    def creer(
        self,
        consultation: Consultation,
    ) -> Consultation:
        """
        Crée une consultation.
        """

        return self.repository.ajouter(
            consultation
        )

    def modifier(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Enregistre les modifications.
        """

        self.repository.sauvegarder()

    def supprimer(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Supprime une consultation.
        """

        self.repository.supprimer(
            consultation
        )
    # =====================================================
    # Recherches
    # =====================================================

    def rechercher_par_id(
        self,
        identifiant: int,
    ) -> Consultation | None:
        """
        Recherche une consultation par son identifiant.
        """

        return self.repository.rechercher_par_id(
            identifiant
        )

    def rechercher_toutes(
        self,
    ) -> list[Consultation]:
        """
        Retourne toutes les consultations.
        """

        return self.repository.rechercher_toutes()

    def rechercher_par_patient(
        self,
        patient_id: int,
    ) -> list[Consultation]:
        """
        Retourne l'historique des consultations
        d'un patient.
        """

        return self.repository.rechercher_par_patient(
            patient_id
        )

    def derniere_consultation(
        self,
        patient_id: int,
    ) -> Consultation | None:
        """
        Retourne la dernière consultation
        d'un patient.
        """

        return self.repository.derniere_consultation(
            patient_id
        )

    def rechercher_par_date(
        self,
        date_consultation,
    ) -> list[Consultation]:
        """
        Recherche les consultations
        d'une date donnée.
        """

        return self.repository.rechercher_par_date(
            date_consultation
        )

    def rechercher_par_periode(
        self,
        date_debut,
        date_fin,
    ) -> list[Consultation]:
        """
        Recherche les consultations
        comprises entre deux dates.
        """

        return self.repository.rechercher_par_periode(
            date_debut,
            date_fin,
        )
    # =====================================================
    # Statistiques
    # =====================================================

    def compter(self) -> int:
        """
        Retourne le nombre total
        de consultations.
        """

        return self.repository.compter()

    def compter_par_patient(
        self,
        patient_id: int,
    ) -> int:
        """
        Retourne le nombre de consultations
        d'un patient.
        """

        return self.repository.compter_par_patient(
            patient_id
        )

    def consultations_du_jour(
        self,
        date_jour,
    ) -> list[Consultation]:
        """
        Retourne les consultations du jour.
        """

        return self.repository.consultations_du_jour(
            date_jour
        )

    # =====================================================
    # Validation métier
    # =====================================================

    def verifier_consultation(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Vérifie la cohérence des données
        d'une consultation.
        """

        if consultation.patient_id is None:

            raise ValueError(
                "Le patient est obligatoire."
            )

        if consultation.date_consultation is None:

            raise ValueError(
                "La date de consultation est obligatoire."
            )

    # =====================================================
    # Création sécurisée
    # =====================================================

    def creer_consultation(
        self,
        consultation: Consultation,
    ) -> Consultation:
        """
        Valide puis crée une consultation.
        """

        self.verifier_consultation(
            consultation
        )

        return self.creer(
            consultation
        )

    # =====================================================
    # Modification sécurisée
    # =====================================================

    def modifier_consultation(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Valide puis enregistre les modifications.
        """

        self.verifier_consultation(
            consultation
        )

        self.modifier(
            consultation
        )