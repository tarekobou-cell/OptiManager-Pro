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

from sqlalchemy.orm import object_session

from ui.components.base_window import BaseWindow

from ui.dialogs.patient_contact_dialog import (
    PatientContactDialog,
)

from ui.dialogs.patient_insurance_dialog import (
    PatientInsuranceDialog,
)


class PatientProfile(BaseWindow):

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
            self.obtenir_nom_patient()
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
            f"N° dossier : {self.obtenir_numero_dossier()}"
        )

        self.statut = QLabel(
            self.obtenir_statut()
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

        self.btn_modifier = QPushButton("Modifier")
        self.btn_imprimer = QPushButton("Imprimer")
        self.btn_archiver = QPushButton("Archiver")

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
    # Données patient
    # =====================================================

    def obtenir_nom_patient(self) -> str:
        if self.patient is None:
            return "Patient"

        prenom = (
            self.patient.prenom or ""
        ).strip()

        nom = (
            self.patient.nom or ""
        ).strip()

        return (
            f"{prenom} {nom}".strip()
            or "Patient"
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

        naissance = self.patient.date_naissance
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

    def obtenir_adresse(self) -> str:
        if self.patient is None:
            return "---"

        return (
            self.patient.adresse
            or "---"
        )

    def obtenir_derniere_visite(self) -> str:
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
            self.creer_assurance(),
            "Assurance",
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

            label_titre = QLabel(titre)
            label_titre.setStyleSheet(
                "font-weight: bold;"
            )

            label_valeur = QLabel(valeur)
            label_valeur.setWordWrap(True)

            bloc.addWidget(label_titre)
            bloc.addWidget(label_valeur)

            grid.addLayout(
                bloc,
                0,
                colonne,
            )

        return cadre

    # =====================================================
    # Identité
    # =====================================================

    def creer_identite(self):
        widget = QWidget()

        layout = QGridLayout(widget)

        donnees = [
            (
                "Nom",
                (
                    self.patient.nom
                    if self.patient
                    else "---"
                ),
            ),
            (
                "Prénom",
                (
                    self.patient.prenom
                    if self.patient
                    else "---"
                ),
            ),
            (
                "Date de naissance",
                (
                    self.patient.date_naissance.strftime(
                        "%d/%m/%Y"
                    )
                    if (
                        self.patient
                        and self.patient.date_naissance
                    )
                    else "---"
                ),
            ),
            (
                "Profession",
                (
                    self.patient.profession
                    or "---"
                    if self.patient
                    else "---"
                ),
            ),
            (
                "Notes",
                (
                    self.patient.notes
                    or "---"
                    if self.patient
                    else "---"
                ),
            ),
        ]

        for ligne, (
            titre,
            valeur,
        ) in enumerate(donnees):

            label_titre = QLabel(titre)
            label_titre.setStyleSheet(
                "font-weight: bold;"
            )

            label_valeur = QLabel(
                str(valeur)
            )

            label_valeur.setWordWrap(True)

            layout.addWidget(
                label_titre,
                ligne,
                0,
            )

            layout.addWidget(
                label_valeur,
                ligne,
                1,
            )

        layout.setColumnStretch(
            1,
            1,
        )

        return widget

    # =====================================================
    # Coordonnées
    # =====================================================

    def creer_coordonnees(self):
        widget = QWidget()

        layout = QGridLayout(widget)

        donnees = [
            (
                "Téléphone",
                self.obtenir_telephone(),
            ),
            (
                "Email",
                self.obtenir_email(),
            ),
            (
                "Adresse",
                self.obtenir_adresse(),
            ),
        ]

        for ligne, (
            titre,
            valeur,
        ) in enumerate(donnees):

            label_titre = QLabel(titre)
            label_titre.setStyleSheet(
                "font-weight: bold;"
            )

            label_valeur = QLabel(valeur)
            label_valeur.setWordWrap(True)

            layout.addWidget(
                label_titre,
                ligne,
                0,
            )

            layout.addWidget(
                label_valeur,
                ligne,
                1,
            )

        layout.setColumnStretch(
            1,
            1,
        )

        return widget

    # =====================================================
    # Assurance
    # =====================================================

    def creer_assurance(self):
        widget = QWidget()

        layout = QVBoxLayout(widget)
        layout.setSpacing(12)

        btn_ajouter = QPushButton(
            "➕ Ajouter assurance"
        )

        btn_ajouter.clicked.connect(
            self.ajouter_assurance
        )

        layout.addWidget(
            btn_ajouter
        )

        assurances = []

        if self.patient is not None:
            assurances = list(
                getattr(
                    self.patient,
                    "insurances",
                    [],
                )
            )

        if not assurances:

            label = QLabel(
                "Aucune assurance enregistrée."
            )

            label.setStyleSheet(
                """
                QLabel {
                    font-size: 16px;
                    padding: 20px;
                }
                """
            )

            layout.addWidget(
                label
            )

            layout.addStretch()

            return widget

        for assurance in assurances:

            carte = QFrame()

            carte.setFrameShape(
                QFrame.StyledPanel
            )

            carte_layout = QGridLayout(
                carte
            )

            donnees = [
                (
                    "Organisme",
                    assurance.organisme
                    or "---",
                ),
                (
                    "N° assuré",
                    assurance.numero_assure
                    or "---",
                ),
                (
                    "N° contrat",
                    assurance.numero_contrat
                    or "---",
                ),
                (
                    "Type de couverture",
                    assurance.type_couverture
                    or "---",
                ),
                (
                    "Date début",
                    (
                        assurance.date_debut.strftime(
                            "%d/%m/%Y"
                        )
                        if assurance.date_debut
                        else "---"
                    ),
                ),
                (
                    "Date fin",
                    (
                        assurance.date_fin.strftime(
                            "%d/%m/%Y"
                        )
                        if assurance.date_fin
                        else "---"
                    ),
                ),
                (
                    "Statut",
                    (
                        "Active"
                        if assurance.actif
                        else "Inactive"
                    ),
                ),
                (
                    "Observations",
                    assurance.observations
                    or "---",
                ),
            ]

            for ligne, (
                titre,
                valeur,
            ) in enumerate(donnees):

                label_titre = QLabel(titre)

                label_titre.setStyleSheet(
                    "font-weight: bold;"
                )

                label_valeur = QLabel(
                    str(valeur)
                )

                label_valeur.setWordWrap(
                    True
                )

                carte_layout.addWidget(
                    label_titre,
                    ligne,
                    0,
                )

                carte_layout.addWidget(
                    label_valeur,
                    ligne,
                    1,
                )

            layout.addWidget(
                carte
            )

        layout.addStretch()

        return widget

    # =====================================================
    # Ajouter assurance
    # =====================================================

    def ajouter_assurance(self):

        if self.patient is None:
            return

        dialog = PatientInsuranceDialog(
            patient=self.patient,
            parent=self,
        )

        if not dialog.exec():
            return

        assurance = (
            dialog.obtenir_assurance()
        )

        session = object_session(
            self.patient
        )

        if session is None:
            return

        session.add(
            assurance
        )

        session.commit()

        session.refresh(
            self.patient
        )

        nouvelle_fiche = self.__class__(
            patient=self.patient
        )

        self._nouvelle_fiche = (
            nouvelle_fiche
        )

        nouvelle_fiche.show()

        self.close()

    # =====================================================
    # Contacts
    # =====================================================

    def creer_contacts(self):
        widget = QWidget()

        layout = QVBoxLayout(widget)
        layout.setSpacing(12)

        btn_ajouter = QPushButton(
            "➕ Ajouter contact"
        )

        btn_ajouter.clicked.connect(
            self.ajouter_contact
        )

        layout.addWidget(
            btn_ajouter
        )

        contacts = []

        if self.patient is not None:
            contacts = list(
                getattr(
                    self.patient,
                    "contacts",
                    [],
                )
            )

        if not contacts:

            label = QLabel(
                "Aucun contact enregistré."
            )

            label.setStyleSheet(
                """
                QLabel {
                    font-size: 16px;
                    padding: 20px;
                }
                """
            )

            layout.addWidget(label)
            layout.addStretch()

            return widget

        for contact in contacts:

            carte = QFrame()

            carte.setFrameShape(
                QFrame.StyledPanel
            )

            carte_layout = QVBoxLayout(
                carte
            )

            nom = (
                f"{contact.prenom or ''} "
                f"{contact.nom or ''}"
            ).strip()

            titre = QLabel(
                nom or "Contact"
            )

            titre.setStyleSheet(
                """
                QLabel {
                    font-size: 18px;
                    font-weight: bold;
                }
                """
            )

            relation = QLabel(
                f"Relation : "
                f"{contact.relation or '---'}"
            )

            telephone = QLabel(
                f"Téléphone : "
                f"{contact.telephone or '---'}"
            )

            telephone_secondaire = QLabel(
                "Téléphone secondaire : "
                f"{contact.telephone_secondaire or '---'}"
            )

            email = QLabel(
                f"Email : "
                f"{contact.email or '---'}"
            )

            adresse = QLabel(
                f"Adresse : "
                f"{contact.adresse or '---'}"
            )

            indications = []

            if contact.contact_principal:
                indications.append(
                    "Contact principal"
                )

            if contact.contact_urgence:
                indications.append(
                    "Contact d'urgence"
                )

            carte_layout.addWidget(titre)
            carte_layout.addWidget(relation)
            carte_layout.addWidget(telephone)
            carte_layout.addWidget(
                telephone_secondaire
            )
            carte_layout.addWidget(email)
            carte_layout.addWidget(adresse)

            if indications:

                indication = QLabel(
                    " • ".join(indications)
                )

                indication.setStyleSheet(
                    "font-weight: bold;"
                )

                carte_layout.addWidget(
                    indication
                )

            layout.addWidget(
                carte
            )

        layout.addStretch()

        return widget

    # =====================================================
    # Ajouter contact
    # =====================================================

    def ajouter_contact(self):

        if self.patient is None:
            return

        dialog = PatientContactDialog(
            patient=self.patient,
            parent=self,
        )

        if not dialog.exec():
            return

        contact = (
            dialog.obtenir_contact()
        )

        session = object_session(
            self.patient
        )

        if session is None:
            return

        session.add(
            contact
        )

        session.commit()

        session.refresh(
            self.patient
        )

        nouvelle_fiche = self.__class__(
            patient=self.patient
        )

        self._nouvelle_fiche = (
            nouvelle_fiche
        )

        nouvelle_fiche.show()

        self.close()

    # =====================================================
    # Autres sections
    # =====================================================

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