# OptiManager Pro

# Clean Architecture

Version : 2.0

Auteur : Mohamed Tarek BOUYAHIAOUI

Architecte : ChatGPT

---

# 1. Philosophie

Toute dépendance pointe vers le centre.

Jamais l'inverse.

Le métier ne dépend de rien.

Ni Qt.

Ni SQLAlchemy.

Ni SQLite.

Ni PostgreSQL.

Ni PDF.

Ni Excel.

Ni Internet.

Le métier est totalement indépendant.

---

# 2. Architecture

                UI

                │

Application Services

                │

      Domain Services

                │

     Domain Entities

                │

Interfaces

                │

Infrastructure

---

# 3. Domain

Le Domain représente le cœur du logiciel.

Il contient :

Entities

Value Objects

Business Rules

Domain Events

Specifications

Factories

Aucune dépendance externe n'est autorisée.

---

# 4. Application

L'application orchestre le métier.

Elle contient :

Use Cases

Commands

Queries

Handlers

DTO

Permissions

Transactions

---

# 5. Infrastructure

L'infrastructure contient :

SQLAlchemy

SQLite

PostgreSQL

Filesystem

PDF

Excel

Cloud

API

Mail

Logs

Backup

---

# 6. UI

L'interface ne fait qu'afficher.

Elle ne contient jamais :

SQL

Calcul métier

Validation métier

Traitement de fichiers

---

# 7. Communication

Toujours :

UI

↓

Application

↓

Domain

↓

Infrastructure

Jamais l'inverse.

---

# 8. Dépendances

Le Domain ne connaît :

aucun framework

aucune base

aucun widget

aucun ORM

aucune bibliothèque graphique

---

# 9. Injection de dépendances

Tous les services sont injectés.

Aucun singleton métier.

---

# 10. Tests

Le Domain doit pouvoir être testé sans :

Qt

SQLAlchemy

SQLite

Interface graphique

---

# 11. Objectif

Le logiciel doit pouvoir changer :

de base de données

de framework graphique

de système Cloud

sans modifier le métier.

FIN