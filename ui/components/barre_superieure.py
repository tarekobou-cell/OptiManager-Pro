from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout
)


class BarreSuperieure(QWidget):

    def __init__(self, utilisateur):
        super().__init__()

        self.utilisateur = utilisateur

        self.creer_interface()


    def creer_interface(self):

        layout = QHBoxLayout()


        titre = QLabel(
            "OptiManager Pro"
        )


        utilisateur = QLabel(
            f"Connecté : {self.utilisateur.prenom} "
            f"{self.utilisateur.nom}"
        )


        bouton = QPushButton(
            "Déconnexion"
        )


        layout.addWidget(titre)
        layout.addStretch()
        layout.addWidget(utilisateur)
        layout.addWidget(bouton)


        self.setLayout(layout)