---
type: concept
tags: [year3]
aliases: [transaction, transactions, ACID, propriétés ACID, COMMIT, ROLLBACK, START TRANSACTION, TCL, Transaction Control Language]
matieres: [Data base]
sources: ["[[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une transaction est une suite de requêtes que le [[Système de gestion de base de données|SGBD]] exécute comme un tout : soit toutes ses modifications sont enregistrées, soit aucune. Elle fait passer la base d'un état cohérent à un autre état cohérent.

**Syntaxe** (SQL standard, [[PostgreSQL]], MySQL) :

```sql
BEGIN;                       -- ou START TRANSACTION
UPDATE compte SET solde = solde - 100 WHERE id = 1;
UPDATE compte SET solde = solde + 100 WHERE id = 2;
COMMIT;                      -- valide ; ROLLBACK annule tout depuis BEGIN
```

Exemple type : le **virement**, qui débite un compte et en crédite un autre, jamais l'un sans l'autre. Si une erreur survient entre les deux `UPDATE`, un `ROLLBACK` remet la base dans l'état d'avant `BEGIN`. Sans `BEGIN` explicite, la plupart des SGBD sont en mode *autocommit* : chaque requête est une transaction à elle seule.

**Propriétés ACID**, garanties par un SGBD relationnel :
- **Atomicité** : tout ou rien ;
- **Cohérence** : à la fin de la transaction, les [[Contrainte d'intégrité|contraintes d'intégrité]] sont toujours respectées, sinon elle est refusée ;
- **Isolation** : des transactions simultanées ne voient pas les modifications à moitié faites les unes des autres ; tout se passe comme si elles s'exécutaient l'une après l'autre (avec des niveaux d'isolation plus ou moins stricts selon le SGBD) ;
- **Durabilité** : une transaction validée par `COMMIT` survit à une panne, car le SGBD l'a inscrite dans un journal sur disque avant de confirmer.

`COMMIT` et `ROLLBACK` (avec `SAVEPOINT`, qui pose un point de retour partiel) forment parfois une famille à part du [[Langage SQL|SQL]], le **TCL** (*Transaction Control Language*), à côté du DDL, du DML et du DCL.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - opérateurs et SQL]], à propos des requêtes DML (`INSERT`, `UPDATE`, `DELETE`) et des familles de commandes SQL.

Voir aussi : [[Langage SQL]], [[Système de gestion de base de données]], [[Contrainte d'intégrité]], [[Gestion des droits SQL]], [[PostgreSQL]]

Résumés : [[2 - opérateurs et SQL]]
