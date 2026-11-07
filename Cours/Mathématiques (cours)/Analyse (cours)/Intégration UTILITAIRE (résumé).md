---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse/chp7/Intégration UTILITAIRE .docx|Intégration UTILITAIRE]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Analyse/chp7/Intégration UTILITAIRE .docx|Intégration UTILITAIRE]], dans [[Analyse (index)]]. Fiche pratique sur l'[[Intégrale]], sans preuves : elle reprend les énoncés utiles de [[chp 7 - Integration (résumé)|Chap7-Integration]] (voir aussi [[chp 7 - Integration (résumé)]]) et ajoute une primitive en $u'\ln u$ et les [[Intégrales de Wallis]]. En cas d'écart, le cours et ses images font foi.

La note ne contient aucune figure : toutes ses images sont des énoncés, recopiés ici.

## Propriétés de l'intégrale

**Linéarité.** Pour $f, g : [a,b] \to \mathbb{R}$ continues et $(\lambda, \mu) \in \mathbb{R}^2$ :
$$\int_{[a,b]} (\lambda f + \mu g) = \lambda \int_{[a,b]} f + \mu \int_{[a,b]} g.$$

**[[Relation de Chasles]].** Pour $f : [a,b] \to \mathbb{R}$ continue et $c \in [a,b]$ :
$$\int_{[a,b]} f = \int_{[a,c]} f + \int_{[c,b]} f.$$

**Positivité, croissance, majorations.** Soient $f, g : I \to \mathbb{R}$ continues sur un intervalle $I$ et $a, b \in I$.
1. $f \ge 0$ et $a \le b \Rightarrow \int_a^b f(x)\,dx \ge 0$ ;
2. $f \le g$ et $a \le b \Rightarrow \int_a^b f(x)\,dx \le \int_a^b g(x)\,dx$ ;
3. $a \le b \Rightarrow \left|\int_a^b f(x)\,dx\right| \le \int_a^b |f(x)|\,dx$ ;
4. si $a \le b$ et $m \le f \le M$ entre $a$ et $b$ : $m(b-a) \le \int_a^b f(x)\,dx \le M(b-a)$.

**[[Inégalité de la moyenne|Valeur moyenne]]** d'une fonction continue $f : [a,b] \to \mathbb{R}$ :
$$\mu = \frac{1}{b-a} \int_{[a,b]} f.$$

**[[Dérivation d'une intégrale à bornes variables]].** Soient $I, J$ deux intervalles, $u, v : I \to \mathbb{R}$ de classe $\mathcal{C}^1$ avec $u(I), v(I) \subset J$, et $f : J \to \mathbb{K}$ continue. Alors $g : x \mapsto \int_{u(x)}^{v(x)} f(t)\,dt$ est définie et $\mathcal{C}^1$ sur $I$, et
$$\forall x \in I,\quad g'(x) = f(v(x))\,v'(x) - f(u(x))\,u'(x).$$

**[[Parité et périodicité d'une intégrale]].** Soit $f : \mathbb{R} \to \mathbb{K}$ [[Limite et continuité|continue]].
1. Si $f$ est périodique de période $T$, pour tous $a, b$ : $\int_a^b f = \int_{a+T}^{b+T} f$ et $\int_a^{a+T} f = \int_b^{b+T} f$.
2. Si $f$ est [[Fonction paire et impaire|paire]] : $\int_{-a}^{a} f = 2\int_0^a f$.
3. Si $f$ est impaire : $\int_{-a}^{a} f = 0$.

## Primitives usuelles

| Fonction | [[Primitive]] |
|---|---|
| $e^x$ | $e^x$ |
| $\ln x$ | $x\ln x - x$ |
| $\frac{1}{x}$ | $\ln\lvert x\rvert$ |
| $x^a\ (a \neq -1)$ | $\frac{x^{a+1}}{a+1}$ |
| $\sin x$ | $-\cos x$ |
| $\cos x$ | $\sin x$ |
| $\tan x$ | $-\ln\lvert\cos x\rvert$ |

$$\int \frac{du}{u^2+a^2} = \frac{1}{a}\arctan\left(\frac{u}{a}\right) + C$$

| Primitive | Fonction | Dérivée |
|---|---|---|
| $x\arcsin(x)+\sqrt{1-x^2}$ | $\arcsin(x)$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $x\arccos(x)-\sqrt{1-x^2}$ | $\arccos(x)$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $x\arctan(x)-\frac{1}{2}\ln(1+x^2)$ | $\arctan(x)$ | $\frac{1}{1+x^2}$ |

| Fonction $f$ | Primitive $F$ |
|---|---|
| $k \in \mathbb{R}$ | $kx + C$ |
| $x^n,\ n \in \mathbb{N}$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{\sqrt{x}}$ | $2\sqrt{x} + C$ |
| $\frac{1}{x^n},\ n \in \mathbb{N}^*\setminus\{1\}$ | $\frac{-1}{(n-1)x^{n-1}} + C$ |
| $u'(x)\,u^n(x),\ n \in \mathbb{N}^*$ | $\frac{u^{n+1}(x)}{n+1} + C$ |
| $\frac{u'(x)}{\sqrt{u(x)}}$ | $2\sqrt{u(x)} + C$ |
| $\frac{u'(x)}{u^n(x)},\ n \in \mathbb{N}^*\setminus\{1\}$ | $\frac{-1}{(n-1)u^{n-1}(x)} + C$ |
| $\frac{u'(x)}{u(x)}$ | $\ln\lvert u(x)\rvert + C$ |
| $e^x$ | $e^x + C$ |
| $u'(x)\,e^{u(x)}$ | $e^{u(x)} + C$ |
| $\cos x$ | $\sin x + C$ |
| $u'(x)\cos(u(x))$ | $\sin(u(x)) + C$ |
| $\sin x$ | $-\cos x + C$ |
| $u'(x)\sin(u(x))$ | $-\cos(u(x)) + C$ |

Ajout de cette fiche :
$$\int u'(x)\ln(u(x))\,dx = u(x)\ln(u(x)) - u(x) + C.$$

## Techniques de calcul

**[[Intégration par parties]].** Si $f$ et $g$ sont $\mathcal{C}^1$ sur $[a,b]$ à valeurs dans $\mathbb{K}$ :
$$\int_a^b f'(t)\,g(t)\,dt = \big[f(t)\,g(t)\big]_a^b - \int_a^b f(t)\,g'(t)\,dt.$$

**[[Changement de variable dans une intégrale|Changement de variable]].** Soient $I$ un intervalle, $f : I \to \mathbb{K}$ continue et $\varphi : [a,b] \to I$ de classe $\mathcal{C}^1$. Alors
$$\int_{\varphi(a)}^{\varphi(b)} f(x)\,\mathrm{d}x = \int_a^b f(\varphi(t))\,\varphi'(t)\,\mathrm{d}t \qquad (x = \varphi(t)).$$
En pratique, changer les trois éléments : la variable $x = \varphi(t)$, l'élément différentiel $dx = \varphi'(t)\,dt$, et les bornes ($t$ entre $a$ et $b$, donc $x$ entre $\varphi(a)$ et $\varphi(b)$).

**[[Règles de Bioche]]**, pour $\int P(\cos x, \sin x)\,dx$ ou $\int \frac{P(\cos x, \sin x)}{Q(\cos x, \sin x)}\,dx$, écrites ici sur $f$ :
- $f(-x) = -f(x) \Rightarrow t = \cos x$ ;
- $f(\pi - x) = -f(x) \Rightarrow t = \sin x$ ;
- $f(\pi + x) = f(x) \Rightarrow t = \tan x$ ;
- si rien ne marche, $t = \tan(x/2)$.

## Somme de Riemann

[[Somme de Riemann]] :
$$\lim_{n\to+\infty} \frac{b-a}{n} \sum_{k=1}^{n} f\left(a + k\frac{b-a}{n}\right) = \int_a^b f(t)\,dt.$$

## Intégrales de Wallis

[[Intégrales de Wallis]] : les deux intégrales sont égales,
$$W_n = \int_0^{\pi/2} \sin^n x\,\mathrm{d}x = \int_0^{\pi/2} \cos^n x\,\mathrm{d}x.$$

## Points à vérifier

Aucun point à vérifier dans le fond. Mentions « À vérifier » des transcriptions, reprises :
1. Le tableau des fonctions trigonométriques réciproques n'a pas d'en-tête ; « Primitive », « Fonction », « Dérivée » sont déduits du contenu.
2. Dans le tableau en $\frac{u'}{u^n}$, le texte est coupé à gauche ; l'accolade de $\mathbb{N}^*\setminus\{1\}$ a été reconstituée.
3. L'énoncé du changement de variable passe de $\varphi$ à $\phi$ dans les remarques pratiques (même fonction).
4. L'image de la forme $\int P(\cos x, \sin x)\,dx$ est très petite et coupée à gauche.
5. Les règles de Bioche sont écrites ici sur $f$ (« $f(-x) = -f(x)$ »), alors que [[chp 7 - Integration (résumé)|Chap7-Integration]] les écrit sur $\omega(x) = f(x)\,dx$ (« $\omega(-x) = \omega(x)$ »). Les deux formulations sont équivalentes, puisque $\omega(-x) = -f(-x)\,dx$.
