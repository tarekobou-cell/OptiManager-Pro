from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        self.setStyleSheet("""
            QWidget{
                background:#1E293B;
            }

            QLabel{
                color:white;
                font-size:22px;
                font-weight:bold;
                padding:20px;
            }

            QPushButton{
                color:white;
                background:transparent;
                border:none;
                text-align:left;
                padding:12px 20px;
                font-size:14px;
            }

            QPushButton:hover{
                background:#334155;
            }
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        titre = QLabel("OptiManager")
        layout.addWidget(titre)

        menus = [
            "🏠 Tableau de bord",
            "👤 Patients",
            "🩺 Consultations",
            "📄 Prescriptions",
            "📦 Stock",
            "🛒 Ventes",
            "📅 Rendez-vous",
            "📊 Statistiques",
            "⚙ Paramètres"
        ]

        self.buttons = {}

        for menu in menus:

            bouton = QPushButton(menu)

            bouton.setCursor(Qt.PointingHandCursor)

            layout.addWidget(bouton)

            self.buttons[menu] = bouton

        layout.addStretch()

        self.setLayout(layout)

    # ===================================================
    # Connexion des boutons avec le Dashboard
    # ===================================================

    def connecter(self, dashboard):

        self.buttons["🏠 Tableau de bord"].clicked.connect(
            dashboard.afficher_dashboard
        )

        self.buttons["👤 Patients"].clicked.connect(
            dashboard.afficher_patients
        )