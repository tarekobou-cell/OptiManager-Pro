# OptiManager Pro

# Architecture de la Base de Données

Version : 2.0

Auteur : Mohamed Tarek BOUYAHIAOUI

Architecte : ChatGPT

---

# 1. Philosophie

La base de données est le cœur du logiciel.

Toutes les données doivent être :

- normalisées
- cohérentes
- extensibles
- historisées
- auditables

Le modèle est conçu pour évoluer pendant plusieurs années.

---

# 2. Organisation

La base est organisée par domaines.

Patient Care

Clinical

Optical Laboratory

Inventory

Retail

Administration

Business Intelligence

---

# 3. Patient Care

Entités :

Patient

PatientAddress

PatientContact

PatientInsurance

PatientPhoto

PatientDocument

EmergencyContact

PatientNotes

MedicalHistory

Allergy

Medication

Consent

---

# 4. Clinical

Consultation

Appointment

VisualAcuity

ObjectiveRefraction

SubjectiveRefraction

Keratometry

Tonometry

BinocularVision

ColorVision

Diagnosis

Treatment

Prescription

FollowUp

ClinicalAttachment

---

# 5. Optical Laboratory

LensOrder

Lens

LensMaterial

LensCoating

LensTreatment

LensIndex

Frame

FrameBrand

WorkshopOrder

Assembly

QualityControl

Delivery

Repair

Warranty

---

# 6. Inventory

Product

Category

Supplier

PurchaseOrder

PurchaseOrderLine

StockMovement

InventoryAdjustment

Warehouse

Location

Batch

SerialNumber

---

# 7. Retail

Sale

SaleLine

Payment

Invoice

Quotation

CustomerLoyalty

GiftCard

Refund

CashRegister

Session

---

# 8. Administration

User

Role

Permission

AuditLog

Notification

Setting

Backup

License

---

# 9. Business

DashboardCache

Statistic

KPI

Target

MonthlyReport

YearlyReport

---

# 10. Relations

Patient

↓

Consultation

↓

Prescription

↓

LensOrder

↓

WorkshopOrder

↓

Delivery

↓

AfterSalesService

---

# 11. Historique

Toutes les données médicales sont historisées.

Aucune consultation ne doit être écrasée.

Chaque modification importante est conservée.

---

# 12. Audit

Toutes les opérations critiques sont enregistrées.

Création

Modification

Suppression logique

Connexion

Export

Import

Paiement

Annulation

---

# 13. Suppression

Aucune suppression physique.

Le logiciel utilise :

deleted_at

deleted_by

is_active

---

# 14. Dates

Toutes les tables possèdent :

created_at

updated_at

created_by

updated_by

---

# 15. Identifiants

Chaque table possède :

id

uuid

Le UUID permet la synchronisation Cloud future.

---

# 16. Performances

Toutes les clés étrangères sont indexées.

Les recherches fréquentes sont indexées.

Les statistiques utilisent des tables dédiées.

---

# 17. Objectif

Construire une base de données capable de gérer :

des centaines de milliers de patients,

des millions de consultations,

plusieurs magasins,

plusieurs utilisateurs,

sans modification majeure du schéma.

FIN