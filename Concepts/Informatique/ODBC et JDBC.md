---
type: concept
tags: [year3]
aliases: [ODBC, JDBC, psycopg]
matieres: [ligue football]
sources: ["[[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]", "[[readme (résumé)|readme]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : ODBC (Open Database Connectivity) et JDBC (Java Database Connectivity) sont des interfaces de programmation standard qui permettent à une application de se connecter à une base de données, d'y envoyer des requêtes [[Langage SQL|SQL]] et d'en lire les résultats sans dépendre du [[Système de gestion de base de données|SGBD]] utilisé. ODBC est une interface indépendante du langage, utilisée surtout depuis C ; JDBC est son équivalent pour [[Langage Java|Java]]. Dans les deux cas, un pilote propre à chaque SGBD fait la traduction. En Python, le rôle équivalent revient à des bibliothèques comme psycopg pour [[PostgreSQL]].

## Dans le cours

Nommés sans définition : le sujet database ([[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]) demande une application en Java, Python ou C reliée à la base par ODBC ou JDBC. Le rendu du projet étudiant ([[readme (résumé)|readme]]) utilise Python avec psycopg.

Voir aussi : [[PostgreSQL]], [[Langage Java]].

Résumés : [[sujet database (résumé)]], [[readme (résumé)]]
