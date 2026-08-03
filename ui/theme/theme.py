"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : theme.py
Description : Point d'entrée officiel du Design System.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from ui.theme.tokens import animation
from ui.theme.tokens import colors
from ui.theme.tokens import fonts
from ui.theme.tokens import icons
from ui.theme.tokens import metrics
from ui.theme.tokens import radius
from ui.theme.tokens import spacing


class Theme:
    """
    Point d'entrée unique du Design System.

    Utilisation :

        Theme.colors.PRIMARY

        Theme.fonts.FONT_TITLE

        Theme.metrics.BUTTON_HEIGHT

        Theme.spacing.PADDING_MD

        Theme.radius.FIELD_RADIUS

        Theme.icons.SAVE
    """

    # =====================================================
    # Tokens
    # =====================================================

    colors = colors

    fonts = fonts

    metrics = metrics

    spacing = spacing

    radius = radius

    icons = icons

    animation = animation

    # =====================================================
    # Informations
    # =====================================================

    NAME = "OptiManager Theme"

    VERSION = "2.0.0"

    AUTHOR = "Mohamed Tarek & ChatGPT"