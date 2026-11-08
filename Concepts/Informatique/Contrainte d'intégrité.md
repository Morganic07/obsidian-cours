---
type: concept
tags: [year3]
aliases: [contrainte CHECK, contrainte UNIQUE, contraintes CHECK, integrity constraint, contraintes d'intégrité, intégrité référentielle, referential integrity, ON DELETE CASCADE, ON DELETE SET NULL]
matieres: [Data base, ligue football]
sources: ["[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]", "[[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]]", "[[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une contrainte d'intégrité est une règle déclarée dans le schéma de la base, que le [[Système de gestion de base de données|SGBD]] fait respecter à chaque insertion, modification ou suppression : une opération qui la violerait est refusée avec une erreur. Les données restent ainsi valides quelle que soit l'application qui les écrit.

**Contraintes déclarées dans `CREATE TABLE`** (complément, hors du cours) :

| Contrainte | Effet |
|---|---|
| `PRIMARY KEY` | identifiant de la ligne : unique et non NULL |
| `NOT NULL` | valeur obligatoire (voir [[Valeur NULL]]) |
| `UNIQUE` | deux lignes ne peuvent avoir la même valeur (clé candidate) |
| `DEFAULT valeur` | valeur mise si l'insertion n'en donne pas |
| `CHECK (condition)` | condition vraie pour chaque ligne (`CHECK (age >= 0)`) |
| `FOREIGN KEY (col) REFERENCES table(col)` | la valeur doit exister dans la table référencée |

**Intégrité référentielle** (complément, hors du cours) : une [[Clé primaire et clé étrangère|clé étrangère]] doit correspondre à une clé primaire existante de la table référencée, ou être `NULL` si la colonne l'autorise. Quand on supprime (ou modifie) la ligne référencée, le comportement se déclare sur la clé étrangère :
- par défaut, la suppression est **refusée** tant que des lignes la référencent (`NO ACTION` ou `RESTRICT`) ;
- `ON DELETE CASCADE` : les lignes qui la référencent sont supprimées en chaîne ; c'est le choix naturel pour une entité faible, qui n'a pas de sens sans son entité forte (les enfants d'un employé) ;
- `ON DELETE SET NULL` : la clé étrangère des lignes qui la référencent est mise à `NULL` (un étudiant dont le tuteur part).

## Dans le projet Ligue Football

Règles que la base impose aux données. Dans le DDL du projet de ligue de football (rapport d'étudiants) :

- `CHECK` : numéro de maillot entre 0 et 99, minutes entre 0 et 120, scores positifs, deux équipes différentes dans un match, `annee_fin > annee_debut` ; le statut d'un match doit prendre les quatre valeurs prévues par l'énoncé et le dictionnaire de données, `CHECK (statut IN ('Planifié', 'En cours', 'Terminé', 'Reporté'))` (le script du rapport omet « En cours ») ; [[Erreurs du cours#^e-contrainte-d-integrite|✎]]
- `UNIQUE` : sur l'e-mail, sur le nom d'équipe et sur `(id_saison, numero_journee)`.

Le cours de Data base ne nomme pas les contraintes d'intégrité : seul le rapport les emploie. Elles apparaissent dans les compléments de [[1 - Database]] (intégrité référentielle, entité faible) et de [[2 - opérateurs et SQL]] (contraintes du `CREATE TABLE`).

Notion parente : [[Langage SQL]]. Voir aussi : [[Clé primaire et clé étrangère]], [[Valeur NULL]], [[Types de données SQL]], [[Dictionnaire de données]], [[Transaction (base de données)]].
Résumés : [[1 - Database]], [[2 - opérateurs et SQL]]
