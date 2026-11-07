---
type: concept
tags:
  - year3
aliases:
  - one to one
  - one to many
  - many to many
  - one-to-many
  - many-to-many
  - association 1-N
  - association N-N
  - association plusieurs-à-plusieurs
matieres:
  - Data base
  - ligue football
sources:
  - "[[1 - Database (résumé)|Cours 1 et 2 - Database]]"
  - "[[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]"
maj: 2026-11-06
---

Selon ses cardinalités, une association se traduit différemment dans le schéma relationnel ([[1 - Database (résumé)|Cours 1 et 2 - Database]]) :

- **1-N** : par une [[Clé primaire et clé étrangère|clé étrangère]] du côté « 1 », par exemple `#code formation` dans la table étudiant ;
- **N-N** : par une [[Table de correspondance]] ;
- **1-1** : ne devrait pas apparaître dans un schéma de conception.

Le sujet database ([[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]) impose des associations 1-N et N-N.

Notion parente : [[Modèle entité-association]]. Voir aussi : [[Table de correspondance]], [[Clé primaire et clé étrangère]], [[Association ternaire]].

## À vérifier

- Le cours range sous « one to one » un cas (1,1 / 0,N) qui est en fait many-to-one ; le titre manuscrit porte « me-to-one ».

Résumés : [[1 - Database (résumé)]], [[sujet database (résumé)]], [[Rapport du projet Ligue Football (résumé)]]
