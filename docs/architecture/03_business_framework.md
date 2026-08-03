# OptiManager Business Framework

Version : 2.0

Auteur : Mohamed Tarek BOUYAHIAOUI

Architecte : ChatGPT

---

# 1. Vision

Le Business Framework représente toute l'intelligence métier
d'OptiManager Pro.

Il est totalement indépendant :

- de Qt
- de SQLAlchemy
- de la base de données

Il représente uniquement les règles métier de l'optique.

---

# 2. Objectif

Transformer les connaissances métier des opticiens et
optométristes en composants réutilisables.

Le Framework métier doit permettre de construire
de nouveaux modules sans réécrire les règles métier.

---

# 3. Architecture

Application

↓

Modules ERP

↓

Business Framework

↓

Framework UI

↓

Infrastructure

---

# 4. Domaines métier

Le Framework est organisé par domaines.

Patient Care

Clinical

Optical Laboratory

Retail

Inventory

Business

Administration

---

# 5. Patient Care

Responsabilités :

Création du patient

Recherche

Historique

Documents

Photos

Consentements

Suivi

Famille

Assurances

---

# 6. Clinical

Gestion des examens.

Il comprend :

Anamnèse

Acuité visuelle

Réfraction objective

Réfraction subjective

Vision binoculaire

Kératométrie

Tonométrie

Vision des couleurs

Champ visuel

Dominance oculaire

Prescription

Suivi clinique

---

# 7. Optical Laboratory

Fabrication.

Gestion :

Verres

Montures

Taillage

Montage

Contrôle qualité

Livraison

Garanties

Réparations

---

# 8. Retail

Gestion commerciale.

Ventes

Paiements

Promotions

Devis

Factures

Avoirs

Programme fidélité

---

# 9. Inventory

Stock.

Montures

Verres

Produits

Accessoires

Commandes

Réceptions

Inventaires

Fournisseurs

---

# 10. Business

Statistiques.

Dashboard

Chiffre d'affaires

Marges

Performance

Indicateurs

Objectifs

Prévisions

---

# 11. Administration

Utilisateurs

Permissions

Audit

Sauvegardes

Paramètres

Sécurité

---

# 12. Philosophie

Le Business Framework ne connaît jamais :

Qt

SQL

Widgets

Styles

Fenêtres

Il contient uniquement les règles métier.

---

# 13. Réutilisabilité

Chaque composant métier doit pouvoir être utilisé
dans plusieurs modules.

Exemple :

PrescriptionWidget

↓

Consultation

↓

Contrôle annuel

↓

Suivi post-opératoire

↓

Lentilles

---

# 14. Objectif

Construire un Framework métier complet
pour les professionnels de la vision.

FIN