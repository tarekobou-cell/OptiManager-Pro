from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QSizePolicy
)

from PySide6.QtCore import Qt


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(240)

        self.setObjectName("sidebar")

        self.setStyleSheet("""

#sidebar{
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

    border-radius:8px;

    text-align:left;

    padding:14px 18px;

    font-size:14px;

}

QPushButton:hover{

    background:#334155;

}

QPushButton:checked{

    background:#2563EB;

    font-weight:bold;

}

        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(10,10,10,10)

        layout.setSpacing(6)

        titre = QLabel("OptiManager")

        titre.setAlignment(Qt.AlignCenter)

        layout.addWidget(titre)

        self.buttons = {}

        menus = [

            ("dashboard","🏠 Tableau de bord"),

            ("patients","👤 Patients"),

            ("consultations","🩺 Consultations"),

            ("prescriptions","📄 Prescriptions"),

            ("ventes","🛒 Ventes"),

            ("stock","📦 Stock"),

            ("rendezvous","📅 Rendez-vous"),

            ("statistiques","📊 Statistiques"),

            ("parametres","⚙ Paramètres")

        ]

        for cle, texte in menus:

            bouton = QPushButton(texte)

            bouton.setCheckable(True)

            bouton.setCursor(Qt.PointingHandCursor)

            bouton.setSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Fixed
            )

            layout.addWidget(bouton)

            self.buttons[cle] = bouton

        layout.addStretch()

        self.buttons["dashboard"].setChecked(True)
    # ===================================================
    # Désélection de tous les boutons
    # ===================================================

    def deselectionner(self):

        for bouton in self.buttons.values():

            bouton.setChecked(False)

    # ===================================================
    # Connexion avec le Dashboard
    # ===================================================

    def connecter(self, dashboard):

        self.buttons["dashboard"].clicked.connect(

            lambda: self.changer_page(
                "dashboard",
                dashboard.afficher_dashboard
            )

        )

        self.buttons["patients"].clicked.connect(

            lambda: self.changer_page(
                "patients",
                dashboard.afficher_patients
            )

        )

    # ===================================================
    # Changement de page
    # ===================================================

    def changer_page(self, page, fonction):

        self.deselectionner()

        self.buttons[page].setChecked(True)

        fonction()