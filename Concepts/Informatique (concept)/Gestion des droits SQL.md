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
  - "[[2 - opérateurs et SQL (résumé)|Cours 3 - opérateurs et SQL]]"
maj: 2026-11-06
---

`GRANT` donne un droit, par exemple `GRANT ALL PRIVILEGES ON dbname TO user IDENTIFIED BY password ;`, et `REVOKE` le retire. La syntaxe diffère beaucoup d'un SGBDR à l'autre ([[2 - opérateurs et SQL (résumé)|Cours 3 - opérateurs et SQL]]).

Notion parente : [[Langage SQL]]. Voir aussi : [[Système de gestion de base de données]].

## À vérifier

- Le cours écrit `REVOKE UPDATE ON dbname.tablename TO user` : il faut `FROM` (à corriger avant un examen).
- `IDENTIFIED BY` est propre à certaines versions de MySQL.

Résumés : [[2 - opérateurs et SQL (résumé)]]
