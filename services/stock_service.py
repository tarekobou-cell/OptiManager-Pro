from database import SessionLocal
from models.produit import Produit


def ajouter_produit(
    reference,
    designation,
    categorie,
    traitement=None,
    fournisseur=None,
    quantite=0,
    prix_achat=0,
    prix_vente=0
):

    db = SessionLocal()

    try:
        produit = Produit(
            reference=reference,
            designation=designation,
            categorie=categorie,
            traitement=traitement,
            fournisseur=fournisseur,
            quantite=quantite,
            prix_achat=prix_achat,
            prix_vente=prix_vente
        )

        db.add(produit)
        db.commit()
        db.refresh(produit)

        return produit

    finally:
        db.close()



def liste_stock():

    db = SessionLocal()

    try:
        return db.query(Produit).all()

    finally:
        db.close()



def rechercher_produit(reference):

    db = SessionLocal()

    try:
        return (
            db.query(Produit)
            .filter(
                Produit.reference == reference
            )
            .first()
        )

    finally:
        db.close()



def modifier_quantite(produit_id, nouvelle_quantite):

    db = SessionLocal()

    try:
        produit = (
            db.query(Produit)
            .filter(
                Produit.id == produit_id
            )
            .first()
        )

        if produit:
            produit.quantite = nouvelle_quantite
            db.commit()

        return produit

    finally:
        db.close()