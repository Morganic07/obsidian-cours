---
type: concept
tags:
  - year3
aliases:
  - projection
  - restriction
  - jointure naturelle
  - jointure
  - division relationnelle
  - opérateurs relationnels
  - renommage d'attributs
  - opérateurs ensemblistes
  - union relationnelle
  - différence relationnelle
  - relational algebra
matieres:
  - Data base
  - ligue football
sources:
  - "[[2 - opérateurs et SQL|Cours 3 - opérateurs et SQL]]"
  - "[[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]]"
maj: 2026-11-08
---

Opérateurs qui s'appliquent à des relations (tables) et renvoient une relation.

| Famille | Opérateur | Rôle |
|---|---|---|
| Sur une relation | projection $\pi_A(R)$ | garder certaines colonnes |
| | restriction $\sigma_F(R)$ | garder les lignes qui vérifient $F$ |
| | renommage $\rho_{A \to B}$ | renommer un attribut le temps de l'opération |
| Entre deux relations | [[Produit cartésien\|produit cartésien]] $R \times S$ | toutes les combinaisons de lignes |
| | jointure naturelle $R \bowtie S$ | lie sur les champs de même nom, souvent clé étrangère et clé primaire |
| | division $R \div S$ | éléments de $R$ associés à tous ceux de $S$ |
| Même schéma | union, intersection, différence | opérations d'ensembles |

Les opérateurs ensemblistes (union, intersection, différence) demandent deux relations de même schéma. La jointure se dérive d'un [[Produit cartésien|produit cartésien]] suivi d'une restriction. La division n'est pas implémentée dans tous les SGBD.

**Exemple de division** : `R` = (employé, certification) et `S` = certifications requises (Sécurité, Réseau). $R \div S$ garde les employés qui possèdent les deux.

## Compléments (hors du cours)

**Origine** : l'algèbre relationnelle accompagne le modèle relationnel proposé par E. F. Codd (IBM) en 1970. Une relation y est un ensemble de tuples, donc sans doublon, et chaque opérateur rend une relation : les opérateurs se composent.

**Correspondances SQL** :

| Algèbre relationnelle | SQL |
|---|---|
| projection $\pi_A(R)$ | `SELECT A FROM R` (`SELECT DISTINCT` pour retirer les doublons, que SQL garde par défaut) |
| restriction $\sigma_F(R)$ | `WHERE F` |
| renommage $\rho$ | `AS` |
| produit cartésien $R \times S$ | `CROSS JOIN` (ou `FROM R, S`) |
| jointure | `JOIN ... ON`, `NATURAL JOIN` |
| union, intersection, différence | `UNION`, `INTERSECT`, `EXCEPT` |

**Formules dérivées** (pour $R(A, C)$ et $S(C)$ ou $S(C, B)$ selon le cas) :

- jointure : $R \bowtie S = \pi\big(\sigma_{R.C = S.C}(R \times S)\big)$, la projection retirant la colonne commune en double ;
- division : $R \div S = \pi_A(R) \setminus \pi_A\big((\pi_A(R) \times S) \setminus R\big)$ — on retire les $A$ auxquels il manque au moins un élément de $S$ ;
- intersection : $R \cap S = R \setminus (R \setminus S)$.

**Division en SQL** (aucun opérateur dédié), sur l'exemple employé / certification :

```sql
-- par comptage
SELECT employe FROM R
WHERE certification IN (SELECT certification FROM S)
GROUP BY employe
HAVING COUNT(DISTINCT certification) = (SELECT COUNT(*) FROM S);

-- par double négation : il n'existe aucune certification requise que l'employé n'a pas
SELECT DISTINCT r1.employe FROM R r1
WHERE NOT EXISTS (
  SELECT * FROM S
  WHERE NOT EXISTS (
    SELECT * FROM R r2
    WHERE r2.employe = r1.employe AND r2.certification = S.certification));
```

Le résumé du sujet du projet Ligue Football y renvoie comme fondement des requêtes à écrire (complément du résumé).

Liens : [[Langage SQL]], [[Schéma relationnel]], [[Sous-requête]], [[Clé primaire et clé étrangère]], [[Produit cartésien]]

Résumés : [[2 - opérateurs et SQL]]
