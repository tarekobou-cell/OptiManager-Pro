"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : main.py
Description : Point d'entrée principal de l'application.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

import sys

from PySide6.QtWidgets import QApplication

from database import db

# =========================================================
# Chargement des modèles
# =========================================================

import models.utilisateur
import models.patient
import models.patient_entities
import models.consultation
import models.prescription
import models.rendez_vous

import models.fournisseur
import models.produit

import models.commande
import models.ligne_commande

import models.mouvement_stock

import models.vente
import models.ligne_vente

import models.paiement

import models.reparation

# =========================================================
# Services / Interface
# =========================================================

from services.creation_admin import creer_admin
from ui.login import LoginWindow


# =========================================================
# Fonction principale
# =========================================================

def main() -> None:
    """
    Point d'entrée principal de l'application.
    """

    # Création des tables
    db.create_tables()

    # Création automatique du compte administrateur
    creer_admin()

    # Démarrage de Qt
    app = QApplication(sys.argv)

    fenetre = LoginWindow()

    fenetre.show()

    sys.exit(app.exec())


# =========================================================
# Lancement
# =========================================================

if __name__ == "__main__":
    main()