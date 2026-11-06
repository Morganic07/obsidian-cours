---
type: source
tags: [year4]
sources: ["[[Chp2 - tree]]"]
maj: 2026-11-05
---

Résumé de [[Chp2 - tree]], dans [[Graph theory (matière)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Arbres et forêts, arbre couvrant, et recherche d'un arbre couvrant de poids minimum par l'algorithme de Kruskal. Voir [[Arbre couvrant minimal]].

## Contenu, dans l'ordre du cours

- **Arbre** : graphe non orienté connexe et sans cycle. Un arbre est simple, et toute chaîne élémentaire est un arbre. Exemples dessinés : chaîne, étoile, deux nœuds internes reliés.
- **Forêt** : graphe non orienté sans cycle, dont chaque composante connexe est un arbre. Note : un arbre est une forêt, une forêt n'est pas toujours un arbre.
- **Pont** : arête dont la suppression ajoute une composante connexe.
- **Arbre couvrant** : sous-graphe qui est un arbre et contient tous les sommets. Un graphe connexe fini en a au moins un : on retire une arête qui n'est pas un pont tant qu'il en reste (terminaison par finitude de $E$). Exemple : un graphe à quatre sommets et un arbre couvrant de coût 6.
- **Valeur** d'un arbre couvrant : somme des poids de ses arêtes. **Arbre couvrant minimal** : de valeur minimale parmi les arbres couvrants d'un graphe simple, connexe, pondéré. Exemple : sept villes et douze arêtes pondérées en kilomètres.
- **Recherche** : l'énumération de tous les arbres couvrants est de complexité exponentielle, donc impraticable. Solution gloutonne : **algorithme de Kruskal** (ajouter l'arête de plus petit poids non testée si elle ne crée pas de cycle, jusqu'à $\text{card}(V) - 1$ arêtes). Le cours donne pré- et postconditions et le pseudo-code, et indique la complexité $O(\text{card}(E)\log\text{card}(V))$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Arbre minimal des villes** : l'image donne les arêtes Paris-Lille 222, Paris-Strasbourg 490, Paris-Brest 596, Paris-Bordeaux 583, Bordeaux-Perpignan 451, Perpignan-Nice 476. En exécutant Kruskal sur les douze arêtes de la transcription, on retrouve exactement ces six arêtes, de valeur totale 2818 (complément, calcul fait ici).
2. **Note finale sur Kruskal** : « minimisant la somme des poids des noeuds » doit se lire poids des arêtes (le cours pondère les arêtes).
3. **Propositions numérotées** (« Proposition 6 », « Théorème 2.5 ») : numéros repris d'un autre document, sans effet sur le contenu.
4. **Preuve de la proposition 6** : n'établit pas que le résultat est acyclique ; il faut ajouter qu'un graphe connexe dont toutes les arêtes sont des ponts n'a pas de cycle (complément).
