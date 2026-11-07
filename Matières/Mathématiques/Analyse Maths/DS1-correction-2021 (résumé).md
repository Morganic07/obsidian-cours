---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/contrôles/correction-DS1-analyse-18-11-2021(1)(1).pdf|correction-DS1-analyse-18-11-2021(1)(1).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de correction-DS1-analyse-18-11-2021 ([[Raw/Year 1/Analyse Maths/contrôles/correction-DS1-analyse-18-11-2021(1)(1).pdf|correction-DS1-analyse-18-11-2021(1)(1).pdf]]) (5 pages, texte), dans [[Analyse Maths (matière)]]. Corrigé du DS1 d'Analyse du 18 novembre 2021 (Département de Mathématiques, PréING1, 2021-2022). Même structure que [[DS1-Analyse-2022-corrigé (résumé)]], sur [[Chap0-Rappels-etc (résumé)]] et [[Chap1-reels (résumé)]]. Le barème est indiqué pour chaque question. Le document ne contient aucune figure (seule image : le logo de la première page).

## Exercice 1 : équations dans $\mathbb{R}$

### 1. $\sin(3x) = \cos(x)$ (1 point)

Méthode : se ramener à une égalité de deux sinus avec $\cos x = \sin\left(x + \frac{\pi}{2}\right)$ (voir [[Équation trigonométrique]], [[Formules trigonométriques]]).

$$
\begin{aligned}
\sin(3x) = \cos(x) &\iff \sin(3x) = \sin\left(x + \tfrac{\pi}{2}\right)\\
&\iff 3x \equiv x + \tfrac{\pi}{2}\ [2\pi] \quad\text{ou}\quad 3x \equiv \pi - x - \tfrac{\pi}{2}\ [2\pi]\\
&\iff 2x \equiv \tfrac{\pi}{2}\ [2\pi] \quad\text{ou}\quad 4x \equiv \tfrac{\pi}{2}\ [2\pi]\\
&\iff x = \tfrac{\pi}{4} + k\pi \quad\text{ou}\quad x = \tfrac{\pi}{8} + \tfrac{k\pi}{2},\ k \in \mathbb{Z}
\end{aligned}
$$

Ensemble solution :

$$S = \left\{\tfrac{\pi}{4} + k\pi,\ \tfrac{\pi}{8} + \tfrac{k\pi}{2} : k \in \mathbb{Z}\right\} = \left\{\tfrac{\pi}{4} + k\pi,\ \tfrac{\pi}{8} + k\pi,\ \tfrac{5\pi}{8} + k\pi : k \in \mathbb{Z}\right\}.$$

### 2. $\tan^2\left(3x + \frac{\pi}{3}\right) - 3 = 0$ (1,5 point)

Domaine : $3x + \frac{\pi}{3} \neq \frac{\pi}{2} + k\pi$, c'est-à-dire $x \neq \frac{\pi}{18} + \frac{k\pi}{3}$, $k \in \mathbb{Z}$. Sur ce domaine :

$$
\begin{aligned}
\tan^2\left(3x + \tfrac{\pi}{3}\right) = 3 &\iff \tan\left(3x + \tfrac{\pi}{3}\right) = \pm\sqrt{3} = \pm\tan\tfrac{\pi}{3}\\
&\iff 3x + \tfrac{\pi}{3} \equiv \tfrac{\pi}{3}\ [\pi] \quad\text{ou}\quad 3x + \tfrac{\pi}{3} \equiv -\tfrac{\pi}{3}\ [\pi]\\
&\iff 3x \equiv 0\ [\pi] \quad\text{ou}\quad 3x \equiv -\tfrac{2\pi}{3}\ [\pi]\\
&\iff x = \tfrac{k\pi}{3} \quad\text{ou}\quad x = -\tfrac{2\pi}{9} + \tfrac{k\pi}{3},\ k \in \mathbb{Z}
\end{aligned}
$$

Ensemble solution :

$$S = \left\{\tfrac{k\pi}{3},\ -\tfrac{2\pi}{9} + \tfrac{k\pi}{3}\right\} = \left\{k\pi,\ \tfrac{\pi}{3} + k\pi,\ \tfrac{2\pi}{3} + k\pi,\ -\tfrac{2\pi}{9} + k\pi,\ \tfrac{\pi}{9} + k\pi,\ \tfrac{4\pi}{9} + k\pi : k \in \mathbb{Z}\right\}.$$

### 3. $(5E(x) + 2)(3E(x) + 6) = 0$ (1,5 point)

$E$ désigne la [[Partie entière]]. Un produit est nul si l'un des facteurs l'est :

$$(5E(x)+2)(3E(x)+6) = 0 \iff E(x) = -\tfrac{2}{5} \quad\text{ou}\quad E(x) = -\tfrac{6}{3} = -2.$$

Comme $E(x)$ est toujours un entier, $E(x) = -\frac25$ n'a pas de solution. Donc l'équation équivaut à $E(x) = -2$, soit $x \in [-2, -1[$.

## Exercice 2 : inéquations dans $\mathbb{R}$

### 1. $\left|\frac{1}{x} + 1\right| < 1$ (1 point)

Il faut $x \neq 0$. L'inéquation équivaut à $-1 < \frac1x + 1 < 1$ ; on multiplie par $x$ en distinguant son signe (voir [[Règles de calcul sur les inégalités]], [[Raisonnement par disjonction des cas]]) :

- si $x > 0$ : $-x < 1 + x < x$, ce qui est impossible ;
- si $x < 0$ : $x < 1 + x < -x$, ce qui implique $x < -\frac12$.

Donc $S_1 = \left]-\infty ; -\frac12\right[$.

### 2. $(2E(x) + 1)^2 < 4$ (1,5 point)

$$(2E(x)+1)^2 < 4 \iff |2E(x)+1| < 2 \iff -2 < 2E(x) + 1 < 2 \iff -\tfrac32 < E(x) < \tfrac12.$$

Comme $E(x)$ est entier : $-1 \le E(x) \le 0$. Le corrigé en déduit $-1 < x < 1$ et $S_2 = ]-1 ; 1[$ (voir « Points à vérifier » : la borne $-1$ est en fait incluse).

### 3. $\sqrt{x^2 - 1} < 2 - x$ (1,5 point)

Domaine : l'inéquation est définie si $x^2 - 1 \ge 0$ et $0 < 2 - x$, soit $x \in ]-\infty ; -1] \cup [1 ; 2[$. Sur ce domaine, les deux membres sont positifs et on passe au carré :

$$x^2 - 1 < 4 - 4x + x^2 \iff 4x < 5 \iff x < \tfrac54.$$

Donc $S_3 = ]-\infty ; -1] \cup \left[1 ; \frac54\right[$.

## Exercice 3 : sommes et produits

### 1. $\displaystyle\sum_{k=0}^{n} \frac{k}{(k+1)!}$ (1,5 point)

Méthode : écrire $k = (k+1) - 1$ pour faire apparaître une [[Somme télescopique]] (voir [[Factorielle]]).

$$\sum_{k=0}^{n} \frac{k}{(k+1)!} = \sum_{k=0}^{n} \left(\frac{k+1}{(k+1)!} - \frac{1}{(k+1)!}\right) = \sum_{k=0}^{n} \left(\frac{1}{k!} - \frac{1}{(k+1)!}\right) = \frac{1}{0!} - \frac{1}{(n+1)!} = 1 - \frac{1}{(n+1)!}.$$

### 2. $\displaystyle\sum_{k=0}^{n} \frac{(-1)^k}{3^{k+1}}\binom{n}{k}$ (1,5 point)

Méthode : [[Formule du binôme de Newton]] avec $a = 1$, $b = -\frac13$ (voir [[Coefficient binomial]]).

$$\sum_{k=0}^{n} \frac{(-1)^k}{3^{k+1}}\binom{n}{k} = \frac13 \sum_{k=0}^{n} \binom{n}{k}\left(-\frac13\right)^k = \frac13 \sum_{k=0}^{n} \binom{n}{k} 1^{n-k}\left(-\frac13\right)^k = \frac13\left(1 - \frac13\right)^n = \frac13\left(\frac23\right)^n.$$

### 3. $\displaystyle\prod_{k=0}^{n} (-5)\,e^k$ (1 point)

$$\prod_{k=0}^{n} (-5)\,e^k = \prod_{k=0}^{n} (-5) \cdot \prod_{k=0}^{n} e^k = (-5)^{n+1}\, e^{\sum_{k=0}^{n} k} = (-5)^{n+1}\, e^{\frac{n(n+1)}{2}}.$$

## Exercice 4 : bornes de deux ensembles

$$A = \left\{x \in \mathbb{R} : x^2 - 2 \ge 0 \text{ et } |x - 1| < 3\right\}, \qquad B = \left\{(-1)^n + \frac1n : n \in \mathbb{N}^*\right\}.$$

### 1. $A$ et $B$ sont-ils majorés, minorés ?

**Ensemble $A$ (1 point).**

$$
\begin{aligned}
x \in A &\iff x^2 \ge 2 \text{ et } -3 < x - 1 < 3\\
&\iff \left(x \le -\sqrt2 \text{ ou } x \ge \sqrt2\right) \text{ et } -2 < x < 4\\
&\iff x \in \left(]-\infty, -\sqrt2] \cup [\sqrt2, +\infty[\right) \cap\ ]-2, 4[\\
&\iff x \in\ ]-2, -\sqrt2] \cup [\sqrt2, 4[.
\end{aligned}
$$

Donc $A = ]-2, -\sqrt2] \cup [\sqrt2, 4[$ : $A$ est majoré par tout réel $\ge 4$ et minoré par tout réel $\le -2$ (voir [[Majorant et minorant]]).

**Ensemble $B$ (1 point).** On distingue la [[Parité d'un entier]] $n$ :

- $n \neq 0$ pair : $(-1)^n = 1$ et $0 < \frac1n \le \frac12$, donc $1 < (-1)^n + \frac1n \le \frac32$ ;
- $n$ impair : $(-1)^n = -1$ et $0 < \frac1n \le 1$, donc $-1 < (-1)^n + \frac1n \le 0$.

Ainsi $\forall n \in \mathbb{N}^*,\ (-1)^n + \frac1n \in ]-1, 0] \cup \left]1, \frac32\right]$ : $B$ est majoré par tout réel $\ge \frac32$ et minoré par tout réel $\le -1$.

### 2. Bornes supérieure et inférieure, plus grand et plus petit élément

**Ensemble $A$ (1,5 point).** $\sup A = 4$ et $\inf A = -2$ ; ces bornes ne sont pas atteintes, donc $A$ n'a ni maximum ni minimum (voir [[Borne supérieure]], [[Plus grand élément]]).

**Ensemble $B$ (2,5 points).**

- $\frac32 = (-1)^2 + \frac12 \in B$ : c'est un majorant qui appartient à $B$, donc $\sup B = \max B = \frac32$.
- Borne inférieure : on étudie la suite $u_k = (-1)^{2k+1} + \frac{1}{2k+1} = -1 + \frac{1}{2k+1}$, $k \in \mathbb{N}$. Pour tout $k$, $u_k \ge \inf B$ ; par passage à la limite (la limite préserve les inégalités larges), $-1 = \lim u_k \ge \inf B$. Or $-1$ est un minorant de $B$ et $\inf B$ est le plus grand des minorants, donc $\inf B \ge -1$. Finalement $\inf B = -1$, et $B$ n'a pas de minimum ($-1$ n'est jamais atteint).

## Exercice 5 : borne inférieure de la racine d'un ensemble (2 points)

**Énoncé.** Soit $A$ une partie non vide et bornée de $\mathbb{R}_+$. On pose $\sqrt{A} = \{\sqrt{x} : x \in A\}$. Montrer que $\inf(\sqrt{A}) = \sqrt{\inf(A)}$.

**Correction.**

1. Existence : $A$ est non vide, borné et positif, donc $\inf(A)$ existe et est positif. $\sqrt{A}$ est alors non vide, positif et borné, donc $\inf(\sqrt A)$ existe et est positif.
2. Minorant : pour tout $x \in A$, $x \ge \inf(A) \ge 0$. La fonction $x \mapsto \sqrt x$ est strictement croissante (voir [[Application monotone]]), donc $\sqrt{x} \ge \sqrt{\inf(A)}$ pour tout $x \in A$ : $\sqrt{\inf(A)}$ minore $\sqrt A$.
3. Plus grand minorant, par [[Raisonnement par l'absurde]] : supposons qu'il existe $\varepsilon > 0$ tel que $\sqrt{x} \ge \sqrt{\inf(A)} + \varepsilon > \sqrt{\inf(A)} \ge 0$ pour tout $x \in A$. En passant au carré :
$$x \ge \inf(A) + 2\varepsilon\sqrt{\inf(A)} + \varepsilon^2 > \inf(A),$$
ce qui est impossible, car $\inf(A)$ est le plus grand minorant de $A$. Donc $\inf(\sqrt A) = \sqrt{\inf(A)}$.

## Points à vérifier

- **Exercice 2, question 2** : le corrigé écrit $-1 \le E(x) \le 0 \Leftrightarrow -1 < x < 1$ et conclut $S_2 = ]-1, 1[$. Or $E(x) = -1$ correspond à $x \in [-1, 0[$, donc $-1$ est solution (pour $x = -1$ : $(2 \cdot (-1) + 1)^2 = 1 < 4$). L'ensemble correct est $[-1, 1[$.
- **Exercice 4, ensemble $B$** : le corrigé écrit d'abord « si $n \neq 0$ est pair » puis « si $n \neq 0$ est impair » alors que $n \in \mathbb{N}^*$ ; la précision $n \neq 0$ est redondante, sans conséquence sur le résultat.

## Liens

[[Relation d'ordre]], [[Borne supérieure]], [[Dénombrement]] (binôme), [[Récurrence]].
