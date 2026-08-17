from __future__ import annotations

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

    Première version :
    structure UI uniquement.
    Les données seront branchées ensuite.
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

        self.nom_patient = QLabel(
            "Patient"
        )
        self.nom_patient.setStyleSheet(
            """
            QLabel {
                font-size: 24px;
                font-weight: bold;
            }
            """
        )

        self.numero_dossier = QLabel(
            "N° dossier : ---"
        )

        self.statut = QLabel(
            "● Actif"
        )

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
        layout.addLayout(informations)
        layout.addStretch()
        layout.addLayout(actions)

        self.layout.addWidget(cadre)

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
        cadre.setFrameShape(QFrame.StyledPanel)

        grid = QGridLayout(cadre)

        elements = [
            ("Âge", "---"),
            ("Téléphone", "---"),
            ("Email", "---"),
            ("Dernière visite", "---"),
        ]

        for colonne, (titre, valeur) in enumerate(
            elements
        ):
            bloc = QVBoxLayout()

            label_titre = QLabel(titre)
            label_titre.setStyleSheet(
                "font-weight: bold;"
            )

            label_valeur = QLabel(valeur)

            bloc.addWidget(label_titre)
            bloc.addWidget(label_valeur)

            grid.addLayout(
                bloc,
                0,
                colonne,
            )

        return cadre

    # =====================================================
    # Onglets
    # =====================================================

    def creer_section(self, titre):
        widget = QWidget()

        layout = QVBoxLayout(widget)

        label = QLabel(titre)
        label.setStyleSheet(
            """
            QLabel {
                font-size: 20px;
                font-weight: bold;
            }
            """
        )

        layout.addWidget(label)
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