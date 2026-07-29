from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton
)


class DashboardWindow(QMainWindow):

    def __init__(self, utilisateur):
        super().__init__()

        self.utilisateur = utilisateur

        self.setWindowTitle(
            "OptiManager Pro - Tableau de bord"
        )

        self.resize(1100, 700)

        self.creer_interface()


    def creer_interface(self):

        central = QWidget()

        layout = QVBoxLayout()

        titre = QLabel(
            f"Bienvenue {self.utilisateur.prenom} "
            f"{self.utilisateur.nom}"
        )

        bouton_deconnexion = QPushButton(
            "Déconnexion"
        )

        layout.addWidget(titre)
        layout.addWidget(bouton_deconnexion)

        central.setLayout(layout)

        self.setCentralWidget(central)