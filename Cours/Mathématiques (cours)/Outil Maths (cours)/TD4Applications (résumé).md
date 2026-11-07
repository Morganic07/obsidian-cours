---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Exos/TD4Applications.pdf|TD4Applications.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de l'énoncé TD4 Applications (PDF) ([[Raw/Year 1/Outil Maths/Exos/TD4Applications.pdf|TD4Applications.pdf]]) (4 pages, cycle pré-ingénieur première année, Algèbre 1, 2023/2024), dans [[Outil Maths (index)]]. **Sans corrigé** : les corrections sont dans [[TD4Applications-Solutions (résumé)]]. Cours : [[Chapitre4-Fonctions (1) (résumé)]], [[Injectivité et surjectivité]], [[Image et image réciproque]], [[Bijection]], [[Composition de fonctions]]. Les exercices marqués « à faire chez soi » sont indiqués. Le document ne contient aucune figure (seulement le logo de l'école).

## Exercice 1 — Images et images réciproques

Déterminer, si c'est possible, $f(\mathbb{R}_+)$, $f(\mathbb{R}_-)$, $f(\{-1\})$, $f^{-1}(\mathbb{R}_+)$, $f^{-1}(\mathbb{R}_-)$, $f^{-1}(\{-1\})$ pour :

a) $f(x) = e^x$ ; b) $f(x) = \ln(x)$ ; *à faire chez soi* : c) $f(x) = \cos(x)$.

## Exercice 2 — Image d'une réunion, d'une intersection

$f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$.

1. Déterminer et comparer : (a) $f([-3;-1])$ ; (b) $f([-2;1])$ ; (c) $f([-3;-1] \cup [-2;1])$ ; (d) $f([-3;-1] \cap [-2;1])$.
2. Mêmes questions pour : (a) $f^{-1}(]-\infty;2])$ ; (b) $f^{-1}([1;+\infty[)$ ; (c) $f^{-1}(]-\infty;2] \cup [1;+\infty[)$ ; (d) $f^{-1}(]-\infty;2] \cap [1;+\infty[)$.

But implicite : constater que l'image d'une intersection n'est pas toujours l'intersection des images, alors que l'image réciproque se comporte bien (voir exercice 11). Voir [[Intersection et union d'ensembles]].

## Exercice 3 — Une fonction avec un minimum

$f : \mathbb{R} \to \mathbb{R}$, $f(x) = \min(x^2, 3)$. Déterminer :

a) $f(\mathbb{R})$ ; b) $f([0,1])$ ; c) $f([1,2])$ ; d) $f([2,+\infty[)$ ; e) $f^{-1}([0;1])$ ; f) $f^{-1}([4;+\infty[)$.

## Exercice 4 — Injective ? surjective ? bijective ?

1. $n \mapsto n + 1$ de $\mathbb{N}$ dans $\mathbb{N}$.
2. $x \mapsto \dfrac{x+1}{x-1}$ de $\mathbb{R}\setminus\{1\}$ dans $\mathbb{R}$.
3. $(x;y) \mapsto (1;\ x - y;\ y)$ de $\mathbb{R}^2$ dans $\mathbb{R}^3$.
4. $(x;y;z) \mapsto (x + y + z;\ x - y - z;\ x)$ de $\mathbb{R}^3$ dans $\mathbb{R}^3$.
5. $(x;y) \mapsto (x + y;\ xy)$ de $\mathbb{R}^2$ dans $\mathbb{R}^2$.

*À faire chez soi* :

7. $n \mapsto n + 1$ de $\mathbb{Z}$ dans $\mathbb{Z}$.
8. $(x;y) \mapsto 2y$ de $\mathbb{R}^2$ dans $\mathbb{R}$.
9. $(x;y) \mapsto (x;\ xy - y^3)$ de $\mathbb{R}^2$ dans $\mathbb{R}^2$.

(La numérotation saute le 6 dans l'énoncé.)

## Exercice 5 — Étude de trois fonctions

$$f_1 : A_1 = \mathbb{R}\setminus\{0\} \to \mathbb{R},\ x \mapsto \frac1x ; \qquad f_2 : A_2 = \mathbb{R} \to \mathbb{R},\ x \mapsto \sin(x) ; \qquad f_3 : A_3 = \mathbb{R} \to \mathbb{R},\ x \mapsto x^2 + x.$$

1. (a) Tracer la courbe représentative de $f_1$ (voir [[Graphe d'une fonction]]).
   (b) $f_1$ est-elle injective, surjective, bijective ?
   (c) Si $f_1$ n'est pas bijective, trouver $E_1$ et $F_1$ tels que la [[Restriction d'une fonction|restriction]] de $f_1$ à ces ensembles soit une bijection.
   (d) Déterminer $f_1(A_1)$, $f_1(]0;2])$, $f_1^{-1}(]-1,1[)$.
2. Mêmes questions pour $f_2$.
3. Déterminer les plus grands ensembles de définition et l'expression de $f_2 \circ f_1$ et $f_1 \circ f_2$ (voir [[Ensemble de définition]]).
4. *À faire chez soi* : (a) à (d), mêmes questions pour $f_3$ (avec $E_2$, $F_2$, et les ensembles $f_3(A_2)$, $f_3(]0;2])$, $f_3^{-1}(]-1,1[)$) ; (e) plus grands ensembles de définition et expression de $f_3 \circ f_1$ et $f_1 \circ f_3$.

## Exercice 6 — Une fonction avec valeurs absolues

$f : E \to F$, $f(x) = |1 + x| + |1 - x| - 2$ (voir [[Valeur absolue]]).

1. $E = F = \mathbb{R}$.
   (a) Pour un réel $x_0$, comparer $f(x_0)$ et $f(-x_0)$. $f$ est-elle injective ? (voir [[Fonction paire et impaire]])
   (b) Donner les différentes expressions de $f$ sans valeur absolue ; représenter $f$.
   (c) Déterminer $f(\mathbb{R})$. $f$ est-elle surjective ?
2. $E = [1, +\infty[$ et $F = \mathbb{R}_+$. Donner l'expression de $f$ et, si elle existe, la réciproque $f^{-1}$ de $F$ dans $E$.

## Exercice 7 — Composées dans $\mathbb{N}$

$$f : \mathbb{N} \to \mathbb{N},\ f(n) = 2n ; \qquad g : \mathbb{N} \to \mathbb{N},\ g(n) = \begin{cases} \dfrac n2 & \text{si } n \text{ pair}\\ n & \text{si } n \text{ impair.}\end{cases}$$

1. $f$ est-elle injective, surjective, bijective ?
2. Mêmes questions pour $g$.
3. Déterminer $f \circ g$ et $g \circ f$.

## Exercice 8 — *À faire chez soi* — $\sin(\pi x)$

1. $f : \mathbb{R} \to [-1;1]$, $f(x) = \sin(\pi x)$ : injective, surjective, bijective ?
2. $g$ est la restriction de $f$ à $\left]-\frac12;\frac12\right[$. Montrer que $g$ est une bijection de $\left]-\frac12;\frac12\right[$ sur $]-1;1[$.

## Exercice 9 — Une homographie

$f : \mathbb{R}\setminus\{2\} \to \mathbb{R}\setminus\{3\}$, $f(x) = \dfrac{3x+1}{x-2}$.

1. Déterminer $f([0,2[ \cup ]2,4])$.
2. Déterminer $f^{-1}([0,3[ \cup ]3,4])$.
3. Montrer que $f$ est une bijection et déterminer sa réciproque.

## Exercice 10 — Applications dans la vie courante

Sur l'ensemble des êtres humains :
1. Associer à chaque individu « sa mère » définit-il une [[Application (mathématiques)|application]] ?
2. Si oui, est-elle injective, surjective, bijective ?
3. Mêmes questions avec « sa sœur ».

## Exercice 11 — Propriétés de l'image et de l'image réciproque

$f : E \to F$, $A, B \subset E$, $C, D \subset F$. Montrer :

(a) $f(A \cup B) = f(A) \cup f(B)$ ;
(b) $f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D)$ ;
(c) $f(A \cap f^{-1}(C)) = f(A) \cap C$.

*À faire chez soi* :
(d) $f(A \cap B) \subset f(A) \cap f(B)$ ;
(e) $f^{-1}(C \cup D) = f^{-1}(C) \cup f^{-1}(D)$.

Méthode habituelle : [[Double inclusion]].

## Exercice 12 — Caractérisations de l'injectivité et de la surjectivité

$f : E \to F$, $A, B \subset E$, $C, D \subset F$. Montrer :

1. $A \subset f^{-1}(f(A))$.
2. $f(f^{-1}(C)) = f(E) \cap C$.
3. $f$ injective $\iff \forall A \subset E,\ A = f^{-1}(f(A))$.
4. $f$ surjective $\iff \forall C \subset F,\ f(f^{-1}(C)) = C$.

## Exercice 13 — Injectivité, surjectivité et composition

$f : E \to F$ et $g : F \to G$. Montrer :

1. $g \circ f$ surjective $\Rightarrow$ $g$ surjective.
2. $g \circ f$ injective $\Rightarrow$ $f$ injective.
3. $g \circ f$ surjective et $g$ injective $\Rightarrow$ $f$ surjective.
4. $g \circ f$ injective et $f$ surjective $\Rightarrow$ $g$ injective.

## Exercice 14 — Trois applications en cycle

$f : E \to F$, $g : F \to G$, $h : G \to E$ telles que $h \circ g \circ f$ est injective, $g \circ f \circ h$ est injective et $f \circ h \circ g$ est surjective. Montrer que $f$, $g$ et $h$ sont bijectives.

## Exercice 15 — Bijection et complémentaire

$f : E \to F$. Montrer :
$$(f \text{ bijective}) \iff \left(\forall A \subset E,\ f(A^c) = f(A)^c\right).$$
Voir [[Complémentaire d'un ensemble]].

## Exercice 16 — *À faire chez soi*

$f : E \to F$, $g : F \to G$, $h : G \to H$. Montrer :
$$(g \circ f \text{ et } h \circ g \text{ bijectives}) \iff (f,\ g \text{ et } h \text{ bijectives}).$$

## Exercice 17 — *À faire chez soi* — Une surjection est simplifiable à droite

$f : E \to F$. Montrer : si $f$ est surjective, alors pour tout ensemble $G$ et toutes applications $g, h : F \to G$,
$$g \circ f = h \circ f \Rightarrow g = h.$$

## Exercice 18 — Pour aller plus loin — Fonctions indicatrices

$A, B, C$ trois parties d'un ensemble $E$ (voir [[Fonction indicatrice]], [[Différence d'ensembles]], [[Différence symétrique]]).

1. Exprimer $\mathbb{1}_{A\setminus B}$ en fonction de $\mathbb{1}_A$ et $\mathbb{1}_B$.
2. Exprimer $\mathbb{1}_{A\Delta B}$ en fonction de $\mathbb{1}_A$ et $\mathbb{1}_B$.
3. Quand a-t-on $A \Delta (B \cap C) = (A \Delta B) \cap (A \Delta C)$ ?

## Exercice 19 — Pour aller plus loin — Une application de $\mathbb{C}^*$

$f : \mathbb{C}\setminus\{0\} \to \mathbb{C}$, $z \mapsto \dfrac1z + z$ (voir [[Nombre complexe]]).

1. $f$ est-elle injective, surjective, bijective ?
2. Déterminer l'image par $f$ du cercle unité (centre $0$, rayon $1$).
3. Déterminer l'image réciproque par $f$ de $i\mathbb{R}$.

## Points à vérifier

- Exercice 4 : la numérotation passe de 5 à 7 (pas de question 6).
- Exercice 5, question 4 (d) : l'énoncé demande $f_3(A_2)$ alors que l'ensemble de départ de $f_3$ est noté $A_3$ (les deux valent $\mathbb{R}$, donc sans effet).
- Pas de correction dans ce document : voir [[TD4Applications-Solutions (résumé)]].
