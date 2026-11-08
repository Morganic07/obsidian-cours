---
type: concept
tags:
  - year3
aliases:
  - GRANT
  - REVOKE
  - DCL
  - droits SQL
  - privilèges SQL
  - GRANT ALL PRIVILEGES
matieres:
  - Data base
sources:
  - "[[2 - opérateurs et SQL|Cours 3 - opérateurs et SQL]]"
maj: 2026-11-08
---

`GRANT` donne un droit **à** un utilisateur, par exemple `GRANT ALL PRIVILEGES ON dbname.* TO user IDENTIFIED BY password ;`, et `REVOKE` le retire **à** cet utilisateur, avec `FROM` : `REVOKE UPDATE ON dbname.tablename FROM user ;`. Sous MySQL, `dbname.*` désigne toute la base, alors qu'un nom seul désigne une table de la base courante (documentation MySQL 8.0, `GRANT` et `REVOKE`). La syntaxe diffère beaucoup d'un SGBDR à l'autre ([[2 - opérateurs et SQL|Cours 3 - opérateurs et SQL]]). [[Erreurs du cours#^e-gestion-des-droits-sql|✎]]

Notion parente : [[Langage SQL]]. Voir aussi : [[Système de gestion de base de données]].

Résumés : [[2 - opérateurs et SQL]]
