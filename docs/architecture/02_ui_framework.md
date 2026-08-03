# OptiManager Framework UI

Version : 2.0

---

# 1. Objectif

Le Framework UI est un framework propriétaire développé pour
OptiManager Pro.

Son objectif est de masquer complètement PySide6.

Les modules métier ne doivent presque jamais manipuler directement :

- QWidget
- QPushButton
- QLabel
- QLineEdit
- QComboBox
- QTableWidget
- QVBoxLayout

Ils utiliseront exclusivement les composants du Framework.

---

# 2. Architecture

```
Application

↓

Business Widgets

↓

Business Components

↓

Framework UI

↓

PySide6
```

PySide6 devient uniquement une bibliothèque technique.

---

# 3. Organisation

```
ui/

framework/

    base/

    controls/

    buttons/

    containers/

    layouts/

    dialogs/

    navigation/

    tables/

    cards/

    forms/

    validation/

    animation/

    theme/

medical/

components/

pages/

dialogs/

widgets/
```

---

# 4. BaseWidget

Tous les composants héritent de BaseWidget.

Responsabilités :

- thème

- visibilité

- animation

- état

- accessibilité

- raccourcis

- focus

---

# 5. BaseControl

Tous les contrôles utilisateur héritent de BaseControl.

Exemple :

LineEdit

ComboBox

SpinBox

DateEdit

CheckBox

RadioButton

Slider

---

# 6. BaseInput

BaseInput ajoute :

validation

erreurs

tooltip

lecture seule

placeholder

champ obligatoire

---

# 7. BaseField

BaseField encapsule :

Label

↓

Input

↓

Erreur

Il ne connaît jamais le type du widget.

---

# 8. BaseContainer

Utilisé pour :

Card

GroupBox

Frame

Panel

Sidebar

Section

---

# 9. BaseDialog

Tous les dialogues héritent de BaseDialog.

Il fournit :

titre

boutons

validation

raccourcis

fermeture

confirmation

---

# 10. BasePage

Toutes les pages héritent de BasePage.

Fonctions communes :

chargement

actualisation

navigation

permissions

titre

toolbar

---

# 11. BaseTable

BaseTable ne contient aucune logique métier.

Elle fournit :

tri

filtre

pagination

export

sélection

copie

clic

menu contextuel

---

# 12. BaseButton

BaseButton gère :

icône

animation

raccourci

thème

tooltip

permissions

chargement

---

# 13. Validation

La validation est indépendante.

```
Validator

↓

Rule

↓

Rules

↓

ValidationResult
```

Chaque contrôle peut recevoir plusieurs validateurs.

---

# 14. Theme Engine

Le Framework ne contient aucun CSS écrit directement.

Tous les styles proviennent du Theme Engine.

```
Theme

↓

Colors

Fonts

Icons

Metrics

Radius

Spacing

Animation
```

---

# 15. Animation Engine

Toutes les animations utilisent :

QPropertyAnimation

Le Framework interdit :

animations dupliquées

durées codées en dur

---

# 16. Accessibilité

Tous les composants doivent supporter :

navigation clavier

Tab

Shift+Tab

Enter

Escape

Screen Readers

ToolTips

---

# 17. Performances

Les composants ne doivent jamais :

charger des données SQL

ouvrir des fichiers

effectuer des calculs métier

Ils sont uniquement responsables de l'affichage.

---

# 18. Objectif

Construire un Framework UI totalement indépendant du métier,
réutilisable dans n'importe quel autre logiciel Python.

FIN