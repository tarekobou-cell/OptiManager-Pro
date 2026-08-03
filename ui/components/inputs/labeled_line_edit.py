"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : labeled_line_edit.py
Description : Champ texte avec libellé.
Auteur : Mohamed Tarek & ChatGPT
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)


class LabeledLineEdit(QWidget):
    """
    Champ texte avec un libellé.
    """

    def __init__(
        self,
        label: str,
        placeholder: str = "",
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.layout.setSpacing(5)

        # ==========================================
        # Label
        # ==========================================

        self.label = QLabel(label)

        self.label.setStyleSheet(
            """
            QLabel{
                font-weight:bold;
            }
            """
        )

        # ==========================================
        # Champ
        # ==========================================

        self.line_edit = QLineEdit()

        self.line_edit.setPlaceholderText(
            placeholder
        )

        self.line_edit.setMinimumHeight(
            34
        )

        # ==========================================
        # Layout
        # ==========================================

        self.layout.addWidget(
            self.label
        )

        self.layout.addWidget(
            self.line_edit
        )

    # =====================================================
    # API
    # =====================================================

    def text(self) -> str:
        return self.line_edit.text()

    def setText(
        self,
        value: str,
    ) -> None:
        self.line_edit.setText(value)

    def clear(self) -> None:
        self.line_edit.clear()

    def setPlaceholderText(
        self,
        text: str,
    ) -> None:
        self.line_edit.setPlaceholderText(text)

    def setReadOnly(
        self,
        value: bool,
    ) -> None:
        self.line_edit.setReadOnly(value)

    def setEnabled(
        self,
        value: bool,
    ) -> None:
        self.line_edit.setEnabled(value)

    def setFocus(self) -> None:
        self.line_edit.setFocus()

    def widget(self) -> QLineEdit:
        """
        Retourne le QLineEdit interne.
        """
        return self.line_edit