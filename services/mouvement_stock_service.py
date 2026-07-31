from database import SessionLocal
from models.produit import Produit
from models.mouvement_stock import MouvementStock


def entree_stock(produit_id, quantite, observation=None):

    db = SessionLocal()

    try:
        produit = db.query(Produit).filter(
            Produit.id == produit_id
        ).first()

        if not produit:
            return None

        produit.quantite += quantite

        mouvement = MouvementStock(
            produit_id=produit_id,
            type_mouvement="ENTREE",
            quantite=quantite,
            observation=observation
        )

        db.add(mouvement)
        db.commit()

        quantite_finale = produit.quantite

        return quantite_finale

    finally:
        db.close()



def sortie_stock(produit_id, quantite, observation=None):

    db = SessionLocal()

    try:
        produit = db.query(Produit).filter(
            Produit.id == produit_id
        ).first()

        if not produit:
            return None

        if produit.quantite < quantite:
            return None

        produit.quantite -= quantite

        mouvement = MouvementStock(
            produit_id=produit_id,
            type_mouvement="SORTIE",
            quantite=quantite,
            observation=observation
        )

        db.add(mouvement)
        db.commit()

        quantite_finale = produit.quantite

        return quantite_finale

    finally:
        db.close()