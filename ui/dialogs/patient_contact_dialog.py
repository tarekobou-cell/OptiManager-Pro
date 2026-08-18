from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

from models.patient_entities.contact import PatientContact


class PatientContactDialog(QDialog):
    """
    Création / modification d'un contact patient.
    """

    def __init__(
        self,
        patient,
        contact: PatientContact | None = None,
        parent=None,
    ):
        super().__init__(parent)

        self.patient = patient
        self.contact = contact

        self.setWindowTitle(
            "Contact patient"
        )

        self.resize(450, 400)

        self.creer_interface()

        if self.contact is not None:
            self.charger_contact()

    def creer_interface(self):
        layout_principal = QVBoxLayout(self)

        formulaire = QFormLayout()

        self.nom = QLineEdit()
        self.prenom = QLineEdit()

        self.relation = QComboBox()
        self.relation.addItems(
            [
                "Parent",
                "Tuteur légal",
                "Conjoint",
                "Contact d'urgence",
                "Autre",
            ]
        )

        self.telephone = QLineEdit()
        self.telephone_secondaire = QLineEdit()
        self.email = QLineEdit()
        self.adresse = QLineEdit()

        self.contact_principal = QComboBox()
        self.contact_principal.addItems(
            [
                "Non",
                "Oui",
            ]
        )

        self.contact_urgence = QComboBox()
        self.contact_urgence.addItems(
            [
                "Non",
                "Oui",
            ]
        )

        formulaire.addRow(
            "Nom",
            self.nom,
        )

        formulaire.addRow(
            "Prénom",
            self.prenom,
        )

        formulaire.addRow(
            "Relation",
            self.relation,
        )

        formulaire.addRow(
            "Téléphone",
            self.telephone,
        )

        formulaire.addRow(
            "Téléphone secondaire",
            self.telephone_secondaire,
        )

        formulaire.addRow(
            "Email",
            self.email,
        )

        formulaire.addRow(
            "Adresse",
            self.adresse,
        )

        formulaire.addRow(
            "Contact principal",
            self.contact_principal,
        )

        formulaire.addRow(
            "Contact d'urgence",
            self.contact_urgence,
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

    def charger_contact(self):
        self.nom.setText(
            self.contact.nom or ""
        )

        self.prenom.setText(
            self.contact.prenom or ""
        )

        index = self.relation.findText(
            self.contact.relation or ""
        )

        if index >= 0:
            self.relation.setCurrentIndex(
                index
            )

        self.telephone.setText(
            self.contact.telephone or ""
        )

        self.telephone_secondaire.setText(
            self.contact.telephone_secondaire
            or ""
        )

        self.email.setText(
            self.contact.email or ""
        )

        self.adresse.setText(
            self.contact.adresse or ""
        )

        self.contact_principal.setCurrentIndex(
            1
            if self.contact.contact_principal
            else 0
        )

        self.contact_urgence.setCurrentIndex(
            1
            if self.contact.contact_urgence
            else 0
        )

    def obtenir_contact(self) -> PatientContact:
        if self.contact is None:
            self.contact = PatientContact(
                patient=self.patient
            )

        self.contact.nom = (
            self.nom.text().strip()
        )

        self.contact.prenom = (
            self.prenom.text().strip()
        )

        self.contact.relation = (
            self.relation.currentText()
        )

        self.contact.telephone = (
            self.telephone.text().strip()
            or None
        )

        self.contact.telephone_secondaire = (
            self.telephone_secondaire
            .text()
            .strip()
            or None
        )

        self.contact.email = (
            self.email.text().strip()
            or None
        )

        self.contact.adresse = (
            self.adresse.text().strip()
            or None
        )

        self.contact.contact_principal = (
            self.contact_principal.currentText()
            == "Oui"
        )

        self.contact.contact_urgence = (
            self.contact_urgence.currentText()
            == "Oui"
        )

        return self.contact