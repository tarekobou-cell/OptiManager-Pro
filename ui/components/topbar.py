from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class TopBar(QWidget):

    def __init__(self, utilisateur):

        super().__init__()

        self.utilisateur = utilisateur

        self.setFixedHeight(70)

        self.setStyleSheet("""

QWidget{

    background:white;

    border-bottom:1px solid #E5E7EB;

}

QLabel{

    color:#1E293B;

}

QPushButton{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:6px;

    padding:8px 16px;

}

QPushButton:hover{

    background:#1D4ED8;

}

        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(20, 10, 20, 10)

        self.titre = QLabel("Tableau de bord")

        police = QFont()

        police.setPointSize(16)

        police.setBold(True)

        self.titre.setFont(police)

        layout.addWidget(self.titre)

        layout.addStretch()

        self.nom_utilisateur = QLabel(

            f"{utilisateur.prenom} {utilisateur.nom}"

        )

        layout.addWidget(self.nom_utilisateur)

        self.btn_deconnexion = QPushButton("Déconnexion")

        layout.addWidget(self.btn_deconnexion)