"""
=========================================================
OptiManager Pro
---------------------------------------------------------
Fichier : constantes.py
Description : Énumérations globales du projet.
Auteur : Mohamed Tarek & ChatGPT
Version : 2.0.0
=========================================================
"""

from enum import Enum


# =========================================================
# Utilisateurs
# =========================================================

class RoleUtilisateur(Enum):
    """
    Rôles disponibles dans l'application.
    """

    ADMIN = "Administrateur"

    OPTOMETRISTE = "Optométriste"

    VENDEUR = "Vendeur"


# =========================================================
# Paiements
# =========================================================

class ModePaiement(Enum):
    """
    Modes de paiement.
    """

    ESPECES = "Espèces"

    CARTE = "Carte bancaire"

    CHEQUE = "Chèque"

    VIREMENT = "Virement"

    MIXTE = "Paiement mixte"


# =========================================================
# Produits
# =========================================================

class TypeProduit(Enum):
    """
    Catégories des produits.
    """

    MONTURE = "Monture"

    VERRE = "Verre"

    LENTILLE = "Lentille"

    ACCESSOIRE = "Accessoire"

    PRODUIT_ENTRETIEN = "Produit d'entretien"

    AUTRE = "Autre"


# =========================================================
# Verres
# =========================================================

class TypeVerre(Enum):
    """
    Types de verres.
    """

    UNIFOCAL = "Unifocal"

    BIFOCAL = "Bifocal"

    PROGRESSIF = "Progressif"

    BUREAUTIQUE = "Bureautique"

    SOLAIRE = "Solaire"


# =========================================================
# Consultations
# =========================================================

class StatutConsultation(Enum):
    """
    Statuts d'une consultation.
    """

    EN_ATTENTE = "En attente"

    EN_COURS = "En cours"

    TERMINEE = "Terminée"

    ANNULEE = "Annulée"


# =========================================================
# Rendez-vous
# =========================================================

class StatutRendezVous(Enum):
    """
    Statuts d'un rendez-vous.
    """

    PREVU = "Prévu"

    CONFIRME = "Confirmé"

    TERMINE = "Terminé"

    ANNULE = "Annulé"

    ABSENT = "Absent"


# =========================================================
# Commandes fournisseurs
# =========================================================

class EtatCommande(Enum):
    """
    États d'une commande fournisseur.
    """

    EN_ATTENTE = "En attente"

    EN_COURS = "En cours"

    RECUE = "Reçue"

    LIVREE = "Livrée"

    ANNULEE = "Annulée"


# =========================================================
# Stock
# =========================================================

class TypeMouvementStock(Enum):
    """
    Types de mouvements de stock.
    """

    ENTREE = "Entrée"

    SORTIE = "Sortie"

    INVENTAIRE = "Inventaire"

    AJUSTEMENT = "Ajustement"

    RETOUR = "Retour"


# =========================================================
# Réparations
# =========================================================

class TypeReparation(Enum):
    """
    Types de réparations.
    """

    REGLAGE = "Réglage"

    PLAQUETTES = "Plaquettes"

    VIS = "Vis"

    BRANCHE = "Branche"

    POLISSAGE = "Polissage"

    SOUDURE = "Soudure"

    AUTRE = "Autre"


class StatutReparation(Enum):
    """
    Statuts d'une réparation.
    """

    EN_ATTENTE = "En attente"

    EN_COURS = "En cours"

    TERMINEE = "Terminée"

    LIVREE = "Livrée"

    ANNULEE = "Annulée"