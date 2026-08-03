"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : icons.py
Description : Gestion centralisée des icônes.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from pathlib import Path

from PySide6.QtGui import QIcon


# =========================================================
# Dossiers
# =========================================================

ROOT_DIR = Path(__file__).resolve().parents[3]

ASSETS_DIR = ROOT_DIR / "assets"

ICONS_DIR = ASSETS_DIR / "icons"


# =========================================================
# Fonction de chargement
# =========================================================

def icon(name: str) -> QIcon:
    """
    Retourne une icône à partir de son nom.

    Exemple :
        icon("patient")
        -> assets/icons/patient.svg
    """

    return QIcon(
        str(
            ICONS_DIR / f"{name}.svg"
        )
    )


# =========================================================
# Icônes générales
# =========================================================

APP = icon("app")

HOME = icon("home")

SEARCH = icon("search")

ADD = icon("add")

EDIT = icon("edit")

DELETE = icon("delete")

SAVE = icon("save")

CANCEL = icon("cancel")

REFRESH = icon("refresh")

PRINT = icon("print")

EXPORT = icon("export")

IMPORT = icon("import")

SETTINGS = icon("settings")

INFO = icon("info")

WARNING = icon("warning")

ERROR = icon("error")

SUCCESS = icon("success")

LOGIN = icon("login")

LOGOUT = icon("logout")


# =========================================================
# Patients
# =========================================================

PATIENT = icon("patient")

CONSULTATION = icon("consultation")

PRESCRIPTION = icon("prescription")

RENDEZVOUS = icon("calendar")


# =========================================================
# Commerce
# =========================================================

PRODUCT = icon("product")

CATEGORY = icon("category")

SUPPLIER = icon("supplier")

STOCK = icon("stock")

SALE = icon("sale")

PAYMENT = icon("payment")


# =========================================================
# Administration
# =========================================================

USER = icon("user")

ROLE = icon("role")

DASHBOARD = icon("dashboard")

REPORT = icon("report")

BACKUP = icon("backup")


# =========================================================
# Atelier
# =========================================================

REPAIR = icon("repair")

TOOLS = icon("tools")


# =========================================================
# Navigation
# =========================================================

LEFT = icon("left")

RIGHT = icon("right")

UP = icon("up")

DOWN = icon("down")

CLOSE = icon("close")