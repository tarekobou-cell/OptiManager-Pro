from database import Base, engine

import models.produit
import models.mouvement_stock

from services.mouvement_stock_service import entree_stock, sortie_stock


# création table si nécessaire
Base.metadata.create_all(bind=engine)


p = entree_stock(
    produit_id=1,
    quantite=10,
    observation="Réception fournisseur"
)

print("Après entrée :", p)


p = sortie_stock(
    produit_id=1,
    quantite=5,
    observation="Vente client"
)
print("Après sortie :", p)

