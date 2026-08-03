"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : patient_dialog.py
Description : Ajout / Modification d'un patient.
Auteur : Mohamed Tarek & ChatGPT
Version : 3.0.0
=========================================================
"""

from datetime import datetime

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QWidget,
)

from controllers.patient_controller import PatientController
from models.patient import Patient
from ui.components.base_dialog import BaseDialog


class PatientDialog(BaseDialog):
    """
    Fenêtre d'ajout / modification d'un patient.
    """

    def __init__(
        self,
        controller: PatientController,
        patient: Patient | None = None,
        parent=None,
    ) -> None:

        self.controller = controller
        self.patient = patient

        titre = (
            "Modifier un patient"
            if patient
            else "Nouveau patient"
        )

        super().__init__(
            titre=titre,
            parent=parent,
        )

        if self.patient is not None:
            self.charger_patient()

    # =====================================================
    # Création du contenu
    # =====================================================

    def _creer_contenu(self) -> None:

        self.formulaire = QWidget()

        self.form_layout = QFormLayout(
            self.formulaire
        )

        self.form_layout.setSpacing(12)

        # -----------------------------
        # Champs
        # -----------------------------

        self.nom = QLineEdit()

        self.prenom = QLineEdit()

        self.telephone = QLineEdit()

        self.date_naissance = QLineEdit()

        self.adresse = QLineEdit()

        self.email = QLineEdit()

        self.profession = QLineEdit()

        self.notes = QTextEdit()

        self.notes.setMaximumHeight(120)

        self.actif = QCheckBox()

        self.actif.setChecked(True)

        # -----------------------------
        # Placeholders
        # -----------------------------

        self.nom.setPlaceholderText("Nom")

        self.prenom.setPlaceholderText("Prénom")

        self.telephone.setPlaceholderText(
            "0550123456"
        )

        self.date_naissance.setPlaceholderText(
            "JJ/MM/AAAA"
        )

        self.adresse.setPlaceholderText(
            "Adresse"
        )

        self.email.setPlaceholderText(
            "nom@email.com"
        )

        self.profession.setPlaceholderText(
            "Profession"
        )

        self.notes.setPlaceholderText(
            "Notes..."
        )

        # -----------------------------
        # Longueurs
        # -----------------------------

        self.nom.setMaxLength(100)

        self.prenom.setMaxLength(100)

        self.telephone.setMaxLength(20)

        self.email.setMaxLength(150)

        self.profession.setMaxLength(100)

        self.adresse.setMaxLength(255)

        # -----------------------------
        # Validation téléphone
        # -----------------------------

        regex = QRegularExpression(
            r"[0-9+ ]+"
        )

        self.telephone.setValidator(
            QRegularExpressionValidator(
                regex
            )
        )

        # -----------------------------
        # Formulaire
        # -----------------------------

        self.form_layout.addRow(
            "Nom *",
            self.nom,
        )

        self.form_layout.addRow(
            "Prénom *",
            self.prenom,
        )

        self.form_layout.addRow(
            "Téléphone *",
            self.telephone,
        )

        self.form_layout.addRow(
            "Date de naissance",
            self.date_naissance,
        )

        self.form_layout.addRow(
            "Adresse",
            self.adresse,
        )

        self.form_layout.addRow(
            "Email",
            self.email,
        )

        self.form_layout.addRow(
            "Profession",
            self.profession,
        )

        self.form_layout.addRow(
            "Notes",
            self.notes,
        )

        self.form_layout.addRow(
            "Patient actif",
            self.actif,
        )

        self.layout.addWidget(
            self.formulaire
        )

        self.nom.setFocus()
    # =====================================================
    # Chargement d'un patient
    # =====================================================

    def charger_patient(self) -> None:
        """
        Charge les informations du patient
        dans le formulaire.
        """

        if self.patient is None:
            return

        self.nom.setText(self.patient.nom)

        self.prenom.setText(self.patient.prenom)

        self.telephone.setText(self.patient.telephone)

        if self.patient.date_naissance:

            self.date_naissance.setText(
                self.patient.date_naissance.strftime(
                    "%d/%m/%Y"
                )
            )

        self.adresse.setText(
            self.patient.adresse or ""
        )

        self.email.setText(
            self.patient.email or ""
        )

        self.profession.setText(
            self.patient.profession or ""
        )

        self.notes.setPlainText(
            self.patient.notes or ""
        )

        self.actif.setChecked(
            self.patient.actif
        )

    # =====================================================
    # Validation
    # =====================================================

    def valider(self) -> bool:
        """
        Vérifie les informations du formulaire.
        """

        if not self.nom.text().strip():

            QMessageBox.warning(
                self,
                "Validation",
                "Le nom est obligatoire.",
            )

            self.nom.setFocus()

            return False

        if not self.prenom.text().strip():

            QMessageBox.warning(
                self,
                "Validation",
                "Le prénom est obligatoire.",
            )

            self.prenom.setFocus()

            return False

        if not self.telephone.text().strip():

            QMessageBox.warning(
                self,
                "Validation",
                "Le téléphone est obligatoire.",
            )

            self.telephone.setFocus()

            return False

        email = self.email.text().strip()

        if email and "@" not in email:

            QMessageBox.warning(
                self,
                "Validation",
                "Adresse e-mail invalide.",
            )

            self.email.setFocus()

            return False

        date = self.date_naissance.text().strip()

        if date:

            try:

                datetime.strptime(
                    date,
                    "%d/%m/%Y",
                )

            except ValueError:

                QMessageBox.warning(
                    self,
                    "Validation",
                    "La date doit être au format JJ/MM/AAAA.",
                )

                self.date_naissance.setFocus()

                return False

        return True        
    # =====================================================
    # Enregistrement
    # =====================================================

    def enregistrer(self) -> None:
        """
        Crée ou modifie un patient.
        """

        if not self.valider():
            return

        date_naissance = None

        if self.date_naissance.text().strip():

            date_naissance = datetime.strptime(
                self.date_naissance.text().strip(),
                "%d/%m/%Y",
            ).date()

        try:

            # ==========================================
            # Création
            # ==========================================

            if self.patient is None:

                patient = Patient(
                    nom=self.nom.text().strip(),
                    prenom=self.prenom.text().strip(),
                    telephone=self.telephone.text().strip(),
                    date_naissance=date_naissance,
                    adresse=self.adresse.text().strip() or None,
                    email=self.email.text().strip() or None,
                    profession=self.profession.text().strip() or None,
                    notes=self.notes.toPlainText().strip() or None,
                    actif=self.actif.isChecked(),
                )

                self.controller.creer_patient(
                    patient
                )

                QMessageBox.information(
                    self,
                    "Succès",
                    "Le patient a été créé avec succès.",
                )

            # ==========================================
            # Modification
            # ==========================================

            else:

                self.patient.nom = self.nom.text().strip()

                self.patient.prenom = self.prenom.text().strip()

                self.patient.telephone = self.telephone.text().strip()

                self.patient.date_naissance = date_naissance

                self.patient.adresse = (
                    self.adresse.text().strip()
                    or None
                )

                self.patient.email = (
                    self.email.text().strip()
                    or None
                )

                self.patient.profession = (
                    self.profession.text().strip()
                    or None
                )

                self.patient.notes = (
                    self.notes.toPlainText().strip()
                    or None
                )

                self.patient.actif = (
                    self.actif.isChecked()
                )

                self.controller.modifier_patient(
                    self.patient
                )

                QMessageBox.information(
                    self,
                    "Succès",
                    "Le patient a été modifié avec succès.",
                )

            self.accept()

        except ValueError as erreur:

            QMessageBox.warning(
                self,
                "Erreur",
                str(erreur),
            )

        except Exception as erreur:

            QMessageBox.critical(
                self,
                "Erreur",
                f"Une erreur est survenue.\n\n{erreur}",
            )
        # ---------------------------------------------
        # Conversion de la date
        # ---------------------------------------------

        date_naissance = None

        if self.date_naissance.text().strip():

            date_naissance = datetime.strptime(
                self.date_naissance.text().strip(),
                "%d/%m/%Y",
            ).date()

        # ---------------------------------------------
        # Création
        # ---------------------------------------------

        if self.patient is None:

            patient = Patient(
                nom=self.nom.text().strip(),
                prenom=self.prenom.text().strip(),
                telephone=self.telephone.text().strip(),
                date_naissance=date_naissance,
                adresse=self.adresse.text().strip() or None,
                email=self.email.text().strip() or None,
                profession=self.profession.text().strip() or None,
                notes=self.notes.toPlainText().strip() or None,
                actif=self.actif.isChecked(),
            )

            self.controller.creer_patient(
                patient
            )

            QMessageBox.information(
                self,
                "Succès",
                "Le patient a été créé avec succès.",
            )

        # ---------------------------------------------
        # Modification
        # ---------------------------------------------

        else:

            self.patient.nom = self.nom.text().strip()

            self.patient.prenom = self.prenom.text().strip()

            self.patient.telephone = self.telephone.text().strip()

            self.patient.date_naissance = date_naissance

            self.patient.adresse = (
                self.adresse.text().strip() or None
            )

            self.patient.email = (
                self.email.text().strip() or None
            )

            self.patient.profession = (
                self.profession.text().strip() or None
            )

            self.patient.notes = (
                self.notes.toPlainText().strip() or None
            )

            self.patient.actif = self.actif.isChecked()

            self.controller.modifier_patient()

            QMessageBox.information(
                self,
                "Succès",
                "Le patient a été modifié avec succès.",
            )

        self.accept()
    # =====================================================
    # Réinitialisation
    # =====================================================

    def vider_formulaire(self) -> None:
        """
        Réinitialise tous les champs du formulaire.
        """

        self.nom.clear()

        self.prenom.clear()

        self.telephone.clear()

        self.date_naissance.clear()

        self.adresse.clear()

        self.email.clear()

        self.profession.clear()

        self.notes.clear()

        self.actif.setChecked(True)

        self.nom.setFocus()

    # =====================================================
    # Accesseurs
    # =====================================================

    def est_modification(self) -> bool:
        """
        Retourne True si le dialogue est en mode modification.
        """

        return self.patient is not None

    def get_patient(self) -> Patient | None:
        """
        Retourne le patient courant.
        """

        return self.patient

    # =====================================================
    # Fermeture
    # =====================================================

    def closeEvent(self, event) -> None:
        """
        Gestion de la fermeture de la fenêtre.
        """

        event.accept()