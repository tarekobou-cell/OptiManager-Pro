from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        titre = QLabel("Bienvenue sur OptiManager Pro")
        titre.setAlignment(Qt.AlignCenter)

        titre.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#0F172A;
        """)

        texte = QLabel(
            "Le tableau de bord affichera prochainement\n"
            "les statistiques de votre magasin."
        )

        texte.setAlignment(Qt.AlignCenter)

        texte.setStyleSheet("""
            font-size:15px;
            color:#64748B;
        """)

        layout.addStretch()

        layout.addWidget(titre)

        layout.addWidget(texte)

        layout.addStretch()