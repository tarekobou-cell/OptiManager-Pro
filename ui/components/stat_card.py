from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class StatCard(QFrame):

    def __init__(self, titre, valeur):

        super().__init__()

        self.setMinimumHeight(140)

        self.setStyleSheet("""

QFrame{

    background:white;

    border:1px solid #E5E7EB;

    border-radius:12px;

}

QLabel{

    border:none;

    background:transparent;

}

        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20,20,20,20)

        self.titre = QLabel(titre)

        self.titre.setStyleSheet("""

font-size:14px;

color:#64748B;

        """)

        self.valeur = QLabel(str(valeur))

        self.valeur.setAlignment(Qt.AlignCenter)

        self.valeur.setStyleSheet("""

font-size:34px;

font-weight:bold;

color:#0F172A;

        """)

        layout.addWidget(self.titre)

        layout.addStretch()

        layout.addWidget(self.valeur)

        layout.addStretch()

    # =========================================

    def setValue(self, valeur):

        self.valeur.setText(str(valeur))
        