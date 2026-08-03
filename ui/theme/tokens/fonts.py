"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : fonts.py
Description : Définition des polices officielles.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from PySide6.QtGui import QFont


# =========================================================
# Famille de police
# =========================================================

FONT_FAMILY = "Segoe UI"


# =========================================================
# Tailles
# =========================================================

SIZE_XS = 10
SIZE_SM = 11
SIZE_MD = 12
SIZE_LG = 14
SIZE_XL = 16
SIZE_XXL = 20
SIZE_TITLE = 24


# =========================================================
# Poids
# =========================================================

WEIGHT_LIGHT = QFont.Light
WEIGHT_NORMAL = QFont.Normal
WEIGHT_MEDIUM = QFont.Medium
WEIGHT_DEMIBOLD = QFont.DemiBold
WEIGHT_BOLD = QFont.Bold


# =========================================================
# Fabrique de polices
# =========================================================

def make_font(
    size: int,
    weight: int = WEIGHT_NORMAL,
    italic: bool = False,
) -> QFont:
    """
    Crée une police standard.
    """

    font = QFont(FONT_FAMILY)

    font.setPointSize(size)

    font.setWeight(weight)

    font.setItalic(italic)

    return font


# =========================================================
# Polices officielles
# =========================================================

FONT_XS = make_font(SIZE_XS)

FONT_SM = make_font(SIZE_SM)

FONT_MD = make_font(SIZE_MD)

FONT_LG = make_font(SIZE_LG)

FONT_XL = make_font(
    SIZE_XL,
    WEIGHT_MEDIUM,
)

FONT_XXL = make_font(
    SIZE_XXL,
    WEIGHT_BOLD,
)

FONT_TITLE = make_font(
    SIZE_TITLE,
    WEIGHT_BOLD,
)

FONT_BUTTON = make_font(
    SIZE_MD,
    WEIGHT_MEDIUM,
)

FONT_LABEL = make_font(
    SIZE_MD,
    WEIGHT_MEDIUM,
)

FONT_TABLE = make_font(
    SIZE_MD,
)

FONT_MENU = make_font(
    SIZE_MD,
)

FONT_STATUS = make_font(
    SIZE_SM,
)

FONT_CAPTION = make_font(
    SIZE_XS,
)