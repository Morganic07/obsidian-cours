---
type: source
tags: [year1]
sources: [".raw/Year 1/Analyse Maths/Exos/td0slides.pdf"]
maj: 2026-11-06
complet: true
---

Résumé de td0slides (`.raw/Year 1/Analyse Maths/Exos/td0slides.pdf`) (85 diapositives, texte, « Analyse 1, premier semestre 2026-2027 »), dans [[Analyse Maths (matière)]]. Ce sont les diapositives corrigées du TD0 « Inégalités, sigma et fonctions trigonométriques » (CY Tech). Les énoncés sont ceux de [[TD0-Rappel (résumé)]] (ordre légèrement différent), avec la solution rédigée pas à pas. Cours associé : [[Chap0-Rappels-etc (résumé)]]. Les diapositives ont été relues en image.

Organisation : exercices 1, 5, 6, 7, 8, 9, 10, 12, 13, 14 en séance ; exercices 2, 3, 4 « à faire chez soi » ; exercice 11 « pour aller plus loin » ; puis des exercices supplémentaires sans corrigé.

## Exercice 1 : inégalités classiques

### 1. $\forall x \in\, ]0,+\infty[,\ x + \frac1x \ge 2$

$$(x-1)^2 \ge 0 \implies x^2 - 2x + 1 \ge 0 \implies x^2 + 1 \ge 2x \underset{\times \frac1x}{\implies} x + \frac1x \ge 2.$$

La multiplication par $\frac1x$ conserve le sens car $x > 0$.

### 2. $\forall x, y \in \mathbb R,\ xy \le \frac12(x^2+y^2)$

$$0 \le (x-y)^2 \implies 0 \le x^2 - 2xy + y^2 \implies 2xy \le x^2 + y^2 \implies xy \le \tfrac12 (x^2+y^2).$$

### 3. $\forall x, y, z \in \mathbb R,\ x^2+y^2+z^2 \ge xy+yz+zx$

D'après 2 : $xy \le \frac12(x^2+y^2)$, $xz \le \frac12(x^2+z^2)$, $yz \le \frac12(y^2+z^2)$. En additionnant les trois inégalités :

$$xy+yz+zx \le \tfrac12(x^2+y^2) + \tfrac12(x^2+z^2) + \tfrac12(y^2+z^2) = x^2+y^2+z^2.$$

### 4. $\forall x \in \mathbb R,\ 0 < \dfrac{x^2+2x+4}{x^2+2x+2} \le 3$

**Positivité, méthode 1 (discriminant)** : pour le dénominateur, $\Delta = b^2 - 4ac = 4 - 8 = -4 < 0$ : pas de racine, il garde le signe de $a = 1$, donc $x^2+2x+2 > 0$. Pour le numérateur, $\Delta = 4 - 16 = -12 < 0$, donc $x^2+2x+4 > 0$. Le quotient est strictement positif.

**Positivité, méthode 2 (forme canonique)** : $x^2+2x+4 = (x+1)^2 + 3 \ge 3 > 0$ et $x^2+2x+2 = (x+1)^2+1 \ge 1 > 0$ ; le quotient de deux réels strictement positifs est strictement positif.

**Majoration, méthode 1 (équivalences)** : le dénominateur étant positif,

$$\frac{x^2+2x+4}{x^2+2x+2} \le 3 \iff x^2+2x+4 \le 3x^2+6x+6 \iff 0 \le 2x^2+4x+2 = 2(x+1)^2,$$

ce qui est vrai ; donc la première inégalité l'est aussi.

**Majoration, méthode 2 (tout passer à gauche)** :

$$\frac{x^2+2x+4}{x^2+2x+2} - 3 = \frac{x^2+2x+4 - 3(x^2+2x+2)}{x^2+2x+2} = \frac{-2x^2-4x-2}{x^2+2x+2}.$$

Numérateur : $\Delta = 16 - 16 = 0$, il garde le signe de $a = -2 < 0$ ; il est négatif, donc le quotient aussi, d'où l'inégalité.

## Exercice 2 (à faire chez soi)

### 1. $\forall x,y \in \mathbb R,\ xy \le \left(\frac{x+y}{2}\right)^2$

$$0 \le (x-y)^2 \implies 2xy \le x^2+y^2 \implies 4xy \le x^2 + 2xy + y^2 = (x+y)^2 \implies xy \le \frac{(x+y)^2}{4} = \left(\frac{x+y}{2}\right)^2.$$

### 2. Minimum de $f(x) = \dfrac{x^2+2x+2}{x^2+2x+3}$ sans étudier les variations

- $x^2+2x+3 = (x+1)^2 + 2 \ge 2$, donc $\dfrac{1}{x^2+2x+3} \le \dfrac12$.
- Réécriture : $f(x) = \dfrac{x^2+2x+3-1}{x^2+2x+3} = 1 - \dfrac{1}{x^2+2x+3} \ge 1 - \dfrac12 = \dfrac12$.
- Et $f(-1) = \dfrac12$ : la minoration est **atteinte**. Le minimum de $f$ est $\dfrac12$.

Méthode : prouver une minoration, puis montrer qu'elle est atteinte.

## Exercice 3 (à faire chez soi) : encadrements

Hypothèses : $0 < a \le x \le b$, $d \le y \le c < 0$, $0 < e \le z \le f$.

### Encadrer $4x - 2y$

- Multiplier par 4 : $0 < 4a \le 4x \le 4b$.
- Multiplier par $-2$ **renverse l'ordre** : $0 < -2c \le -2y \le -2d$.
- Additionner : $4a - 2c \le 4x - 2y \le 4b - 2d$.

### Encadrer $\dfrac{x-y}{z}$

- $0 < a \le x \le b$ (2), et $0 < -c \le -y \le -d$ (3) en multipliant par $-1$.
- Additionner (2) et (3) : $0 < a - c \le x - y \le b - d$ (4).
- $0 < e \le z \le f$ donne $\dfrac1f \le \dfrac1z \le \dfrac1e$ (5) (passage à l'inverse sur des réels strictement positifs : l'ordre s'inverse).
- Multiplier (4) et (5), légitime car tout est strictement positif : $0 < \dfrac{a-c}{f} \le \dfrac{x-y}{z} \le \dfrac{b-d}{e}$.

**Remarque du corrigé** : $1 \le x \le 3$ et $-2 \le y \le -1$ n'impliquent pas $-2 \le xy \le -3$ : on ne multiplie pas des encadrements dont les bornes sont de signes différents (voir « Points à vérifier »).

## Exercice 4 (à faire chez soi) : domaine de $x \mapsto \sqrt{\dfrac{\ln|x|}{x}}$

Rappel donné : la courbe de $\ln$.

![[td0slides - p15.jpg]]
*Figure : courbe de la fonction logarithme népérien, qui s'annule en 1 et vaut 1 en $e \approx 2{,}7$.*

- $x \mapsto \ln|x|$ et $x \mapsto \frac1x$ sont définies ssi $x \ne 0$ : $\dfrac{\ln|x|}{x}$ est définie sur $\mathbb R \setminus \{0\}$.
- $\sqrt{\cdot}$ est définie sur $\mathbb R_+$, donc $\sqrt{\dfrac{\ln|x|}{x}}$ est définie $\iff \dfrac{\ln|x|}{x} \ge 0$.
- $\ln|x| \ge 0 \iff |x| \ge 1$. Étude de signe :

| Intervalle | Signe de $\ln\lvert x\rvert$ | Signe de $x$ | $\frac{\ln\lvert x\rvert}{x}$ |
|---|---|---|---|
| $x \le -1$ | $\ge 0$ | $< 0$ | $\le 0$ |
| $-1 \le x < 0$ | $\le 0$ | $< 0$ | $\ge 0$ |
| $0 < x \le 1$ | $\le 0$ | $> 0$ | $\le 0$ |
| $x \ge 1$ | $\ge 0$ | $> 0$ | $\ge 0$ |

**Domaine** : $[-1, 0[\ \cup\ [1, +\infty[$ (en $x = -1$, le quotient vaut 0, donc la racine est définie).

## Exercice 5 : $|x - a| < |a|$ entraîne $x$ non nul et de même signe que $a$

On suppose $a \ne 0$. Par définition de la [[Valeur absolue]] : $-|a| < x - a < |a|$ (6).

- Si $a > 0$ : $-a < x - a < a$, d'où $0 < x < 2a$ : $x$ est non nul et positif.
- Si $a < 0$ : $a < x - a < -a$, d'où $2a < x < 0$ : $x$ est non nul et négatif.

## Exercice 6 : inéquations avec valeurs absolues et racines

### Rappels du corrigé

- Pour tout $x > 0$ : $x \le a \iff x^2 \le a^2$ et $a \ge 0$.
- Pour tous $x \ge 0$, $a \ge 0$ : $x \le a \iff x^2 \le a^2$.
- Pour tous $x, a \in \mathbb R$ : $x^2 \le a^2 \iff |x| \le |a|$.

### $|x+1| < 0{,}1$

$-0{,}1 < x+1 < 0{,}1 \iff -1{,}1 < x < -0{,}9$. **Solution** : $]-1{,}1\,;\,-0{,}9[$.

### $|x - 2| > 10$

- Si $x \ge 2$ : $x - 2 > 10 \iff x > 12$ ; solution sur $[2,+\infty[$ : $]12,+\infty[$.
- Si $x < 2$ : $-(x-2) > 10 \iff -x > 8 \iff x < -8$ ; solution sur $]-\infty, 2[$ : $]-\infty,-8[$.

**Solution** : $]-\infty,-8[\ \cup\ ]12,+\infty[$.

### $|x| < |x+1|$

**Méthode 1 (cas)** : réécrire $-|x+1| < x < |x+1|$ (7).

- Si $x \ge -1$ : $-x-1 < x < x+1$, d'où $-1 < 2x$, soit $-\frac12 < x$ ; solution sur $[-1,+\infty[$ : $]-\frac12,+\infty[$.
- Si $x < -1$ : $x < 0$ et $x+1 < 0$, donc $|x| < |x+1| \iff -x < -x-1 \iff 0 < -1$ : contradiction, pas de solution.

**Méthode 2 (carrés)** : $|x| < |x+1| \iff x^2 < (x+1)^2 \iff 0 < 2x+1 \iff -\frac12 < x$.

**Solution** : $]-\frac12, +\infty[$.

### $|2x - 1| < |x - 1|$ (méthode des carrés)

$$|2x-1| < |x-1| \iff (2x-1)^2 < (x-1)^2 \iff 4x^2-4x+1 < x^2-2x+1 \iff 3x^2 - 2x < 0 \iff 3x\left(x - \tfrac23\right) < 0 \iff 0 < x < \tfrac23.$$

**Solution** : $]0, \frac23[$.

### $\big||x+3| - 1\big| \le 2$

$-2 \le |x+3| - 1 \le 2 \iff -1 \le |x+3| \le 3$ ; comme $|x+3| \ge 0$, cela équivaut à $0 \le |x+3| \le 3 \iff -3 \le x+3 \le 3 \iff -6 \le x \le 0$. **Solution** : $[-6, 0]$.

### $\dfrac{x-1}{x+2} \ge 3$

**Méthode 1 (cas selon le signe du dénominateur)** :

- Si $x > -2$ : $x - 1 \ge 3x + 6 \iff -7 \ge 2x \iff x \le -\frac72$, incompatible avec $x > -2$ : pas de solution.
- Si $x < -2$ (on multiplie par un négatif, l'ordre s'inverse) : $x - 1 \le 3x + 6 \iff -7 \le 2x \iff -\frac72 \le x$.

**Méthode 2 (tableau de signes)** : $\dfrac{x-1}{x+2} - 3 \ge 0 \iff \dfrac{-2x-7}{x+2} \ge 0$ : numérateur et dénominateur de même signe, ou numérateur nul.

| $x$ | $-\infty$ … $-\frac72$ | $-\frac72$ … $-2$ | $-2$ … $+\infty$ |
|---|---|---|---|
| $-2x-7$ | $+$ | $-$ | $-$ |
| $x+2$ | $-$ | $-$ | $+$ |
| $\frac{-2x-7}{x+2}$ | $-$ | $+$ | $-$ |

**Solution** : $[-\frac72, -2[$.

### $\sqrt{x-3} - \sqrt{2x+1} \le 4$

- Domaine : $x - 3 \ge 0 \iff x \ge 3$ et $2x + 1 \ge 0 \iff x \ge -\frac12$ ; l'inéquation est définie ssi $x \ge 3$.
- Pour $x \ge 3$ : $-4 < x \implies x - 4 < 2x \implies 0 \le x - 3 < 2x + 1$, d'où, par croissance de la racine, $\sqrt{x-3} < \sqrt{2x+1}$, soit $\sqrt{x-3} - \sqrt{2x+1} < 0 \le 4$.

**Solution** : $[3, +\infty[$.

### $\sqrt{x^2 - 2x + 3} \le x - 1$

Trois cas :

- Si $x < 1$ : $x - 1 < 0$ alors que la racine est positive : pas de solution.
- Si $x = 1$ : $\sqrt{1 - 2 + 3} = \sqrt2 > 0$ : pas solution.
- Si $x > 1$ : on élève au carré (les deux membres sont positifs) : $x^2 - 2x + 3 \le x^2 - 2x + 1 \iff 3 \le 1$, contradiction : pas de solution.

**Solution** : aucune ($\varnothing$).

## Exercice 7 : sommes et produits

Voir [[Symboles somme et produit]], [[Somme télescopique]].

### $\sum_{i=1}^n 2$ et $\prod_{i=1}^n 3$

$$\sum_{i=1}^n 2 = 2\sum_{i=1}^n 1 = 2(\underbrace{1 + 1 + \dots + 1}_{n \text{ fois}}) = 2n, \qquad \prod_{i=1}^n 3 = \underbrace{3 \cdot 3 \cdots 3}_{n \text{ fois}} = 3^n.$$

### $\sum_{k=1}^n (2a_{k+1} - 3a_k + a_{k-1})$

On écrit $2a_{k+1} - 3a_k + a_{k-1} = 2(a_{k+1} - a_k) - (a_k - a_{k-1})$, d'où deux sommes télescopiques :

$$\sum_{k=1}^n (a_{k+1}-a_k) = a_{n+1} - a_1, \qquad \sum_{k=1}^n (a_k - a_{k-1}) = a_n - a_0,$$

$$\sum_{k=1}^n (2a_{k+1} - 3a_k + a_{k-1}) = 2(a_{n+1}-a_1) - (a_n - a_0) = 2a_{n+1} - a_n - 2a_1 + a_0.$$

### $\sum_{k=1}^n k$ (méthode de Gauss)

On écrit la somme à l'endroit et à l'envers, puis on additionne terme à terme :

$$2\sum_{k=1}^n k = \underbrace{(n+1) + (n+1) + \dots + (n+1)}_{n \text{ fois}} = n(n+1), \qquad \sum_{k=1}^n k = \frac{n(n+1)}{2}.$$

Voir [[Somme des premiers entiers]].

### $\sum_{k=2}^n 3^{2k}$ : somme géométrique

**Rappel** ([[Suite géométrique]]) : pour $a \ne 1$, $\displaystyle\sum_{k=0}^n a^k = \frac{1 - a^{n+1}}{1-a}$.

Preuve : $\sum_{k=0}^n a^k - a\sum_{k=0}^n a^k = (1 + a + \dots + a^n) - (a + a^2 + \dots + a^{n+1}) = 1 - a^{n+1}$, donc $(1-a)\sum_{k=0}^n a^k = 1 - a^{n+1}$.

Application :

$$\sum_{k=2}^n 3^{2k} = \sum_{k=2}^n 9^k = \sum_{k=0}^n 9^k - (1+9) = \frac{1 - 9^{n+1}}{1-9} - 10 = \frac{9^{n+1}-1}{8} - \frac{80}{8} = \frac{9^{n+1} - 9^2}{8} = \frac{9^2(9^{n-1}-1)}{8}.$$

### $\sum_{k=0}^{n-1} (2k+1) = n^2 = \sum_{k=1}^n (2k-1)$

- $(k+1)^2 - k^2 = 2k+1$, donc $\sum_{k=0}^{n-1}(2k+1) = \sum_{k=0}^{n-1}\big((k+1)^2 - k^2\big)$, somme télescopique de terme $a_k = k^2$ : elle vaut $a_n - a_0 = n^2$.
- $k^2 - (k-1)^2 = 2k - 1$, donc $\sum_{k=1}^n (2k-1) = \sum_{k=1}^n \big(k^2 - (k-1)^2\big) = n^2 - 0^2 = n^2$.
- **Autre manière** : [[Changement d'indice]] $\ell = k+1$ ($k = 0 \Rightarrow \ell = 1$, $k = n-1 \Rightarrow \ell = n$) : $\sum_{k=0}^{n-1}(2k+1) = \sum_{\ell=1}^n \big(2(\ell-1)+1\big) = \sum_{\ell=1}^n (2\ell - 1)$.

### $\sum (k+1)^3 - \sum k^3$ et somme des carrés

Montrer que $\displaystyle\sum_{k=0}^n (k+1)^3 - \sum_{k=0}^n k^3 = 3\sum_{k=1}^n k^2 + \frac{(n+1)(3n+2)}{2}$, puis en déduire $\sum k^2$.

- Développement : $(k+1)^3 - k^3 = 3k^2 + 3k + 1$, donc la différence vaut $3\sum k^2 + 3\sum k + \sum 1$, avec $\sum_{k=0}^n 1 = n+1$ et $\sum_{k=0}^n k = \frac{n(n+1)}{2}$ :

$$3\sum_{k=0}^n k^2 + \frac{3n(n+1)}{2} + n + 1 = 3\sum_{k=0}^n k^2 + \frac{3n(n+1) + 2(n+1)}{2} = 3\sum_{k=0}^n k^2 + \frac{(n+1)(3n+2)}{2}.$$

- Télescopage : la même différence vaut $(n+1)^3 - 0^3 = (n+1)^3$.
- D'où $\displaystyle\sum_{k=0}^n k^2 = \frac{2(n+1)^3 - (n+1)(3n+2)}{6} = \frac{(n+1)(2n^2 + 4n + 2 - 3n - 2)}{6} = \frac{(n+1)(2n^2+n)}{6}$, soit

$$\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}.$$

## Exercice 8 : sommes avec coefficients binomiaux

Outil : la [[Formule du binôme de Newton]] $(a+b)^n = \sum_{k=0}^n \binom nk a^k b^{n-k}$ ; voir [[Coefficient binomial]].

### $\sum_{k=1}^n \binom nk 5^k$

On complète la somme avec le terme $k = 0$ :

$$\sum_{k=1}^n \binom nk 5^k = \sum_{k=0}^n \binom nk 5^k - \binom n0 5^0 = \sum_{k=0}^n \binom nk 5^k\, 1^{n-k} - 1 = (5+1)^n - 1 = 6^n - 1.$$

### $\sum_{k=0}^{n-1} (-3)^k \binom nk$

On ajoute et retire le terme $k = n$ :

$$\sum_{k=0}^{n-1} \binom nk (-3)^k = \sum_{k=0}^{n} \binom nk (-3)^k\, 1^{n-k} - (-3)^n = (-3+1)^n - (-3)^n = (-2)^n - (-3)^n.$$

### $\sum_{k=0}^n k\binom nk$

- Le terme $k = 0$ est nul ; $k\binom nk = \dfrac{k \cdot n!}{k!(n-k)!} = \dfrac{n!}{(k-1)!(n-k)!}$.
- Changement d'indice $\ell = k - 1$ ($k = 1 \Rightarrow \ell = 0$, $k = n \Rightarrow \ell = n-1$) :

$$\sum_{k=1}^n \frac{n!}{(k-1)!(n-k)!} = n\sum_{\ell=0}^{n-1} \frac{(n-1)!}{\ell!\,((n-1)-\ell)!} = n\sum_{\ell=0}^{n-1}\binom{n-1}{\ell} 1^\ell\, 1^{n-1-\ell} = n(1+1)^{n-1} = n\,2^{n-1}.$$

## Exercice 9 : écrire avec des factorielles

- $\displaystyle\prod_{k=1}^n k^2 = \left(\prod_{k=1}^n k\right)^2 = (n!)^2$.
- $\displaystyle\prod_{k=3}^{n-1} k = \frac{1}{1 \cdot 2}\prod_{k=1}^{n-1} k = \frac{(n-1)!}{2}$.
- $\displaystyle\prod_{k=2}^n (2k+1)$ : produit des impairs de 5 à $2n+1$, c'est-à-dire de tous les entiers de 5 à $2n+1$ divisé par les pairs de 6 à $2n$ :

$$\prod_{k=2}^n (2k+1) = \left(\prod_{k=5}^{2n+1} k\right)\left(\prod_{k=3}^n 2k\right)^{-1} = \frac{1}{1\cdot2\cdot3\cdot4}\prod_{k=1}^{2n+1} k \cdot \left(\frac{1}{1\cdot 2}\prod_{k=1}^n k\right)^{-1} \cdot \frac{1}{2^{n+1-3}}$$

$$= \frac{(2n+1)!}{4!}\left(\frac{n!}{2}\right)^{-1}\frac{1}{2^{n-2}} = \frac{(2n+1)!}{12 \cdot 2^{n-2}\, n!} = \frac{(2n+1)!}{3 \cdot 2^n\, n!}.$$

Voir [[Factorielle]].

## Exercice 10 : produits

- $\displaystyle\prod_{k=0}^n 3^k = 3 \cdot 3^2 \cdot 3^3 \cdots 3^n = 3^{1+2+\dots+n} = 3^{\sum_{k=1}^n k} = 3^{\frac{n(n+1)}{2}}$.
- $\displaystyle\prod_{k=2}^n \frac{k}{k+2} = \frac{\prod_{k=2}^n k}{\prod_{k=2}^n (k+2)}$ ; changement d'indice $\ell = k + 2$ ($k = 2 \Rightarrow \ell = 4$, $k = n \Rightarrow \ell = n+2$) : $\prod_{k=2}^n (k+2) = \prod_{\ell=4}^{n+2} \ell$. Ainsi

$$\prod_{k=2}^n \frac{k}{k+2} = \frac{2 \cdot 3 \cdot \prod_{k=4}^n k}{\prod_{k=4}^n k \cdot (n+1)(n+2)} = \frac{6}{(n+1)(n+2)}.$$

## Exercice 11 (pour aller plus loin) : $\binom{n}{p+1} = \binom pp + \binom{p+1}{p} + \dots + \binom{n-1}{p}$

Pour $p, n \in \mathbb N^*$ avec $p < n$.

### Rappels

- **[[Coefficient binomial]]** : pour $0 \le k \le n$, $\binom nk = \dfrac{n!}{k!(n-k)!}$, qui se lit « $k$ parmi $n$ ».
- **[[Formule de Pascal]]** : pour $0 < k \le n$, $\binom{n}{k+1} = \binom{n-1}{k+1} + \binom{n-1}{k}$.

**Preuve de la formule de Pascal** :

$$\binom{n-1}{k+1} + \binom{n-1}{k} = (n-1)!\left(\frac{1}{(k+1)!(n-2-k)!} + \frac{1}{k!(n-1-k)!}\right).$$

Avec $(k+1)! = k!(k+1)$ et $(n-1-k)! = (n-2-k)!(n-1-k)$, on met au même dénominateur $(k+1)!(n-1-k)!$ :

$$= (n-1)!\,\frac{(n-1-k) + (k+1)}{(k+1)!(n-1-k)!} = \frac{(n-1)!\,n}{(k+1)!(n-1-k)!} = \frac{n!}{(k+1)!(n-(k+1))!} = \binom{n}{k+1}.$$

### Méthode 1 : Pascal en cascade

$$\binom{n}{p+1} = \binom{n-1}{p+1} + \binom{n-1}{p},\quad \binom{n-1}{p+1} = \binom{n-2}{p+1} + \binom{n-2}{p},\quad \dots,\quad \binom{p+2}{p+1} = \binom{p+1}{p+1} + \binom{p+1}{p} = \binom pp + \binom{p+1}{p}.$$

On remplace de proche en proche le premier terme ; il reste $\binom{n}{p+1} = \binom pp + \binom{p+1}{p} + \dots + \binom{n-2}{p} + \binom{n-1}{p}$.

### Méthode 2 : [[Récurrence]] sur $n$

$\mathcal P(n)$ : $\binom{n}{p+1} = \binom pp + \binom{p+1}{p} + \dots + \binom{n-1}{p}$.

- **Initialisation** ($n = 2$, donc nécessairement $p = 1$) : $\binom{2}{2} = 1$ et $\binom11 = 1$ ; les deux membres sont égaux.
- **Hérédité** : on suppose $\mathcal P(n)$. Alors

$$\binom pp + \dots + \binom{n-1}{p} + \binom np = \binom{n}{p+1} + \binom np = \binom{n+1}{p+1}$$

par l'hypothèse de récurrence puis la formule de Pascal : $\mathcal P(n+1)$ est vraie.

## Exercice 12 : formules trigonométriques

Voir [[Fonctions trigonométriques]], [[Formules trigonométriques]].

### Rappels du corrigé

- Périodicité et parité : $\sin(x + 2\pi) = \sin x$, $\cos(x+2\pi) = \cos x$, $\sin(-x) = -\sin x$, $\cos(-x) = \cos x$, $\sin^2 x + \cos^2 x = 1$.
- **Formules d'addition** :

$$\sin(x+y) = \sin x\cos y + \cos x \sin y, \qquad \sin(x-y) = \sin x \cos y - \cos x \sin y,$$
$$\cos(x+y) = \cos x\cos y - \sin x\sin y, \qquad \cos(x-y) = \cos x\cos y + \sin x \sin y.$$

- **Formules de duplication** ($x = y$) : $\sin 2x = 2\sin x\cos x$ ; $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$.
- Conséquences, telles qu'écrites sur la diapositive :

| | | Remarque |
|---|---|---|
| $\sin(x+\pi) = -\sin x$ | $\sin(x - \pi) = \sin x$ | **faux** : $\sin(x-\pi) = -\sin x$ |
| $\sin(x + \pi/2) = \cos x$ | $\sin(x-\pi/2) = \cos x$ | **faux** : $\sin(x - \pi/2) = -\cos x$ |
| $\cos(x+\pi) = -\cos x$ | $\cos(x-\pi) = -\cos x$ | correct |
| $\cos(x + \pi/2) = -\sin x$ | $\cos(x+\pi/2) = \sin x$ | coquille : il s'agit de $\cos(x - \pi/2) = \sin x$ |

### $\sin x + \sin y = 2\sin\frac{x+y}{2}\cos\frac{x-y}{2}$

**Méthode 1** : écrire $x = \frac{x+y}{2} + \frac{x-y}{2}$ et $y = \frac{x+y}{2} - \frac{x-y}{2}$, puis développer :

$$\sin x = \sin\tfrac{x+y}{2}\cos\tfrac{x-y}{2} + \cos\tfrac{x+y}{2}\sin\tfrac{x-y}{2}, \qquad \sin y = \sin\tfrac{x+y}{2}\cos\tfrac{x-y}{2} - \cos\tfrac{x+y}{2}\sin\tfrac{x-y}{2}.$$

En additionnant : $\sin x + \sin y = 2\sin\frac{x+y}{2}\cos\frac{x-y}{2}$.

**Méthode 2 (formule de produit)** : $\sin\frac{x+y}{2}\cos\frac{x-y}{2} = \frac12\left(\sin\left(\frac{x+y}{2} + \frac{x-y}{2}\right) + \sin\left(\frac{x+y}{2} - \frac{x-y}{2}\right)\right) = \frac12(\sin x + \sin y)$.

### $\cos x - \cos y = -2\sin\frac{x-y}{2}\sin\frac{x+y}{2}$

**Méthode 1** : $\sin(x + \frac\pi2) = \sin x\cos\frac\pi2 + \cos x\sin\frac\pi2 = \cos x$, donc $-\cos y = -\sin(y + \frac\pi2) = \sin(-y - \frac\pi2)$ (imparité). Ainsi $\cos x - \cos y = \sin(x + \frac\pi2) + \sin(-y - \frac\pi2)$, et la formule précédente donne

$$\cos x - \cos y = 2\sin\tfrac{x-y}{2}\cos\left(\tfrac{x+y}{2} + \tfrac\pi2\right) = -2\sin\tfrac{x-y}{2}\sin\tfrac{x+y}{2},$$

car $\cos(\frac{x+y}{2} + \frac\pi2) = \cos\frac{x+y}{2}\cos\frac\pi2 - \sin\frac{x+y}{2}\sin\frac\pi2 = -\sin\frac{x+y}{2}$.

**Méthode 2 (formule de produit)** $\sin a\sin b = \frac12\big(\cos(a-b) - \cos(a+b)\big)$ :

$$\sin\tfrac{x-y}{2}\sin\tfrac{x+y}{2} = \tfrac12\left(\cos\left(\tfrac{x+y}{2} - \tfrac{x-y}{2}\right) - \cos\left(\tfrac{x+y}{2} + \tfrac{x-y}{2}\right)\right) = \tfrac12\big(\cos y - \cos x\big),$$

d'où $\cos x - \cos y = -2\sin\frac{x-y}{2}\sin\frac{x+y}{2}$.

### $\tan(x+y) = \dfrac{\tan x + \tan y}{1 - \tan x\tan y}$

**Méthode 1** (on part de la droite et on multiplie haut et bas par $\cos x\cos y$) :

$$\frac{\tan x + \tan y}{1 - \tan x \tan y} = \frac{\frac{\sin x\cos y + \cos x \sin y}{\cos x \cos y}}{\frac{\cos x\cos y - \sin x\sin y}{\cos x\cos y}} = \frac{\sin(x+y)}{\cos(x+y)} = \tan(x+y).$$

**Méthode 2** (on part de la gauche et on factorise par $\cos x\cos y$) : $\tan(x+y) = \dfrac{\sin x\cos y + \cos x\sin y}{\cos x\cos y - \sin x\sin y} = \dfrac{\cos x\cos y\left(\frac{\sin x}{\cos x} + \frac{\sin y}{\cos y}\right)}{\cos x \cos y\left(1 - \frac{\sin x\sin y}{\cos x\cos y}\right)} = \dfrac{\tan x + \tan y}{1 - \tan x\tan y}$.

### Formules en $t = \tan\frac x2$

$$\frac{1-t^2}{1+t^2} = \cos x, \qquad \frac{2t}{1+t^2} = \sin x.$$

- Première : $\dfrac{1 - \tan^2\frac x2}{1 + \tan^2\frac x2} = \dfrac{\frac{\cos^2\frac x2 - \sin^2\frac x2}{\cos^2\frac x2}}{\frac{\cos^2\frac x2 + \sin^2\frac x2}{\cos^2\frac x2}} = \cos^2\tfrac x2 - \sin^2\tfrac x2 = \cos\left(\tfrac x2 + \tfrac x2\right) = \cos x$.
- Seconde : $\dfrac{2\tan\frac x2}{1 + \tan^2\frac x2} = \dfrac{2\frac{\sin(x/2)}{\cos(x/2)}}{\frac{1}{\cos^2(x/2)}} = 2\sin\tfrac x2\cos\tfrac x2 = \sin x$.

## Exercice 13 : $\cos\frac{\pi}{12}$, $\sin\frac{\pi}{12}$, $\tan\frac{\pi}{12}$

Valeurs remarquables rappelées :

| $x$ | $0$ | $\frac\pi6$ | $\frac\pi4$ | $\frac\pi3$ | $\frac\pi2$ |
|---|---|---|---|---|---|
| $\sin x$ | $0$ | $\frac12$ | $\frac{1}{\sqrt2}$ | $\frac{\sqrt3}{2}$ | $1$ |
| $\cos x$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $0$ |
| $\tan x$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | non définie |

On note que $\frac{\pi}{12} = \frac\pi4 - \frac\pi6$ :

$$\cos\frac{\pi}{12} = \cos\frac\pi4\cos\frac\pi6 + \sin\frac\pi4\sin\frac\pi6 = \frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2} + \frac{\sqrt2}{2}\cdot\frac12 = \frac{\sqrt6 + \sqrt2}{4},$$

$$\sin\frac{\pi}{12} = \sin\frac\pi4\cos\frac\pi6 - \cos\frac\pi4\sin\frac\pi6 = \frac{\sqrt6 - \sqrt2}{4}, \qquad \tan\frac{\pi}{12} = \frac{\sqrt6 - \sqrt2}{\sqrt6 + \sqrt2}.$$

Le corrigé s'arrête là ; en simplifiant (ajout, pas dans le cours), on obtient $\tan\frac{\pi}{12} = 2 - \sqrt3$.

## Exercice 14 : équations trigonométriques

Voir [[Équation trigonométrique]].

**Résolution d'équations** : pour tous $x, y \in \mathbb R$, avec $k \in \mathbb Z$ :

- $\sin x = \sin y \iff x = y + 2k\pi$ ou $x = \pi - y + 2k\pi$ ;
- $\cos x = \cos y \iff x = y + 2k\pi$ ou $x = -y + 2k\pi$ ;
- $\tan x = \tan y \iff x = y + k\pi$.

### $\sin x + \sin 2x = 0$

$\sin x + 2\sin x\cos x = 0 \iff \sin x\,(1 + 2\cos x) = 0 \iff \sin x = 0$ ou $\cos x = -\frac12$.

- $\sin x = 0 \iff x = k\pi$.
- $\cos\frac\pi3 = \frac12$ et $\cos(\pi - \frac\pi3) = -\cos\frac\pi3$, donc $\cos\frac{2\pi}{3} = -\frac12$ : $x = \frac{2\pi}{3} + 2k\pi$ ou $x = -\frac{2\pi}{3} + 2k\pi$, ou de manière équivalente $x = \frac{4\pi}{3} + 2k\pi$.

$$S = \left\{k\pi,\ \tfrac{2\pi}{3} + 2k\pi,\ \tfrac{4\pi}{3} + 2k\pi : k \in \mathbb Z\right\}.$$

### $\cos x = \sqrt3 \sin x$

**Méthode 1** : si $\cos x = 0$, alors $\sin x = \pm1$ et l'équation donnerait $0 = \pm\sqrt3$, absurde. On peut donc diviser par $\cos x$ :

$$\cos x = \sqrt3 \sin x \iff \tan x = \frac{1}{\sqrt3} = \tan\frac\pi6, \qquad S = \left\{\tfrac\pi6 + k\pi : k \in \mathbb Z\right\}.$$

**Méthode 2** : $\cos x - \sqrt3 \sin x = 0 \iff 2\left(\frac12\cos x - \frac{\sqrt3}{2}\sin x\right) = 0 \iff \cos\frac\pi3\cos x - \sin\frac\pi3\sin x = 0 \iff \cos\left(x + \frac\pi3\right) = \cos\frac\pi2$

$$\iff x + \tfrac\pi3 = \tfrac\pi2 + 2k\pi \text{ ou } x + \tfrac\pi3 = -\tfrac\pi2 + 2k\pi \iff x = \tfrac\pi6 + 2k\pi \text{ ou } x = -\tfrac{5\pi}{6} + 2k\pi,$$

ce qui donne le même ensemble $\left\{\frac\pi6 + k\pi : k \in\mathbb Z\right\}$.

### $\tan 2x = 3\tan x$

Conditions d'existence : $x \ne \frac\pi2 + k\pi$ et $x \ne \frac\pi4 + k\frac\pi2$, $k \in \mathbb Z$. Avec $\tan 2x = \dfrac{2\tan x}{1 - \tan^2 x}$ :

$$\frac{2\tan x}{1-\tan^2 x} = 3\tan x \iff 2\tan x = 3\tan x(1 - \tan^2 x) \iff \tan x\,\big(3\tan^2 x - 1\big) = 0$$

$$\iff \tan x = 0 \text{ ou } \tan x = \sqrt{\tfrac13} \text{ ou } \tan x = -\sqrt{\tfrac13}.$$

- $\tan x = 0 \iff x = k\pi$ ; $\tan x = \frac{1}{\sqrt3} \iff x = \frac\pi6 + k\pi$ ; $\tan x = -\frac{1}{\sqrt3} \iff x = -\frac\pi6 + k\pi$.

$$S = \left\{k\pi,\ \tfrac\pi6 + k\pi,\ -\tfrac\pi6 + k\pi : k \in \mathbb Z\right\}.$$

## Exercices supplémentaires (sans corrigé)

- Résoudre $\dfrac{3}{x-1} \le \dfrac{5}{2x+1}$ et $\dfrac{x^2-6x+8}{x-1} < 0$.
- Calculer $\displaystyle\sum_{k=1}^n 3^k$.
- Résoudre $\cos^2 x - \cos x = 0$, $\tan x = 1$, $\tan\left(\frac\pi4(\sin x + 1)\right) = 1$.

## Pièges mis en avant

- Résoudre sans préciser le domaine (racine, quotient, tangente).
- Diviser par une quantité qui peut s'annuler.
- Multiplier ou soustraire des inégalités sans tenir compte des signes.
- Après élévation au carré, vérifier que les solutions du problème d'origine sont bien conservées.

## Points à vérifier

- Diapositive des conséquences des formules d'addition (exercice 12) : $\sin(x - \pi) = \sin x$ et $\sin(x - \pi/2) = \cos x$ sont faux (il faut $-\sin x$ et $-\cos x$) ; la dernière ligne répète $\cos(x + \pi/2)$ avec deux valeurs différentes, alors qu'il s'agit sans doute de $\cos(x - \pi/2) = \sin x$. Erreurs du cours, signalées sans être corrigées dans le document.
- Remarque de l'exercice 3 : « $1 \le x \le 3$ et $-2 \le y \le -1$ n'implique pas que $-2 \le xy \le -3$ ». L'encadrement cité est vide ($-2 > -3$) ; l'idée est qu'on ne peut pas multiplier les bornes terme à terme (le vrai encadrement est $-6 \le xy \le -1$). Formulation du cours à relire.
- Exercice 11, méthode 2 : l'initialisation est faite pour $n = 2$, mais la diapositive conclut « donc $\mathcal P(1)$ est vraie », et annonce une récurrence « sur $n > 2$ » : incohérence d'indice.
- Exercice 7, somme des carrés : la diapositive écrit $(n+1)^3 = 3\sum_{k=1}^n k^2 + \dots$ puis $\sum_{k=0}^n k^2$ ; le changement de borne est sans effet (le terme $k = 0$ est nul).

## Liens

[[Récurrence]], [[Dénombrement]], [[Norme]].
