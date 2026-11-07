---
type: concept
tags:
  - year3
aliases:
  - MLD
  - modèle logique de données
  - schéma relationnel
  - relational diagram
  - relation (base de données)
  - attribut (base de données)
matieres:
  - Data base
  - ligue football
sources:
  - "[[1 - Database (résumé)|Cours 1 et 2 - Database]]"
  - "[[2 - opérateurs et SQL (résumé)|Cours 3 - opérateurs et SQL]]"
maj: 2026-11-06
---

Le MLD (modèle logique de données) est la liste des tables avec leurs clés primaires (soulignées) et leurs clés étrangères (précédées de `#`). C'est la troisième étape de la méthode MERISE, obtenue à partir du [[Modèle entité-association]]. Vocabulaire : une **relation** est une table, ses **attributs** sont les colonnes. Exemple : `ETUDIANT(numero, nom, date_naissance)`.

**Règles de passage du MCD au MLD** (cours)
- Cardinalité 1-N : la clé étrangère est placée du côté de la cardinalité « 1 ». Exemple : `ETUDIANT(numero, ..., #code)` pour un étudiant qui suit une formation.
- Cardinalité N-N : on crée une table de correspondance, `est_inscrit(#code, #numero)`, dont le couple est la clé primaire.
- Association avec attributs portés : une table supplémentaire.
- Cardinalité 1-1 : elle ne devrait pas apparaître dans un schéma de conception.
- Héritage : `Client(numero)`, `PersonnePhysique(#numeroPP, ...)`, `PersonneMorale(#numeroPM, ...)`.

Le rapport du projet Ligue Football donne un MLD de 11 tables, clés étrangères notées `#`, avec des clés composées pour `STATISTIQUE_JOUEUR_MATCH` et `SPONSOR_EQUIPE_SAISON`.

Liens : [[Clé primaire et clé étrangère]], [[Table de correspondance]], [[Algèbre relationnelle]], [[Héritage en base de données]]

Résumés : [[1 - Database (résumé)]], [[2 - opérateurs et SQL (résumé)]], [[Rapport du projet Ligue Football (résumé)]]
