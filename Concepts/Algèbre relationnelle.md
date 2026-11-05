---
type: concept
aliases: [projection, restriction, jointure naturelle, jointure, produit cartésien, division relationnelle, opérateurs relationnels, renommage d'attributs]
matieres: [Data base]
sources: ["[[Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-05
---

Opérateurs qui s'appliquent à des relations (tables) et renvoient une relation.

| Famille | Opérateur | Rôle |
|---|---|---|
| Sur une relation | projection $\pi_A(R)$ | garder certaines colonnes |
| | restriction $\sigma_F(R)$ | garder les lignes qui vérifient $F$ |
| | renommage $\rho_{A \to B}$ | renommer un attribut le temps de l'opération |
| Entre deux relations | produit cartésien $R \times S$ | toutes les combinaisons de lignes |
| | jointure naturelle $R \bowtie S$ | lie sur les champs de même nom, souvent clé étrangère et clé primaire |
| | division $R \div S$ | éléments de $R$ associés à tous ceux de $S$ |
| Même schéma | union, intersection, différence | opérations d'ensembles |

La jointure se dérive d'un produit cartésien suivi d'une restriction. La division n'est pas implémentée dans tous les SGBD.

**Exemple de division** : `R` = (employé, certification) et `S` = certifications requises (Sécurité, Réseau). $R \div S$ garde les employés qui possèdent les deux.

Liens : [[Langage SQL]], [[Clé primaire et clé étrangère]]

Résumé : [[Cours 3 - opérateurs et SQL (résumé)]]
