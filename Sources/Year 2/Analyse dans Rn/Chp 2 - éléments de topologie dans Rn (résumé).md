---
type: source
sources: ["[[Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-05
---

Résumé de [[Chp 2 - éléments de topologie dans Rn]], dans [[Year 2 - Analyse dans Rn]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une norme permet de mesurer des distances, donc de parler de points « proches ». Le chapitre en tire le vocabulaire utilisé ensuite pour les limites : boules, voisinages, ouverts, fermés, intérieur et adhérence.

## Contenu, dans l'ordre du cours

- **[[Norme]]** : séparation, absolue homogénéité, inégalité triangulaire. Sur $\mathbb{R}^n$ : $\|x\|_1$ (Manhattan), $\|x\|_2$ (euclidienne) et $\|x\|_\infty$. En dimension finie, toutes les normes sont équivalentes.
- **Distance** : symétrique, nulle seulement si les points sont égaux, avec l'inégalité triangulaire. Toute norme en donne une : $d(X, Y) = \|X - Y\|$.
- **[[Boule et voisinage]]** : $B(a, r)$, $\overline{B}(a, r)$ et $S(a, r)$. Dans $\mathbb{R}^2$, la boule fermée de rayon 1 est un losange pour $\|\cdot\|_1$, un disque pour $\|\cdot\|_2$ et un carré pour $\|\cdot\|_\infty$. $V$ est un voisinage de $a$ s'il contient une boule ouverte centrée en $a$. Une intersection infinie de voisinages n'en est pas forcément un. Tout EVN est séparé.
- **[[Ouvert et fermé]]** : $U$ est ouvert s'il est voisinage de chacun de ses points, $F$ est fermé si son complémentaire est ouvert. $\emptyset$ et $E$ sont les deux à la fois. Ces notions ne dépendent pas de la norme en dimension finie.
- **[[Intérieur et adhérence]]** : $\mathring{A}$ est le plus grand ouvert contenu dans $A$, $\overline{A}$ le plus petit fermé contenant $A$, et $\partial A = \overline{A} \setminus \mathring{A}$.
- **Méthodes** : montrer qu'un ensemble n'est pas ouvert ou pas fermé, et trouver $\overline{A}$ ou $\mathring{A}$ en 3 étapes à partir d'un candidat $B$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Propriété 2** : image lue directement, $\|x + y\| = \|x\| + \|y\| \iff x = \lambda y$ avec $\lambda \in \mathbb{R}$. Il faut $\lambda \ge 0$ : pour $y = -x$ non nul, on a $0 \neq 2\|x\|$ (complément). **À corriger avant un examen.**
2. **Propriété 7** : image lue directement, $r < r' \iff B(a, r) \subset B(a, r')$. Pour $r = r'$, l'inclusion est vraie alors que $r < r'$ est faux. Il faudrait $r \le r'$ (complément).
3. **Sommaire** : l'encadré d'ouverture annonce les compacts et les suites (convergence, Cauchy, Banach), que la note ne traite pas. Le plan du chapitre n'est donc couvert qu'en partie.
4. **Figure de la boule pour $\|\cdot\|_1$** : d'après sa transcription, l'étiquette du quadrant $x < 0, y > 0$ porte $y = x - 1$, alors que le texte donne $y = 1 + x$. Je n'ai pas ouvert cette image.
5. **Coquilles** : « $\mathbb{E}$ » pour $E$ dans la définition 1, et « Fr(a) » pour Fr(A) dans la définition 11.
