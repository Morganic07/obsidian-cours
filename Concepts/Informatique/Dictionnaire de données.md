---
type: concept
tags:
  - year3
aliases:
  - data dictionary
  - dictionnaire des données
sources:
  - "[[1 - Database|Cours 1 et 2 - Database]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
maj: 2026-11-07
---

Première étape de la méthode MERISE : lister les données non décomposables, avec pour chacune son nom, son type, si elle peut être nulle, ses autres caractéristiques et sa valeur par défaut ([[1 - Database|Cours 1 et 2 - Database]]).

Le rapport du projet étudiant Ligue Football ajoute à chaque donnée son domaine, sa contrainte et un exemple. Son dictionnaire et son DDL n'emploient pas les mêmes types : `ENUM`, `YEAR` et `AUTO_INCREMENT` (à la manière de MySQL) dans le dictionnaire, `VARCHAR` avec `CHECK`, `INT` et `SERIAL` (à la manière de PostgreSQL) dans le DDL.

Notion parente : [[Modèle entité-association]]. Voir aussi : [[Schéma relationnel]], [[Types de données SQL]].

Résumés : [[1 - Database]]
