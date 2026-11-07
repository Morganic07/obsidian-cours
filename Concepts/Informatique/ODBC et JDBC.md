---
type: concept
tags: [year3]
aliases: [ODBC, JDBC, psycopg]
matieres: [ligue football]
sources: ["sujet database.pdf, dans Raw/Year 3/ligue football/for me (exclu du miroir)", "readme.docx, dans Raw/Year 3/ligue football (exclu du miroir)"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : ODBC (Open Database Connectivity) et JDBC (Java Database Connectivity) sont des interfaces de programmation standard qui permettent à une application de se connecter à une base de données, d'y envoyer des requêtes [[Langage SQL|SQL]] et d'en lire les résultats sans dépendre du [[Système de gestion de base de données|SGBD]] utilisé. ODBC est une interface indépendante du langage, utilisée surtout depuis C ; JDBC est son équivalent pour [[Langage Java|Java]]. Dans les deux cas, un pilote propre à chaque SGBD fait la traduction. En Python, le rôle équivalent revient à des bibliothèques comme psycopg pour [[PostgreSQL]].

## Dans le cours

Nommés sans définition : le sujet database (dans Raw/Year 3/ligue football/for me, exclu du miroir) demande une application en Java, Python ou C reliée à la base par ODBC ou JDBC. Le rendu du projet étudiant (readme.docx, dans Raw/Year 3/ligue football, exclu du miroir) utilise Python avec psycopg.

Voir aussi : [[PostgreSQL]], [[Langage Java]].

Résumés (rapprochement, complément hors du cours) : [[2 - opérateurs et SQL]]
