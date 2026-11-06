---
type: source
tags: [year3]
sources: ["[[Cours/Year 3/ligue football/readme|readme (ligue football)]]"]
maj: 2026-11-05
---

Résumé de [[Cours/Year 3/ligue football/readme|readme]], dans [[Ligue football (matière)]]. Note très courte : un fichier de présentation de projet de base de données.

Contenu du rendu décrit :
- un rapport PDF : dictionnaire de données, MCD, MLD, schéma d'architecture, DDL (création des tables et jeu de données), DML (9 requêtes SQL) ;
- `base.sql` (tables et `INSERT INTO`) et `requete.sql` (9 requêtes) ;
- `app.py` : application en ligne de commande en Python (psycopg) avec 7 fonctions : classement des buteurs, capitaines par équipe, historique des matchs d'une saison, changement de capitaine (UPDATE), ajout d'un joueur (INSERT), suppression d'un joueur (DELETE), liste des joueurs ;
- une vidéo de présentation.

Points d'attention notés : l'ajout exige un identifiant de joueur inédit ; la suppression ne marche que pour un joueur sans statistique, à cause de la clé étrangère.
