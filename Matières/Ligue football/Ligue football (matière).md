---
type: matiere
tags:
  - year3
sources:
  - "[[readme|readme (ligue football)]]"
maj: 2026-11-06
---

Projet de base de données de 3e année sur une ligue de football : modélisation (MCD, MLD), SQL (création, insertion, 9 requêtes) et application Python en ligne de commande avec 7 fonctions.

| Note | Résumé |
|---|---|
| [[readme\|readme]] | [[readme (résumé)\|Résumé]] |

`base.sql`, `requete.sql` et `app.py` ne sont pas dans le wiki : seule une note très courte existe pour le dépôt.

## Documents PDF

| Document | Contenu | Résumé |
|---|---|---|
| [[raw/Year 3/ligue football/for me/sujet database.pdf\|sujet database]] | Sujet de la SAÉ : attendus, livrables, calendrier | [[sujet database (résumé)\|Résumé]] |
| [[raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf\|Ligue Football - Projet DATABASE ID3-B]] | Rapport : contexte, dictionnaire, MLD, DDL, jeu de données, 9 requêtes | [[Rapport du projet Ligue Football (résumé)\|Résumé]] |

## Concepts

- **Gestion du projet** : [[Diagramme de Gantt]]
- **Modélisation (MERISE)** : [[Dictionnaire de données]], [[Modèle entité-association]], [[Type d'association]], [[Association ternaire]], [[Héritage en base de données]] (entité `Personne` et ses spécialisations `Joueur` et `Arbitre`), [[Schéma relationnel]], [[Table de correspondance]]
- **Création de la base (DDL)** : [[PostgreSQL]], [[Système de gestion de base de données]], [[Types de données SQL]], [[Clé primaire et clé étrangère]], [[Clé auto-incrémentée]], [[Contrainte d'intégrité]], [[Valeur NULL]]
- **Requêtes** : [[Langage SQL]], [[Algèbre relationnelle]], [[Jointure externe]], [[Sous-requête]], [[Fonction d'agrégation]], [[Expression CASE]]
- **Application** : [[Architecture n-tiers]], [[ODBC et JDBC]], [[Langage Java]]

## Liens avec les autres matières

- [[Data base (matière)]] : cours dont le projet applique les notions (MERISE, SQL, architectures d'accès).
- [[Java (matière)]] : un des langages proposés par le sujet pour l'application ([[Langage Java]], [[ODBC et JDBC]]).

## À revoir en priorité

- [[Rapport du projet Ligue Football (résumé)]] : le DDL imprimé contient des erreurs de syntaxe, et diffère du dictionnaire de données (types, statuts).
