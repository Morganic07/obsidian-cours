---
type: source
tags:
  - year3
sources:
  - "[[Raw/Year 3/ligue football/readme.docx|readme (ligue football)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/ligue football/readme.docx|readme]], dans [[Ligue football (matière)]]. Note très courte : un fichier de présentation de projet de base de données.

Il accompagne le rendu demandé par [[sujet database (résumé)]] ; le rapport est résumé dans [[Rapport du projet Ligue Football (résumé)]].

## Fichiers du rendu

| Fichier | Contenu |
|---|---|
| `Ligue Football - Projet DATABASE ID3-B.pdf` | le rapport : dictionnaire de données, [[Modèle entité-association\|MCD]], [[Schéma relationnel\|MLD]], schéma d'architecture contextualisé, DDL (`CREATE TABLE` et insertion d'un jeu de données), DML (9 requêtes SQL représentatives) |
| `base.sql` | création des tables et `INSERT INTO` du jeu de données initial ([[Langage SQL]]) |
| `requete.sql` | les 9 requêtes représentatives |
| `app.py` | toute l'application en Python, avec psycopg ([[ODBC et JDBC]]) |
| `Presentation.mp4` | courte présentation du script Python |

## L'application `app.py`

Application en ligne de commande ([[Interface en ligne de commande]]) qui manipule les données par 7 fonctions :

1. classement des meilleurs buteurs (`SELECT`) ;
2. liste des capitaines de chaque équipe (`SELECT`) ;
3. historique des matchs d'une saison (`SELECT`) ;
4. changer le capitaine d'une équipe (`UPDATE`) ;
5. ajouter un joueur (`INSERT INTO`) ;
6. supprimer un joueur (`DELETE`) ;
7. afficher tous les joueurs (`SELECT`).

## Points d'attention signalés par le readme

- **Ajout d'un joueur** : il ne faut pas saisir un identifiant de joueur qui existe déjà dans la table `PERSONNE` (l'identifiant du joueur est aussi celui de la personne, par héritage : [[Héritage en base de données]]).
- **Suppression d'un joueur** : la fonction ne peut supprimer qu'un joueur « totalement neuf », jamais associé à une statistique dans `STATISTIQUE_JOUEUR_MATCH` ; sinon la [[Clé primaire et clé étrangère|clé étrangère]] empêche la suppression ([[Contrainte d'intégrité]]).
