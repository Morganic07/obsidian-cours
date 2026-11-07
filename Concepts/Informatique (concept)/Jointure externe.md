---
type: concept
tags: [year3]
aliases: [LEFT JOIN, outer join, left outer join]
sources: ["[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une jointure externe associe les lignes de deux tables selon une condition, comme une jointure interne, mais conserve aussi les lignes qui n'ont pas de correspondance, en complétant les colonnes de l'autre table par des [[Valeur NULL|valeurs NULL]]. `LEFT JOIN` (ou `LEFT OUTER JOIN`) garde toutes les lignes de la table de gauche, `RIGHT JOIN` celles de la table de droite, `FULL OUTER JOIN` celles des deux. Par exemple, un `LEFT JOIN` des équipes vers les matchs gagnés fait apparaître aussi les équipes sans victoire.

## Dans le cours

Nommée sans définition dans le rapport du projet étudiant Ligue Football, qui emploie un `LEFT JOIN` pour classer les équipes par victoires. La jointure externe n'apparaît pas dans le cours de Data base.

Notion parente : [[Algèbre relationnelle]].

Résumés (rapprochement, complément hors du cours) : [[2 - opérateurs et SQL (résumé)]]
