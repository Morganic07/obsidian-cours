---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chp4 - dérivabilité.docx|Chp4 - dérivabilité]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 1/Analyse Maths/Cours/Chp4 - dérivabilité.docx|Chp4 - dérivabilité]], dans [[Analyse Maths (matière)]] : dérivabilité en un point, opérations sur les dérivées, classes $\mathcal{C}^n$, extremums, théorème de Rolle, accroissements finis, fonctions lipschitziennes et règle de l'Hôpital. En cas d'écart, le cours et ses images font foi.

## La base

### Dérivabilité en un point

$f$ est **[[Dérivabilité|dérivable]] en $a$** si la limite du taux d'accroissement

$$\lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

**existe et est finie**. Cette limite est notée $f'(a)$.

| Notion | Condition | Notation |
|---|---|---|
| $f$ dérivable à gauche en $a$ | $\lim_{x \to a^-} \frac{f(x) - f(a)}{x - a}$ existe et est finie | $f'_g(a)$ |
| $f$ dérivable à droite en $a$ | $\lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}$ existe et est finie | $f'_d(a)$ |

- $f$ dérivable en $a$ $\Leftrightarrow$ $f'_g(a) = f'_d(a)$ (les deux [[Limite et continuité|limites]] existant et étant finies).
- $f$ dérivable sur $I$ $\Rightarrow$ $f$ continue sur $I$ (la réciproque est fausse).
- $D(I, \mathbb{R})$ : ensemble des fonctions dérivables sur $I$ à valeurs dans $\mathbb{R}$.

### Tangente

| Situation | [[Tangente à une courbe\|Tangente]] en $a$ |
|---|---|
| $f$ dérivable en $a$ | $T_a : y = f(a) + f'(a)(x - a)$ |
| $\lim_{x \to a} \frac{f(x) - f(a)}{x - a} = \pm\infty$ | tangente verticale $T_a : x = a$ |

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

### Règles de calcul

Soient $u$ et $v$ dérivables sur $I$, à valeurs dans $\mathbb{R}$.

| Opération | Règle |
|---|---|
| [[Combinaison linéaire]] | $(\alpha u + \beta v)' = \alpha u' + \beta v'$ |
| Produit | $(uv)' = u'v + uv'$ |
| Quotient | si $v$ ne s'annule pas : $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ |
| Composition | $(u \circ v)' = v' \cdot (u' \circ v)$ (voir Points à vérifier, 4) |
| Réciproque | $f \in D(I, \mathbb{R})$ bijective de $I$ sur $f(I)$ ; si $f'$ ne s'annule pas : $(f^{-1})' = \frac{1}{f' \circ f^{-1}}$ (voir Points à vérifier, 2) |
| Dérivée successive | si $u, v \in \mathcal{C}^n(I, \mathbb{R})$, alors $\alpha u + \beta v \in \mathcal{C}^n(I, \mathbb{R})$ et $(\alpha u + \beta v)^{(n)} = \alpha u^{(n)} + \beta v^{(n)}$ |

## Dérivées successives, fonctions de classe $\mathcal{C}^n$

- Notations : $f^{(0)} = f$, $f^{(1)} = f'$, $f^{(2)} = f''$, etc.
- $f$ est **de [[Fonction de classe Ck|classe $\mathcal{C}^n$]]** sur $I$ si $f$ est **$n$ fois dérivable** sur $I$ **et** $f^{(n)}$ **est continue** sur $I$.
- $f$ est de classe $\mathcal{C}^\infty$ si elle est infiniment dérivable sur $I$.
- Attention : classe $\mathcal{C}^1$ ≠ « dérivable et continue » ; classe $\mathcal{C}^1$ = « **dérivable à dérivée continue** ».
- $\mathcal{C}^n(I, \mathbb{R})$ : ensemble des fonctions de classe $\mathcal{C}^n$ sur $I$ à valeurs dans $\mathbb{R}$.

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

**Procédure pour déterminer les extremums de $f$ :**
1. Résoudre $f'(x) = 0$ pour $x$ qui n'est pas une extrémité de $I$, puis vérifier que les $x$ trouvés sont bien des extremums locaux (avec le [[Monotonie et signe de la dérivée|tableau de variation]]).
2. Étudier séparément si les extrémités de $I$ sont des extremums locaux.

### Théorème de Rolle

**[[Théorème de Rolle]]** : soit $f : [a, b] \to \mathbb{R}$ **continue** sur $[a, b]$, **dérivable** sur $]a, b[$, avec **$f(a) = f(b)$**. Alors
$$\exists c \in [a, b],\ f'(c) = 0$$
(le cours écrit $[a, b]$ : voir Points à vérifier, 3).

![[Chp4 - dérivabilité - image12.png]]
*Figure : quatre situations autour du théorème de Rolle. 1. Cas standard ($f(a) = f(b)$, tangente horizontale entre $a$ et $b$). 2. Sans dérivabilité en un seul point (point anguleux), plus de tangente horizontale. 3. Sans continuité au bord (saut en $a$), « encore pire ». 4. Si $f(a) \ne f(b)$, « toujours la cata ».*

### Théorème des accroissements finis

Soit $f : [a, b] \to \mathbb{R}$ **continue** sur $[a, b]$ et **dérivable** sur $]a, b[$. Alors
$$\exists c \in [a, b],\ f'(c) = \frac{f(b) - f(a)}{b - a} \iff f'(c)(b - a) = f(b) - f(a).$$

Conséquence : toute majoration ou minoration de $f'$ peut être convertie en majoration ou minoration de $f$.

### Sens de variation et dérivabilité

Soit $f : I \to \mathbb{R}$ dérivable sur $I$ :
- $f$ constante sur $I$ $\Leftrightarrow$ $f'$ nulle sur $I$ ;
- $f$ croissante sur $I$ $\Leftrightarrow$ $f'$ positive sur $I$ (« pareil avec strictement », selon le cours : voir Points à vérifier, 1) ;
- $f$ décroissante sur $I$ $\Leftrightarrow$ $f'$ négative sur $I$ (idem).

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

### Règle de l'Hôpital

**[[Règle de l'Hôpital]]** : soient $f, g : I \to \mathbb{R}$ deux fonctions dérivables et $x_0 \in I$. On suppose que
- $f(x_0) = g(x_0) = 0$,
- $\forall x \in I \setminus \{x_0\},\ g'(x) \ne 0$.

Si $\lim_{x \to x_0} \frac{f'(x)}{g'(x)} = \ell$ ($\ell \in \mathbb{R}$), alors $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \ell$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« f croissante ⇔ f' positive (pareil avec strictement) »** : faux pour le cas strict. $x^3$ est strictement croissante, alors que sa dérivée s'annule en 0. Seul $f' > 0 \Rightarrow$ strictement croissante est vrai. De plus, ces équivalences demandent que $I$ soit un intervalle (complément). **À corriger avant un examen.**
2. **Réciproque** : le tableau écrit « si $f$ ne s'annule pas ». Il faut $f'$, comme dans le théorème en image de la même note.
3. **Rolle et accroissements finis** : le cours écrit $c \in [a, b]$. Le théorème usuel donne $c \in \,]a, b[$, ce qui est plus fort (complément).
4. **Composition** : le tableau écrit $u \circ v = u(v(x)) = v'(u' \circ v)$. Il faut lire $(u \circ v)' = v'(u' \circ v)$.
5. **Hypothèse de continuité** : le cours écrit « $f : [a ; b] \to \mathbb{R}$, continue et dérivable sur $]a ; b[$ » pour Rolle et les accroissements finis ; l'énoncé usuel demande la continuité sur le segment fermé $[a, b]$, comme le montre la figure 3 (discontinuité au bord). La fiche l'écrit ainsi (complément).
6. **Lipschitz** : la note donne la définition, mais ne fait pas le lien explicite avec l'inégalité des accroissements finis ($|f'| \le k$ sur un intervalle $\Rightarrow$ $f$ $k$-lipschitzienne), qui en est la conséquence usuelle (complément, absent du cours).
