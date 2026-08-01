from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QComboBox,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox
)

from services.patient_service import liste_patients
from services.consultation_service import (
    creer_consultation,
    modifier_consultation
)


class ConsultationDialog(QDialog):

    def __init__(self, consultation=None, parent=None):

        super().__init__(parent)

        self.consultation = consultation

        if consultation:
            self.setWindowTitle("Modifier une consultation")
        else:
            self.setWindowTitle("Nouvelle consultation")

        self.resize(600, 450)

        self.creer_interface()

        self.charger_patients()

        if consultation:
            self.charger_consultation()

    # =====================================================

    def creer_interface(self):

        layout = QVBoxLayout(self)

        formulaire = QFormLayout()

        self.patient = QComboBox()

        self.motif = QTextEdit()
        self.motif.setFixedHeight(80)

        self.observations = QTextEdit()
        self.observations.setFixedHeight(180)

        formulaire.addRow("Patient *", self.patient)
        formulaire.addRow("Motif", self.motif)
        formulaire.addRow("Observations", self.observations)

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
    # =====================================================
    # Chargement des patients
    # =====================================================

    def charger_patients(self):

        self.patient.clear()

        patients = liste_patients()

        for patient in patients:

            self.patient.addItem(
                f"{patient.nom} {patient.prenom}",
                patient.id
            )

    # =====================================================
    # Chargement d'une consultation
    # =====================================================

    def charger_consultation(self):

        index = self.patient.findData(
            self.consultation.patient_id
        )

        if index >= 0:
            self.patient.setCurrentIndex(index)

        self.motif.setPlainText(
            self.consultation.motif or ""
        )

        self.observations.setPlainText(
            self.consultation.observations or ""
        )

    # =====================================================
    # Validation
    # =====================================================

    def verifier(self):

        if self.patient.currentIndex() == -1:

            QMessageBox.warning(
                self,
                "Erreur",
                "Veuillez sélectionner un patient."
            )

            return False

        return True
    # =====================================================
    # Enregistrement
    # =====================================================

    def enregistrer(self):

        if not self.verifier():
            return

        patient_id = self.patient.currentData()

        motif = self.motif.toPlainText()

        observations = self.observations.toPlainText()

        try:

            if self.consultation is None:

                creer_consultation(

                    patient_id=patient_id,

                    motif=motif,

                    observations=observations

                )

            else:

                modifier_consultation(

                    consultation_id=self.consultation.id,

                    motif=motif,

                    observations=observations

                )

            QMessageBox.information(
                self,
                "Succès",
                "Consultation enregistrée."
            )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Erreur",
                str(e)
            )