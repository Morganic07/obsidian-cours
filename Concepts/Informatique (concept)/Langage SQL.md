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
  - "[[2 - opérateurs et SQL (résumé)|Cours 3 - opérateurs et SQL]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
maj: 2026-11-06
---

SQL (Structured Query Language) est le langage de requêtes des SGBDR ([[Système de gestion de base de données]]). Sa syntaxe dépend du SGBD et de l'implémentation.

- **DDL** (Data Definition Language) : `CREATE`, `ALTER`, `DROP`, `DESCRIBE`. Uniquement lors de la conception ou de la modification du modèle.
- **DML** (Data Manipulation Language) : `INSERT INTO ... VALUES ...`, `UPDATE ... SET ... WHERE ...`, `DELETE FROM ... WHERE ...`, `SELECT ... FROM ... [WHERE ...]`. Les plus courantes, surtout `SELECT`.
- **Droits** ([[Gestion des droits SQL]]) : `GRANT` et `REVOKE`, en général réservés aux administrateurs.

**Dans le projet de ligue de football** : un DDL PostgreSQL et neuf requêtes, avec jointures, `LEFT JOIN`, [[Fonction d'agrégation|fonctions d'agrégation]] (`SUM`, `AVG`), `GROUP BY`, `HAVING`, `CASE` et [[Sous-requête|sous-requêtes]] ([[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Rapport du projet]]). Voir aussi [[Types de données SQL]].

**Architecture** : client-serveur 2 tiers, web 3 tiers (navigateur, serveur web, SGBD).

> [!warning] Écart dans le cours
> Le cours écrit `REVOKE ... TO user`. La syntaxe SQL est `REVOKE ... FROM user` (complément).

Liens : [[Algèbre relationnelle]], [[Clé primaire et clé étrangère]]

## À vérifier

- Le DDL du rapport du projet n'est pas exécutable tel quel (guillemets doubles, virgules).

Résumés : [[2 - opérateurs et SQL (résumé)]]
