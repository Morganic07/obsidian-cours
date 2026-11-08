---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chp4 - dérivabilité.docx|Chp4 - dérivabilité]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Analyse Maths/Cours/Chp4 - dérivabilité.docx|Chp4 - dérivabilité]], dans [[Cours/Mathématiques/Analyse Maths/_index|Analyse Maths]] : dérivabilité en un point, opérations sur les dérivées, classes $\mathcal{C}^n$, extremums, théorème de Rolle, accroissements finis, fonctions lipschitziennes et règle de l'Hôpital.

## La base

### Dérivabilité en un point

$f$ est **[[Dérivabilité|dérivable]] en $a$** si la limite du taux d'accroissement

$$\lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

**existe et est finie**. Cette limite est notée $f'(a)$.

Le quotient $\frac{f(x) - f(a)}{x - a}$ est la pente de la corde (ou sécante) qui joint les points $(a, f(a))$ et $(x, f(x))$ de la courbe ; $f'(a)$ est la limite de ces pentes quand $x$ se rapproche de $a$, c'est-à-dire la pente de la tangente. En physique, c'est le passage de la vitesse moyenne à la vitesse instantanée. On écrit souvent la même limite avec $x = a + h$ : $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$. [[Complément hors du cours|ⓘ]]

Formulation équivalente : $f$ est dérivable en $a$ si et seulement si $f(a + h) = f(a) + f'(a)\,h + o(h)$ quand $h \to 0$ : près de $a$, $f$ ressemble à la fonction affine de sa tangente, à une erreur négligeable devant $h$ près (c'est le $DL_1(a)$ du [[5 - Analyse Maths|chapitre 5]]). [[Complément hors du cours|ⓘ]]

| Notion | Condition | Notation |
|---|---|---|
| $f$ dérivable à gauche en $a$ | $\lim_{x \to a^-} \frac{f(x) - f(a)}{x - a}$ existe et est finie | $f'_g(a)$ |
| $f$ dérivable à droite en $a$ | $\lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}$ existe et est finie | $f'_d(a)$ |

- $f$ dérivable en $a$ $\Leftrightarrow$ $f'_g(a) = f'_d(a)$ (les deux [[Limite et continuité|limites]] existant et étant finies).
- $f$ dérivable sur $I$ $\Rightarrow$ $f$ continue sur $I$ (la réciproque est fausse).
- $D(I, \mathbb{R})$ : ensemble des fonctions dérivables sur $I$ à valeurs dans $\mathbb{R}$.

Pourquoi dérivable implique continue : pour $x \ne a$, $f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \times (x - a)$, produit d'un terme qui tend vers $f'(a)$ et d'un terme qui tend vers 0, donc $f(x) \to f(a)$. Contre-exemple de la réciproque : $x \mapsto |x|$ est continue en 0, mais $f'_g(0) = -1 \ne f'_d(0) = 1$ (point anguleux), donc elle n'est pas dérivable en 0. [[Complément hors du cours|ⓘ]]

### Tangente

| Situation | [[Tangente à une courbe\|Tangente]] en $a$ |
|---|---|
| $f$ dérivable en $a$ | $T_a : y = f(a) + f'(a)(x - a)$ |
| $\lim_{x \to a} \frac{f(x) - f(a)}{x - a} = \pm\infty$ | tangente verticale $T_a : x = a$ |

Exemple de tangente verticale : $x \mapsto \sqrt{x}$ en 0, car $\frac{\sqrt{x} - 0}{x - 0} = \frac{1}{\sqrt{x}} \to +\infty$ quand $x \to 0^+$. La fonction est continue en 0 mais pas dérivable, d'où la condition $x > 0$ pour la dérivée $\frac{1}{2\sqrt{x}}$ ci-dessous. [[Complément hors du cours|ⓘ]]

## Opérations

### Dérivées usuelles

Tableau du cours, avec la version [[Composition de fonctions|composée]] avec une fonction $u$ :

| Fonction | Dérivée | Fonction composée | Dérivée |
|---|---|---|---|
| $x^n$ | $nx^{n-1}$ ($n \in \mathbb{Z}$) | $u^n$ | $nu'u^{n-1}$ ($n \in \mathbb{Z}$) |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ | $\frac{1}{u}$ | $-\frac{u'}{u^2}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ | $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ |
| $x^\alpha$ | $\alpha x^{\alpha-1}$ ($\alpha \in \mathbb{R}$) | $u^\alpha$ | $\alpha u'u^{\alpha-1}$ ($\alpha \in \mathbb{R}$) |
| $e^x$ | $e^x$ | $e^u$ | $u'e^u$ |
| $\ln x$ | $\frac{1}{x}$ | $\ln u$ | $\frac{u'}{u}$ |
| $\cos x$ | $-\sin x$ | $\cos u$ | $-u'\sin u$ |
| $\sin x$ | $\cos x$ | $\sin u$ | $u'\cos u$ |
| $\tan x$ | $1 + \tan^2 x = \frac{1}{\cos^2 x}$ | $\tan u$ | $u'(1 + \tan^2 u) = \frac{u'}{\cos^2 u}$ |

Le tableau ne donne pas les [[Fonctions trigonométriques réciproques|fonctions trigonométriques réciproques]], qui s'obtiennent avec la règle de la réciproque ci-dessous : [[Complément hors du cours|ⓘ]]
- $\arcsin' x = \dfrac{1}{\sqrt{1 - x^2}}$ et $\arccos' x = -\dfrac{1}{\sqrt{1 - x^2}}$ sur $]-1, 1[$ (pas dérivables en $\pm 1$, tangentes verticales) ; [[Complément hors du cours|ⓘ]]
- $\arctan' x = \dfrac{1}{1 + x^2}$ sur $\mathbb{R}$. Par exemple, $\tan$ ayant pour dérivée $1 + \tan^2$, on a $\arctan'(x) = \dfrac{1}{1 + \tan^2(\arctan x)} = \dfrac{1}{1 + x^2}$. [[Complément hors du cours|ⓘ]]

### Règles de calcul

Soient $u$ et $v$ dérivables sur $I$, à valeurs dans $\mathbb{R}$.

| Opération | Règle |
|---|---|
| [[Combinaison linéaire]] | $(\alpha u + \beta v)' = \alpha u' + \beta v'$ |
| Produit | $(uv)' = u'v + uv'$ |
| Quotient | si $v$ ne s'annule pas : $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ |
| Composition | $(u \circ v)' = v' \cdot (u' \circ v)$ [[Erreurs du cours#^e-4-derivabilite\|✎]] |
| Réciproque | $f \in D(I, \mathbb{R})$ bijective de $I$ sur $f(I)$ ; si $f'$ ne s'annule pas : $(f^{-1})' = \frac{1}{f' \circ f^{-1}}$ [[Erreurs du cours#^e-4-derivabilite\|✎]] |
| Dérivée successive | si $u, v \in \mathcal{C}^n(I, \mathbb{R})$, alors $\alpha u + \beta v \in \mathcal{C}^n(I, \mathbb{R})$ et $(\alpha u + \beta v)^{(n)} = \alpha u^{(n)} + \beta v^{(n)}$ |

Exemple de [[Dérivation en chaîne|composition]] : pour $f(x) = \sin(x^2)$, on prend $v(x) = x^2$ et $u = \sin$, d'où $f'(x) = v'(x)\, u'(v(x)) = 2x \cos(x^2)$. La formule de la réciproque se retrouve en dérivant l'identité $f(f^{-1}(y)) = y$ : $(f^{-1})'(y) \times f'(f^{-1}(y)) = 1$. [[Complément hors du cours|ⓘ]]

## Dérivées successives, fonctions de classe $\mathcal{C}^n$

- Notations : $f^{(0)} = f$, $f^{(1)} = f'$, $f^{(2)} = f''$, etc.
- $f$ est **de [[Fonction de classe Ck|classe $\mathcal{C}^n$]]** sur $I$ si $f$ est **$n$ fois dérivable** sur $I$ **et** $f^{(n)}$ **est continue** sur $I$.
- $f$ est de classe $\mathcal{C}^\infty$ si elle est infiniment dérivable sur $I$.
- Attention : classe $\mathcal{C}^1$ ≠ « dérivable et continue » ; classe $\mathcal{C}^1$ = « **dérivable à dérivée continue** ».
- $\mathcal{C}^n(I, \mathbb{R})$ : ensemble des fonctions de classe $\mathcal{C}^n$ sur $I$ à valeurs dans $\mathbb{R}$.
- Exemple classique d'une fonction dérivable mais pas $\mathcal{C}^1$ : $f(x) = x^2 \sin\frac{1}{x}$ pour $x \ne 0$, $f(0) = 0$. Le taux d'accroissement en 0 vaut $x \sin\frac{1}{x} \to 0$, donc $f'(0) = 0$ ; mais pour $x \ne 0$, $f'(x) = 2x\sin\frac{1}{x} - \cos\frac{1}{x}$ n'a pas de limite en 0, donc $f'$ n'est pas continue en 0. [[Complément hors du cours|ⓘ]]
- Exemples : les polynômes, $\exp$, $\sin$, $\cos$ sont $\mathcal{C}^\infty$ sur $\mathbb{R}$, $\ln$ l'est sur $]0, +\infty[$ ; $x \mapsto x|x|$ est $\mathcal{C}^1$ mais pas deux fois dérivable en 0 (sa dérivée est $2|x|$). [[Complément hors du cours|ⓘ]]

Chaîne d'implications du cours :

$$\mathcal{C}^\infty \Rightarrow \dots \Rightarrow \mathcal{C}^2 \Rightarrow \text{deux fois dérivable} \Rightarrow \mathcal{C}^1 \Rightarrow \text{dérivable} \Rightarrow \text{continue} = \mathcal{C}^0$$

### Stabilité de la classe $\mathcal{C}^n$

- **[[Formule de Leibniz]]** : soient $n \in \mathbb{N}$ et $f, g : I \to \mathbb{R}$ de classe $\mathcal{C}^n$ sur $I$. Alors $fg$ est de classe $\mathcal{C}^n$ sur $I$ et
$$(fg)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)} g^{(n-k)}.$$
- **Quotient** : soient $f, g : I \to \mathbb{R}$ de classe $\mathcal{C}^n$. Si $g$ ne s'annule pas, $\frac{f}{g}$ est $\mathcal{C}^n$ sur $I$.
- **Composée** : soient $f : I \to \mathbb{R}$ et $g : J \to \mathbb{R}$ de classe $\mathcal{C}^n$, avec $f(I) \subset J$. Alors $g \circ f$ est de classe $\mathcal{C}^n$ sur $I$.
- **Réciproque** : soit $f : I \to J$ [[Bijection|bijective]], de classe $\mathcal{C}^n$ sur $I$, telle que $f'$ ne s'annule pas. Alors $f^{-1}$ est de classe $\mathcal{C}^n$ sur $J$.

## Propriétés des fonctions dérivables

### Extremums locaux

| [[Extremum local]] | Définition (il existe $\eta > 0$ tel que…) |
|---|---|
| Maximum local en $a$ | $\forall x \in I \cap [a - \eta, a + \eta],\ f(x) \le f(a)$ |
| Minimum local en $a$ | $\forall x \in I \cap [a - \eta, a + \eta],\ f(a) \le f(x)$ |

- Si $f$ admet un extremum local en $a$, **$a$ n'étant pas une extrémité de $I$**, alors $f'(a) = 0$.
- $f'(a) = 0$ **n'implique pas** que $a$ soit un extremum local.
- Pourquoi $f'(a) = 0$ en un maximum local intérieur : pour $x$ proche de $a$, $f(x) - f(a) \le 0$, donc le taux d'accroissement est $\ge 0$ à gauche ($x - a < 0$) et $\le 0$ à droite ; en passant à la limite, $f'_g(a) \ge 0$ et $f'_d(a) \le 0$, et comme les deux sont égaux à $f'(a)$, $f'(a) = 0$. Au bord de $I$, on n'a qu'un côté, d'où l'exception : $x \mapsto x$ sur $[0, 1]$ a un minimum en 0 avec une dérivée égale à 1. [[Complément hors du cours|ⓘ]]
- Contre-exemple de la réciproque : $x \mapsto x^3$ a une dérivée nulle en 0, mais elle est strictement croissante, donc 0 n'est pas un extremum ; on parle de point d'inflexion à tangente horizontale. Un point où $f'(a) = 0$ s'appelle un **point critique**. [[Complément hors du cours|ⓘ]]
- Critère du second ordre : si $f$ est deux fois dérivable, $f'(a) = 0$ et $f''(a) > 0$, alors $a$ est un minimum local strict ($f''(a) < 0$ : maximum local strict). Si $f''(a) = 0$, on ne peut pas conclure ($x^3$, $x^4$, $-x^4$ en 0). [[Complément hors du cours|ⓘ]]

**Procédure pour déterminer les extremums de $f$ :**
1. Résoudre $f'(x) = 0$ pour $x$ qui n'est pas une extrémité de $I$, puis vérifier que les $x$ trouvés sont bien des extremums locaux (avec le [[Monotonie et signe de la dérivée|tableau de variation]]).
2. Étudier séparément si les extrémités de $I$ sont des extremums locaux.

### Théorème de Rolle

**[[Théorème de Rolle]]** : soit $f : [a, b] \to \mathbb{R}$ **continue** sur $[a, b]$, **dérivable** sur $]a, b[$, avec **$f(a) = f(b)$**. Alors [[Erreurs du cours#^e-4-derivabilite|✎]]
$$\exists c \in\, ]a, b[,\ f'(c) = 0$$

![[Chp4 - dérivabilité - image12.png]]
*Figure : quatre situations autour du théorème de Rolle. 1. Cas standard ($f(a) = f(b)$, tangente horizontale entre $a$ et $b$). 2. Sans dérivabilité en un seul point (point anguleux), plus de tangente horizontale. 3. Sans continuité au bord (saut en $a$), « encore pire ». 4. Si $f(a) \ne f(b)$, « toujours la cata ».*

Le point $c$ est **strictement** entre $a$ et $b$ : $f$ n'est supposée dérivable que sur $]a, b[$. Idée de la preuve : $f$ est continue sur le segment $[a, b]$, donc elle y atteint un maximum et un minimum ([[Théorème des bornes atteintes]]). Si les deux sont atteints aux bornes, ils valent $f(a) = f(b)$ et $f$ est constante, donc $f' = 0$ partout. Sinon, l'un d'eux est atteint en un point $c$ intérieur, qui est un extremum local, d'où $f'(c) = 0$ (paragraphe précédent). [[Complément hors du cours|ⓘ]]

### Théorème des accroissements finis

Soit $f : [a, b] \to \mathbb{R}$ **continue** sur $[a, b]$ et **dérivable** sur $]a, b[$. Alors [[Erreurs du cours#^e-4-derivabilite|✎]]
$$\exists c \in\, ]a, b[,\ f'(c) = \frac{f(b) - f(a)}{b - a} \iff f'(c)(b - a) = f(b) - f(a).$$

Conséquence : toute majoration ou minoration de $f'$ peut être convertie en majoration ou minoration de $f$.

Interprétation : il existe un point (là aussi dans $]a, b[$) où la tangente est parallèle à la corde qui joint $(a, f(a))$ et $(b, f(b))$ ; en cinématique, une voiture qui a roulé en moyenne à 90 km/h a roulé exactement à 90 km/h à au moins un instant. Preuve : on applique le théorème de Rolle à $g(x) = f(x) - \frac{f(b) - f(a)}{b - a}(x - a)$, qui vérifie $g(a) = g(b) = f(a)$ ; $g'(c) = 0$ donne le résultat. Rolle est le cas particulier $f(a) = f(b)$. [[Complément hors du cours|ⓘ]]

### Sens de variation et dérivabilité

Soit $f : I \to \mathbb{R}$ dérivable sur $I$ :
- $f$ constante sur $I$ $\Leftrightarrow$ $f'$ nulle sur $I$ ;
- $f$ croissante sur $I$ $\Leftrightarrow$ $f'$ positive sur $I$ ;
- $f$ décroissante sur $I$ $\Leftrightarrow$ $f'$ négative sur $I$ ;
- si $f' > 0$ sur $I$, alors $f$ est strictement croissante (de même avec $f' < 0$ et strictement décroissante) ; la réciproque est fausse : $x \mapsto x^3$ est strictement croissante et sa dérivée s'annule en 0. [[Erreurs du cours#^e-4-derivabilite|✎]]

Ces équivalences se démontrent avec les accroissements finis : si $f' \ge 0$ et $x < y$ dans $I$, il existe $c$ entre $x$ et $y$ tel que $f(y) - f(x) = f'(c)(y - x) \ge 0$. L'hypothèse « $I$ intervalle » est indispensable : $x \mapsto \frac{1}{x}$ a une dérivée strictement négative sur $\mathbb{R}^*$ mais n'est pas décroissante sur $\mathbb{R}^*$ ($-1 < 1$ et pourtant $f(-1) = -1 < f(1) = 1$). [[Complément hors du cours|ⓘ]]

### Inégalité des accroissements finis

Soit $f : [a, b] \to \mathbb{R}$ continue sur $[a, b]$ et dérivable sur $]a, b[$.
- S'il existe $(m, M) \in \mathbb{R}^2$ tel que $\forall x \in\, ]a, b[,\ m \le f'(x) \le M$, alors
$$m(b - a) \le f(b) - f(a) \le M(b - a).$$
- S'il existe $M \ge 0$ tel que $\forall x \in\, ]a, b[,\ |f'(x)| \le M$, alors
$$|f(b) - f(a)| \le M(b - a).$$

Voir [[Inégalité des accroissements finis]].

### Fonctions lipschitziennes

Soit $f : I \to \mathbb{R}$ et $k \ge 0$. $f$ est **$k$-[[Application lipschitzienne|lipschitzienne]]** sur $I$ $\Leftrightarrow$
$$\forall (x, y) \in I^2,\ |f(x) - f(y)| \le k|x - y|.$$

Lien avec ce qui précède : si $f$ est dérivable sur l'intervalle $I$ avec $|f'| \le k$, l'inégalité des accroissements finis appliquée entre $x$ et $y$ montre que $f$ est $k$-lipschitzienne. Exemple : $\sin$ est 1-lipschitzienne sur $\mathbb{R}$ car $|\cos| \le 1$, d'où $|\sin x - \sin y| \le |x - y|$ et $|\sin x| \le |x|$. [[Complément hors du cours|ⓘ]]

Une fonction lipschitzienne est continue, et même [[Continuité uniforme|uniformément continue]] : si $|x - y| < \frac{\varepsilon}{k}$, alors $|f(x) - f(y)| < \varepsilon$. La réciproque est fausse : $\sqrt{\cdot}$ est continue sur $[0, 1]$ mais pas lipschitzienne (son taux d'accroissement en 0 tend vers $+\infty$). [[Complément hors du cours|ⓘ]]

Quand $k < 1$, on parle de fonction **contractante** : c'est l'outil standard pour montrer qu'une suite récurrente $u_{n+1} = f(u_n)$ converge vers un [[Point fixe|point fixe]] $\ell$ de $f$, car $|u_{n+1} - \ell| = |f(u_n) - f(\ell)| \le k|u_n - \ell|$, donc $|u_n - \ell| \le k^n |u_0 - \ell| \to 0$ (à condition que l'intervalle soit stable par $f$). [[Complément hors du cours|ⓘ]]

### Règle de l'Hôpital

**[[Règle de l'Hôpital]]** : soient $f, g : I \to \mathbb{R}$ deux fonctions dérivables et $x_0 \in I$. On suppose que
- $f(x_0) = g(x_0) = 0$,
- $\forall x \in I \setminus \{x_0\},\ g'(x) \ne 0$.

Si $\lim_{x \to x_0} \frac{f'(x)}{g'(x)} = \ell$ ($\ell \in \mathbb{R}$), alors $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \ell$.

Elle sert à lever les [[Forme indéterminée|formes indéterminées]] « $\frac{0}{0}$ ». Exemple : $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ ; on dérive en haut et en bas, $\frac{\sin x}{2x} \to \frac{1}{2}$, donc la limite vaut $\frac{1}{2}$. Si le nouveau quotient est encore indéterminé, on peut réappliquer la règle. [[Complément hors du cours|ⓘ]]

Deux précautions : on dérive le numérateur et le dénominateur **séparément** (ce n'est pas la dérivée du quotient), et la réciproque est fausse, la limite de $\frac{f}{g}$ pouvant exister sans celle de $\frac{f'}{g'}$. Dans les cas simples, $\frac{f(x)}{g(x)} = \frac{(f(x) - f(x_0))/(x - x_0)}{(g(x) - g(x_0))/(x - x_0)} \to \frac{f'(x_0)}{g'(x_0)}$ si $g'(x_0) \ne 0$ : la règle n'est alors qu'un quotient de taux d'accroissement. [[Complément hors du cours|ⓘ]]