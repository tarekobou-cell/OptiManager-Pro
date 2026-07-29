from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem
)


class ListePatients(QWidget):

    def __init__(self):
        super().__init__()

        self.creer_interface()


    def creer_interface(self):

        layout_principal = QVBoxLayout()


        # Titre
        titre = QLabel(
            "Gestion des patients"
        )


        # Barre de recherche
        zone_recherche = QHBoxLayout()

        self.recherche = QLineEdit()

        self.recherche.setPlaceholderText(
            "Rechercher un patient..."
        )

        bouton_recherche = QPushButton(
            "Rechercher"
        )


        zone_recherche.addWidget(
            self.recherche
        )

        zone_recherche.addWidget(
            bouton_recherche
        )


        # Bouton ajout
        bouton_ajouter = QPushButton(
            "Ajouter un patient"
        )


        # Tableau patients
        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(
            [
                "Nom",
                "Prénom",
                "Téléphone",
                "Dernière visite",
                "Type verre"
            ]
        )


        self.table.setRowCount(0)


        # Assemblage
        layout_principal.addWidget(
            titre
        )

        layout_principal.addLayout(
            zone_recherche
        )

        layout_principal.addWidget(
            bouton_ajouter
        )

        layout_principal.addWidget(
            self.table
        )


        self.setLayout(
            layout_principal
        )