"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : patients_page.py
Description : Gestion des patients.
Auteur : Mohamed Tarek & ChatGPT
Version : 3.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)

from controllers.patient_controller import (
    PatientController,
)

from database import SessionLocal

from ui.components.base_window import BaseWindow
from ui.dialogs.patient_dialog import (
    PatientDialog,
)
from ui.patients.profile.patient_profile import PatientProfile

class PatientsPage(BaseWindow):
    """
    Gestion des patients.
    """

    def __init__(self):

        super().__init__(
            "Gestion des patients"
        )

        self.session = SessionLocal()

        self.controller = PatientController(
            self.session
        )

        self.construire_interface()

        self.connecter_signaux()

        self.charger_patients()

    # =====================================================
    # Interface
    # =====================================================

    def construire_interface(self):

        titre = QLabel(
            "👤 Gestion des patients"
        )

        titre.setStyleSheet(
            """
            QLabel{
                font-size:24px;
                font-weight:bold;
            }
            """
        )

        self.ajouter_widget(
            titre
        )

        self.creer_barre_recherche()

        self.creer_tableau()

        self.creer_boutons()

    # =====================================================
    # Barre de recherche
    # =====================================================

    def creer_barre_recherche(self):

        layout = QHBoxLayout()

        self.recherche = QLineEdit()

        self.recherche.setPlaceholderText(
            "Rechercher un patient..."
        )

        layout.addWidget(
            self.recherche
        )

        self.layout.addLayout(
            layout
        )

    # =====================================================
    # Tableau
    # =====================================================

    def creer_tableau(self):

        self.table = QTableWidget()

        self.table.setColumnCount(7)

        self.table.setHorizontalHeaderLabels(
            [
                "N° dossier",
                "Nom",
                "Prénom",
                "Téléphone",
                "Profession",
                "Actif",
                "ID",
            ]
        )

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.setAlternatingRowColors(
            True
        )

        self.table.setSortingEnabled(
            True
        )

        self.table.setColumnHidden(
            6,
            True,
        )

        header = self.table.horizontalHeader()

        header.setStretchLastSection(
            False
        )

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents,
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.Stretch,
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.Stretch,
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents,
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.Stretch,
        )

        header.setSectionResizeMode(
            5,
            QHeaderView.ResizeToContents,
        )

        self.layout.addWidget(
            self.table
        )

    # =====================================================
    # Boutons
    # =====================================================

    def creer_boutons(self):

        layout = QHBoxLayout()

        self.btn_ajouter = QPushButton(
            "➕ Nouveau"
        )

        self.btn_modifier = QPushButton(
            "✏ Modifier"
        )

        self.btn_dossier = QPushButton(
            "📋 Ouvrir dossier"
        )

        self.btn_supprimer = QPushButton(
            "🗑 Désactiver"
        )

        self.btn_actualiser = QPushButton(
            "🔄 Actualiser"
        )

        layout.addWidget(
            self.btn_ajouter
        )

        layout.addWidget(
            self.btn_modifier
        )

        layout.addWidget(
            self.btn_dossier
        )

        layout.addWidget(
            self.btn_supprimer
        )

        layout.addStretch()

        layout.addWidget(
            self.btn_actualiser
        )

        self.layout.addLayout(
            layout
        )
    # =====================================================
    # Signaux
    # =====================================================

    def connecter_signaux(self):

        self.btn_ajouter.clicked.connect(
            self.ajouter_patient
        )

        self.btn_modifier.clicked.connect(
            self.modifier_patient
        )
        self.btn_dossier.clicked.connect(
            self.ouvrir_dossier
        )
        self.btn_supprimer.clicked.connect(
            self.supprimer_patient
        )

        self.btn_actualiser.clicked.connect(
            self.actualiser
        )

        self.recherche.textChanged.connect(
            self.rechercher
        )

        self.table.doubleClicked.connect(
            lambda _: self.modifier_patient()
        )

    # =====================================================
    # Chargement
    # =====================================================

    def charger_patients(self):

        self.table.setRowCount(0)

        patients = (
            self.controller.rechercher_tous()
        )

        for patient in patients:

            ligne = self.table.rowCount()

            self.table.insertRow(ligne)

            self.table.setItem(
                ligne,
                0,
                QTableWidgetItem(
                    patient.numero_dossier
                ),
            )

            self.table.setItem(
                ligne,
                1,
                QTableWidgetItem(
                    patient.nom
                ),
            )

            self.table.setItem(
                ligne,
                2,
                QTableWidgetItem(
                    patient.prenom
                ),
            )

            self.table.setItem(
                ligne,
                3,
                QTableWidgetItem(
                    patient.telephone
                ),
            )

            self.table.setItem(
                ligne,
                4,
                QTableWidgetItem(
                    patient.profession or ""
                ),
            )

            self.table.setItem(
                ligne,
                5,
                QTableWidgetItem(
                    "Oui"
                    if patient.actif
                    else "Non"
                ),
            )

            self.table.setItem(
                ligne,
                6,
                QTableWidgetItem(
                    str(patient.id)
                ),
            )

        self.table.resizeRowsToContents()

    # =====================================================
    # Recherche
    # =====================================================

    def rechercher(self):

        texte = (
            self.recherche.text()
            .strip()
        )

        if not texte:

            self.charger_patients()

            return

        self.table.setRowCount(0)

        patients = (
            self.controller.rechercher(
                texte
            )
        )

        for patient in patients:

            ligne = self.table.rowCount()

            self.table.insertRow(ligne)

            self.table.setItem(
                ligne,
                0,
                QTableWidgetItem(
                    patient.numero_dossier
                ),
            )

            self.table.setItem(
                ligne,
                1,
                QTableWidgetItem(
                    patient.nom
                ),
            )

            self.table.setItem(
                ligne,
                2,
                QTableWidgetItem(
                    patient.prenom
                ),
            )

            self.table.setItem(
                ligne,
                3,
                QTableWidgetItem(
                    patient.telephone
                ),
            )

            self.table.setItem(
                ligne,
                4,
                QTableWidgetItem(
                    patient.profession or ""
                ),
            )

            self.table.setItem(
                ligne,
                5,
                QTableWidgetItem(
                    "Oui"
                    if patient.actif
                    else "Non"
                ),
            )

            self.table.setItem(
                ligne,
                6,
                QTableWidgetItem(
                    str(patient.id)
                ),
            )

        self.table.resizeRowsToContents()

    # =====================================================
    # Patient sélectionné
    # =====================================================

    def patient_selectionne(self):

        ligne = self.table.currentRow()

        if ligne < 0:

            QMessageBox.warning(
                self,
                "Patient",
                "Veuillez sélectionner un patient.",
            )

            return None

        identifiant = int(
            self.table.item(
                ligne,
                6,
            ).text()
        )

        return (
            self.controller.rechercher_par_id(
                identifiant
            )
        )

#====================================
# ouvrir dossier
#==================================
    def ouvrir_dossier(self):

        patient = self.patient_selectionne()

        if patient is None:
            return

        self.patient_profile = PatientProfile(
            patient=patient
        )

        self.patient_profile.show()

    # =====================================================
    # Ajouter un patient
    # =====================================================

    def ajouter_patient(self):

        dialog = PatientDialog(
            controller=self.controller,
            parent=self,
        )

        if dialog.exec():

            self.charger_patients()

    # =====================================================
    # Modifier un patient
    # =====================================================

    def modifier_patient(self):

        patient = self.patient_selectionne()

        if patient is None:
            return

        dialog = PatientDialog(
            controller=self.controller,
            patient=patient,
            parent=self,
        )

        if dialog.exec():

            self.charger_patients()

    # =====================================================
    # Désactiver un patient
    # =====================================================

    def supprimer_patient(self):

        patient = self.patient_selectionne()

        if patient is None:
            return

        reponse = QMessageBox.question(
            self,
            "Confirmation",
            (
                f"Voulez-vous désactiver le patient\n\n"
                f"{patient.nom} {patient.prenom} ?"
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reponse != QMessageBox.Yes:
            return

        patient.actif = False

        self.controller.modifier_patient(
            patient
        )

        self.charger_patients()

        QMessageBox.information(
            self,
            "Succès",
            "Le patient a été désactivé.",
        )

    # =====================================================
    # Actualiser
    # =====================================================

    def actualiser(self):

        self.recherche.clear()

        self.charger_patients()

    # =====================================================
    # Fermeture
    # =====================================================

    def closeEvent(
        self,
        event,
    ):

        try:

            self.session.close()

        except Exception:
            pass

        event.accept()