---
type: concept
tags:
  - year3
aliases:
  - types SQL
  - VARCHAR
  - DECIMAL
  - BLOB
  - ENUM
  - TIMESTAMP
  - DATETIME
  - SQL data types
matieres:
  - Data base
  - ligue football
sources:
  - "[[1 - Database (résumé)|Cours 1 et 2 - Database]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
maj: 2026-11-06
---

Types de colonnes présentés par le cours :

- **texte** : `VARCHAR(n)`, `CHAR(n)` de longueur fixe, `TEXT`, `ENUM` ;
- **nombres** : `INT`, `DECIMAL(p,s)`, exact et à préférer pour l'argent, `FLOAT` ;
- **dates** : `DATE`, `DATETIME` ou `TIMESTAMP` ;
- `BOOLEAN` et `BLOB`.

Le projet étudiant Ligue Football utilise aussi `YEAR` et, en PostgreSQL, `SERIAL`.

Notion parente : [[Langage SQL]]. Voir aussi : [[Valeur NULL]], [[Dictionnaire de données]].

## À vérifier

- `DATETIME` et `TIMESTAMP` sont présentés comme un seul type, alors qu'ils diffèrent selon le SGBD.

Résumés : [[1 - Database (résumé)]], [[Rapport du projet Ligue Football (résumé)]], [[sujet database (résumé)]]
