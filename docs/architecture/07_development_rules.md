# Règles de Développement

---

# Une classe

Une responsabilité.

---

# Une méthode

Une responsabilité.

---

# Une fonction

Une seule raison de changer.

---

# Les pages

Ne contiennent aucune logique métier.

---

# Les Dialogs

Ne contiennent aucune logique SQL.

---

# Les Services

Ne connaissent jamais Qt.

---

# Les Repositories

Ne connaissent jamais Qt.

---

# Les Widgets

Ne connaissent jamais SQL.

---

# Les Models

Ne connaissent jamais Qt.

---

# Les Tests

Obligatoires pour les Services critiques.

---

# Les Exceptions

Jamais ignorées.

---

# Les Logs

Toutes les opérations critiques sont journalisées.

---

# Les Permissions

Toujours vérifiées avant une action.

---

# Les Suppressions

Jamais physiques.

Toujours logiques.

---

# Les Migrations

Toujours versionnées.

---

# Les Noms

Toujours explicites.

Jamais :

data

temp

test

value

foo

bar

obj

Utiliser :

patient

consultation

prescription

invoice

supplier

lens

frame

FIN