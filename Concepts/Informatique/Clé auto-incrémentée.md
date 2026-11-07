---
type: concept
tags: [year3]
aliases: [SERIAL, AUTO_INCREMENT, auto-incrément, auto increment]
matieres: [ligue football]
sources: ["[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une clé auto-incrémentée est une [[Clé primaire et clé étrangère|clé primaire]] dont le [[Système de gestion de base de données|SGBD]] génère lui-même la valeur à chaque insertion, en prenant l'entier suivant d'un compteur : on n'a pas à fournir l'identifiant dans l'`INSERT`. La syntaxe dépend du SGBD : `AUTO_INCREMENT` en MySQL, `SERIAL` (ou `GENERATED … AS IDENTITY`) en [[PostgreSQL]], où `SERIAL` crée en fait une séquence associée à la colonne.

## Dans le cours

Nommé dans le rapport du projet de ligue de football (travail d'étudiants) sans définition : le dictionnaire de données annonce une clé `AUTO_INCREMENT` (syntaxe MySQL), alors que le DDL [[PostgreSQL]] utilise `SERIAL PRIMARY KEY`.

Notion parente : [[Clé primaire et clé étrangère]]. Voir aussi : [[Types de données SQL]].

Résumés : [[Rapport du projet Ligue Football (résumé)]]
