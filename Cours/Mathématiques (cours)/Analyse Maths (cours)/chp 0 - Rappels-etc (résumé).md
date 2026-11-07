---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de Chap0-Rappels-etc ([[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]) (PDF de 6 pages, « Chapitre 0 : Rappels et symboles sigma et pi »), dans [[Analyse Maths (index)]]. Le PDF est fait de pages scannées ou collées en image, avec quelques titres en texte : il a été lu sur l'image. Une seule figure (la droite réelle, page 2).

## I. Équations, inéquations, encadrements, valeur absolue, racine carrée

### Équations

- Une **équation** est une égalité avec une inconnue ; la **résoudre**, c'est appliquer des transformations autorisées jusqu'à obtenir $x = \dots$
- Opérations autorisées : ajouter ou soustraire un même nombre, multiplier par un même nombre, diviser par un nombre non nul.
- Équations et inéquations du second degré : signe du trinôme, discriminant ([[Équation du second degré]]).
- Degrés supérieurs : chercher une racine « évidente », puis factoriser ; sinon, étude de fonction.

### Rappels sur les inégalités

Voir [[Règles de calcul sur les inégalités]].

**Théorème.** Soient $a, b, c, d, \lambda \in \mathbb{R}$.
- **Strict / large** : si $a < b$, alors $a \le b$. **La réciproque est fausse.**

Dans les règles suivantes, on peut remplacer les inégalités larges par des inégalités strictes.
- **Somme** : si $a \le b$ et $c \le d$, alors $a + c \le b + d$.
- **Produit** :
  - par un réel positif : si $a \le b$ et $\lambda \ge 0$, alors $\lambda a \le \lambda b$ ;
  - par un réel négatif : si $a \le b$ et $\lambda \le 0$, alors $\lambda a \ge \lambda b$ — **on renverse** ;
  - d'inégalités positives : si $0 \le a \le b$ et $0 \le c \le d$, alors $0 \le ac \le bd$.
- **Passage à l'inverse** : si $a \le b$ et si $a$ et $b$ sont **de même signe**, alors $\dfrac{1}{b} \le \dfrac{1}{a}$.

**Règle** : **majorer** une fraction de réels positifs, c'est majorer son numérateur et **minorer** son dénominateur ; **minorer** une fraction de réels positifs, c'est minorer son numérateur et majorer son dénominateur.

**Exemple 1.** Soit $x \in [1, 2]$ ; encadrer grossièrement $\dfrac{2x+1}{3x^2+4}$.
*Démonstration* : par hypothèse $1 \le x \le 2$, donc $3 \le 2x+1 \le 5$ et $1 \le x^2 \le 4$, puis $7 \le 3x^2 + 4 \le 16$. Par quotient :

$$\frac{3}{16} \le \frac{2x+1}{3x^2+4} \le \frac{5}{7}.$$

**Exemple 2.** Pour tout $x > 0$ : $x + \dfrac{1}{x} \ge 2$.
*Démonstration* : au brouillon, partir du résultat :

$$x + \frac{1}{x} \ge 2 \overset{x>0}{\iff} x^2 + 1 \ge 2x \iff x^2 - 2x + 1 \ge 0 \iff (x-1)^2 \ge 0,$$

ce qui est toujours vrai (un carré est positif). Sur la copie, pour un calcul aussi simple, il vaut mieux partir de la fin : $(x-1)^2 \ge 0$, et en déduire l'inégalité voulue.

**Attention !** Il est **rigoureusement interdit de soustraire** deux inégalités de même sens. Exemple : $0 \le 1$ et $0 \le 2$, mais on ne peut accepter $0 = 0 - 0 \le 1 - 2 = -1$.

### Rappels sur les valeurs absolues

Voir [[Valeur absolue]] et [[Inégalité triangulaire]].

**Définition-théorème.**
- **Définition** : pour $x \in \mathbb{R}$, la *valeur absolue* de $x$ est

$$|x| = \begin{cases} x & \text{si } x \ge 0 \\ -x & \text{si } x < 0. \end{cases}$$

  Ce réel est positif ou nul, et nul seulement si $x = 0$.
- **Interprétation géométrique** : $|x|$ est la distance entre $0$ et $x$ sur la droite réelle. En particulier $-|x| \le x \le |x|$.
- **Somme et produit** : pour tous $x, y \in \mathbb{R}$,

$$|x + y| \le |x| + |y| \quad (\textit{inégalité triangulaire}) \qquad\text{et}\qquad |xy| = |x| \times |y|.$$

**Équivalences à retenir** (très utilisées plus tard, notamment pour les limites) : pour tous $x, a \in \mathbb{R}$, $|x - a|$ est la distance entre $a$ et $x$, donc pour tout $\varepsilon > 0$ :

$$|x - a| \le \varepsilon \iff x \in [a - \varepsilon, a + \varepsilon] \qquad\text{et}\qquad |x - a| < \varepsilon \iff x \in \,]a - \varepsilon, a + \varepsilon[.$$

![[Chap0-Rappels - p2.jpg]]
*Figure : sur la droite réelle, $x$ est à moins de $\varepsilon$ de $a$ quand il est entre $a - \varepsilon$ et $a + \varepsilon$ ; $|x - a|$ est la distance de $a$ à $x$.*

**Attention !** $|x - y| \not\le |x| - |y|$. Dans l'inégalité triangulaire $|x+y| \le |x| + |y|$, quand on remplace $y$ par $-y$, c'est toujours un « $+$ » qu'on trouve à droite : $|x - y| \le |x| + |y|$.

**Exemple 3.** Exprimer $|x-3| - |x+2|$ sans valeur absolue, selon $x$.
*Démonstration* :

$$|x-3| = \begin{cases} x-3 & \text{si } x \ge 3 \\ -(x-3) & \text{si } x < 3 \end{cases} \qquad |x+2| = \begin{cases} x+2 & \text{si } x \ge -2 \\ -(x+2) & \text{si } x < -2 \end{cases}$$

donc on distingue trois intervalles, $]-\infty, -2[$, $[-2, 3[$ et $[3, +\infty[$ :

$$|x-3| - |x+2| = \begin{cases} -(x-3) + (x+2) = 5 & \text{si } x \in \,]-\infty, -2[ \\ -(x-3) - (x+2) = 1 - 2x & \text{si } x \in [-2, 3[ \\ (x-3) - (x+2) = -5 & \text{si } x \in [3, +\infty[. \end{cases}$$

**Exemple 4.** Résoudre $|x - 4| = 2x + 10$, d'inconnue $x \in \mathbb{R}$.
*Démonstration* : pour tout $x$, $|x-4| = x - 4$ si $x \ge 4$, et $4 - x$ si $x < 4$.
- Sur $[4, +\infty[$ : $|x-4| = 2x + 10 \iff x - 4 = 2x + 10 \iff x = -14$ ; or $-14 \notin [4, +\infty[$, donc pas de solution sur cet intervalle.
- Sur $]-\infty, 4[$ : $|x-4| = 2x + 10 \iff 4 - x = 2x + 10 \iff x = -2$, et $-2 \in \,]-\infty, 4[$, donc $-2$ est solution.

Finalement, $-2$ est la seule solution sur $\mathbb{R}$.

### Rappels sur les puissances

**Définition-théorème.**
- Pour $x \in \mathbb{R}$ et $n \in \mathbb{N}$, *$x$ puissance $n$* est $x^n = \underbrace{x \times \dots \times x}_{n \text{ fois}}$, avec $x^0 = 1$ par convention.
- Si $x \ne 0$, *$x$ puissance $-n$* est $x^{-n} = \dfrac{1}{x^n} = \left(\dfrac{1}{x}\right)^n = \underbrace{\dfrac{1}{x} \times \dots \times \dfrac{1}{x}}_{n \text{ fois}}$.
- **Règles de calcul** : pour tous $x, y \in \mathbb{R}$ et $m, n \in \mathbb{N}$,

$$x^{m+n} = x^m x^n, \qquad x^{mn} = (x^m)^n, \qquad (xy)^n = x^n y^n.$$

  Ces formules restent vraies si $m$ ou $n$ est négatif, à condition que $x$ et $y$ soient non nuls.

Il faut surtout **comprendre** ces règles à chaque usage. Par exemple :

$$x^m x^n = \underbrace{x \times \dots \times x}_{m \text{ fois}} \times \underbrace{x \times \dots \times x}_{n \text{ fois}} = \underbrace{x \times \dots \times x}_{m+n \text{ fois}} = x^{m+n},$$

$$(x^m)^n = \underbrace{x^m \times \dots \times x^m}_{n \text{ fois}} = \underbrace{x \times \dots \times x}_{m + \dots + m \text{ fois}} = \underbrace{x \times \dots \times x}_{mn \text{ fois}} = x^{mn}.$$

### Rappels sur les racines carrées

Voir [[Racine carrée]].

**Définition-théorème.**
- **Définition** : soit $x \ge 0$. Il existe un et un seul réel $r \ge 0$ tel que $x = r^2$ ; c'est la *racine carrée* de $x$, notée $\sqrt{x}$.
- **Somme et produit** : pour tous $x, y \ge 0$, $\sqrt{xy} = \sqrt{x} \times \sqrt{y}$, et $\sqrt{x^2} = |x|$.

**Attention !** $(\sqrt{x})^2$ n'est définie que si $x \ge 0$, et alors $(\sqrt{x})^2 = x$ par définition. $\sqrt{x^2}$ est au contraire toujours définie, mais le passage au carré « tue » le signe de $x$ : $\sqrt{x^2} = |x|$. À retenir : en général $\sqrt{x^2} \ne x$. Autre erreur à éviter : $\sqrt{x + y} \ne \sqrt{x} + \sqrt{y}$.

**Attention ! Erreurs graves.** Pour $a, b, x, y \in \mathbb{R}$ :
- $ax = ay \not\Rightarrow x = y$ ;
- $a^2 = b^2 \not\Rightarrow a = b$ ;
- et pour $a \ge 0$ : $x^2 = a \not\Rightarrow x = \sqrt{a}$.

Pour les corriger, un rappel : **un produit est nul si et seulement si l'un de ses facteurs l'est.** Il en découle :

$$ax = ay \iff a(x - y) = 0 \iff a = 0 \text{ ou } x = y,$$

$$a^2 = b^2 \iff (a+b)(a-b) = 0 \iff a = b \text{ ou } a = -b \iff |a| = |b|,$$

$$\text{si } a \ge 0 : \quad x^2 = a \iff (x + \sqrt{a})(x - \sqrt{a}) = 0 \iff x = \sqrt{a} \text{ ou } x = -\sqrt{a}.$$

Version corrigée des règles : pour tous $a, b, x, y \in \mathbb{R}$,

$$ax = ay \iff a = 0 \text{ ou } x = y, \qquad a^2 = b^2 \iff a = b \text{ ou } a = -b \iff |a| = |b|,$$

et pour $a \ge 0$ : $x = \sqrt{a} \iff x^2 = a$ et $x \ge 0$.

**Exemple 5.** Résoudre $|x - 2| = 2|x + 1|$, d'inconnue $x \in \mathbb{R}$ (méthode : élever au carré, licite car $|a| = |b| \iff a^2 = b^2$).

$$|x - 2| = 2|x + 1| \iff (x-2)^2 = 4(x+1)^2 \iff 3x^2 + 12x = 0 \iff x(x + 4) = 0 \iff x \in \{-4, 0\}.$$

(Annotation du cours : « pas de discriminant ! » — on factorise directement.)

### Le principe des substitutions

Voir [[Principe des substitutions]]. Principe fondamental, sans rapport direct avec les inégalités, mais que celles-ci illustrent bien : si une inégalité est vraie « pour **tout** $x \in \mathbb{R}$ », on peut remplacer $x$ par **n'importe quel réel de son choix**, ce qui mène souvent à de nouveaux résultats.

**Exemple.**
- **Point de départ**, l'inégalité triangulaire : pour tous $x, y$, $|x + y| \le |x| + |y|$.
- **Premier rebondissement** : on l'applique à $x$ et $-y$ : $|x + (-y)| \le |x| + |-y|$, donc $|x - y| \le |x| + |y|$. Nouveau résultat.
- **Deuxième rebondissement** : on l'applique à $x + y$ et $-y$ : $|(x+y) + (-y)| \le |x+y| + |-y|$, donc $|x| \le |x+y| + |y|$, puis $|x + y| \ge |x| - |y|$. Encore un nouveau résultat.
- **Rebondissement sur le deuxième** : on vient de montrer $|x + y| \ge |x| - |y|$ pour tous $x, y$, donc aussi $|y + x| \ge |y| - |x|$. Ainsi $|x+y|$ est supérieur ou égal aux deux nombres **opposés** $|x| - |y|$ et $|y| - |x|$, donc à la valeur absolue $\big||x| - |y|\big|$.

D'où l'**inégalité triangulaire généralisée** : pour tous $x, y \in \mathbb{R}$,

$$\big||x| - |y|\big| \le |x + y| \le |x| + |y|.$$

Le cours renvoie au formulaire `00_inegalites.pdf`, non joint.

## II. Formules et équations trigonométriques

Renvoi au formulaire `formtrig.pdf`, non joint au PDF (voir [[Formules trigonométriques]] et [[Équation trigonométrique]]).

## III. Symboles sigma et pi

Voir [[Symboles somme et produit]].

### 1. Sommes et produits

#### 1.1 Définitions et propriétés

**Définition.** Soit $I$ un sous-ensemble fini non vide d'entiers et $(a_i)_{i \in I}$ une famille de nombres réels ou complexes. On note :
- $\displaystyle\sum_{i \in I} a_i$ la somme des éléments de la famille ;
- $\displaystyle\prod_{i \in I} a_i$ leur produit.

Par convention, lorsque $I = \emptyset$ : $\sum_{i \in I} a_i = 0$ et $\prod_{i \in I} a_i = 1$.

**Notations.** Si $I = [\![m, n]\!] = \{m, m+1, \dots, n-1, n\}$ avec $m \le n$ :

$$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + \dots + a_n \;;\qquad \prod_{i=m}^{n} a_i = a_m \times a_{m+1} \times \dots \times a_n$$

(« $m - n + 1$ termes » selon le cours, voir point à vérifier 1).

**Remarque.** L'indice $i$ est **muet** : on peut le remplacer par tout autre symbole non utilisé ailleurs :

$$\sum_{i=m}^{n} a_i = \sum_{j=m}^{n} a_j = \sum_{k=m}^{n} a_k \qquad\text{et}\qquad \prod_{i=m}^{n} a_i = \prod_{j=m}^{n} a_j = \prod_{k=m}^{n} a_k.$$

**Propriété 1 (règles de calcul pour les sommes).** Soient $I$ un sous-ensemble fini non vide d'entiers et $(a_i)_{i\in I}$, $(b_i)_{i\in I}$ deux familles de réels ou complexes.
- $\displaystyle\sum_{i \in I} (a_i + b_i) = \sum_{i \in I} a_i + \sum_{i \in I} b_i$ ;
- pour tout $\lambda$ réel ou complexe, $\displaystyle\sum_{i \in I} (\lambda a_i) = \lambda \sum_{i \in I} a_i$.

**Propriété 2 (règles de calcul pour les produits).** Mêmes hypothèses.
- $\displaystyle\prod_{i \in I} (a_i b_i) = \prod_{i \in I} a_i \times \prod_{i \in I} b_i$ ;
- pour tout $\lambda$ réel ou complexe, $\displaystyle\prod_{i \in I} (\lambda a_i) = \lambda^p \prod_{i \in I} a_i$, où $p$ est le nombre d'éléments de $I$.

#### 1.2 Méthodes de calcul de sommes et de produits

**Sommes et produits télescopiques** ([[Somme télescopique]]) : quand le terme à sommer est de la forme $u_{k+1} - u_k$, les termes s'éliminent deux à deux et il ne reste que le premier et le dernier :

$$\sum_{k=m}^{n} (u_{k+1} - u_k) = u_{n+1} - u_m.$$

De même pour les produits de la forme $\prod \dfrac{u_{k+1}}{u_k}$ :

$$\prod_{k=m}^{n} \frac{u_{k+1}}{u_k} = \frac{u_{n+1}}{u_m}.$$

*Exemples* (énoncés sans correction dans le cours) : calculer

$$S_n = \sum_{k=1}^{n} \frac{1}{k(k+1)} \qquad\text{et}\qquad P_n = \prod_{k=2}^{n} \left(1 - \frac{1}{k}\right).$$

**Changement d'indice** ([[Changement d'indice]]) : on définit le nouvel indice en fonction de l'ancien, puis on réécrit la somme avec ce nouvel indice, en changeant **les bornes** et **le terme** sous la somme.
*Exemple* (sans correction) : avec $j = n - k$, retrouver la valeur de $S_n = \displaystyle\sum_{k=1}^{n} k$ ([[Somme des premiers entiers]]).

**Regroupement de termes** : on décompose la somme en plusieurs sommes plus simples.
*Exemple* (sans correction) : calculer $S_n = \displaystyle\sum_{k=0}^{2n} \min(k, n)$, où $\min(k, n)$ est le plus petit des entiers $k$ et $n$.

### 2. Coefficients binomiaux et formule du binôme

#### 2.1 Coefficients binomiaux

Voir [[Factorielle]] et [[Coefficient binomial]].

**Définition.** Pour $n \in \mathbb{N}$, la **factorielle** de $n$ est l'entier $n! = \displaystyle\prod_{k=1}^{n} k$.

**Remarque.** $0! = 1$, et si $n \ge 1$, $n! = n \times (n-1)!$.

**Définition.** Pour $n \in \mathbb{N}$ et $p \in \mathbb{Z}$ :

$$\binom{n}{p} = \begin{cases} \dfrac{n!}{p!\,(n-p)!} & \text{si } p \in [\![0, n]\!] \\[2mm] 0 & \text{si } p > n \text{ ou } p < 0. \end{cases}$$

$\binom{n}{p}$ est le **coefficient binomial** et se lit « $p$ parmi $n$ ».

**Propriété 9 (relations sur les coefficients binomiaux).** Soit $n$ un entier naturel non nul.
1. Pour tout $p \in [\![0, n]\!]$, $\binom{n}{p} = \binom{n}{n-p}$ (symétrie).
2. Pour tout $p \in [\![1, n]\!]$, $p \binom{n}{p} = n \binom{n-1}{p-1}$.
3. Pour tout $p \in [\![1, n-1]\!]$, $\binom{n}{p} = \binom{n-1}{p-1} + \binom{n-1}{p}$ (formule du triangle de Pascal, [[Formule de Pascal]]).

**Remarque : le triangle de Pascal.** La dernière relation permet de construire rapidement les premiers coefficients :

| | $p=0$ | $p=1$ | $p=2$ | $p=3$ | $p=4$ |
|---|---|---|---|---|---|
| $n=0$ | 1 | | | | |
| $n=1$ | 1 | 1 | | | |
| $n=2$ | 1 | 2 | 1 | | |
| $n=3$ | 1 | 3 | 3 | 1 | |
| $n=4$ | 1 | 4 | 6 | 4 | 1 |

Chaque coefficient de la ligne $n+1$ est la somme des deux coefficients de la ligne $n$ situés au-dessus : $\binom{n+1}{p+1} = \binom{n}{p} + \binom{n}{p+1}$.

**Remarque : $\binom{n}{p}$ est un entier.** Grâce à la formule de Pascal, pour tout $(n, p) \in \mathbb{N}^2$ avec $p \le n$, $\binom{n}{p} \in \mathbb{N}$. Par [[Récurrence]] sur $n$ :
- *Initialisation* : pour $n = 0$, $p = 0$, $\binom{0}{0} = 1 \in \mathbb{N}$.
- *Hérédité* : soit $n \in \mathbb{N}$ tel que $\forall p \in [\![0, n]\!]$, $\binom{n}{p} \in \mathbb{N}$. Soit $p \in [\![0, n+1]\!]$. Si $p = n+1$, $\binom{n+1}{p} = 1 \in \mathbb{N}$. Si $p \le n$,

$$\binom{n+1}{p} = \binom{n}{p} + \binom{n}{p-1} \in \mathbb{N}$$

  par hypothèse de récurrence.
- *Conclusion* : par principe de récurrence, $\binom{n}{p} \in \mathbb{N}$ pour tout $(n, p) \in \mathbb{N}^2$ avec $p \le n$.

#### 2.2 Formule du binôme de Newton

**Théorème 10 (formule du binôme de Newton).** Soient $a$ et $b$ deux réels et $n$ un entier naturel :

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}.$$

*Preuve* : par récurrence sur $n \in \mathbb{N}$ (non détaillée). Voir [[Formule du binôme de Newton]].

**Exemples.**
- Pour $a = b = 1$ : $2^n = \displaystyle\sum_{k=0}^{n} \binom{n}{k}$.
- Pour $a = 1$ et $b = -1$ : $0 = \displaystyle\sum_{k=0}^{n} (-1)^k \binom{n}{k}$ (pour $n \ge 1$, voir point à vérifier 3).

## Liens

[[Récurrence]], [[Dénombrement]] (coefficients binomiaux), [[Norme]] (la valeur absolue en est le cas réel).

## Points à vérifier

1. **Nombre de termes** : le cours écrit « $(m - n + 1$ termes$)$ » pour $\sum_{i=m}^{n}$ ; il y en a $n - m + 1$ (coquille du cours, non corrigée dans la source).
2. **Formulaires absents** : `00_inegalites.pdf` et `formtrig.pdf` sont cités mais ne sont pas dans le PDF ; la partie II est donc vide.
3. **Exemple $a = 1, b = -1$** : $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$ n'est vrai que pour $n \ge 1$ ; pour $n = 0$ la somme vaut $1$ (complément).
4. **Hérédité de la récurrence** : pour $p = 0$, la formule utilise $\binom{n}{-1}$, qui vaut $0$ par la définition étendue à $p \in \mathbb{Z}$ ; la formule de Pascal n'est énoncée dans la propriété 9 que pour $p \in [\![1, n-1]\!]$ (complément).
5. **Exemples de la partie III** (télescopage, changement d'indice, regroupement) : énoncés sans correction dans le document.
6. **Numérotation** : la section « 4 Le principe des substitutions » et la « Propriété 9 » / « Théorème 10 » suggèrent que les pages viennent de plusieurs documents assemblés ; la numérotation n'est pas continue.
