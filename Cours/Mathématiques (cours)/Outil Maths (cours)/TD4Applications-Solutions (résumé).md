---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du TD4 Applications, corrigé (PDF) ([[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]) (94 diapositives, algèbre, premier semestre 2023), dans [[Outil Maths (index)]]. C'est le corrigé de [[TD4Applications (résumé)]] (les énoncés y sont listés). Cours : [[Chapitre4-Fonctions (1) (résumé)]], [[Injectivité et surjectivité]], [[Opérations sur les ensembles]]. Texte extrait en entier ; chaque exercice est repris avec son énoncé et les étapes de la correction.

Notions mobilisées : [[Application (mathématiques)]], [[Image et image réciproque]], [[Bijection]], [[Composition de fonctions]], [[Ensemble de définition]], [[Intersection et union d'ensembles]], [[Complémentaire d'un ensemble]], [[Fonction indicatrice]], [[Différence symétrique]], [[Quantificateur]].

Les diapositives marquées « À faire chez soi » ou « Pour aller plus loin » sont signalées ; elles sont corrigées comme les autres.

## Exercice 1 : images et images réciproques

**Énoncé.** Déterminer $f(\mathbb{R}_+)$, $f(\mathbb{R}_-)$, $f(\{-1\})$, $f^{-1}(\mathbb{R}_+)$, $f^{-1}(\mathbb{R}_-)$, $f^{-1}(\{-1\})$ pour (1) $f(x) = e^x$, (2) $f(x) = \ln x$, (3) $f(x) = \cos x$ (à faire chez soi).

**Méthode** : rappeler ensemble de départ, image et monotonie, tracer le graphe, puis lire.

### (1) $f(x) = e^x$

Départ $\mathbb{R}$, image $\mathbb{R}_+^*$, strictement croissante.

![[TD4Applications-Solutions - p3.jpg]]

*Figure : graphe de $x \mapsto e^x$.*

$$f(\mathbb{R}_+) = [1, +\infty[,\quad f(\mathbb{R}_-) = ]0, 1],\quad f(\{-1\}) = \{e^{-1}\}$$
$$f^{-1}(\mathbb{R}_+) = \mathbb{R},\quad f^{-1}(\mathbb{R}_-) = \emptyset,\quad f^{-1}(\{-1\}) = \emptyset$$

### (2) $f(x) = \ln x$

Départ $\mathbb{R}_+^*$, image $\mathbb{R}$, strictement croissante.

![[TD4Applications-Solutions - p5.jpg]]

*Figure : graphe de $x \mapsto \ln x$.*

$$f(\mathbb{R}_+) = \mathbb{R},\quad f(\mathbb{R}_-) = \emptyset,\quad f(\{-1\}) = \emptyset$$
$$f^{-1}(\mathbb{R}_+) = [1, +\infty[,\quad f^{-1}(\mathbb{R}_-) = ]0, 1]$$

Comme $\ln(e^{-1}) = -1$ et $\ln$ est strictement croissante : $f^{-1}(\{-1\}) = \{e^{-1}\}$.

### (3) $f(x) = \cos x$ (à faire chez soi)

Départ $\mathbb{R}$, image $[-1, 1]$, périodique de période $2\pi$.

![[TD4Applications-Solutions - p7.jpg]]

*Figure : graphe de $x \mapsto \cos x$.*

$$f(\mathbb{R}_+) = [-1, 1],\quad f(\mathbb{R}_-) = [-1, 1],\quad f(\{-1\}) = \{\cos(-1)\}$$
$$f^{-1}(\mathbb{R}_+) = \left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right] + 2k\pi,\quad f^{-1}(\mathbb{R}_-) = \left[\tfrac{\pi}{2}, \tfrac{3\pi}{2}\right] + 2k\pi,\quad f^{-1}(\{-1\}) = \{\pi + 2k\pi\}$$

## Exercice 2 : $f(x) = x^2$, images et unions

**Énoncé.** $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$.

1. Déterminer $f([-3,-1])$, $f([-2,1])$, $f([-3,-1] \cup [-2,1])$, $f([-3,-1] \cap [-2,1])$ et les comparer.
2. Mêmes questions pour $f^{-1}(]-\infty, 2])$, $f^{-1}([1, +\infty[)$, $f^{-1}(]-\infty,2] \cup [1,+\infty[)$, $f^{-1}(]-\infty,2] \cap [1,+\infty[)$.

Départ $\mathbb{R}$, image $\mathbb{R}_+$, fonction paire.

![[TD4Applications-Solutions - p10.jpg]]

*Figure : la parabole $y = x^2$.*

**Question 1.**

- $f([-3,-1]) = [1, 9]$ ; $f([-2,1]) = [0, 4]$.
- $f([-3,-1] \cup [-2,1]) = f([-3,1]) = [0, 9] = [1,9] \cup [0,4] = f([-3,-1]) \cup f([-2,1])$.
- $f([-3,-1] \cap [-2,1]) = f([-2,-1]) = [1, 4] = [1,9] \cap [0,4] = f([-3,-1]) \cap f([-2,1])$.

L'égalité avec l'intersection est ici un cas particulier : en général on n'a que l'inclusion $f(A \cap B) \subset f(A) \cap f(B)$ (exercice 11).

**Question 2.**

- $f^{-1}(]-\infty, 2]) = f^{-1}([0, 2]) = [-\sqrt2, \sqrt2]$ ; $f^{-1}([1, +\infty[) = ]-\infty, -1] \cup [1, +\infty[$.
- $f^{-1}(]-\infty,2] \cup [1,+\infty[) = f^{-1}(\mathbb{R}) = \mathbb{R} = [-\sqrt2, \sqrt2] \cup (]-\infty,-1] \cup [1,+\infty[)$.
- $f^{-1}(]-\infty,2] \cap [1,+\infty[) = f^{-1}([1,2]) = [-\sqrt2, -1] \cup [1, \sqrt2] = [-\sqrt2,\sqrt2] \cap (]-\infty,-1] \cup [1,+\infty[)$.

Les images réciproques commutent avec l'union et l'intersection.

## Exercice 3 : $f(x) = \min\{x^2, 3\}$

**Énoncé.** Déterminer $f(\mathbb{R})$, $f([0,1])$, $f([1,2])$, $f([2,+\infty[)$, $f^{-1}([0,1])$, $f^{-1}([4,+\infty[)$.

On écrit d'abord
$$\min\{x^2, 3\} = \begin{cases} x^2 & \text{si } -\sqrt3 \le x \le \sqrt3 \\ 3 & \text{si } x > \sqrt3 \text{ ou } x < -\sqrt3. \end{cases}$$

![[TD4Applications-Solutions - p14.jpg]]

*Figure : graphe de $\min\{x^2, 3\}$, parabole tronquée par le palier $y = 3$.*

$$f(\mathbb{R}) = [0, 3],\quad f([0,1]) = [0,1],\quad f([1,2]) = [1,3],\quad f([2,+\infty[) = \{3\}$$
$$f^{-1}([0,1]) = [-1, 1],\quad f^{-1}([4, +\infty[) = \emptyset$$

## Exercice 4 : injective ? surjective ? bijective ?

**Méthode** : injective, partir de $f(x) = f(x')$ et montrer $x = x'$ ; non injective, exhiber deux antécédents distincts ; non surjective, exhiber un élément sans antécédent ; surjective, construire un antécédent.

| # | Application | Injective | Surjective | Argument du corrigé |
|---|---|---|---|---|
| 1 | $n \mapsto n+1$, $\mathbb{N} \to \mathbb{N}$ | oui | non | $n+1 = n'+1 \Rightarrow n = n'$ ; 0 n'a pas d'antécédent ($n = -1 \notin \mathbb{N}$) |
| 2 | $x \mapsto \frac{x+1}{x-1}$, $\mathbb{R}\setminus\{1\} \to \mathbb{R}$ | oui | non | produit en croix : $xx' - x + x' = xx' + x - x'$, d'où $x = x'$ ; $f(x) = 1 \Rightarrow x + 1 = x - 1 \Rightarrow 0 = 2$ |
| 3 | $(x,y) \mapsto (1, x-y, y)$, $\mathbb{R}^2 \to \mathbb{R}^3$ | oui | non | $y = y'$ puis $x = x'$ ; tout $(a,b,c)$ avec $a \neq 1$ est sans antécédent |
| 4 | $(x,y,z) \mapsto (x+y+z, x-y-z, x)$, $\mathbb{R}^3 \to \mathbb{R}^3$ | non | non | $(0, y, -y)$ a toujours l'image $(0,0,0)$ ; le système donne $y + z = a - c$ et $y + z = -(b - c)$, incompatible si $a - c \neq -(b-c)$ ; ex. $(0,1,1)$ : $x = 1$ puis $0 = y+z = -1$, absurde |
| 5 | $(x,y) \mapsto (x+y, xy)$, $\mathbb{R}^2 \to \mathbb{R}^2$ | non | non | $(a,b)$ et $(b,a)$ ont la même image ; $(a,b)$ a un antécédent ssi $x^2 - ax + b = 0$ a une racine réelle ; $(0,1)$ n'en a pas |
| 6 | $n \mapsto n+1$, $\mathbb{Z} \to \mathbb{Z}$ | oui | oui | $f(n-1) = n$ : $n - 1$ est l'unique antécédent, donc bijective |
| 7 | $(x,y) \mapsto 2y$, $\mathbb{R}^2 \to \mathbb{R}$ | non | oui | $f(1,2) = f(3,2) = 4$ ; $f(x, y/2) = y$ pour tout $x$ |
| 8 | $(x,y) \mapsto (x, xy - y^3)$, $\mathbb{R}^2 \to \mathbb{R}^2$ | — | — | « À vous de vérifier » : pas de correction |

## Exercice 5 : $1/x$, $\sin$, $x^2 + x$ et composées

Pour chaque fonction : (a) tracer la courbe ; (b) dire si elle est injective, surjective, bijective ; (c) sinon, trouver $E_i$, $F_i$ tels que $f_i$ soit une bijection de $E_i$ sur $F_i$ ; (d) déterminer $f_i(A_i)$, $f_i(]0,2])$, $f_i^{-1}(]-1,1[)$.

### $f_1 : \mathbb{R}\setminus\{0\} \to \mathbb{R}$, $x \mapsto 1/x$

![[TD4Applications-Solutions - p26.jpg]]

*Figure : l'hyperbole $y = 1/x$.*

- (b) Injective : $1/x = 1/y \Rightarrow x = y$. Non surjective : 0 n'a pas d'antécédent.
- (c) L'image est $\mathbb{R}\setminus\{0\}$ : $E_1 = F_1 = \mathbb{R}\setminus\{0\}$.
- (d) $f_1(A_1) = \mathbb{R}\setminus\{0\}$ ; $f_1(]0,2]) = [\tfrac12, +\infty[$ ; $f_1^{-1}(]-1,1[) = ]-\infty,-1[ \cup ]1,+\infty[$.

### $f_2 : \mathbb{R} \to \mathbb{R}$, $x \mapsto \sin x$

![[TD4Applications-Solutions - p29.jpg]]

*Figure : la sinusoïde $y = \sin x$.*

- (b) Non injective (périodique de période $2\pi$). Non surjective : tout réel hors de $[-1,1]$ est sans antécédent.
- (c) Par exemple $E_2 = [-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$, $F_2 = [-1, 1]$.
- (d) $f_2(A_2) = [-1,1]$ ; $f_2(]0,2]) = ]0,1]$ ; le corrigé donne $f_2^{-1}(]-1,1[) = ]-\tfrac{\pi}{2}, \tfrac{\pi}{2}[ + k\pi$ (voir le point à vérifier).

### Composées $f_2 \circ f_1$ et $f_1 \circ f_2$

- $(f_2 \circ f_1)(x) = \sin(1/x)$, définie sur $\mathbb{R}\setminus\{0\}$.
- $(f_1 \circ f_2)(x) = \dfrac{1}{\sin x}$ ; $\sin x = 0 \iff x = k\pi$, donc définie sur $\mathbb{R} \setminus \{k\pi, k \in \mathbb{Z}\}$.

### $f_3 : \mathbb{R} \to \mathbb{R}$, $x \mapsto x^2 + x$ (à faire chez soi)

![[TD4Applications-Solutions - p33.jpg]]

*Figure : la parabole $y = x^2 + x$.*

- (b) Non injective : $f_3(0) = 0 = f_3(-1)$. Non surjective : l'axe de symétrie de $ax^2 + bx + c$ est $x = -\frac{b}{2a}$, ici $x = -\tfrac12$, donc $f_3(x) \ge f_3(-\tfrac12) = -\tfrac14$ ; tout réel $< -\tfrac14$ est sans antécédent, et $\mathrm{Im}(f_3) = [-\tfrac14, +\infty[$.
- (c) $E_3 = [-\tfrac12, +\infty[$, $F_3 = [-\tfrac14, +\infty[$.
- (d) $f_3(\mathbb{R}) = [-\tfrac14, +\infty[$ ; $f_3(]0,2]) = ]0, 6]$ ; $x \in f_3^{-1}(]-1,1[) \iff -1 < x^2 + x < 1$, d'où
$$f_3^{-1}(]-1,1[) = \left]\frac{-1-\sqrt5}{2}, \frac{-1+\sqrt5}{2}\right[.$$

## Exercice 6 : $f(x) = |1+x| + |1-x| - 2$

**Énoncé.** (1) $E = F = \mathbb{R}$ : comparer $f(x_0)$ et $f(-x_0)$, $f$ est-elle injective ? Donner les expressions de $f$ sans valeurs absolues, tracer le graphe. Déterminer $f(\mathbb{R})$, $f$ est-elle surjective ? (2) $E = [1,+\infty[$, $F = \mathbb{R}_+$ : expression de $f$ et réciproque si elle existe.

1. $f(-x_0) = |1 - x_0| + |1 + x_0| - 2 = f(x_0)$ : $f$ est **paire**, donc **non injective**.
2. Sur $[0, +\infty[$ : $f(x) = 0$ si $0 \le x \le 1$, $f(x) = 2x - 2$ si $x \ge 1$. Par parité :
$$f(x) = \begin{cases} -2x - 2 & \text{si } x \le -1 \\ 0 & \text{si } -1 \le x \le 1 \\ 2x - 2 & \text{si } x \ge 1 \end{cases}$$

![[TD4Applications-Solutions - p39.jpg]]

*Figure : graphe en « cuvette » de $f$, nul sur $[-1, 1]$, affine de pente $\pm 2$ ailleurs.*

3. D'après le graphe, $f(\mathbb{R}) = \mathbb{R}_+$ : **non surjective** sur $\mathbb{R}$.
4. Sur $[1, +\infty[$, $f(x) = 2x - 2$ ; pour $y \in \mathbb{R}_+$, $y = 2x - 2 \iff x = \frac{y+2}{2}$, antécédent unique. $f$ est bijective, de réciproque $g : \mathbb{R}_+ \to [1, +\infty[$, $y \mapsto \frac{y+2}{2}$.

## Exercice 7 : inverse à gauche sans bijection

**Énoncé.** $f : \mathbb{N} \to \mathbb{N}$, $f(n) = 2n$ ; $g : \mathbb{N} \to \mathbb{N}$, $g(n) = n/2$ si $n$ pair, $g(n) = n$ si $n$ impair. Étudier $f$, $g$, puis $f \circ g$ et $g \circ f$.

- $f$ : injective ($2n = 2n' \Rightarrow n = n'$) ; non surjective (aucun impair n'a d'antécédent) ; donc non bijective.
- $g$ : non injective, car $g(2n+1) = 2n+1 = \frac{2(2n+1)}{2} = g(4n+2)$ ; surjective, car $n = g(2n)$ ; donc non bijective.
- $(f \circ g)(n) = 2g(n) = n$ si $n$ pair, $2n$ si $n$ impair ; $(g \circ f)(n) = g(2n) = n$.

Donc $g \circ f = \mathrm{id}_\mathbb{N}$ alors que $f \circ g \neq \mathrm{id}_\mathbb{N}$ : exemple type d'inverse à gauche sans bijection.

## Exercice 8 : $\sin(\pi x)$ (à faire chez soi)

**Énoncé.** (1) $f : \mathbb{R} \to [-1,1]$, $f(x) = \sin(\pi x)$ : injective, surjective, bijective ? (2) $g$ restriction de $f$ à $]-\tfrac12, \tfrac12[$ : montrer que $g$ est une bijection de $]-\tfrac12,\tfrac12[$ sur $]-1,1[$.

1. Non injective : $f(0) = 0 = \sin \pi = f(1)$. Surjective : tout $y \in [-1,1]$ s'écrit $y = \sin x = f(x/\pi)$. Donc non bijective.
2. $g$ est la composée de $x \mapsto \pi x$, bijective de $]-\tfrac12, \tfrac12[$ sur $]-\tfrac{\pi}{2}, \tfrac{\pi}{2}[$, et de $\sin$, bijective de $]-\tfrac{\pi}{2}, \tfrac{\pi}{2}[$ sur $]-1, 1[$. Résultat du cours : si $h : E \to F$ et $f : F \to G$ sont bijectives, alors $f \circ h$ est bijective. Donc $g$ est bijective.

## Exercice 9 : homographie $\frac{3x+1}{x-2}$ (à faire chez soi)

**Énoncé.** $f : \mathbb{R}\setminus\{2\} \to \mathbb{R}\setminus\{3\}$, $f(x) = \frac{3x+1}{x-2}$. (1) $f([0,2[ \cup ]2,4])$. (2) $f^{-1}([0,3[ \cup ]3,4])$. (3) Montrer que $f$ est une bijection, déterminer sa réciproque.

**Étude préalable.** $\dfrac{3x+1}{x-2} = 3 + \dfrac{7}{x-2}$. Pour $x < y$ : $x - 2 < y - 2 \Rightarrow \frac{7}{y-2} < \frac{7}{x-2} \Rightarrow f(y) < f(x)$ : le corrigé conclut que $f$ est décroissante. Limites : $f \to 3$ en $\pm\infty$ ; $f(x) = 0 \iff x = -\tfrac13$ ; $f \to -\infty$ en $2^-$ et $+\infty$ en $2^+$.

![[TD4Applications-Solutions - p48.jpg]]

*Figure : l'hyperbole $y = \frac{3x+1}{x-2}$, asymptotes $x = 2$ et $y = 3$.*

1. $f([0,2[ \cup ]2,4]) = f([0,2[) \cup f(]2,4])$ ; le corrigé écrit $\left]-\infty, -\tfrac12\right[ \cup \left]\tfrac{13}{2}, +\infty\right[$ (bornes à corriger, voir les points à vérifier).
2. $x \in f^{-1}([0,3[) \iff 0 \le 3 + \frac{7}{x-2} < 3 \iff x \in \left]-\infty, -\tfrac13\right]$ ; $x \in f^{-1}(]3,4]) \iff x \in [9, +\infty[$. D'où $f^{-1}([0,3[ \cup ]3,4]) = \left]-\infty, -\tfrac13\right] \cup [9, +\infty[$.
3. Pour $y \in \mathbb{R}\setminus\{3\}$ : $y = \frac{3x+1}{x-2} \iff xy - 2y = 3x + 1 \iff x(y - 3) = 2y + 1 \iff x = \frac{2y+1}{y-3}$. Antécédent unique, donc $f$ bijective, de réciproque
$$g : \mathbb{R}\setminus\{3\} \to \mathbb{R}\setminus\{2\},\quad y \mapsto \frac{2y+1}{y-3}.$$

## Exercice 10 : « sa mère », « sa sœur » (à faire chez soi)

**Énoncé.** Sur l'ensemble des êtres humains, « à chaque individu sa mère » définit-il une application ? Si oui, injective, surjective, bijective ? Mêmes questions avec « sa sœur ».

1. Chaque individu a exactement une mère (biologique), même si elle n'est plus vivante : c'est une **application**.
2. Non injective (deux individus peuvent avoir la même mère) ; non surjective (tout individu, notamment les hommes, n'est pas la mère de quelqu'un).
3. Un individu peut n'avoir aucune sœur, ou plusieurs : « sa sœur » **n'est pas une application**.

## Exercice 11 : images, images réciproques et opérations

**Énoncé.** $f : E \to F$, $A, B \subset E$, $C, D \subset F$. Montrer :

- (a) $f(A \cup B) = f(A) \cup f(B)$ ;
- (b) $f(A \cap B) \subset f(A) \cap f(B)$ (à faire chez soi) ;
- (c) $f^{-1}(C \cup D) = f^{-1}(C) \cup f^{-1}(D)$ (à faire chez soi) ;
- (d) $f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D)$ ;
- (e) $f(A \cap f^{-1}(C)) = f(A) \cap C$.

**Méthode générale : double inclusion**, en partant d'un élément.

- **(a)** $\subset$ : soit $y \in f(A \cup B)$, il existe $x \in A \cup B$ avec $y = f(x)$ ; si $x \in A$, $y \in f(A)$ ; si $x \in B$, $y \in f(B)$ ; dans les deux cas $y \in f(A) \cup f(B)$. $\supset$ : si $y \in f(A)$, $y = f(x)$ avec $x \in A \subset A \cup B$, donc $y \in f(A \cup B)$ ; idem pour $B$.
- **(b)** Soit $y = f(x)$ avec $x \in A \cap B$ : $x \in A \Rightarrow y \in f(A)$ et $x \in B \Rightarrow y \in f(B)$.
- **(c)** $\subset$ : $x \in f^{-1}(C \cup D) \Rightarrow f(x) \in C$ ou $f(x) \in D$, donc $x \in f^{-1}(C)$ ou $x \in f^{-1}(D)$. $\supset$ : si $f(x) \in C \subset C \cup D$, alors $x \in f^{-1}(C \cup D)$ ; idem pour $D$.
- **(d)** $\subset$ : $f(x) \in C \cap D \subset C$ et $\subset D$. $\supset$ : $f(x) \in C$ et $f(x) \in D$ donne $f(x) \in C \cap D$.
- **(e)** $\subset$ : $y = f(x)$ avec $x \in A$ (donc $y \in f(A)$) et $x \in f^{-1}(C)$ (donc $y \in C$). $\supset$ : $y \in f(A) \cap C$, il existe $x \in A$ avec $f(x) = y \in C$, donc $x \in A \cap f^{-1}(C)$ et $y \in f(A \cap f^{-1}(C))$.

## Exercice 12 : caractérisations de l'injectivité et de la surjectivité

**Énoncé.** Montrer :

- (a) $A \subset f^{-1}(f(A))$ ;
- (b) $f(f^{-1}(C)) = f(E) \cap C$ ;
- (c) $f$ injective $\iff \forall A \subset E,\ A = f^{-1}(f(A))$ ;
- (d) $f$ surjective $\iff \forall C \subset F,\ f(f^{-1}(C)) = C$.

- **(a)** $x \in A \Rightarrow f(x) \in f(A) \Rightarrow x \in f^{-1}(f(A))$.
- **(b)** $\subset$ : $y = f(x)$ avec $x \in f^{-1}(C)$ donne $y \in C$, et $x \in E$ donne $y \in f(E)$. $\supset$ : $y \in f(E)$ s'écrit $y = f(x)$, et $y \in C$ donne $x \in f^{-1}(C)$, donc $y \in f(f^{-1}(C))$.
- **(c)** $\Rightarrow$ : il suffit de montrer $f^{-1}(f(A)) \subset A$ ; si $f(x) \in f(A)$, il existe $y \in A$ avec $f(x) = f(y)$, et l'injectivité donne $x = y \in A$. $\Leftarrow$ : si $f(x) = f(y)$, poser $A = \{x\}$ : $f^{-1}(\{f(x)\}) = \{x\}$ contient $y$, donc $x = y$.
- **(d)** $\Rightarrow$ : on a déjà $f(f^{-1}(C)) = f(E) \cap C \subset C$ ; pour $x \in C$, la surjectivité donne $a$ avec $x = f(a)$, d'où $a \in f^{-1}(C)$ et $x \in f(f^{-1}(C))$. $\Leftarrow$ : pour $y \in F$, poser $C = \{y\}$ : $f(f^{-1}(\{y\})) = \{y\} \neq \emptyset$, donc $f^{-1}(\{y\}) \neq \emptyset$ : $y$ a un antécédent.

## Exercice 13 : injectivité, surjectivité et composition

**Énoncé.** $f : E \to F$, $g : F \to G$. Montrer :

1. $g \circ f$ surjective $\Rightarrow$ $g$ surjective ;
2. $g \circ f$ injective $\Rightarrow$ $f$ injective ;
3. $g \circ f$ surjective et $g$ injective $\Rightarrow$ $f$ surjective ;
4. $g \circ f$ injective et $f$ surjective $\Rightarrow$ $g$ injective.

**Corrections.**

1. Soit $y \in G$ ; il existe $t \in E$ avec $y = g(f(t))$ ; poser $x = f(t)$ : $y = g(x)$.
2. $f(x) = f(y) \Rightarrow g(f(x)) = g(f(y)) \Rightarrow x = y$ (injectivité de $g \circ f$).
3. Soit $y \in F$ ; $g(y) \in G$, donc il existe $x \in E$ avec $g(y) = g(f(x))$ ; $g$ injective donne $y = f(x)$.
4. Soient $x, y \in F$ avec $g(x) = g(y)$ ; $f$ surjective donne $a, b$ avec $f(a) = x$, $f(b) = y$ ; $g(f(a)) = g(f(b))$ donne $a = b$, donc $x = f(a) = f(b) = y$.

**Méthode** : nommer l'élément cherché et le construire avec $f(t)$ ou $g(y)$.

## Exercice 14 : trois applications en boucle

**Énoncé.** $f : E \to F$, $g : F \to G$, $h : G \to E$ telles que $h \circ g \circ f$ injective, $g \circ f \circ h$ injective et $f \circ h \circ g$ surjective. Montrer que $f$, $g$, $h$ sont bijectives.

Avec l'exercice 13 (le corrigé le cite comme « question 4.10 ») :

- $(h \circ g) \circ f$ injective $\Rightarrow$ $f$ injective ; $f \circ (h \circ g)$ surjective $\Rightarrow$ $f$ surjective. Donc **$f$ bijective**.
- $(g \circ f) \circ h$ injective $\Rightarrow$ $h$ injective ; $(f \circ h) \circ g$ surjective $\Rightarrow$ $f \circ h$ surjective ; avec $f$ injective, le point (3) donne $h$ surjective. Donc **$h$ bijective**.
- $f$ et $h$ injectives $\Rightarrow$ $f \circ h$ injective (cours) ; $f \circ h$ est donc bijective. Point (3) : $(f \circ h) \circ g$ surjective et $f \circ h$ injective $\Rightarrow$ $g$ surjective. Point (4) : $g \circ (f \circ h)$ injective et $f \circ h$ surjective $\Rightarrow$ $g$ injective. Donc **$g$ bijective**.

## Exercice 15 : bijection et complémentaire

**Énoncé.** Montrer : $f$ bijective $\iff \forall A \subset E,\ f(A^c) = f(A)^c$.

- **$\Rightarrow$**, par double inclusion. $\subset$ : soit $y = f(x)$ avec $x \in A^c$ ; si $y \in f(A)$, $y = f(x')$ avec $x' \in A$, et l'injectivité donne $x = x'$, absurde ; donc $y \in f(A)^c$. $\supset$ : soit $y \in f(A)^c$ ; la surjectivité donne $x$ avec $y = f(x)$ ; si $x \in A$, $y \in f(A)$, absurde ; donc $x \in A^c$ et $y \in f(A^c)$.
- **$\Leftarrow$**. Injectivité : si $x \neq y$, alors $y \in \{x\}^c$, donc $f(y) \in f(\{x\}^c) = \{f(x)\}^c$, soit $f(y) \neq f(x)$. Surjectivité : avec $A = E$, $f(E) = ((f(E))^c)^c = (f(E^c))^c = (f(\emptyset))^c = \emptyset^c = F$.

## Exercice 16 : composées bijectives (à faire chez soi)

**Énoncé.** $f : E \to F$, $g : F \to G$, $h : G \to H$. Montrer : $g \circ f$ et $h \circ g$ bijectives $\iff$ $f$, $g$, $h$ bijectives.

- **$\Leftarrow$** : la composée de deux bijections est une bijection (cours).
- **$\Rightarrow$** (exercice 13) :
  - $h \circ g$ injective $\Rightarrow$ $g$ injective ; $g \circ f$ surjective $\Rightarrow$ $g$ surjective : **$g$ bijective** ;
  - $g \circ f$ injective $\Rightarrow$ $f$ injective ; $g \circ f$ surjective et $g$ injective $\Rightarrow$ $f$ surjective (point 3) : **$f$ bijective** ;
  - $h \circ g$ surjective $\Rightarrow$ $h$ surjective ; $h \circ g$ injective et $g$ surjective $\Rightarrow$ $h$ injective (point 4) : **$h$ bijective**.

## Exercice 17 : une surjection est simplifiable à droite (à faire chez soi)

**Énoncé.** $f : E \to F$ surjective $\Rightarrow$ pour tout ensemble $G$ et toutes $g, h : F \to G$, $g \circ f = h \circ f \Rightarrow g = h$.

Soit $x \in F$ ; $f$ surjective donne $y \in E$ avec $x = f(y)$ ; $(g \circ f)(y) = (h \circ f)(y)$ donne $g(x) = h(x)$. Donc $g = h$.

## Exercice supplémentaire : quantificateurs (à faire chez soi)

**Énoncé.** $f : E \to F$, avec $E$ et $F$ de [[Cardinal d'un ensemble|cardinal]] strictement supérieur à 1. Discuter :

| # | Proposition | Valeur selon le corrigé |
|---|---|---|
| 1 | $\forall x \in E, \forall y \in F, f(x) = y$ | Faux : il suffit que $F$ ait plus d'un élément |
| 2 | $\forall x \in E, \exists y \in F, f(x) = y$ | Vrai : définition d'une application |
| 3 | $\exists x \in E, \forall y \in F, f(x) = y$ | Faux : il suffit que $F$ ait plus d'un élément |
| 4 | $\exists x \in E, \exists y \in F, f(x) = y$ | Vrai : définition d'une application |
| 5 | $\forall y \in F, \forall x \in E, f(x) = y$ | Faux : équivalente à la 1 |
| 6 | $\forall y \in F, \exists x \in E, f(x) = y$ | Vrai uniquement si $f$ est surjective |
| 7 | $\exists y \in F, \forall x \in E, f(x) = y$ | Vrai uniquement si $f$ est constante |
| 8 | $\exists y \in F, \exists x \in E, f(x) = y$ | Vrai : équivalente à la 4 |

L'ordre $\forall\exists$ ou $\exists\forall$ change tout.

## Exercice 18 : fonctions indicatrices (pour aller plus loin)

**Énoncé.** $A, B, C \subset E$. (1) $1_{A \setminus B}$ en fonction de $1_A$, $1_B$. (2) $1_{A \Delta B}$ en fonction de $1_A$, $1_B$. (3) Quand a-t-on $A \Delta (B \cap C) = (A \Delta B) \cap (A \Delta C)$ ?

**Rappel** : $1_A : E \to \{0,1\}$, $1_A(x) = 1$ si $x \in A$, $0$ sinon. Propriétés :

1. $1_A = 1_B \iff A = B$, et $1_A^2 = 1_A$ ;
2. $1_{A \cap B} = 1_A \cdot 1_B$ ;
3. $1_{A \cup B} = 1_A + 1_B - 1_{A \cap B}$ ;
4. $1_{A^c} = 1 - 1_A$ ($1$ : fonction constante égale à 1).

**(1)** $A \setminus B = A \cap B^c$, donc $1_{A\setminus B} = 1_A \cdot 1_{B^c} = 1_A(1 - 1_B) = 1_A - 1_A 1_B = 1_A - 1_{A \cap B}$.

**(2)** $A \Delta B = (A \cup B) \setminus (A \cap B)$, donc, avec (1) et $A \cap B \subset A \cup B$ :
$$1_{A\Delta B} = 1_{A\cup B} - 1_{A\cap B} = 1_A + 1_B - 2 \cdot 1_A 1_B.$$

**(3)** D'une part $1_{A\Delta(B\cap C)} = 1_A + 1_B 1_C - 2\, 1_A 1_B 1_C$. D'autre part, en développant avec $1_A^2 = 1_A$ :
$$1_{(A\Delta B)\cap(A\Delta C)} = (1_A + 1_B - 2\,1_A1_B)(1_A + 1_C - 2\,1_A1_C) = 1_A - 1_A1_C - 1_A1_B + 1_B1_C.$$
L'égalité équivaut à $0 = 1_A1_B + 1_A1_C - 2\,1_A1_B1_C = 1_A(1_B + 1_C - 2\,1_B1_C) = 1_A \cdot 1_{B\Delta C} = 1_{A\cap(B\Delta C)}$.

**Conclusion** : $A \Delta (B \cap C) = (A \Delta B) \cap (A \Delta C) \iff A \cap (B \Delta C) = \emptyset \iff B \Delta C \subset A^c$.

## Exercice 19 : $z \mapsto z + 1/z$ sur $\mathbb{C}^*$ (pour aller plus loin)

**Énoncé.** $f : \mathbb{C}\setminus\{0\} \to \mathbb{C}$, $f(z) = \frac1z + z$. (1) Injective, surjective, bijective ? (2) Image du cercle unité. (3) Image réciproque de $i\mathbb{R}$.

1. **Non injective** : $f(z) = f(1/z)$ (par exemple $f(2) = f(\tfrac12)$). **Surjective** : $f(z) = a \iff z^2 - az + 1 = 0$, équation du second degré qui a toujours des solutions dans $\mathbb{C}$ (non nulles, car leur produit vaut 1). Les antécédents de $a$ sont $\frac{a+\delta}{2}$ et $\frac{a-\delta}{2}$, où $\delta$ est une racine carrée du discriminant $\Delta = a^2 - 4$.
2. $z \in \mathbb{U} \iff z = e^{i\theta}$, $\theta \in ]-\pi, \pi]$ ; $f(e^{i\theta}) = e^{-i\theta} + e^{i\theta} = 2\cos\theta$. Donc $f(\mathbb{U}) = 2\cos(]-\pi,\pi]) = [-2, 2]$.
3. $\frac1z = \frac{\bar z}{|z|^2}$, donc $\mathrm{Re}\left(\frac1z\right) = \frac{\mathrm{Re}(z)}{|z|^2}$ et $\mathrm{Re}(f(z)) = \mathrm{Re}(z)\left(1 + \frac{1}{|z|^2}\right)$. Ainsi $\mathrm{Re}(f(z)) = 0 \iff \mathrm{Re}(z) = 0$, et le corrigé conclut $f^{-1}(i\mathbb{R}) = i\mathbb{R}$ (voir le point à vérifier : $i\mathbb{R}^*$).

## Méthodes à retenir

- Pour une image ou une image réciproque d'intervalle : tracer le graphe, puis découper selon la monotonie.
- Pour la bijectivité : résoudre $y = f(x)$ et vérifier qu'il y a une solution unique ; la solution est la réciproque.
- Pour une propriété de $f(A)$ ou $f^{-1}(C)$ : double inclusion en partant d'un élément.
- Pour les implications sur les composées : donner un nom à l'élément cherché et le construire avec $f(t)$ ou $g(y)$.
- Pour une égalité d'ensembles compliquée : passer aux fonctions indicatrices et calculer.

## Points à vérifier

- **Exercice 5, $f_2^{-1}(]-1,1[)$** : le corrigé donne $]-\pi/2, \pi/2[ + k\pi$. C'est faux : $\sin x \in ]-1,1[$ équivaut à $x \notin \pi/2 + \pi\mathbb{Z}$, soit $\mathbb{R} \setminus (\pi/2 + \pi\mathbb{Z})$ (complément).
- **Exercice 9, question 1** : le corrigé dit $f$ « décroissante » sur $\mathbb{R} \setminus \{2\}$, ce qui n'est vrai que sur chaque intervalle. Il écrit ensuite des bornes ouvertes pour $f([0,2[)$ et $f(]2,4])$ alors que $0$ et $4$ appartiennent aux intervalles : les images sont $]-\infty, -1/2]$ et $[13/2, +\infty[$ (complément).
- **Exercice 9, question 2** : les inégalités écrites pour $f^{-1}(]3,4])$ (« $3 \leq \ldots < 4$ ») ne correspondent pas à l'intervalle $]3,4]$ ; le résultat $[9, +\infty[$ est, lui, cohérent avec $]3,4]$ (complément). Les crochets de $f^{-1}([0,3[)$ sont illisibles dans le texte extrait : la bonne réponse est $]-\infty, -1/3]$.
- **Exercice 8, question 1** : « $\pi x$ est un antécédent de $y$ » doit se lire « $x/\pi$ » (coquille).
- **Exercice 19, question 3** : le raisonnement donne $\mathrm{Re}(z) = 0$ avec $z \neq 0$, donc $f^{-1}(i\mathbb{R}) = i\mathbb{R}^* $ et non $i\mathbb{R}$ (0 est exclu du départ) (complément).
- **Exercice 2, question 2** : une des égalités finales est écrite avec $]-\infty, 2[$ au lieu de $]-\infty, 2]$ (coquille).
- **Exercice 3** : l'énoncé écrit « $f([0, 1)$ » (crochet manquant) ; la correction traite $f([0,1])$.
- **Exercice 14** : une ligne de la diapositive est mal placée (« $f \circ (h \circ g)$ surjective $\Rightarrow f$ surjective » apparaît au milieu du raisonnement sur $h$) ; le raisonnement reconstitué ci-dessus suit l'ordre logique. Les renvois « question 4.10 » et « exercice 4.1 » désignent l'exercice 13 et l'exercice 18 de ce TD (numérotation d'une autre version).
- **Exercice 5, $f_3$** : le titre de la diapositive dit « Tracer la courbe représentative de $f_2$ » au lieu de $f_3$ (coquille).
- **Exercice 4.8** : aucune correction (« À vous de vérifier »).
