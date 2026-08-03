"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : base_dialog.py
Description : Boîte de dialogue de base.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class BaseDialog(QDialog):
    """
    Classe de base pour toutes les boîtes de dialogue.
    """

    def __init__(
        self,
        titre: str,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setWindowTitle(titre)

        self.setModal(True)

        self.resize(700, 500)

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        self.layout.setSpacing(15)

        self._creer_titre()

        self._creer_contenu()

        self._creer_boutons()

    # =====================================================
    # Titre
    # =====================================================

    def _creer_titre(self) -> None:

        self.lbl_titre = QLabel(
            self.windowTitle()
        )

        self.lbl_titre.setAlignment(
            Qt.AlignCenter
        )

        self.lbl_titre.setStyleSheet(
            """
            QLabel{
                font-size:20px;
                font-weight:bold;
            }
            """
        )

        self.layout.addWidget(
            self.lbl_titre
        )

    # =====================================================
    # Contenu
    # =====================================================

    def _creer_contenu(self) -> None:
        """
        À redéfinir dans les classes filles.
        """
        pass

    # =====================================================
    # Validation
    # =====================================================

    def enregistrer(self) -> None:
        """
        Méthode appelée par défaut lorsque
        l'utilisateur clique sur Enregistrer.

        Les classes filles peuvent la redéfinir.
        """

        self.accept()

    # =====================================================
    # Boutons
    # =====================================================

    def _creer_boutons(self) -> None:

        self.buttons = QDialogButtonBox()

        self.bouton_enregistrer = QPushButton(
            "Enregistrer"
        )

        self.bouton_annuler = QPushButton(
            "Annuler"
        )

        self.buttons.addButton(
            self.bouton_enregistrer,
            QDialogButtonBox.AcceptRole,
        )

        self.buttons.addButton(
            self.bouton_annuler,
            QDialogButtonBox.RejectRole,
        )

        self.bouton_enregistrer.clicked.connect(
            self.enregistrer
        )

        self.bouton_annuler.clicked.connect(
            self.reject
        )

        self.layout.addWidget(
            self.buttons
        )