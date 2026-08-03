# OptiManager Pro V2

# Architecture Générale

Version : 2.0

Auteur : Mohamed Tarek BOUYAHIAOUI

Architecte logiciel : ChatGPT

---

# 1. Vision

OptiManager Pro est une plateforme professionnelle destinée aux :

- Opticiens
- Optométristes
- Cabinets de réfraction
- Laboratoires d'optique
- Chaînes de magasins
- Centres de santé visuelle

Le projet est conçu pour évoluer pendant plusieurs années sans nécessiter une réécriture complète.

L'objectif est de fournir un logiciel moderne, rapide, modulaire et facilement extensible.

---

# 2. Philosophie

Le développement suit les principes :

- SOLID
- Clean Architecture
- Separation of Concerns
- DRY
- KISS
- Composition over Inheritance
- MVC
- Repository Pattern
- Service Layer Pattern

---

# 3. Architecture générale

Le logiciel est divisé en plusieurs couches indépendantes.

```
Application
        │
        ▼
Modules ERP
        │
        ▼
Framework Métier
        │
        ▼
Framework UI
        │
        ▼
Infrastructure
```

Chaque couche possède une responsabilité unique.

Une couche supérieure peut utiliser une couche inférieure.

Une couche inférieure ne dépend jamais d'une couche supérieure.

---

# 4. Structure officielle

```
OptiManager/

assets/

backups/

controllers/

core/

database/

docs/

exports/

models/

repositories/

reports/

services/

tests/

ui/

main.py
```

---

# 5. Core

Le dossier Core contient tout ce qui est partagé par l'ensemble du logiciel.

```
core/

config.py

constants.py

enums.py

exceptions.py

logger.py

validators.py

utils.py
```

Aucune logique métier ne doit être placée ici.

---

# 6. Models

Chaque modèle représente une entité métier.

Exemple :

Patient

Consultation

Prescription

Lens

Frame

Sale

Supplier

Appointment

Repair

Insurance

Audit

Chaque modèle possède son propre fichier.

---

# 7. Repository

Le Repository est le seul responsable des accès à la base de données.

Les repositories ne contiennent aucune logique métier.

Ils ne doivent jamais communiquer avec l'interface graphique.

---

# 8. Services

Les Services contiennent uniquement les règles métier.

Ils ne connaissent jamais Qt.

Ils utilisent uniquement les repositories.

---

# 9. Controllers

Les Controllers servent de passerelle entre :

Interface graphique

↓

Services

Ils ne contiennent jamais de requêtes SQL.

---

# 10. Interface graphique

L'interface est entièrement basée sur un Framework UI propriétaire.

Aucun widget Qt ne doit être utilisé directement dans les pages métier.

Les pages utilisent exclusivement les composants développés par OptiManager Framework.

---

# 11. Framework UI

Le Framework UI est totalement indépendant du métier.

Il peut être réutilisé dans d'autres logiciels.

Il contient :

BaseWidget

BaseField

BaseInput

BaseButton

BaseTable

BaseDialog

BasePage

Layouts

Theme

Validation

Navigation

---

# 12. Framework Métier

Le Framework Métier contient tous les composants spécifiques au domaine de l'optique.

Exemple :

PatientIdentityWidget

VisualAcuityWidget

RefractionWidget

PrescriptionWidget

LensSelectorWidget

WorkshopWidget

LaboratoryWidget

Ces composants pourront être utilisés dans plusieurs modules.

---

# 13. Modules ERP

Chaque fonctionnalité majeure est développée sous forme de module.

Patients

Consultations

Prescriptions

Appointments

Inventory

Sales

Laboratory

Workshop

Accounting

Dashboard

Statistics

CRM

Marketing

Cloud

Chaque module est indépendant.

---

# 14. Design System

Toutes les couleurs, polices, dimensions et espacements sont centralisés dans :

ui/theme

Aucune valeur numérique ne doit être écrite directement dans les composants.

---

# 15. Validation

Toutes les validations sont centralisées.

Le Framework UI ne contient aucune règle métier.

Les validations métier sont placées dans les Services ou les Validators.

---

# 16. Base de données

La base de données est entièrement abstraite via SQLAlchemy.

Aucun SQL brut n'est autorisé en dehors des cas exceptionnels documentés.

---

# 17. Documentation

Chaque composant important possède une documentation.

Chaque module possède sa spécification.

Toute évolution importante est documentée avant son implémentation.

---

# 18. Tests

Chaque composant critique possède des tests unitaires.

Les services métier sont testés indépendamment de l'interface graphique.

---

# 19. Objectif

Construire une plateforme professionnelle capable d'évoluer pendant plusieurs années sans dette technique majeure.

Le code doit privilégier :

la lisibilité,

la maintenabilité,

la modularité,

la robustesse,

avant la rapidité de développement.

---

FIN DU DOCUMENT