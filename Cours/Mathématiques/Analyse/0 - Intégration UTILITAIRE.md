---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse/chp7/Intégration UTILITAIRE .docx|Intégration UTILITAIRE]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Analyse/chp7/Intégration UTILITAIRE .docx|Intégration UTILITAIRE]], dans [[Cours/Mathématiques/Analyse/_index|Analyse]]. Fiche pratique sur l'[[Intégrale]], sans preuves : elle reprend les énoncés utiles de [[1 - Integration|Chap7-Integration]] (voir aussi [[1 - Integration]]) et ajoute une primitive en $u'\ln u$ et les [[Intégrales de Wallis]].
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

**Formule de la moyenne** : comme $f$ est continue, elle atteint sa valeur moyenne, il existe $c \in [a,b]$ tel que $\int_a^b f = (b-a)\,f(c)$ (conséquence du point 4 avec $m = \min f$, $M = \max f$ et du [[Théorème des valeurs intermédiaires]]). Géométriquement, l'aire sous la courbe est celle d'un rectangle de base $b-a$ et de hauteur $f(c)$. [[Complément hors du cours|ⓘ]]

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

Elle vaut pour $u > 0$ et se vérifie en dérivant : $(u\ln u - u)' = u'\ln u + u\cdot\frac{u'}{u} - u' = u'\ln u$. C'est la primitive de $\ln$ composée avec $u$. [[Complément hors du cours|ⓘ]]

Primitives usuelles absentes des tableaux du cours, à connaître aussi ($a > 0$, $a \neq 1$ ; [[Fonctions hyperboliques]] pour $\mathrm{ch}$, $\mathrm{sh}$) : [[Complément hors du cours|ⓘ]]

| Fonction | Primitive |
|---|---|
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\frac{1}{\cos^2 x} = 1 + \tan^2 x$ | $\tan x + C$ |
| $\frac{1}{\sin^2 x}$ | $-\frac{1}{\tan x} + C$ |
| $\frac{1}{\sqrt{1-x^2}}$ (sur $]-1,1[$) | $\arcsin x + C$ |
| $\frac{1}{\sqrt{a^2-x^2}}$ (sur $]-a,a[$) | $\arcsin\frac{x}{a} + C$ |
| $\frac{1}{x^2-a^2}$ | $\frac{1}{2a}\ln\left\lvert\frac{x-a}{x+a}\right\rvert + C$ |
| $\mathrm{ch}\,x$ | $\mathrm{sh}\,x + C$ |
| $\mathrm{sh}\,x$ | $\mathrm{ch}\,x + C$ |
| $\frac{1}{\sqrt{x^2+1}}$ | $\ln\left(x + \sqrt{x^2+1}\right) + C$ |

Toute primitive se donne **sur un intervalle** : $\ln\lvert x\rvert$ est une primitive de $\frac{1}{x}$ sur $]-\infty,0[$ et sur $]0,+\infty[$ séparément, la constante pouvant différer de part et d'autre de $0$. [[Complément hors du cours|ⓘ]]

## Techniques de calcul

**[[Intégration par parties]].** Si $f$ et $g$ sont $\mathcal{C}^1$ sur $[a,b]$ à valeurs dans $\mathbb{K}$ :
$$\int_a^b f'(t)\,g(t)\,dt = \big[f(t)\,g(t)\big]_a^b - \int_a^b f(t)\,g'(t)\,dt.$$

Choix pratique : on dérive le facteur qui se simplifie en dérivant (polynôme, $\ln$, $\arctan$) et on intègre celui qui se primitive sans peine ($e^x$, $\sin$, $\cos$, polynôme). Exemple : avec $g(t) = t$ et $f'(t) = e^t$, $\int_0^1 t\,e^t\,dt = \big[t\,e^t\big]_0^1 - \int_0^1 e^t\,dt = e - (e-1) = 1$. Pour $\int \ln x\,dx$, on prend $f'(x) = 1$ et $g(x) = \ln x$, ce qui redonne $x\ln x - x$. [[Complément hors du cours|ⓘ]]

**[[Changement de variable dans une intégrale|Changement de variable]].** Soient $I$ un intervalle, $f : I \to \mathbb{K}$ continue et $\varphi : [a,b] \to I$ de classe $\mathcal{C}^1$. Alors
$$\int_{\varphi(a)}^{\varphi(b)} f(x)\,\mathrm{d}x = \int_a^b f(\varphi(t))\,\varphi'(t)\,\mathrm{d}t \qquad (x = \varphi(t)).$$
En pratique, changer les trois éléments : la variable $x = \varphi(t)$, l'élément différentiel $dx = \varphi'(t)\,dt$, et les bornes ($t$ entre $a$ et $b$, donc $x$ entre $\varphi(a)$ et $\varphi(b)$).

**[[Règles de Bioche]]**, pour $\int P(\cos x, \sin x)\,dx$ ou $\int \frac{P(\cos x, \sin x)}{Q(\cos x, \sin x)}\,dx$, écrites ici sur $f$ :
- $f(-x) = -f(x) \Rightarrow t = \cos x$ ;
- $f(\pi - x) = -f(x) \Rightarrow t = \sin x$ ;
- $f(\pi + x) = f(x) \Rightarrow t = \tan x$ ;
- si rien ne marche, $t = \tan(x/2)$.

Formules du changement $t = \tan\frac{x}{2}$ (sur un intervalle où $x \in ]-\pi,\pi[$) : $\cos x = \frac{1-t^2}{1+t^2}$, $\sin x = \frac{2t}{1+t^2}$, $dx = \frac{2\,dt}{1+t^2}$ ; elles sont démontrées et appliquées dans [[1 - démonstrations]]. [[Complément hors du cours|ⓘ]]

Pour un produit $\sin^p x\cos^q x$ dont les deux exposants sont pairs, Bioche indique $t = \tan x$, mais il est souvent plus rapide de [[Linéarisation trigonométrique|linéariser]], par exemple $\cos^2 x = \frac{1+\cos 2x}{2}$, d'où $\int \cos^2 x\,dx = \frac{x}{2} + \frac{\sin 2x}{4} + C$. [[Complément hors du cours|ⓘ]]

## Somme de Riemann

[[Somme de Riemann]] :
$$\lim_{n\to+\infty} \frac{b-a}{n} \sum_{k=1}^{n} f\left(a + k\frac{b-a}{n}\right) = \int_a^b f(t)\,dt.$$

Usage typique : calculer la limite d'une somme en y reconnaissant une somme de Riemann, le plus souvent sur $[0,1]$ avec $\frac{1}{n}\sum_{k=1}^n f\left(\frac{k}{n}\right) \to \int_0^1 f$. Exemple : $\sum_{k=1}^{n} \frac{1}{n+k} = \frac{1}{n}\sum_{k=1}^{n} \frac{1}{1 + k/n} \to \int_0^1 \frac{dx}{1+x} = \ln 2$. [[Complément hors du cours|ⓘ]]

## Intégrales de Wallis

[[Intégrales de Wallis]] : les deux intégrales sont égales,
$$W_n = \int_0^{\pi/2} \sin^n x\,\mathrm{d}x = \int_0^{\pi/2} \cos^n x\,\mathrm{d}x.$$

L'égalité vient du [[Changement de variable dans une intégrale|changement de variable]] $x = \frac{\pi}{2} - t$, qui échange $\sin$ et $\cos$. [[Complément hors du cours|ⓘ]]

Résultats classiques, obtenus par [[Intégration par parties]] sur $W_{n+2} = \int_0^{\pi/2} \sin^{n+1}x \cdot \sin x\,dx$ : [[Complément hors du cours|ⓘ]]
- $W_0 = \frac{\pi}{2}$, $W_1 = 1$ et la récurrence $W_{n+2} = \frac{n+1}{n+2}\,W_n$ ;
- $W_{2p} = \frac{(2p)!}{2^{2p}(p!)^2}\cdot\frac{\pi}{2}$ et $W_{2p+1} = \frac{2^{2p}(p!)^2}{(2p+1)!}$ ;
- $(W_n)$ est décroissante et positive, $(n+1)\,W_n W_{n+1} = \frac{\pi}{2}$ pour tout $n$, d'où $W_n \sim W_{n+1}$ et $W_n \sim \sqrt{\frac{\pi}{2n}}$.

Culture : ces intégrales donnent le **produit de Wallis** $\frac{\pi}{2} = \prod_{k=1}^{+\infty} \frac{4k^2}{4k^2-1}$ et servent à établir la constante $\sqrt{2\pi}$ de la formule de Stirling $n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$. [[Complément hors du cours|ⓘ]]
