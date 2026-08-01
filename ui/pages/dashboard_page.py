from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout
)

from ui.components.stat_card import StatCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.creer_interface()

    # ==================================================

    def creer_interface(self):

        layout = QVBoxLayout(self)

        titre = QLabel("Tableau de bord")

        titre.setStyleSheet("""

font-size:28px;

font-weight:bold;

padding:15px;

        """)

        layout.addWidget(titre)

        grille = QGridLayout()

        self.nb_patients = StatCard(
            "Patients",
            "0"
        )

        self.nb_consultations = StatCard(
            "Consultations",
            "0"
        )

        self.nb_ventes = StatCard(
            "Ventes",
            "0"
        )

        self.chiffre_affaires = StatCard(
            "Chiffre d'affaires",
            "0 DA"
        )

        grille.addWidget(self.nb_patients,0,0)
        grille.addWidget(self.nb_consultations,0,1)
        grille.addWidget(self.nb_ventes,1,0)
        grille.addWidget(self.chiffre_affaires,1,1)

        layout.addLayout(grille)

        layout.addStretch()