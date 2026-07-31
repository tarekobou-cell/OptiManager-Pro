import sys

from PySide6.QtWidgets import QApplication

from database import Base, engine

from models.rendez_vous import RendezVous

# Charger tous les modèles AVANT création des tables
import models.utilisateur
import models.patient
import models.rendez_vous
import models.consultation
import models.prescription
import models.produit
import models.mouvement_stock
import models.vente
import models.ligne_vente

from services.creation_admin import creer_admin
from ui.login import LoginWindow


Base.metadata.create_all(bind=engine)

creer_admin()


app = QApplication(sys.argv)

fenetre = LoginWindow()
fenetre.show()

sys.exit(app.exec())