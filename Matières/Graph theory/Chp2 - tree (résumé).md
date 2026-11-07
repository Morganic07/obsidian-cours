---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Chp2 - tree.docx|Chp2 - tree]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 4/graph theory/Chp2 - tree.docx|Chp2 - tree]], dans [[Graph theory (matière)]]. Cours en anglais (pseudo-code en français). En cas d'écart, le cours et ses images font foi. Images non ouvertes : lues par leur transcription.

## Idée générale

Arbres et forêts, arbre couvrant, et recherche d'un arbre couvrant de poids minimum par l'algorithme de Kruskal. Voir [[Arbre couvrant minimal]].

## Arbre

**Définition.** Un **arbre** (*tree*) est un [[Graphe non orienté|graphe non orienté]] **connexe** et **acyclique** (sans cycle). Voir [[Arbre (théorie des graphes)]].

**Propositions 1 et 2.**
- Tout arbre est un [[Graphe simple|graphe simple]].
- Toute [[Chaîne (graphe)|chaîne élémentaire]] est un arbre.

![[Chp2 - tree - image2.png]]
*Figure : trois exemples d'arbres — une chaîne élémentaire de 4 sommets alignés ; une étoile (un sommet central relié à 3 feuilles) ; deux sommets internes reliés entre eux, portant 2 et 3 feuilles.*

## Forêt et pont

- **Forêt** (*forest*) : graphe non orienté **acyclique**. Voir [[Forêt (graphe)]].
- Toute [[Graphe connexe|composante connexe]] d'une forêt est un arbre.
- **Pont** (*bridge*) : soit $G = (V, E, \gamma)$ ; un pont de $G$ est une arête $e$ telle que $G - e$ a **une composante connexe de plus** que $G$. Voir [[Pont (graphe)]].

Note de l'étudiante : un arbre est une forêt ; une forêt n'est pas (forcément) un arbre.

## Arbre couvrant (*spanning tree*)

**Définition.** Soit $G = (V, E, \gamma)$. Un [[Sous-graphe|sous-graphe]] $T$ est un **arbre couvrant** de $G$ si et seulement si $T$ est un arbre **et** un sous-graphe couvrant de $G$.

**Remarque du cours.** Un sous-graphe (couvrant) de $G = (V, E, \gamma)$ est un graphe $G' = (V, E')$ avec $E' \subseteq E$ : mêmes sommets, une partie des arêtes.

Note de l'étudiante : un arbre couvrant de $G$ reprend **tous les nœuds** de $G$ et un sous-ensemble des arêtes tel que le sous-graphe soit un arbre.

**Proposition 6.** Tout graphe **fini connexe** possède au moins un arbre couvrant.

*Preuve du cours* : soit $G$ fini ; tant qu'il reste des arêtes qui ne sont pas des ponts, on en retire une ; le processus termine parce que $E$ est fini (voir Points à vérifier, 4).

![[Chp2 - tree - image9.png]]
*Figure (« FIG. 2.15 ») : un graphe complet sur a, b, c, d (a–b 2, a–c 6, a–d 3, b–c 3, b–d 7, c–d 1) et un arbre couvrant de coût minimum 6 (a–b 2, b–c 3, c–d 1).*

## Graphe pondéré et arbre couvrant minimal

**Définition (valeur).** Soient $G = (V, E, \gamma, w)$ un [[Graphe pondéré|graphe pondéré]] non orienté et $T = (V, E', \gamma|_{E'})$ un arbre couvrant de $G$, $E' \subseteq E$. La **valeur** de $T$ est
$$w(T) = \sum_{e \in E'} w(e).$$

**Définition (arbre couvrant minimal).** Soit $G = (V, E, w)$ un graphe **simple, connexe, pondéré**. Un **arbre couvrant minimal** (*minimum spanning tree*) de $G$ est un arbre couvrant dont la valeur est **minimale** parmi tous les arbres couvrants de $G$.

### Exemple : sept villes

| Arête | Poids (km) |
|---|---|
| Lille – Brest | 725 |
| Lille – Paris | 222 |
| Lille – Strasbourg | 522 |
| Brest – Paris | 596 |
| Brest – Bordeaux | 623 |
| Strasbourg – Paris | 490 |
| Strasbourg – Nice | 804 |
| Paris – Bordeaux | 583 |
| Paris – Perpignan | 857 |
| Paris – Nice | 932 |
| Bordeaux – Perpignan | 451 |
| Nice – Perpignan | 476 |

![[Chp2 - tree - image3.png]]
*Figure : le graphe $G$ des sept villes, puis un arbre couvrant minimal : Paris relié à Lille (222), Strasbourg (490), Brest (596) et Bordeaux (583) ; Bordeaux – Perpignan (451) ; Perpignan – Nice (476).*

## Trouver un arbre couvrant minimal

### Solution 1 : recherche exhaustive

1. Lister tous les arbres couvrants ;
2. calculer la valeur de chacun ;
3. en choisir un de valeur minimale.

Complexité **exponentielle** : impraticable, trop coûteuse (voir [[Recherche exhaustive]]).

### Solution 2 : algorithme glouton de Kruskal

Principe ([[Algorithme glouton]]) :
1. initialiser le graphe couvrant **sans arête** ;
2. soit $e$ l'arête **non testée de plus petit poids** : si $e$ ne forme pas de cycle, l'ajouter au graphe couvrant courant ; recommencer.

**[[Algorithme de Kruskal]]** (pseudo-code du cours) :

- *Préconditions* : $G = (V, E, \gamma, w)$ graphe valué **simple et connexe**.
- *Postconditions* : $G(F)$ est un arbre couvrant minimal de $G$.

```
E^c ← E
F ← ∅
tant que card F < card V − 1 faire
    e est choisi dans argmin{w(e), e ∈ E^c}
    E^c ← E^c \ {e}
    si G(F ∪ {e}) est acyclique alors
        F ← F ∪ {e}
    fin si
fin tant que
```

**Théorème 2.5 (terminaison et complexité).** L'algorithme de Kruskal converge vers un arbre couvrant minimum. Sa complexité est
$$O(\text{card}\,E \cdot \log(\text{card}\,V)).$$

Note de l'étudiante : l'algorithme relie tous les nœuds en minimisant la somme des poids (des arêtes, voir Points à vérifier, 2).

### Déroulé sur l'exemple des villes (complément, calcul fait ici)

Le cours donne le résultat, pas les étapes. Arêtes triées par poids croissant, arrêt à $\text{card}\,V - 1 = 6$ arêtes :

| Étape | Arête testée | Poids | Décision |
|---|---|---|---|
| 1 | Lille – Paris | 222 | ajoutée |
| 2 | Bordeaux – Perpignan | 451 | ajoutée |
| 3 | Nice – Perpignan | 476 | ajoutée |
| 4 | Strasbourg – Paris | 490 | ajoutée |
| 5 | Lille – Strasbourg | 522 | rejetée (cycle Lille – Paris – Strasbourg) |
| 6 | Paris – Bordeaux | 583 | ajoutée |
| 7 | Brest – Paris | 596 | ajoutée : 6 arêtes, arrêt |

Valeur totale : $222 + 451 + 476 + 490 + 583 + 596 = 2818$ km.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Arbre minimal des villes** : l'image donne les arêtes Paris-Lille 222, Paris-Strasbourg 490, Paris-Brest 596, Paris-Bordeaux 583, Bordeaux-Perpignan 451, Perpignan-Nice 476. En exécutant Kruskal sur les douze arêtes de la transcription, on retrouve exactement ces six arêtes, de valeur totale 2818 (complément, calcul fait ici).
2. **Note finale sur Kruskal** : « minimisant la somme des poids des noeuds » doit se lire poids des arêtes (le cours pondère les arêtes).
3. **Propositions numérotées** (« Proposition 6 », « Théorème 2.5 ») : numéros repris d'un autre document, sans effet sur le contenu.
4. **Preuve de la proposition 6** : n'établit pas que le résultat est acyclique ; il faut ajouter qu'un graphe connexe dont toutes les arêtes sont des ponts n'a pas de cycle (complément).
5. **« Une forêt n'est pas un arbre »** : la note de l'étudiante est trop forte ; une forêt connexe est un arbre. Il faut lire « une forêt n'est pas toujours un arbre ».
6. **Sous-graphe couvrant** : la remarque du cours appelle « sous-graphe » un graphe $(V, E')$ avec $E' \subseteq E$, c'est-à-dire un sous-graphe **couvrant** (mêmes sommets) ; un sous-graphe général peut aussi retirer des sommets.
