from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout
)

from PySide6.QtCore import Qt


class TopBar(QWidget):

    def __init__(self, utilisateur):
        super().__init__()

        self.utilisateur = utilisateur

        self.setFixedHeight(60)

        self.setStyleSheet("""
            QWidget{
                background:white;
                border-bottom:1px solid #E5E7EB;
            }

            QLabel#titre{
                font-size:22px;
                font-weight:bold;
                color:#0F172A;
            }

            QLabel#user{
                color:#64748B;
                font-size:13px;
                font-weight:normal;
            }
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(20, 10, 20, 10)

        # =========================
        # Titre dynamique
        # =========================

        self.titre = QLabel("Tableau de bord")
        self.titre.setObjectName("titre")

        layout.addWidget(self.titre)

        layout.addStretch()

        # =========================
        # Utilisateur connecté
        # =========================

        self.user = QLabel(
            f"Bienvenue : {self.utilisateur.login}"
        )

        self.user.setObjectName("user")

        layout.addWidget(self.user)