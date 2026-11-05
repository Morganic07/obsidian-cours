---
type: concept
aliases: [SQL, DDL, DML, requête SQL, requêtes SQL, SGBDR, Structured Query Language]
matieres: [Data base]
sources: ["[[Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-05
---

SQL (Structured Query Language) est le langage de requêtes des SGBDR. Sa syntaxe dépend du SGBD et de l'implémentation.

- **DDL** (Data Definition Language) : `CREATE`, `ALTER`, `DROP`, `DESCRIBE`. Uniquement lors de la conception ou de la modification du modèle.
- **DML** (Data Manipulation Language) : `INSERT INTO ... VALUES ...`, `UPDATE ... SET ... WHERE ...`, `DELETE FROM ... WHERE ...`, `SELECT ... FROM ... [WHERE ...]`. Les plus courantes, surtout `SELECT`.
- **Droits** : `GRANT` et `REVOKE`, en général réservés aux administrateurs.

**Architecture** : client-serveur 2 tiers, web 3 tiers (navigateur, serveur web, SGBD).

> [!warning] Écart dans le cours
> Le cours écrit `REVOKE ... TO user`. La syntaxe SQL est `REVOKE ... FROM user` (complément).

Liens : [[Algèbre relationnelle]], [[Clé primaire et clé étrangère]]

Résumé : [[Cours 3 - opérateurs et SQL (résumé)]]
