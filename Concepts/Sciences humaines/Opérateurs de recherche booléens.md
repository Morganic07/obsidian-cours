---
type: concept
tags:
  - year3
aliases:
  - opérateurs booléens
  - recherche booléenne
sources:
  - "[[1 - Savoir rechercher sur Google|Cours BU - Savoir rechercher sur Google]]"
  - "[[Raw/Year 3/Cours BU - Savoir rechercher sur Google.docx|Cours BU - Savoir rechercher sur Google]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : mots de liaison qui combinent les termes d'une requête selon la logique de George Boole (algèbre de Boole) : ce sont les connecteurs de la [[Logique propositionnelle]] appliqués à des ensembles de documents. Chaque terme désigne l'ensemble des documents qui le contiennent ; l'opérateur dit comment combiner ces ensembles.

Opérateurs présentés par la BU pour une recherche Google :

- `mot1 AND mot2` : les deux mots (mode par défaut) ;
- `OR` : l'un ou l'autre ;
- `NOT` : le premier sans le second (l'ordre compte) ;
- `"phrase"` : recherche exacte ;
- `archi*` : troncature (architecte, architecture…).

## Compléments (hors du cours)

- **Sens ensembliste** : `AND` = intersection (moins de résultats, plus précis) ; `OR` = réunion (plus de résultats : synonymes, traductions, variantes) ; `NOT` = différence (on retire un sens parasite).
- **Parenthèses** : elles fixent l'ordre d'évaluation, comme en logique : `(climat OR environnement) AND design` cherche les documents sur le design qui parlent de climat ou d'environnement.
- **Sur Google** : l'exclusion s'écrit `-mot` (sans espace après le tiret) ; `OR` doit être en majuscules ; il n'y a pas de vraie troncature, Google élargissant déjà de lui-même aux variantes d'un mot ; `*` y remplace un mot entier dans une expression entre guillemets (`"le * de la recherche"`). La troncature `archi*` fonctionne surtout dans les catalogues de bibliothèque et les bases documentaires.
- **Bien tronquer** : une troncature trop courte produit du bruit (`archi*` ramène aussi Archimède ou archives) ; tronquer après une racine propre au sujet (`architect*`).
- **Filtres Google** : `site:` limite à un site ou un domaine (`site:gouv.fr`), `filetype:` à un format de fichier (`filetype:pdf`), `intitle:` aux pages dont le titre contient le mot.

Voir aussi : [[Logique propositionnelle]].

Résumés : [[1 - Savoir rechercher sur Google]]
