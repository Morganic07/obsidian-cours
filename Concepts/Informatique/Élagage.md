---
type: concept
tags: [year4]
aliases: [pruning, tree pruning]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'élagage simplifie un [[Arbre de décision]] pour combattre le [[Surapprentissage]]. Un arbre développé jusqu'à des feuilles pures apprend aussi le bruit : ses dernières coupes ne valent que pour les exemples d'apprentissage.

- **Pré-élagage** : arrêter la croissance de l'arbre en cours de construction (profondeur maximale, effectif minimal par feuille, gain trop faible). Ce sont les conditions d'arrêt.
- **Post-élagage** : construire l'arbre entier, puis remplacer par des feuilles les sous-arbres qui n'améliorent pas l'erreur estimée. C'est la pratique de C4.5 et de CART. Elle est en général plus sûre : une coupe peu utile peut en préparer une très utile, que le pré-élagage n'aurait jamais atteinte.
- L'ensemble qui sert à choisir l'arbre élagué joue le rôle d'un ensemble de validation ; l'évaluation finale se fait sur un ensemble de test distinct (voir [[Ensemble d'entraînement et de test]], [[Validation d'un classifieur]]).

## Dans le cours

Dans l'[[Algorithme CART]] : on construit l'arbre entier, on l'élague successivement (en supprimant deux feuilles filles d'un même nœud), puis on garde l'arbre élagué le plus performant, celui qui a la plus petite erreur sur la base de test. L'[[Algorithme C4.5]] prévoit aussi l'élagage.

Notion parente : [[Arbre de décision]].

Résumés : [[1 - pdf du prof]], [[1 - intro to data mining]]
