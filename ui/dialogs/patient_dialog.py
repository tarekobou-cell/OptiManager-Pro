from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox
)

from services.patient_service import (
    creer_patient,
    modifier_patient
)


class PatientDialog(QDialog):

    def __init__(self, patient=None, parent=None):
        super().__init__(parent)

        self.patient = patient

        if self.patient:
            self.setWindowTitle("Modifier un patient")
        else:
            self.setWindowTitle("Nouveau patient")

        self.resize(500, 500)

        self.creer_interface()

        if self.patient:
            self.charger_patient()

    # =========================================

    def creer_interface(self):

        layout = QVBoxLayout(self)

        formulaire = QFormLayout()

        self.nom = QLineEdit()
        self.prenom = QLineEdit()
        self.telephone = QLineEdit()

        self.date_naissance = QLineEdit()
        self.date_naissance.setPlaceholderText("JJ/MM/AAAA")

        self.adresse = QLineEdit()

        self.notes = QTextEdit()

        formulaire.addRow("Nom *", self.nom)
        formulaire.addRow("Prénom *", self.prenom)
        formulaire.addRow("Téléphone *", self.telephone)
        formulaire.addRow("Date naissance", self.date_naissance)
        formulaire.addRow("Adresse", self.adresse)
        formulaire.addRow("Notes", self.notes)

        layout.addLayout(formulaire)

        boutons = QHBoxLayout()

        self.btn_annuler = QPushButton("Annuler")
        self.btn_enregistrer = QPushButton("Enregistrer")

        boutons.addStretch()
        boutons.addWidget(self.btn_annuler)
        boutons.addWidget(self.btn_enregistrer)

        layout.addLayout(boutons)

        self.btn_annuler.clicked.connect(self.reject)
        self.btn_enregistrer.clicked.connect(self.enregistrer)

    # =========================================

    def charger_patient(self):

        self.nom.setText(self.patient.nom)
        self.prenom.setText(self.patient.prenom)
        self.telephone.setText(self.patient.telephone or "")
        self.date_naissance.setText(self.patient.date_naissance or "")
        self.adresse.setText(self.patient.adresse or "")
        self.notes.setPlainText(self.patient.notes or "")

    # =========================================

    def enregistrer(self):

        if self.nom.text().strip() == "":
            QMessageBox.warning(
                self,
                "Erreur",
                "Le nom est obligatoire."
            )
            return

        if self.prenom.text().strip() == "":
            QMessageBox.warning(
                self,
                "Erreur",
                "Le prénom est obligatoire."
            )
            return

        if self.patient is None:

            creer_patient(
                nom=self.nom.text(),
                prenom=self.prenom.text(),
                telephone=self.telephone.text(),
                date_naissance=self.date_naissance.text(),
                adresse=self.adresse.text(),
                notes=self.notes.toPlainText()
            )

        else:

            modifier_patient(
                patient_id=self.patient.id,
                nom=self.nom.text(),
                prenom=self.prenom.text(),
                telephone=self.telephone.text(),
                date_naissance=self.date_naissance.text(),
                adresse=self.adresse.text(),
                notes=self.notes.toPlainText()
            )

        self.accept()