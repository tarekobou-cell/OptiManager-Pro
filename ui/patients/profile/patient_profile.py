from __future__ import annotations

from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from ui.components.base_window import BaseWindow


class PatientProfile(BaseWindow):
    """
    Fiche détaillée d'un patient.
    """

    def __init__(self, patient=None):
        super().__init__("Dossier patient")

        self.patient = patient

        self.construire_interface()

    # =====================================================
    # Interface
    # =====================================================

    def construire_interface(self):
        self.creer_entete()
        self.creer_contenu()

    # =====================================================
    # En-tête
    # =====================================================

    def creer_entete(self):
        cadre = QFrame()
        cadre.setFrameShape(QFrame.StyledPanel)

        layout = QHBoxLayout(cadre)

        avatar = QLabel("👤")
        avatar.setAlignment(Qt.AlignCenter)
        avatar.setFixedSize(70, 70)

        informations = QVBoxLayout()

        nom = self.obtenir_nom_patient()

        self.nom_patient = QLabel(nom)
        self.nom_patient.setStyleSheet(
            """
            QLabel {
                font-size: 24px;
                font-weight: bold;
            }
            """
        )

        numero = self.obtenir_numero_dossier()

        self.numero_dossier = QLabel(
            f"N° dossier : {numero}"
        )

        statut = self.obtenir_statut()

        self.statut = QLabel(statut)

        informations.addWidget(
            self.nom_patient
        )

        informations.addWidget(
            self.numero_dossier
        )

        informations.addWidget(
            self.statut
        )

        actions = QHBoxLayout()

        self.btn_modifier = QPushButton(
            "Modifier"
        )

        self.btn_imprimer = QPushButton(
            "Imprimer"
        )

        self.btn_archiver = QPushButton(
            "Archiver"
        )

        actions.addWidget(
            self.btn_modifier
        )

        actions.addWidget(
            self.btn_imprimer
        )

        actions.addWidget(
            self.btn_archiver
        )

        layout.addWidget(avatar)

        layout.addLayout(
            informations
        )

        layout.addStretch()

        layout.addLayout(
            actions
        )

        self.layout.addWidget(cadre)

    # =====================================================
    # Données patient
    # =====================================================

    def obtenir_nom_patient(self) -> str:
        if self.patient is None:
            return "Patient"

        prenom = (
            self.patient.prenom
            or ""
        ).strip()

        nom = (
            self.patient.nom
            or ""
        ).strip()

        nom_complet = (
            f"{prenom} {nom}"
        ).strip()

        return (
            nom_complet
            if nom_complet
            else "Patient"
        )

    def obtenir_numero_dossier(self) -> str:
        if self.patient is None:
            return "---"

        return (
            self.patient.numero_dossier
            or "---"
        )

    def obtenir_statut(self) -> str:
        if self.patient is None:
            return "● Actif"

        return (
            "● Actif"
            if self.patient.actif
            else "● Inactif"
        )

    def obtenir_age(self) -> str:
        if (
            self.patient is None
            or self.patient.date_naissance is None
        ):
            return "---"

        naissance = (
            self.patient.date_naissance
        )

        aujourd_hui = date.today()

        age = (
            aujourd_hui.year
            - naissance.year
            - (
                (
                    aujourd_hui.month,
                    aujourd_hui.day,
                )
                <
                (
                    naissance.month,
                    naissance.day,
                )
            )
        )

        return f"{age} ans"

    def obtenir_telephone(self) -> str:
        if self.patient is None:
            return "---"

        return (
            self.patient.telephone
            or "---"
        )

    def obtenir_email(self) -> str:
        if self.patient is None:
            return "---"

        return (
            self.patient.email
            or "---"
        )

    def obtenir_derniere_visite(self) -> str:
        """
        Dernière visite.

        Pour l'instant, cette donnée n'est pas
        calculée depuis les consultations.
        Elle sera branchée dans la prochaine étape.
        """

        return "---"

    # =====================================================
    # Contenu
    # =====================================================

    def creer_contenu(self):
        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        contenu = QWidget()

        layout = QVBoxLayout(contenu)

        layout.setSpacing(15)

        layout.addWidget(
            self.creer_resume()
        )

        tabs = QTabWidget()

        tabs.addTab(
            self.creer_identite(),
            "Identité",
        )

        tabs.addTab(
            self.creer_coordonnees(),
            "Coordonnées",
        )

        tabs.addTab(
            self.creer_contacts(),
            "Contacts",
        )

        tabs.addTab(
            self.creer_clinique(),
            "Clinique",
        )

        tabs.addTab(
            self.creer_rendez_vous(),
            "Rendez-vous",
        )

        tabs.addTab(
            self.creer_prescriptions(),
            "Prescriptions",
        )

        tabs.addTab(
            self.creer_ventes(),
            "Ventes",
        )

        tabs.addTab(
            self.creer_documents(),
            "Documents",
        )

        tabs.addTab(
            self.creer_historique(),
            "Historique",
        )

        layout.addWidget(tabs)

        scroll.setWidget(contenu)

        self.layout.addWidget(scroll)

    # =====================================================
    # Résumé
    # =====================================================

    def creer_resume(self):
        cadre = QFrame()

        cadre.setFrameShape(
            QFrame.StyledPanel
        )

        grid = QGridLayout(cadre)

        elements = [
            (
                "Âge",
                self.obtenir_age(),
            ),
            (
                "Téléphone",
                self.obtenir_telephone(),
            ),
            (
                "Email",
                self.obtenir_email(),
            ),
            (
                "Dernière visite",
                self.obtenir_derniere_visite(),
            ),
        ]

        for colonne, (
            titre,
            valeur,
        ) in enumerate(elements):

            bloc = QVBoxLayout()

            label_titre = QLabel(
                titre
            )

            label_titre.setStyleSheet(
                "font-weight: bold;"
            )

            label_valeur = QLabel(
                valeur
            )

            bloc.addWidget(
                label_titre
            )

            bloc.addWidget(
                label_valeur
            )

            grid.addLayout(
                bloc,
                0,
                colonne,
            )

        return cadre

    # =====================================================
    # Sections
    # =====================================================

    def creer_section(
        self,
        titre,
    ):
        widget = QWidget()

        layout = QVBoxLayout(
            widget
        )

        label = QLabel(titre)

        label.setStyleSheet(
            """
            QLabel {
                font-size: 20px;
                font-weight: bold;
            }
            """
        )

        layout.addWidget(
            label
        )

        layout.addStretch()

        return widget

    def creer_identite(self):
        return self.creer_section(
            "Informations d'identité"
        )

    def creer_coordonnees(self):
        return self.creer_section(
            "Coordonnées"
        )

    def creer_contacts(self):
        return self.creer_section(
            "Contacts et entourage"
        )

    def creer_clinique(self):
        return self.creer_section(
            "Informations cliniques"
        )

    def creer_rendez_vous(self):
        return self.creer_section(
            "Rendez-vous"
        )

    def creer_prescriptions(self):
        return self.creer_section(
            "Prescriptions"
        )

    def creer_ventes(self):
        return self.creer_section(
            "Historique des ventes"
        )

    def creer_documents(self):
        return self.creer_section(
            "Documents du patient"
        )

    def creer_historique(self):
        return self.creer_section(
            "Timeline et historique"
        )