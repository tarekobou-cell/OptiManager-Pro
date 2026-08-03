# OptiManager Pro - Architecture V1

**Version :** 1.0.0
**Auteur :** Mohamed Tarek & ChatGPT

---

# 1. Vision du projet

OptiManager Pro est un logiciel professionnel destiné aux magasins d'optique.

Son objectif est de centraliser l'ensemble des activités d'un opticien :

* Gestion des patients
* Gestion des consultations
* Gestion des prescriptions
* Gestion des rendez-vous
* Gestion des ventes
* Gestion du stock
* Gestion des fournisseurs
* Gestion des réparations
* Gestion des paiements
* Tableau de bord décisionnel

Le logiciel doit rester :

* rapide ;
* fiable ;
* évolutif ;
* simple à utiliser.

---

# 2. Philosophie

Le patient est au centre du logiciel.

Toutes les informations médicales doivent être historisées.

Toutes les opérations commerciales doivent être traçables.

Aucune donnée importante ne doit être perdue.

Le logiciel doit pouvoir évoluer pendant plusieurs années sans remettre en cause son architecture.

---

# 3. Architecture générale

Le projet est organisé en couches.

```
Interface (UI)

↓

Controller

↓

Service

↓

Repository

↓

SQLAlchemy

↓

SQLite
```

Chaque couche possède une responsabilité unique.

---

# 4. Structure du projet

```
OptiManager/

assets/
backups/
config/
controllers/
core/
database/
docs/
logs/
models/
repositories/
reports/
resources/
services/
styles/
tests/
ui/
utils/

main.py
database.py
```

---

# 5. Modules fonctionnels

Le logiciel est composé des modules suivants :

* Authentification
* Dashboard
* Patients
* Rendez-vous
* Consultations
* Prescriptions
* Produits
* Stock
* Fournisseurs
* Commandes
* Ventes
* Paiements
* Réparations
* Rapports
* Administration

---

# 6. Modèle de données

## Utilisateur

Responsabilité :

Gérer les utilisateurs du logiciel.

Principaux champs :

* id
* nom
* prenom
* login
* mot_de_passe
* role
* actif
* derniere_connexion
* date_creation
* date_modification

---

## Patient

Responsabilité :

Conserver uniquement les informations d'identité.

Contient :

* nom
* prénom
* téléphone
* date de naissance
* adresse
* email
* profession
* notes générales

Ne contient jamais :

* correction optique
* ordonnance
* type de verre
* traitement

Ces informations appartiennent à la prescription.

---

## RendezVous

Responsabilité :

Planifier les rendez-vous.

Contient :

* patient
* utilisateur
* date et heure
* motif
* statut
* notes

---

## Consultation

Responsabilité :

Représente une visite du patient.

Contient :

* patient
* utilisateur
* date
* motif
* diagnostic
* observations

Une consultation peut produire une prescription.

---

## Prescription

Responsabilité :

Historiser la correction optique.

Contient notamment :

* sphère OD

* cylindre OD

* axe OD

* addition OD

* sphère OG

* cylindre OG

* axe OG

* addition OG

* type de verre

* traitement

* filtre

* photochromique

* remarques

---

## Produit

Responsabilité :

Référentiel des produits.

Contient :

* référence
* désignation
* catégorie
* marque
* prix achat
* prix vente
* stock
* stock minimum

---

## MouvementStock

Responsabilité :

Tracer toutes les entrées et sorties de stock.

Aucun stock ne doit être modifié directement.

---

## Vente

Responsabilité :

Représente une facture.

Contient :

* patient
* utilisateur
* date
* total
* remise
* statut

---

## LigneVente

Responsabilité :

Articles composant une vente.

---

## Paiement

Responsabilité :

Enregistrer tous les paiements liés à une vente.

Une vente peut comporter plusieurs paiements.

---

## Fournisseur

Responsabilité :

Gestion des fournisseurs.

---

## Commande

Responsabilité :

Gestion des commandes fournisseurs.

---

## Réparation

Responsabilité :

Gestion des réparations des lunettes.

---

# 7. Relations

* Un patient possède plusieurs consultations.
* Une consultation possède au maximum une prescription.
* Un patient possède plusieurs rendez-vous.
* Une vente possède plusieurs lignes.
* Une ligne correspond à un produit.
* Une vente peut posséder plusieurs paiements.
* Un produit possède plusieurs mouvements de stock.
* Une réparation peut être liée à une vente.

---

# 8. Règles métier

* Les données médicales sont historisées.
* Les ventes ne sont jamais supprimées.
* Les paiements sont conservés.
* Le stock est modifié uniquement par les mouvements de stock.
* Une prescription appartient toujours à une consultation.
* Une consultation appartient toujours à un patient.

---

# 9. Règles de développement

* Les interfaces ne communiquent jamais directement avec SQLAlchemy.
* Les services n'exécutent jamais de requêtes SQL.
* Toutes les requêtes passent par un Repository.
* Tous les modèles héritent de BaseModel.
* Tous les Repository héritent de BaseRepository.
* Toutes les erreurs sont journalisées.
* Les transactions utilisent commit/rollback.
* Le code doit être typé et documenté.

---

# 10. Objectif de la Version 1

La première version doit permettre à un magasin d'optique de gérer son activité quotidienne de manière fiable :

* patients ;
* consultations ;
* prescriptions ;
* ventes ;
* stock ;
* paiements ;
* réparations ;
* tableau de bord.

Une fois cette version stabilisée, les fonctionnalités avancées (cloud, multi-magasins, synchronisation, SMS, etc.) seront développées dans les versions suivantes.
