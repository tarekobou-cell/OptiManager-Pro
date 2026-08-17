# OptiManager Pro — Patient Domain

## 1. Objectif

Le domaine Patient constitue le dossier central du patient dans OptiManager Pro.

Il doit permettre de gérer l'identité, les coordonnées, les contacts, les relations familiales, les assurances, les documents, les photos, les alertes, les tags et l'historique du patient.

---

## 2. Fonctionnalités

### 2.1 Identité
- Numéro de dossier
- Nom
- Prénom
- Nom de naissance
- Date de naissance
- Sexe
- Nationalité
- Lieu de naissance
- Numéro de pièce d'identité
- Profession
- Situation familiale
- Photo principale

### 2.2 Coordonnées
- Téléphone principal
- Téléphone secondaire
- Email
- Adresse
- Ville
- Wilaya
- Code postal
- Pays

### 2.3 Contacts
- Parent
- Tuteur légal
- Conjoint
- Contact d'urgence
- Autre contact

### 2.4 Patient mineur
- Parent ou tuteur légal
- Relation parent-enfant
- Autorisation
- Coordonnées du responsable
- Historique des responsables

### 2.5 Informations administratives
- Statut actif/inactif
- Source du patient
- Tags
- Notes administratives
- Date de création
- Date de modification
- Utilisateur créateur
- Utilisateur dernière modification

### 2.6 Assurance
- Organisme
- Numéro assuré
- Numéro de contrat
- Type de couverture
- Date de début
- Date de fin
- Observations
- Documents justificatifs

### 2.7 Documents
- Pièce d'identité
- Assurance
- Ordonnance
- Compte rendu
- Résultat d'examen
- Document libre

### 2.8 Photos
- Photo patient
- Photo document
- Photos complémentaires

### 2.9 Alertes
- Patient mineur
- Allergie
- Assurance expirée
- Document manquant
- Suivi à effectuer
- Alerte administrative

### 2.10 Tags
- VIP
- Nouveau
- Fidèle
- Entreprise
- Enfant
- Lentilles
- Progressifs
- Suivi annuel
- Tags personnalisés

---

## 3. Actions

- Créer
- Modifier
- Archiver
- Restaurer
- Fusionner
- Imprimer
- Exporter
- Ajouter document
- Ajouter photo
- Ajouter note
- Ajouter alerte
- Ajouter contact

---

## 4. Recherche

Recherche sur :

- Numéro de dossier
- Nom
- Prénom
- Téléphone
- Email
- Numéro assuré

Filtres :

- Âge
- Sexe
- Ville
- Wilaya
- Statut
- Assurance
- Tags
- Date de création
- Dernière visite

---

## 5. Historique

Le dossier doit permettre de consulter chronologiquement :

- Création du patient
- Rendez-vous
- Consultation
- Prescription
- Vente
- Commande
- Livraison
- Réparation
- Garantie
- Suivi

---

## 6. Fusion des doublons

Le système doit permettre :

1. Sélection de deux patients.
2. Détection des conflits.
3. Choix des informations à conserver.
4. Fusion.
5. Conservation de l'historique.
6. Journalisation de l'opération.

---

## 7. Permissions

- patient.view
- patient.create
- patient.edit
- patient.archive
- patient.restore
- patient.merge
- patient.export
- patient.print
- patient.documents
- patient.photo
- patient.insurance
- patient.notes
- patient.history

---

## 8. Modèle de données

### Patient

- id
- numero_dossier
- nom
- prenom
- nom_naissance
- date_naissance
- sexe
- nationalite
- lieu_naissance
- numero_identite
- profession
- situation_familiale
- photo_principale
- actif
- source
- created_at
- updated_at
- created_by
- updated_by

### PatientContact

- id
- patient_id
- nom
- prenom
- relation
- telephone
- telephone_secondaire
- email
- adresse
- contact_principal
- contact_urgence
- created_at

### PatientAddress

- id
- patient_id
- type
- adresse
- ville
- wilaya
- code_postal
- pays
- principale

### PatientRelationship

- id
- patient_id
- related_patient_id
- relation
- responsable_legal
- created_at

### PatientInsurance

- id
- patient_id
- organisme
- numero_assure
- numero_contrat
- type_couverture
- date_debut
- date_fin
- actif
- observations

### PatientDocument

- id
- patient_id
- type
- nom_fichier
- chemin
- mime_type
- taille
- description
- date_document
- created_at
- created_by

### PatientPhoto

- id
- patient_id
- type
- chemin
- description
- prise_le
- created_by

### PatientAlert

- id
- patient_id
- type
- titre
- message
- niveau
- active
- date_debut
- date_fin
- created_by

### PatientTag

- id
- patient_id
- tag
- created_at

---

## 9. Relations

- Patient 1 → N PatientContact
- Patient 1 → N PatientAddress
- Patient 1 → N PatientRelationship
- Patient 1 → N PatientInsurance
- Patient 1 → N PatientDocument
- Patient 1 → N PatientPhoto
- Patient 1 → N PatientAlert
- Patient 1 → N PatientTag
- Patient 1 → N Consultation
- Patient 1 → N RendezVous
- Patient 1 → N Vente
- Patient 1 → N Reparation

---

## 10. Contraintes

- numero_dossier unique
- numero_dossier indexé
- téléphone indexé
- email indexé
- numéro assuré indexé
- toutes les relations utilisent des clés étrangères
- historique conservé
- archivage plutôt que suppression physique
- created_at obligatoire
- updated_at obligatoire

---

## 11. Interface cible

### Patient Profile

- En-tête patient
- Résumé
- Identité
- Coordonnées
- Contacts
- Assurance
- Documents
- Photos
- Alertes
- Timeline
- Rendez-vous
- Consultations
- Prescriptions
- Ventes
- Commandes
- SAV

---

## 12. Règles fondamentales

1. Un patient possède un dossier maître unique.
2. Le numéro de dossier est unique.
3. L'archivage conserve l'historique.
4. Une fusion est traçable.
5. Les données cliniques détaillées appartiennent au domaine Clinical.
6. Les opérations sensibles sont auditables.
7. Un patient peut avoir plusieurs consultations.
8. Un patient peut avoir plusieurs rendez-vous.
9. Un patient peut avoir plusieurs ventes.
10. Un patient peut avoir plusieurs documents, photos et contacts.

---

## 13. État

Statut : CONCEPTION

Prochaine étape : PATIENT-007 — Validation détaillée du modèle de données.