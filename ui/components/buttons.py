"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : buttons.py
Description : Boutons réutilisables du logiciel.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import QPushButton


class PrimaryButton(QPushButton):
    """
    Bouton principal.
    """

    def __init__(self, texte: str):

        super().__init__(texte)

        self.setMinimumHeight(38)

        self.setStyleSheet("""
            QPushButton{
                background:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:8px 16px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#1D4ED8;
            }

            QPushButton:pressed{
                background:#1E40AF;
            }
        """)


class SuccessButton(QPushButton):

    def __init__(self, texte: str):

        super().__init__(texte)

        self.setMinimumHeight(38)

        self.setStyleSheet("""
            QPushButton{
                background:#22C55E;
                color:white;
                border:none;
                border-radius:8px;
                padding:8px 16px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#16A34A;
            }
        """)


class DangerButton(QPushButton):

    def __init__(self, texte: str):

        super().__init__(texte)

        self.setMinimumHeight(38)

        self.setStyleSheet("""
            QPushButton{
                background:#EF4444;
                color:white;
                border:none;
                border-radius:8px;
                padding:8px 16px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#DC2626;
            }
        """)


class SecondaryButton(QPushButton):

    def __init__(self, texte: str):

        super().__init__(texte)

        self.setMinimumHeight(38)

        self.setStyleSheet("""
            QPushButton{
                background:white;
                color:#374151;
                border:1px solid #D1D5DB;
                border-radius:8px;
                padding:8px 16px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#F3F4F6;
            }
        """)