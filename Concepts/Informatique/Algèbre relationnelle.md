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
matieres:
  - Data base
  - ligue football
sources:
  - "[[2 - opérateurs et SQL|Cours 3 - opérateurs et SQL]]"
maj: 2026-11-06
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

Le résumé du sujet du projet Ligue Football y renvoie comme fondement des requêtes à écrire (complément du résumé).

Liens : [[Langage SQL]], [[Schéma relationnel]], [[Sous-requête]], [[Clé primaire et clé étrangère]], [[Produit cartésien]]

Résumés : [[2 - opérateurs et SQL]]
