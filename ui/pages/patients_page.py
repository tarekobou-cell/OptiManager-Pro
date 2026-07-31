from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QMessageBox
)

from services.patient_service import (
    liste_patients,
    rechercher_patients,
    detail_patient
)

from ui.dialogs.patient_dialog import PatientDialog


class PatientsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.creer_interface()
        self.charger_patients()

    # =====================================================

    def creer_interface(self):

        layout = QVBoxLayout(self)

        # -------------------------
        # Barre supérieure
        # -------------------------

        barre = QHBoxLayout()

        titre = QLabel("Patients")

        titre.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        barre.addWidget(titre)
        barre.addStretch()

        self.btn_nouveau = QPushButton("➕ Nouveau")
        self.btn_modifier = QPushButton("✏ Modifier")
        self.btn_supprimer = QPushButton("🗑 Supprimer")

        barre.addWidget(self.btn_nouveau)
        barre.addWidget(self.btn_modifier)
        barre.addWidget(self.btn_supprimer)

        layout.addLayout(barre)

        # -------------------------
        # Recherche
        # -------------------------

        self.recherche = QLineEdit()

        self.recherche.setPlaceholderText(
            "Rechercher un patient..."
        )

        layout.addWidget(self.recherche)

        # -------------------------
        # Tableau
        # -------------------------

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Nom",
            "Prénom",
            "Téléphone",
            "Naissance",
            "Dernière visite"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
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

        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)

        layout.addWidget(self.table)

        # -------------------------
        # Connexions
        # -------------------------

        self.btn_nouveau.clicked.connect(
            self.nouveau_patient
        )

        self.btn_modifier.clicked.connect(
            self.modifier_patient
        )

        self.table.doubleClicked.connect(
            self.modifier_patient
        )

        self.recherche.textChanged.connect(
            self.rechercher
        )

    # =====================================================

    def charger_patients(self):

        self.afficher_patients(
            liste_patients()
        )

    # =====================================================

    def afficher_patients(self, patients):

        self.table.setRowCount(len(patients))

        for ligne, patient in enumerate(patients):

            self.table.setItem(
                ligne,
                0,
                QTableWidgetItem(str(patient.id))
            )

            self.table.setItem(
                ligne,
                1,
                QTableWidgetItem(patient.nom)
            )

            self.table.setItem(
                ligne,
                2,
                QTableWidgetItem(patient.prenom)
            )

            self.table.setItem(
                ligne,
                3,
                QTableWidgetItem(patient.telephone or "")
            )

            self.table.setItem(
                ligne,
                4,
                QTableWidgetItem(patient.date_naissance or "")
            )

            self.table.setItem(
                ligne,
                5,
                QTableWidgetItem(patient.date_derniere_visite or "")
            )

    # =====================================================

    def patient_selectionne(self):

        ligne = self.table.currentRow()

        if ligne < 0:

            return None

        return int(
            self.table.item(ligne, 0).text()
        )

    # =====================================================

    def nouveau_patient(self):

        dialog = PatientDialog(parent=self)

        if dialog.exec():

            self.charger_patients()

    # =====================================================

    def modifier_patient(self):

        patient_id = self.patient_selectionne()

        if patient_id is None:

            QMessageBox.information(
                self,
                "Information",
                "Sélectionnez un patient."
            )

            return

        patient = detail_patient(patient_id)

        dialog = PatientDialog(
            patient=patient,
            parent=self
        )

        if dialog.exec():

            self.charger_patients()

    # =====================================================

    def rechercher(self):

        texte = self.recherche.text().strip()

        if texte == "":

            self.charger_patients()

            return

        self.afficher_patients(
            rechercher_patients(texte)
        )