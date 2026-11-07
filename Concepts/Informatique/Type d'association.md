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
  - "[[1 - Database|Cours 1 et 2 - Database]]"
  - "sujet database.pdf, dans Raw/Year 3/ligue football/for me (exclu du miroir)"
maj: 2026-11-07
---

Selon ses cardinalités, une association se traduit différemment dans le schéma relationnel ([[1 - Database|Cours 1 et 2 - Database]]) :

- **1-N** : par une [[Clé primaire et clé étrangère|clé étrangère]] du côté « 1 », par exemple `#code formation` dans la table étudiant ;
- **N-N** : par une [[Table de correspondance]] ;
- **1-1** : ne devrait pas apparaître dans un schéma de conception.

Le sujet database (dans Raw/Year 3/ligue football/for me, exclu du miroir) impose des associations 1-N et N-N.

Notion parente : [[Modèle entité-association]]. Voir aussi : [[Table de correspondance]], [[Clé primaire et clé étrangère]], [[Association ternaire]].

## Erreurs du cours

- [[1 - Database|Cours 1 et 2 - Database]] titre « One to one : 1 étudiant = 1 formation » le cas étudiant (1,1) – formation (0,N) ; il faut « many-to-one » (association 1-N) : une formation a plusieurs étudiants, d'où la clé étrangère `#code formation` dans la table étudiant. Le schéma manuscrit qui suit (titre peu lisible, « me-to-one » ou « one-to-one ») envoie d'ailleurs $e_3$ et $e_4$ sur le même $f_3$.

Résumés : [[1 - Database]]
