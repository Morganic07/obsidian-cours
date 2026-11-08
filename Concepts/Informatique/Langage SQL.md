---
type: concept
tags:
  - year3
aliases:
  - SQL
  - DDL
  - DML
  - requête SQL
  - requêtes SQL
  - Structured Query Language
matieres:
  - Data base
  - ligue football
sources:
  - "[[2 - opérateurs et SQL|Cours 3 - opérateurs et SQL]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
maj: 2026-11-08
---

SQL (Structured Query Language) est le langage de requêtes des SGBDR ([[Système de gestion de base de données]]). Sa syntaxe dépend du SGBD et de l'implémentation.

- **DDL** (Data Definition Language) : `CREATE`, `ALTER`, `DROP`, `DESCRIBE`. Uniquement lors de la conception ou de la modification du modèle.
- **DML** (Data Manipulation Language) : `INSERT INTO ... VALUES ...`, `UPDATE ... SET ... WHERE ...`, `DELETE FROM ... WHERE ...`, `SELECT ... FROM ... [WHERE ...]`. Les plus courantes, surtout `SELECT`.
- **Droits** ([[Gestion des droits SQL]]) : `GRANT ... TO user` et `REVOKE ... FROM user`, en général réservés aux administrateurs. [[Erreurs du cours#^e-langage-sql|✎]]

**Dans le projet de ligue de football** : un DDL PostgreSQL avec des [[Contrainte d'intégrité|contraintes d'intégrité]] (`CHECK`, `UNIQUE`), et neuf requêtes, avec jointures, [[Jointure externe|jointure externe]] (`LEFT JOIN`), [[Fonction d'agrégation|fonctions d'agrégation]] (`SUM`, `AVG`), `GROUP BY`, `HAVING`, [[Expression CASE|expression `CASE`]] et [[Sous-requête|sous-requêtes]] ([[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Rapport du projet]]). Voir aussi [[Types de données SQL]]. Dans ce DDL, les valeurs des `CHECK` et des `DEFAULT` s'écrivent entre apostrophes (`CHECK (poste IN ('Gardien', ...))`, `DEFAULT 'En cours'`), car PostgreSQL lit les guillemets doubles comme des noms de colonnes, et la dernière ligne d'un `CREATE TABLE` ne prend pas de virgule avant `)` (le script du rapport emploie des guillemets doubles et laisse une virgule en trop dans `ARBITRE`). [[Erreurs du cours#^e-langage-sql|✎]]

**Architecture** : client-serveur 2 tiers, web 3 tiers (navigateur, serveur web, SGBD).

Liens : [[Algèbre relationnelle]], [[Clé primaire et clé étrangère]]

Résumés : [[2 - opérateurs et SQL]]
