"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : dashboard_repository.py
Description : Accès aux données du tableau de bord.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from models.patient import Patient
from models.rendez_vous import RendezVous
from models.vente import Vente


class DashboardRepository:
    """
    Fournit les indicateurs affichés sur le tableau de bord.
    """

    def __init__(self, session: Session):
        self.session = session

    def nombre_patients(self) -> int:
        """Retourne le nombre total de patients."""
        return self.session.query(Patient).count()

    def nombre_rdv_du_jour(self) -> int:
        """Retourne le nombre de rendez-vous du jour."""
        return (
            self.session.query(RendezVous)
            .filter(RendezVous.date_rdv == date.today())
            .count()
        )

    def nombre_ventes_du_jour(self) -> int:
        """Retourne le nombre de ventes du jour."""
        return (
            self.session.query(Vente)
            .filter(func.date(Vente.date_vente) == date.today())
            .count()
        )

    def chiffre_affaires_du_jour(self) -> float:
        """Retourne le chiffre d'affaires du jour."""

        resultat = (
            self.session.query(func.sum(Vente.total))
            .filter(func.date(Vente.date_vente) == date.today())
            .scalar()
        )

        return float(resultat or 0)