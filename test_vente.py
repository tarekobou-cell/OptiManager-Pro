from database import Base, engine

import models.produit
import models.vente
import models.ligne_vente


from services.vente_service import creer_vente, liste_ventes


Base.metadata.create_all(bind=engine)


vente = creer_vente(
    client_nom="Ahmed",
    produits=[
        {
            "produit_id": 1,
            "quantite": 2
        }
    ]
)


print(
    "Vente :",
    vente.id,
    vente.total
)


for v in liste_ventes():
    print(
        v.client_nom,
        v.total
    )