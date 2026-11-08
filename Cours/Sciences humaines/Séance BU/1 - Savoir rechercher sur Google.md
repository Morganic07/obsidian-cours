---
type: source
tags:
  - year3
sources:
  - "[[Raw/Year 3/Cours BU - Savoir rechercher sur Google.docx|Cours BU - Savoir rechercher sur Google]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Cours BU - Savoir rechercher sur Google.docx|Cours BU - Savoir rechercher sur Google]]. Note très courte, sans matière associée, prise pendant une séance à la bibliothèque universitaire : les [[Opérateurs de recherche booléens]] pour faire une recherche Google.

## Faire une recherche Google

Le cours conseille d'utiliser des booléens pour faire de bonnes recherches.

Les opérateurs booléens viennent de l'algèbre de Boole (XIXᵉ siècle) : `AND`, `OR` et `NOT` sont la conjonction, la disjonction et la négation de la [[Logique propositionnelle|logique propositionnelle]]. Appliqués à une recherche, chaque mot désigne l'ensemble des pages qui le contiennent : `AND` en prend l'intersection (moins de résultats, plus précis), `OR` la réunion (plus de résultats, utile pour les synonymes et les traductions), `NOT` la différence (on retire un sens parasite). [[Complément hors du cours|ⓘ]]

| Syntaxe | Effet (d'après la note) |
|---|---|
| `mot1 AND mot2` | la recherche comprend les deux mots ; c'est le mode par défaut |
| `mot1 OR mot2` | l'un ou l'autre des mots |
| `mot1 NOT mot2` | l'un sans l'autre : l'ordre compte, on cherche le mot 1 sans le mot 2 |
| `"phrase"` | recherche exacte de la phrase entre guillemets |
| `archi*` | troncature : architecte, architecture, archimède, etc. |

Exemple : `archi*` renvoie à la fois *architecte*, *architecture* et *Archimède*.

L'exemple montre la limite de la troncature : couper trop court ramène des mots sans rapport (*Archimède*, *archipel*). On tronque donc après une racine assez longue et propre au sujet (`architect*`). [[Complément hors du cours|ⓘ]]

Quand on combine plusieurs opérateurs, les **parenthèses** fixent l'ordre d'évaluation, comme en logique : `(climat OR environnement) AND design` cherche les documents sur le design qui parlent de climat ou d'environnement. Sans parenthèses, le résultat dépend des règles de priorité de l'outil, qui varient d'une base à l'autre. [[Complément hors du cours|ⓘ]]

## Point à signaler

Sur Google, l'opérateur d'exclusion usuel est le signe moins (`-mot`) et `OR` doit être écrit en majuscules ; la note donne la syntaxe booléenne telle quelle. [[Complément hors du cours|ⓘ]]

Google ne gère pas vraiment la troncature : il élargit déjà de lui-même la recherche aux variantes d'un mot (pluriels, formes proches), et son astérisque `*` remplace un mot entier inconnu dans une expression entre guillemets (`"le * de la rose"`). La troncature `archi*` telle que la décrit la note fonctionne surtout dans les catalogues de bibliothèque et les bases de données documentaires. [[Complément hors du cours|ⓘ]]

## Autres opérateurs utiles sur Google

Google propose aussi des opérateurs qui filtrent sur une partie du document plutôt que sur son texte : [[Complément hors du cours|ⓘ]]

| Syntaxe | Effet |
|---|---|
| `site:gouv.fr` | limite la recherche à un site ou à un domaine |
| `filetype:pdf` | limite à un type de fichier (pdf, pptx, docx…), pratique pour trouver rapports et supports de cours |
| `intitle:mot` | le mot doit figurer dans le titre de la page |

Exemple : `"empreinte carbone" filetype:pdf site:ademe.fr` cherche l'expression exacte dans les PDF du site de l'Ademe. Les mêmes filtres existent sans syntaxe dans la page « Recherche avancée » de Google. [[Complément hors du cours|ⓘ]]

## Au-delà de Google

Pour un travail universitaire, Google n'est qu'un point de départ : [[Complément hors du cours|ⓘ]]
- **Google Scholar** ne cherche que dans les publications académiques (articles, thèses, livres) et indique par qui chaque texte est cité ;
- le **catalogue de la BU** et le **Sudoc** (catalogue collectif des bibliothèques universitaires françaises) disent où trouver un livre ou une revue ;
- les **bases de données** auxquelles la BU est abonnée donnent accès au texte intégral d'articles payants ; c'est là que les opérateurs booléens et la troncature servent le plus.

Un résultat trouvé se juge avant d'être utilisé : qui en est l'auteur et à quel titre il écrit, de quand il date, dans quel but il est publié (informer, vendre, convaincre), et s'il cite ses propres sources. Une source retenue se cite ensuite avec ses références complètes, pour éviter le plagiat. [[Complément hors du cours|ⓘ]]
