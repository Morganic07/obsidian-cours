---
type: concept
tags: [year3]
aliases: [Postgres]
matieres: [ligue football]
sources: ["sujet database.pdf, dans Raw/Year 3/ligue football/for me (exclu du miroir)", "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : PostgreSQL est un [[Système de gestion de base de données|système de gestion de bases de données]] relationnel libre (SGBDR), réputé pour son respect de la norme [[Langage SQL|SQL]] et sa robustesse transactionnelle. Il fonctionne en [[Modèle client-serveur|client-serveur]] : on l'interroge avec le client en ligne de commande `psql` ou depuis un programme (psycopg en Python, JDBC en Java). Il ajoute au SQL standard des types et fonctionnalités propres, comme le pseudo-type `SERIAL` pour les [[Clé auto-incrémentée|clés auto-incrémentées]].

## Dans le cours

Nommé sans définition : SGBDR imposé par le sujet database (dans Raw/Year 3/ligue football/for me, exclu du miroir). Le DDL du rapport du projet étudiant est écrit pour lui (`SERIAL`, `CHECK`), et l'application Python s'y connecte par psycopg.

Notion parente : [[Système de gestion de base de données]]. Voir aussi : [[ODBC et JDBC]].

Résumés : [[1 - OS]], [[2 - opérateurs et SQL]]
