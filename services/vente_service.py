from sqlalchemy.orm import joinedload

from database import SessionLocal

from models.vente import Vente
from models.ligne_vente import LigneVente
from models.produit import Produit


def creer_vente(client_nom, produits):

    db = SessionLocal()

    try:

        vente = Vente(
            client_nom=client_nom,
            total=0
        )

        db.add(vente)
        db.flush()

        total = 0

        for item in produits:

            produit = db.query(Produit).filter(
                Produit.id == item["produit_id"]
            ).first()

            if not produit:
                continue

            quantite = item["quantite"]

            if produit.quantite < quantite:
                continue

            sous_total = produit.prix_vente * quantite

            ligne = LigneVente(
                vente_id=vente.id,
                produit_id=produit.id,
                designation=produit.designation,
                quantite=quantite,
                prix_unitaire=produit.prix_vente,
                sous_total=sous_total
            )

            produit.quantite -= quantite

            total += sous_total

            db.add(ligne)

        vente.total = total

        db.commit()
        db.refresh(vente)

        return {
            "id": vente.id,
            "client_nom": vente.client_nom,
            "total": vente.total
        }

    except Exception as e:

        db.rollback()
        raise e

    finally:

        db.close()


def liste_ventes():

    db = SessionLocal()

    try:

        ventes = db.query(Vente).all()

        return [
            {
                "id": v.id,
                "client_nom": v.client_nom,
                "total": v.total
            }
            for v in ventes
        ]

    finally:

        db.close()


def detail_vente(vente_id):

    db = SessionLocal()

    try:

        vente = (
            db.query(Vente)
            .options(joinedload(Vente.lignes))
            .filter(Vente.id == vente_id)
            .first()
        )

        return vente

    finally:

        db.close()