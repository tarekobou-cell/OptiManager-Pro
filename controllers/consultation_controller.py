"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : consultation_controller.py
Description : Contrôleur des consultations.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from sqlalchemy.orm import Session

from models.consultation import Consultation
from services.consultation_service import (
    ConsultationService,
)


class ConsultationController:
    """
    Contrôleur des consultations.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self.service = ConsultationService(
            session
        )

    # =====================================================
    # CRUD
    # =====================================================

    def creer_consultation(
        self,
        consultation: Consultation,
    ) -> Consultation:
        """
        Crée une consultation.
        """

        return (
            self.service.creer_consultation(
                consultation
            )
        )

    def modifier_consultation(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Modifie une consultation.
        """

        self.service.modifier_consultation(
            consultation
        )

    def supprimer_consultation(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Supprime une consultation.
        """

        self.service.supprimer(
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

        return self.service.rechercher_par_id(
            identifiant
        )

    def rechercher_toutes(
        self,
    ) -> list[Consultation]:
        """
        Retourne toutes les consultations.
        """

        return self.service.rechercher_toutes()

    def rechercher_par_patient(
        self,
        patient_id: int,
    ) -> list[Consultation]:
        """
        Retourne l'historique des consultations
        d'un patient.
        """

        return self.service.rechercher_par_patient(
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

        return self.service.derniere_consultation(
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

        return self.service.rechercher_par_date(
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

        return self.service.rechercher_par_periode(
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

        return self.service.compter()

    def compter_par_patient(
        self,
        patient_id: int,
    ) -> int:
        """
        Retourne le nombre de consultations
        d'un patient.
        """

        return self.service.compter_par_patient(
            patient_id
        )

    def consultations_du_jour(
        self,
        date_jour,
    ) -> list[Consultation]:
        """
        Retourne les consultations du jour.
        """

        return self.service.consultations_du_jour(
            date_jour
        )