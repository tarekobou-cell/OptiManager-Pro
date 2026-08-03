"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : base_field.py
Description : Classe abstraite de tous les champs.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from ui.theme import Theme


class BaseField(QWidget, ABC):
    """
    Classe mère de tous les champs.

    Cette classe ne crée jamais
    le widget de saisie.

    Celui-ci sera injecté par
    les classes filles.
    """

    def __init__(
        self,
        label: str,
        required: bool = False,
        tooltip: str = "",
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._required = required

        self._field: QWidget | None = None

        self._build_ui(
            label,
            tooltip,
        )

    # =====================================================
    # Construction
    # =====================================================

    def _build_ui(
        self,
        label: str,
        tooltip: str,
    ) -> None:
        """
        Construit l'interface du champ.
        """

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            Theme.spacing.MARGIN_NONE,
            Theme.spacing.MARGIN_NONE,
            Theme.spacing.MARGIN_NONE,
            Theme.spacing.MARGIN_NONE,
        )

        self.layout.setSpacing(
            Theme.spacing.LAYOUT_SPACING_SM
        )

        # -------------------------------------------------
        # Label
        # -------------------------------------------------

        texte = label

        if self._required:
            texte += " *"

        self.label = QLabel(texte)

        self.label.setFont(
            Theme.fonts.FONT_LABEL
        )

        self.label.setAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )

        if tooltip:
            self.label.setToolTip(
                tooltip
            )

        self.layout.addWidget(
            self.label
        )

        # -------------------------------------------------
        # Le widget sera ajouté ici
        # -------------------------------------------------

        # -------------------------------------------------
        # Message d'erreur
        # -------------------------------------------------

        self.error_label = QLabel()

        self.error_label.setVisible(False)

        self.error_label.setWordWrap(True)

        self.error_label.setStyleSheet(
            f"""
            QLabel {{
                color: {Theme.colors.DANGER};
            }}
            """
        )

        self.layout.addWidget(
            self.error_label
        )

    # =====================================================
    # Injection du widget
    # =====================================================

    def set_field(
        self,
        widget: QWidget,
    ) -> None:
        """
        Injecte le widget de saisie.
        """

        self._field = widget

        self.layout.insertWidget(
            1,
            widget,
        )

    # =====================================================
    # Accès au widget
    # =====================================================

    @property
    def field(self) -> QWidget:
        """
        Retourne le widget interne.
        """

        if self._field is None:
            raise RuntimeError(
                "Aucun widget n'a été injecté dans BaseField."
            )

        return self._field
    # =====================================================
    # Erreurs
    # =====================================================

    def show_error(
        self,
        message: str,
    ) -> None:
        """
        Affiche un message d'erreur.
        """

        self.error_label.setText(message)

        self.error_label.setVisible(True)

    def clear_error(
        self,
    ) -> None:
        """
        Masque le message d'erreur.
        """

        self.error_label.clear()

        self.error_label.setVisible(False)

    # =====================================================
    # Etat
    # =====================================================

    def set_required(
        self,
        required: bool,
    ) -> None:
        """
        Définit si le champ est obligatoire.
        """

        self._required = required

    def is_required(
        self,
    ) -> bool:
        """
        Retourne True si le champ est obligatoire.
        """

        return self._required

    def set_enabled(
        self,
        enabled: bool,
    ) -> None:
        """
        Active ou désactive le champ.
        """

        self.field.setEnabled(enabled)

    def set_read_only(
        self,
        read_only: bool,
    ) -> None:
        """
        Passe le champ en lecture seule.
        """

        if hasattr(
            self.field,
            "setReadOnly",
        ):
            self.field.setReadOnly(
                read_only
            )

    def focus(
        self,
    ) -> None:
        """
        Donne le focus au champ.
        """

        self.field.setFocus()

    # =====================================================
    # Validation
    # =====================================================

    def validate(
        self,
    ) -> bool:
        """
        Validation minimale.

        Les classes filles peuvent
        redéfinir cette méthode.
        """

        self.clear_error()

        return True

    # =====================================================
    # API abstraite
    # =====================================================

    @abstractmethod
    def value(
        self,
    ):
        """
        Retourne la valeur du champ.
        """
        raise NotImplementedError

    @abstractmethod
    def set_value(
        self,
        value,
    ) -> None:
        """
        Définit la valeur du champ.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(
        self,
    ) -> None:
        """
        Vide le champ.
        """
        raise NotImplementedError
    # =====================================================
    # Label
    # =====================================================

    def set_label(
        self,
        text: str,
    ) -> None:
        """
        Modifie le texte du label.
        """

        if self._required:
            text += " *"

        self.label.setText(text)

    def label_text(
        self,
    ) -> str:
        """
        Retourne le texte du label.
        """

        return self.label.text()

    # =====================================================
    # Tooltip
    # =====================================================

    def set_tooltip(
        self,
        text: str,
    ) -> None:
        """
        Définit le tooltip du champ.
        """

        self.label.setToolTip(text)

        self.field.setToolTip(text)

    # =====================================================
    # Visibilité
    # =====================================================

    def show_field(
        self,
    ) -> None:
        """
        Affiche le champ.
        """

        self.show()

    def hide_field(
        self,
    ) -> None:
        """
        Masque le champ.
        """

        self.hide()

    # =====================================================
    # Informations
    # =====================================================

    def has_error(
        self,
    ) -> bool:
        """
        Retourne True si un message
        d'erreur est affiché.
        """

        return self.error_label.isVisible()

    def is_empty(
        self,
    ) -> bool:
        """
        Indique si le champ est vide.

        Les classes filles peuvent
        redéfinir cette méthode.
        """

        value = self.value()

        if value is None:
            return True

        if isinstance(value, str):
            return value.strip() == ""

        return False

    # =====================================================
    # Représentation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(label='{self.label.text()}')"
        )