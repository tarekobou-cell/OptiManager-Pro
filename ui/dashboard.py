from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget
)

from ui.components.sidebar import Sidebar
from ui.components.topbar import TopBar

from ui.pages.patients_page import PatientsPage


class DashboardWindow(QWidget):

    def __init__(self, utilisateur):
        super().__init__()

        self.utilisateur = utilisateur

        self.setWindowTitle("OptiManager Pro")
        self.resize(1400, 800)

        self.creer_interface()

    def creer_interface(self):

        # ==========================================
        # Layout principal
        # ==========================================

        layout_principal = QHBoxLayout(self)

        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        # ==========================================
        # Sidebar
        # ==========================================

        self.sidebar = Sidebar()

        layout_principal.addWidget(self.sidebar)

        # ==========================================
        # Partie droite
        # ==========================================

        droite = QWidget()

        layout_principal.addWidget(droite)

        layout_droite = QVBoxLayout(droite)

        layout_droite.setContentsMargins(0, 0, 0, 0)

        layout_droite.setSpacing(0)

        # ==========================================
        # TopBar
        # ==========================================

        self.topbar = TopBar(self.utilisateur)

        layout_droite.addWidget(self.topbar)

        # ==========================================
        # Pages
        # ==========================================

        self.stack = QStackedWidget()

        layout_droite.addWidget(self.stack)

        # ==========================================
        # Dashboard
        # ==========================================

        self.page_dashboard = QWidget()

        accueil = QVBoxLayout(self.page_dashboard)

        titre = QLabel("Bienvenue sur OptiManager Pro")

        titre.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:25px;
        """)

        accueil.addWidget(titre)

        accueil.addStretch()

        # ==========================================
        # Patients
        # ==========================================

        self.page_patients = PatientsPage()

        # ==========================================
        # Ajout des pages
        # ==========================================

        self.stack.addWidget(self.page_dashboard)
        self.stack.addWidget(self.page_patients)

        self.stack.setCurrentWidget(
            self.page_dashboard
        )

        # ==========================================
        # Connexion Sidebar
        # ==========================================

        self.sidebar.connecter(self)

    # =======================================================
    # Navigation
    # =======================================================

    def afficher_dashboard(self):

        self.topbar.titre.setText(
            "Tableau de bord"
        )

        self.stack.setCurrentWidget(
            self.page_dashboard
        )

    def afficher_patients(self):

        self.topbar.titre.setText(
            "Patients"
        )

       
        self.stack.setCurrentWidget(
            self.page_patients
        )