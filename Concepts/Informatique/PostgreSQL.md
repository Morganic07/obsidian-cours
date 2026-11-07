---
type: concept
tags: [year3]
aliases: [Postgres]
matieres: [ligue football]
sources: ["[[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]", "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : PostgreSQL est un [[Système de gestion de base de données|système de gestion de bases de données]] relationnel libre (SGBDR), réputé pour son respect de la norme [[Langage SQL|SQL]] et sa robustesse transactionnelle. Il fonctionne en [[Modèle client-serveur|client-serveur]] : on l'interroge avec le client en ligne de commande `psql` ou depuis un programme (psycopg en Python, JDBC en Java). Il ajoute au SQL standard des types et fonctionnalités propres, comme le pseudo-type `SERIAL` pour les [[Clé auto-incrémentée|clés auto-incrémentées]].

## Dans le cours

Nommé sans définition : SGBDR imposé par le sujet database ([[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]). Le DDL du rapport du projet étudiant est écrit pour lui (`SERIAL`, `CHECK`), et l'application Python s'y connecte par psycopg.

Notion parente : [[Système de gestion de base de données]]. Voir aussi : [[ODBC et JDBC]].

Résumés : [[sujet database (résumé)]], [[Rapport du projet Ligue Football (résumé)]], [[readme (résumé)]]
