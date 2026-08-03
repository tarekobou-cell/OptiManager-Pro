"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : consultation_repository.py
Description : Repository des consultations.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from sqlalchemy.orm import Session

from models.consultation import Consultation
from repositories.base_repository import BaseRepository


class ConsultationRepository(
    BaseRepository[Consultation]
):
    """
    Repository dédié aux consultations.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session,
            Consultation,
        )

    # =====================================================
    # Recherche
    # =====================================================

    def rechercher_par_id(
        self,
        identifiant: int,
    ) -> Consultation | None:

        return self.session.get(
            Consultation,
            identifiant,
        )

    def rechercher_toutes(
        self,
    ) -> list[Consultation]:

        return (
            self.session.query(
                Consultation
            )
            .order_by(
                Consultation.date_consultation.desc()
            )
            .all()
        )
    # =====================================================
    # Recherches par patient
    # =====================================================

    def rechercher_par_patient(
        self,
        patient_id: int,
    ) -> list[Consultation]:
        """
        Retourne toutes les consultations
        d'un patient.
        """

        return (
            self.session.query(
                Consultation
            )
            .filter(
                Consultation.patient_id == patient_id
            )
            .order_by(
                Consultation.date_consultation.desc()
            )
            .all()
        )

    def derniere_consultation(
        self,
        patient_id: int,
    ) -> Consultation | None:
        """
        Retourne la dernière consultation
        d'un patient.
        """

        return (
            self.session.query(
                Consultation
            )
            .filter(
                Consultation.patient_id == patient_id
            )
            .order_by(
                Consultation.date_consultation.desc()
            )
            .first()
        )

    # =====================================================
    # Recherches par date
    # =====================================================

    def rechercher_par_date(
        self,
        date_consultation,
    ) -> list[Consultation]:
        """
        Retourne les consultations
        d'une date donnée.
        """

        return (
            self.session.query(
                Consultation
            )
            .filter(
                Consultation.date_consultation == date_consultation
            )
            .all()
        )

    def rechercher_par_periode(
        self,
        date_debut,
        date_fin,
    ) -> list[Consultation]:
        """
        Retourne les consultations
        comprises entre deux dates.
        """

        return (
            self.session.query(
                Consultation
            )
            .filter(
                Consultation.date_consultation >= date_debut,
                Consultation.date_consultation <= date_fin,
            )
            .order_by(
                Consultation.date_consultation.desc()
            )
            .all()
        )

    # =====================================================
    # Consultations du jour
    # =====================================================

    def consultations_du_jour(
        self,
        date_jour,
    ) -> list[Consultation]:
        """
        Retourne toutes les consultations
        du jour.
        """

        return (
            self.session.query(
                Consultation
            )
            .filter(
                Consultation.date_consultation >= date_jour
            )
            .order_by(
                Consultation.date_consultation.asc()
            )
            .all()
        )

    # =====================================================
    # Comptage
    # =====================================================

    def compter(
        self,
    ) -> int:
        """
        Retourne le nombre total
        de consultations.
        """

        return (
            self.session.query(
                Consultation
            )
            .count()
        )

    def compter_par_patient(
        self,
        patient_id: int,
    ) -> int:
        """
        Retourne le nombre de consultations
        d'un patient.
        """

        return (
            self.session.query(
                Consultation
            )
            .filter(
                Consultation.patient_id == patient_id
            )
            .count()
        )

    # =====================================================
    # Suppression
    # =====================================================

    def supprimer(
        self,
        consultation: Consultation,
    ) -> None:
        """
        Supprime une consultation.
        """

        self.session.delete(
            consultation
        )

        self.session.commit()

    # =====================================================
    # Sauvegarde
    # =====================================================

    def sauvegarder(
        self,
    ) -> None:
        """
        Enregistre les modifications.
        """

        self.session.commit()