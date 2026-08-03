"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : base_window.py
Description : Fenêtre de base de toutes les interfaces.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QMessageBox,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class BaseWindow(QMainWindow):
    """
    Fenêtre principale utilisée par toutes les pages
    d'OptiManager Pro.
    """

    def __init__(
        self,
        titre: str = "OptiManager Pro",
    ):
        super().__init__()

        self.setWindowTitle(titre)

        self.resize(1400, 850)

        self.setMinimumSize(1100, 700)

        self._creer_interface()

    # =====================================================
    # Construction
    # =====================================================

    def _creer_interface(self):

        self._creer_toolbar()

        self._creer_centre()

        self._creer_statusbar()

    # =====================================================
    # Zone centrale
    # =====================================================

    def _creer_centre(self):

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        self.layout.setSpacing(12)

        self.central_widget.setLayout(self.layout)

    # =====================================================
    # Toolbar
    # =====================================================

    def _creer_toolbar(self):

        self.toolbar = QToolBar()

        self.toolbar.setMovable(False)

        self.toolbar.setFloatable(False)

        self.toolbar.setToolButtonStyle(
            Qt.ToolButtonTextBesideIcon
        )

        self.addToolBar(self.toolbar)

    # =====================================================
    # StatusBar
    # =====================================================

    def _creer_statusbar(self):

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        self.status.showMessage("Prêt")

    # =====================================================
    # Actions
    # =====================================================

    def ajouter_action(
        self,
        texte,
        callback,
        raccourci=None,
    ):

        action = QAction(texte, self)

        if raccourci:
            action.setShortcut(raccourci)

        action.triggered.connect(callback)

        self.toolbar.addAction(action)

        return action

    # =====================================================
    # Widgets
    # =====================================================

    def ajouter_widget(self, widget):

        self.layout.addWidget(widget)

    # =====================================================
    # Titres
    # =====================================================

    def ajouter_titre(self, texte):

        titre = QLabel(texte)

        titre.setStyleSheet(
            """
            QLabel{
                font-size:22px;
                font-weight:bold;
            }
            """
        )

        self.layout.addWidget(titre)

        return titre

    # =====================================================
    # Messages
    # =====================================================

    def information(
        self,
        titre,
        message,
    ):

        QMessageBox.information(
            self,
            titre,
            message,
        )

    def erreur(
        self,
        titre,
        message,
    ):

        QMessageBox.critical(
            self,
            titre,
            message,
        )

    def confirmation(
        self,
        titre,
        message,
    ):

        return QMessageBox.question(
            self,
            titre,
            message,
        )

    # =====================================================
    # Barre d'état
    # =====================================================

    def afficher_message(
        self,
        message,
        duree=3000,
    ):

        self.status.showMessage(
            message,
            duree,
        )