---
type: matiere
tags: [year2]
sources: ["[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]", "[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]", "[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]", "[[5 - Calcul différentiel d'ordre supérieur|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
---

Analyse des fonctions de plusieurs variables : topologie, limites, calcul différentiel et équations aux dérivées partielles. Les 4 notes sont intégrées. Il n'y a pas de note pour un chapitre 1.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[2 - éléments de topologie dans Rn\|Chp 2 - éléments de topologie dans Rn]] | Normes, boules, ouverts, adhérence | [[2 - éléments de topologie dans Rn\|Résumé]] |
| [[3 - Limite et continuité d’applications\|Chp 3 - Limite et continuité d’applications]] | Limites, continuité, lipschitz | [[3 - Limite et continuité d’applications\|Résumé]] |
| [[4 - Calcul différentiel du premier ordre\|Chp 4 - Calcul différentiel du premier ordre]] | Différentielle, gradient, EDP d'ordre 1 | [[4 - Calcul différentiel du premier ordre\|Résumé]] |
| [[5 - Calcul différentiel d'ordre supérieur\|Chp 5 - Calcul différentiel d'ordre supérieur]] | Classe $\mathcal{C}^k$, Schwarz, EDP d'ordre 2 | [[5 - Calcul différentiel d'ordre supérieur\|Résumé]] |

## Concepts

- **Topologie (chp 2)** : [[Norme]], [[Distance]], [[Inégalité triangulaire]], [[Boule et voisinage]], [[Ouvert et fermé]], [[Intérieur et adhérence]], [[Espace séparé]], [[Partie compacte]], [[Suite de Cauchy]]
- **Limites (chp 3)** : [[Limite et continuité]], [[Continuité uniforme]], [[Application lipschitzienne]], [[Coordonnées polaires]]
- **Calcul différentiel (chp 4 et 5)** : [[Dérivée partielle]], [[Différentielle]], [[Fonction de classe Ck]], [[Matrice jacobienne]], [[Gradient]], [[Dérivation en chaîne]], [[Partie convexe]], [[Inégalité des accroissements finis]], [[Théorème de Schwarz]]
- **Équations** : [[Équation aux dérivées partielles]], [[Difféomorphisme]]
- **Ajoutés par l'enrichissement** : [[Dérivée directionnelle]], [[Plan tangent]], [[Matrice hessienne]], [[Théorème d'inversion locale]], [[Équation des ondes]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[3 - Limite et continuité d’applications]] : lipschitzienne $\Rightarrow$ uniformément continue, sans réciproque ($\sqrt{x}$ sur $[0, 1]$). En polaires, un résultat indépendant de $\theta$ ne suffit pas à prouver une limite : il faut une majoration indépendante de $\theta$ qui tend vers 0.
- [[2 - éléments de topologie dans Rn]] : cas d'égalité de l'inégalité triangulaire euclidienne, $y = 0$ ou $x = \lambda y$ avec $\lambda \ge 0$.
- [[4 - Calcul différentiel du premier ordre]] : les dérivées partielles d'une fonction différentiable existent mais ne sont pas forcément continues.
- [[5 - Calcul différentiel d'ordre supérieur]] : la dérivée croisée comme limite d'un taux d'accroissement de $\partial f / \partial x$ en $y$.

## Liens avec les autres matières

- **[[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]]** : la [[Norme]] euclidienne est celle qui vient du [[Produit scalaire]]. La [[Différentielle]] est une [[Transformation linéaire]], la [[Matrice jacobienne]] est sa matrice, et le jacobien est un [[Déterminant]].
- **[[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]]** : la [[Matrice jacobienne]] applique la matrice d'une application linéaire dans les bases canoniques.
- **[[Cours/Mathématiques/Analyse Maths/_index|Analyse Maths]] et [[Cours/Mathématiques/Analyse/_index|Analyse]]** : les mêmes notions en une variable. La [[Différentielle]] généralise la [[Dérivabilité]], et le [[Gradient]] donne la version à plusieurs variables des accroissements finis.
- **[[Cours/Mathématiques/Analyse/_index|Analyse]]** : les [[Coordonnées polaires]] et la [[Matrice jacobienne]] servent au changement de variables des intégrales multiples (chp 9).
- **[[Cours/Informatique/Data mining/_index|Data mining]]** : la [[Distance]] y mesure la similarité entre individus.
