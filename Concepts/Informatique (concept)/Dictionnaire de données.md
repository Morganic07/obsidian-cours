---
type: concept
tags:
  - year3
aliases:
  - data dictionary
  - dictionnaire des données
sources:
  - "[[1 - Database (résumé)|Cours 1 et 2 - Database]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
maj: 2026-11-06
---

Première étape de la méthode MERISE : lister les données non décomposables, avec pour chacune son nom, son type, si elle peut être nulle, ses autres caractéristiques et sa valeur par défaut ([[1 - Database (résumé)|Cours 1 et 2 - Database]]).

Le rapport du projet étudiant Ligue Football ajoute à chaque donnée son domaine, sa contrainte et un exemple.

Notion parente : [[Modèle entité-association]]. Voir aussi : [[Schéma relationnel]], [[Types de données SQL]].

## À vérifier

- Dans le rapport, le dictionnaire et le DDL ne coïncident pas : `ENUM`, `YEAR`, `AUTO_INCREMENT` d'un côté, `VARCHAR` + `CHECK`, `SERIAL` de l'autre.

Résumés : [[1 - Database (résumé)]], [[Rapport du projet Ligue Football (résumé)]], [[sujet database (résumé)]]
