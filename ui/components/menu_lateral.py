from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel
)


class MenuLateral(QWidget):

    def __init__(self):
        super().__init__()

        self.creer_interface()


    def creer_interface(self):

        layout = QVBoxLayout()

        titre = QLabel(
            "OptiManager Pro"
        )

        layout.addWidget(titre)


        boutons = [
            "👤 Patients",
            "👓 Prescriptions",
            "🕶 Produits",
            "📦 Stock",
            "💰 Ventes",
            "🔧 Réparations",
            "📊 Statistiques",
            "⚙ Paramètres",
            "🚪 Déconnexion"
        ]


        for texte in boutons:

            bouton = QPushButton(
                texte
            )

            layout.addWidget(bouton)


        layout.addStretch()

        self.setLayout(layout)