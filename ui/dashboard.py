from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget
)

from ui.components.sidebar import Sidebar
from ui.components.topbar import TopBar

from ui.pages.dashboard_page import DashboardPage
from ui.pages.patients_page import PatientsPage


class DashboardWindow(QWidget):

    def __init__(self, utilisateur):

        super().__init__()

        self.utilisateur = utilisateur

        self.setWindowTitle("OptiManager Pro")

        self.resize(1400, 800)

        self.creer_interface()

    # =====================================================

    def creer_interface(self):

        layout_principal = QHBoxLayout(self)

        layout_principal.setContentsMargins(0, 0, 0, 0)

        layout_principal.setSpacing(0)

        # ==============================================
        # Sidebar
        # ==============================================

        self.sidebar = Sidebar()

        layout_principal.addWidget(self.sidebar)

        # ==============================================
        # Partie droite
        # ==============================================

        droite = QWidget()

        layout_principal.addWidget(droite)

        layout_droite = QVBoxLayout(droite)

        layout_droite.setContentsMargins(0, 0, 0, 0)

        layout_droite.setSpacing(0)

        # ==============================================
        # TopBar
        # ==============================================

        self.topbar = TopBar(self.utilisateur)

        layout_droite.addWidget(self.topbar)

        # ==============================================
        # Stack
        # ==============================================

        self.stack = QStackedWidget()

        layout_droite.addWidget(self.stack)
        # ==============================================
        # Pages
        # ==============================================

        self.page_dashboard = DashboardPage()

        self.page_patients = PatientsPage()

        # ==============================================
        # Ajout des pages
        # ==============================================

        self.stack.addWidget(
            self.page_dashboard
        )

        self.stack.addWidget(
            self.page_patients
        )

        self.stack.setCurrentWidget(
            self.page_dashboard
        )

        # ==============================================
        # Sidebar
        # ==============================================

        self.sidebar.connecter(self)

        # ==============================================
        # TopBar
        # ==============================================

        self.topbar.titre.setText(
            "Tableau de bord"
        )
    # =====================================================
    # Navigation
    # =====================================================

    def afficher_dashboard(self):

        self.topbar.titre.setText(
            "Tableau de bord"
        )

        self.stack.setCurrentWidget(
            self.page_dashboard
        )

    # =====================================================

    def afficher_patients(self):

        self.topbar.titre.setText(
            "Patients"
        )

        self.stack.setCurrentWidget(
            self.page_patients
        )

    # =====================================================
    # Modules en préparation
    # =====================================================

    def afficher_consultations(self):
        pass

    def afficher_prescriptions(self):
        pass

    def afficher_stock(self):
        pass

    def afficher_ventes(self):
        pass

    def afficher_rendezvous(self):
        pass

    def afficher_statistiques(self):
        pass

    def afficher_parametres(self):
        pass