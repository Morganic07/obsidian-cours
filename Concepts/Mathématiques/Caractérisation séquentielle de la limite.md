---
type: concept
tags: [year1, year2]
aliases: [caractérisation séquentielle, caractérisation séquentielle de la continuité, sequential characterization of limits]
matieres: [Analyse Maths, Analyse dans Rn]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]", "[[Raw/Year 2/Analyse dans Rn/Chp 2 : éléments de topologie dans Rn.docx|Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-08
---

$f(x) \to \ell$ quand $x \to a$ si et seulement si $f(u_n) \to \ell$ pour toute suite $(u_n)$ d'éléments de $I$ qui tend vers $a$ (théorème 6 du chapitre 3, pour $f : I \to \mathbb{R}$, $\ell \in \overline{\mathbb{R}}$ et $a \in \overline{I}$).

Pour réfuter une limite, on exhibe deux suites de même limite $a$ dont les images ont des limites différentes. Le cours s'en sert pour démontrer les opérations sur les limites de fonctions, et l'énonce aussi pour la continuité.

## Dans un espace vectoriel normé

Le chapitre 3 d'Analyse dans Rn s'en sert dans sa méthode sans l'énoncer. *Énoncé (complément, hors du cours)* : pour $f : A \subset E \to F$ et $a \in \overline{A}$ (voir [[Intérieur et adhérence]]),

$$\lim_{x \to a} f(x) = \ell \iff \text{pour toute suite } (x_n) \text{ de } A \text{ telle que } x_n \to a, \ f(x_n) \to \ell.$$

**Usage** : deux suites $u_n, v_n \to (0, 0)$ dont les images ont des limites différentes prouvent qu'il n'y a pas de limite. Exemple : $f(x, y) = \dfrac{xy}{x^2 + y^2}$, avec $u_n = (1/n, 1/n)$ on a $f(u_n) = 1/2$, avec $v_n = (0, 1/n)$ on a $f(v_n) = 0$ ; $f$ n'a donc pas de limite en $(0, 0)$. Pour prouver qu'une limite existe, il faudrait traiter toutes les suites : on passe plutôt par une majoration $|f(x) - \ell| \le g(\|x - a\|)$ avec $g(t) \to 0$.

**Versions voisines** (chapitre 2) :

- $x \in \overline{A}$ si et seulement si $x$ est limite d'une suite d'éléments de $A$ ;
- $F$ est fermé si et seulement s'il contient la limite de toute suite convergente d'éléments de $F$ (voir [[Ouvert et fermé]]).

Notion parente : [[Limite et continuité]]. Voir aussi : [[Suite extraite]], [[Intérieur et adhérence]], [[Ouvert et fermé]].

Résumés : [[0 - rappels pdf]], [[3 - Limite et continuité d’applications]], [[2 - éléments de topologie dans Rn]]
