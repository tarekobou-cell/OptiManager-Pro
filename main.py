import sys

from PySide6.QtWidgets import QApplication

from database import Base, engine

# Chargement des modèles
import models.utilisateur

# Création automatique de l'administrateur
from services.creation_admin import creer_admin

# Fenêtre de connexion
from ui.login import LoginWindow


# Création des tables dans la base de données
Base.metadata.create_all(bind=engine)

# Création du compte administrateur si nécessaire
creer_admin()


# Lancement de l'application
app = QApplication(sys.argv)

fenetre = LoginWindow()

fenetre.show()

sys.exit(app.exec())