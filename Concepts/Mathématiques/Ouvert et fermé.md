---
type: concept
tags: [year2]
aliases: [ouvert, ouverts, fermé, fermés, open set, closed set]
matieres: [Analyse dans Rn]
sources: ["[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]", "[[Raw/Year 2/Analyse dans Rn/Chp 2 : éléments de topologie dans Rn.docx|Chp 2 - éléments de topologie dans Rn]]", "[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-08
---

- **Ouvert** : $U$ est voisinage de chacun de ses points : $\forall x \in U, \exists r > 0, B(x, r) \subset U$. Le rayon $r$ peut dépendre de $x$. Une boule ouverte est un ouvert. Toute union, et toute intersection finie, d'ouverts est un ouvert.
- **Fermé** : $F$ a pour complémentaire un ouvert. Une boule fermée est un fermé. Toute intersection, et toute union finie, de fermés est un fermé.

$\emptyset$ et $E$ sont à la fois ouverts et fermés. Dans $\mathbb{R}$, $]a, b[$ est ouvert et $[a, b]$ est fermé. En dimension finie, être un ouvert ne dépend pas de la norme.

**Méthodes** : pour montrer que $A$ n'est pas ouvert, trouver un point de sa frontière dont toute boule ouverte sort de $A$. Pour montrer que $A$ n'est pas fermé, appliquer cette méthode à son complémentaire.

## Compléments (hors du cours)

- **La restriction « finie » est nécessaire** : $\bigcap_{n \ge 1} \left]-\tfrac{1}{n}, \tfrac{1}{n}\right[ = \{0\}$ n'est pas ouvert, et $\bigcup_{n \ge 1} \left[\tfrac{1}{n}, 1\right] = \left]0, 1\right]$ n'est pas fermé.
- **Fermé n'est pas le contraire d'ouvert** : $[a, b[$ n'est ni ouvert ni fermé. Dans $\mathbb{R}^n$, $\emptyset$ et $\mathbb{R}^n$ sont les seules parties à la fois ouvertes et fermées.
- **Caractérisation séquentielle des fermés** : $F$ est fermé si et seulement si la limite de toute suite convergente d'éléments de $F$ appartient à $F$ (voir [[Caractérisation séquentielle de la limite]]).
- **Preuve qu'une boule ouverte est un ouvert** : pour $x \in B(a, r)$, on pose $\rho = r - \|x - a\| > 0$. Si $\|y - x\| < \rho$, l'[[Inégalité triangulaire]] donne $\|y - a\| \le \|y - x\| + \|x - a\| < r$, donc $B(x, \rho) \subset B(a, r)$.
- **Méthode par image réciproque** (s'appuie sur le chapitre 3) : si $g : \mathbb{R}^n \to \mathbb{R}$ est continue et $c \in \mathbb{R}$, alors $\{g < c\}$ est ouvert, et $\{g \le c\}$ et $\{g = c\}$ sont fermés. Exemple : $\{(x, y) : x^2 + y^2 < 1\}$ est ouvert, le disque fermé $\{x^2 + y^2 \le 1\}$ et le cercle $\{x^2 + y^2 = 1\}$ sont fermés.

Notion parente : [[Boule et voisinage]]. Voir aussi : [[Intérieur et adhérence]], [[Norme]], [[Partie compacte]], [[Caractérisation séquentielle de la limite]]

Résumé : [[2 - éléments de topologie dans Rn]], [[3 - Limite et continuité d’applications]]
