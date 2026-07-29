from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from ui.components.menu_lateral import MenuLateral
from ui.components.barre_superieure import BarreSuperieure
from ui.components.cartes import CarteStatistique


class DashboardWindow(QMainWindow):

    def __init__(self, utilisateur):
        super().__init__()

        self.utilisateur = utilisateur

        self.setWindowTitle(
            "OptiManager Pro - Tableau de bord"
        )

        self.resize(1200, 750)

        self.creer_interface()


    def creer_interface(self):

        # Fenêtre principale
        principal = QWidget()

        layout_principal = QVBoxLayout()


        # Barre supérieure
        barre = BarreSuperieure(
            self.utilisateur
        )


        # Zone centrale
        zone_centrale = QWidget()

        layout_zone = QHBoxLayout()


        # Menu gauche
        menu = MenuLateral()


        # Partie droite avec les statistiques
        contenu = QWidget()

        layout_cartes = QHBoxLayout()


        carte_patients = CarteStatistique(
            "👤 Patients",
            0
        )

        carte_ca = CarteStatistique(
            "💰 Chiffre d'affaires",
            "0 DA"
        )

        carte_stock = CarteStatistique(
            "📦 Stock faible",
            0
        )

        carte_visites = CarteStatistique(
            "📅 Visites aujourd'hui",
            0
        )


        layout_cartes.addWidget(
            carte_patients
        )

        layout_cartes.addWidget(
            carte_ca
        )

        layout_cartes.addWidget(
            carte_stock
        )

        layout_cartes.addWidget(
            carte_visites
        )


        contenu.setLayout(
            layout_cartes
        )


        # Assemblage menu + contenu
        layout_zone.addWidget(
            menu
        )

        layout_zone.addWidget(
            contenu
        )


        zone_centrale.setLayout(
            layout_zone
        )


        # Assemblage final
        layout_principal.addWidget(
            barre
        )

        layout_principal.addWidget(
            zone_centrale
        )


        principal.setLayout(
            layout_principal
        )


        self.setCentralWidget(
            principal
        )