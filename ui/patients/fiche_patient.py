from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QTextEdit,
    QComboBox
)


class FichePatient(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Fiche patient"
        )

        self.creer_interface()


    def creer_interface(self):

        layout_principal = QVBoxLayout()


        titre = QLabel(
            "Nouvelle fiche patient"
        )


        formulaire = QFormLayout()


        self.nom = QLineEdit()
        self.prenom = QLineEdit()
        self.telephone = QLineEdit()
        self.date_naissance = QLineEdit()
        self.adresse = QLineEdit()

        self.date_visite = QLineEdit()


        # Correction OD

        self.od_sphere = QLineEdit()
        self.od_cylindre = QLineEdit()
        self.od_axe = QLineEdit()


        # Correction OG

        self.og_sphere = QLineEdit()
        self.og_cylindre = QLineEdit()
        self.og_axe = QLineEdit()


        self.type_verre = QComboBox()

        self.type_verre.addItems(
            [
                "Unifocal",
                "Progressif",
                "Bifocal"
            ]
        )


        self.traitement = QComboBox()

        self.traitement.addItems(
            [
                "Aucun",
                "Anti-reflet",
                "Blue Block",
                "Anti-rayures",
                "Hydrophobe"
            ]
        )


        self.notes = QTextEdit()


        formulaire.addRow(
            "Nom",
            self.nom
        )

        formulaire.addRow(
            "Prénom",
            self.prenom
        )

        formulaire.addRow(
            "Téléphone",
            self.telephone
        )

        formulaire.addRow(
            "Date naissance",
            self.date_naissance
        )

        formulaire.addRow(
            "Adresse",
            self.adresse
        )

        formulaire.addRow(
            "Dernière visite",
            self.date_visite
        )


        formulaire.addRow(
            "OD Sphère",
            self.od_sphere
        )

        formulaire.addRow(
            "OD Cylindre",
            self.od_cylindre
        )

        formulaire.addRow(
            "OD Axe",
            self.od_axe
        )


        formulaire.addRow(
            "OG Sphère",
            self.og_sphere
        )

        formulaire.addRow(
            "OG Cylindre",
            self.og_cylindre
        )

        formulaire.addRow(
            "OG Axe",
            self.og_axe
        )


        formulaire.addRow(
            "Type verre",
            self.type_verre
        )

        formulaire.addRow(
            "Traitement",
            self.traitement
        )

        formulaire.addRow(
            "Notes",
            self.notes
        )


        bouton = QPushButton(
            "Enregistrer patient"
        )


        layout_principal.addWidget(
            titre
        )

        layout_principal.addLayout(
            formulaire
        )

        layout_principal.addWidget(
            bouton
        )


        self.setLayout(
            layout_principal
        )