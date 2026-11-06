---
type: concept
aliases: [table d'association, table de jonction, junction table, table de liaison]
sources: ["[[Cours 1 et 2 - Database]]"]
maj: 2026-11-06
---

Table créée pour traduire une association N-N, par exemple `est_inscrit(#code, #numéro)`, dont le couple d'attributs forme la clé primaire. Si l'association porte des attributs (redoublement, bourse), ils entrent dans la table : `est_inscrit(#code, #numéro, année universitaire, boursier)`, avec trois attributs en clé primaire ([[Cours 1 et 2 - Database]]).

Le rapport du projet étudiant Ligue Football a aussi une association N-N, les statistiques par joueur et par match ([[Rapport du projet Ligue Football (résumé)]]).

Notion parente : [[Type d'association]]. Voir aussi : [[Clé primaire et clé étrangère]].

## À vérifier

- L'année « 24-23 » de l'exemple du cours est incohérente.

Résumés : [[Cours 1 et 2 - Database (résumé)]], [[Rapport du projet Ligue Football (résumé)]]
