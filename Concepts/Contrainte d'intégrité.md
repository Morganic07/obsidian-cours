---
type: concept
aliases: [contrainte CHECK, contrainte UNIQUE, contraintes CHECK, integrity constraint, contraintes d'intégrité]
sources: ["[[raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B]]"]
maj: 2026-11-06
---

Règles que la base impose aux données. Dans le DDL du projet de ligue de football (rapport d'étudiants) :

- `CHECK` : numéro de maillot entre 0 et 99, minutes entre 0 et 120, scores positifs, deux équipes différentes dans un match, `annee_fin > annee_debut` ;
- `UNIQUE` : sur l'e-mail, sur le nom d'équipe et sur `(id_saison, numero_journee)`.

Le cours de Data base ne nomme pas les contraintes d'intégrité : seul le rapport les emploie.

Notion parente : [[Langage SQL]]. Voir aussi : [[Clé primaire et clé étrangère]], [[Valeur NULL]], [[Types de données SQL]].

## À vérifier

Le statut « En cours » est absent de la contrainte `CHECK` du rapport.

Résumés : [[Rapport du projet Ligue Football (résumé)]]
