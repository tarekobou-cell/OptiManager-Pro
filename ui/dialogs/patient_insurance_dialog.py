from __future__ import annotations

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QDateEdit,
    QVBoxLayout,
)

from models.patient_entities.insurance import PatientInsurance


class PatientInsuranceDialog(QDialog):
    """
    Création / modification d'une assurance patient.
    """

    def __init__(
        self,
        patient,
        insurance: PatientInsurance | None = None,
        parent=None,
    ):
        super().__init__(parent)

        self.patient = patient
        self.insurance = insurance

        self.setWindowTitle(
            "Assurance patient"
        )

        self.resize(450, 500)

        self.creer_interface()

        if self.insurance is not None:
            self.charger_assurance()

    def creer_interface(self):
        layout_principal = QVBoxLayout(self)

        formulaire = QFormLayout()

        self.organisme = QLineEdit()
        self.numero_assure = QLineEdit()
        self.numero_contrat = QLineEdit()
        self.type_couverture = QLineEdit()

        self.date_debut = QDateEdit()
        self.date_debut.setCalendarPopup(True)
        self.date_debut.setDate(QDate.currentDate())

        self.date_fin = QDateEdit()
        self.date_fin.setCalendarPopup(True)
        self.date_fin.setDate(QDate.currentDate())

        self.actif = QCheckBox("Assurance active")
        self.actif.setChecked(True)

        self.observations = QLineEdit()

        formulaire.addRow(
            "Organisme",
            self.organisme,
        )

        formulaire.addRow(
            "N° assuré",
            self.numero_assure,
        )

        formulaire.addRow(
            "N° contrat",
            self.numero_contrat,
        )

        formulaire.addRow(
            "Type de couverture",
            self.type_couverture,
        )

        formulaire.addRow(
            "Date début",
            self.date_debut,
        )

        formulaire.addRow(
            "Date fin",
            self.date_fin,
        )

        formulaire.addRow(
            "Statut",
            self.actif,
        )

        formulaire.addRow(
            "Observations",
            self.observations,
        )

        boutons = QDialogButtonBox(
            QDialogButtonBox.Save
            | QDialogButtonBox.Cancel
        )

        boutons.accepted.connect(
            self.accept
        )

        boutons.rejected.connect(
            self.reject
        )

        layout_principal.addLayout(
            formulaire
        )

        layout_principal.addWidget(
            boutons
        )

    def charger_assurance(self):

        self.organisme.setText(
            self.insurance.organisme or ""
        )

        self.numero_assure.setText(
            self.insurance.numero_assure or ""
        )

        self.numero_contrat.setText(
            self.insurance.numero_contrat or ""
        )

        self.type_couverture.setText(
            self.insurance.type_couverture or ""
        )

        if self.insurance.date_debut:
            self.date_debut.setDate(
                QDate(
                    self.insurance.date_debut.year,
                    self.insurance.date_debut.month,
                    self.insurance.date_debut.day,
                )
            )

        if self.insurance.date_fin:
            self.date_fin.setDate(
                QDate(
                    self.insurance.date_fin.year,
                    self.insurance.date_fin.month,
                    self.insurance.date_fin.day,
                )
            )

        self.actif.setChecked(
            self.insurance.actif
        )

        self.observations.setText(
            self.insurance.observations or ""
        )

    def obtenir_assurance(self) -> PatientInsurance:

        if self.insurance is None:
            self.insurance = PatientInsurance(
                patient=self.patient
            )

        self.insurance.organisme = (
            self.organisme.text().strip()
        )

        self.insurance.numero_assure = (
            self.numero_assure.text().strip()
            or None
        )

        self.insurance.numero_contrat = (
            self.numero_contrat.text().strip()
            or None
        )

        self.insurance.type_couverture = (
            self.type_couverture.text().strip()
            or None
        )

        self.insurance.date_debut = (
            self.date_debut.date().toPython()
        )

        self.insurance.date_fin = (
            self.date_fin.date().toPython()
        )

        self.insurance.actif = (
            self.actif.isChecked()
        )

        self.insurance.observations = (
            self.observations.text().strip()
            or None
        )

        return self.insurance
