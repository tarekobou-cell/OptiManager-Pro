from database import Base, engine

import models.produit

from services.stock_service import ajouter_produit, liste_stock


# création de la table produits
Base.metadata.create_all(bind=engine)


p = ajouter_produit(
    reference="VERRE001",
    designation="Verre unifocal 1.56",
    categorie="Verre",
    traitement="Blue Block",
    fournisseur="Essilor",
    quantite=20,
    prix_achat=1500,
    prix_vente=3500
)


print(
    p.reference,
    p.designation,
    p.quantite
)


stock = liste_stock()

for produit in stock:
    print(
        produit.reference,
        produit.quantite
    )