---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/TD5-AnalAsympt.pdf|TD5-AnalAsympt.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de TD5-AnalAsympt ([[Raw/Year 1/Analyse Maths/Exos/TD5-AnalAsympt.pdf|TD5-AnalAsympt.pdf]]) (5 pages, énoncés seuls, version 2020-2021 « CPI 1 »), dans [[Analyse Maths (index)]]. Son corrigé est résumé dans [[TD5-AnalyseAsymptotiqueCorrection (1) (résumé)]]. Le TD accompagne le cours [[chp 5 - Analyse Maths (résumé)|chp5 (Analyse)]] : voir [[chp 5 - Analyse Maths (résumé)|son résumé]].

Ce document ne contient que les énoncés (aucune correction, voir le corrigé ci-dessus) et aucune figure (la seule image est le logo). Notions : [[Comparaison asymptotique]] ($o$, $O$, $\sim$), [[Équivalent (comparaison asymptotique)|équivalents]], [[Développement limité|développements limités]] (DL), [[Développement asymptotique|développements asymptotiques]], [[Asymptote oblique|asymptotes obliques]].

## Partie I — Comparaison des suites

### Exercice 1
Vrai ou faux, et pourquoi ?
1. Si $u_n = o(v_n)$ alors $u_n = O(v_n)$.
2. Si $u_n = O(v_n)$ et $v_n = O(u_n)$ alors $u_n \sim v_n$.
3. Si $u_n \sim v_n$ alors $u_n - v_n = o(v_n)$ et $(u_n - v_n) \to 0$ quand $n \to +\infty$.
4. $\dfrac{3^n}{n} = O(2^n)$.

### Exercice 2
Équivalents simples de :
1. $u_n = \ln\left(1 + \frac{1}{n}\right)$ ;
2. $v_n = \ln\left(n + \sqrt{n^2+1}\right)$ ;
3. $w_n = \sqrt{1 + \sqrt{n}}$ ;
4. $x_n = \sqrt{n^3 + 2n^2} - \sqrt{n^3 + n^2}$ ;
5. $y_n = \sin\left(\dfrac{n^2+n+1}{n+1}\pi\right)$.

### Exercice 3
Limites, par équivalents :
1. $\lim_{n\to+\infty} \left(1 + \frac{x}{n}\right)^n$, $x \in \mathbb{R}$ ;
2. $\lim_{n\to+\infty} \sqrt[n]{n^2}$ ;
3. $\lim_{n\to+\infty} \sin\left(\dfrac{n^2+2n+3}{n+1}\pi\right)$ ;
4. $\lim_{n\to+\infty} \left(\sqrt{n^2+2n+3} - \sqrt{n^2+n+1}\right)$.

### Exercice 4
Équivalent le plus simple possible quand $n \to +\infty$ :
1. $(1 + \sqrt{n})^{-\sqrt{n}}$ ;
2. $\ln\left(\cos\frac{1}{n}\right)\,\ln\left(\sin\frac{1}{n}\right)$ ;
3. $\sqrt{1 + \frac{(-1)^n}{\sqrt{n}}} - 1$ ;
4. $e^{\sqrt{n+1} - \sqrt{n}}$.

### Exercice 5
Montrer que $\displaystyle\sum_{k=0}^{n} k! \sim n!$.

### Exercice 6
Soit $(s_n)$ une suite réelle de limite $0$ telle que $s_n + s_{n+1} \sim \frac{1}{n}$.
1. Si $(s_n)$ est décroissante, montrer que $s_n \sim \frac{1}{2n}$.
2. Avec la suite $\left(\frac{1}{2n} + \frac{(-1)^n}{\sqrt{n}}\right)_{n\ge1}$, prouver que le résultat est en défaut si $(s_n)$ n'est pas décroissante.

## Partie II — Comparaison de fonctions

### Exercice 7
Limites :
$$\lim_{x\to0} \frac{\sin x}{x + 3x^2} \;;\quad \lim_{x\to0} \frac{\sin(x^4)}{x(\tan x - \sin x)} \;;\quad \lim_{x\to+\infty} \sqrt{4x+1}\,\ln\left(1 - \frac{\sqrt{x+1}}{x+2}\right) \;;$$
$$\lim_{x\to0} \frac{e^{4x^2} - 1}{\ln(\cos x)} \;;\quad \lim_{x\to0} \frac{x^4 + 3x^2 + x}{2x^3 + x^2} \;;\quad \lim_{x\to\pi} \frac{3e^{x^2} - 5x^4}{\ln(7x^2) + 2x}.$$

### Exercice 8
Limites de :
1. $\dfrac{\sin x\,\ln(1+x^2)}{x\tan x}$ en $0$ ;
2. $\dfrac{\ln(1 + \sin x)}{\tan(6x)}$ en $0$ ;
3. $(\ln(e + x))^{1/x}$ en $0$ ;
4. $(\ln(1 + e^{-x}))^{1/x}$ en $+\infty$.

### Exercice 9
1. $\lim_{x\to1} \dfrac{x^3 - 2x^2 + 2x - 1}{x^3 - x^2 + x - 1}$ ;
2. $\lim_{x\to0} \dfrac{x\sin x}{1 - \cos x}$ ;
3. $\lim_{x\to+\infty} f(x)$ où $f(x) = (x+1) - \sqrt[3]{x^3 + 1}$ ;
4. $\lim_{x\to0} \exp\left(\dfrac{(1 - \cos x)\sin x}{x^3}\right)$ ;
5. $\lim_{x\to0} \dfrac{\ln(\cos x)}{1 - \cos 2x}$ ;
6. $\lim_{x\to+\infty} \left(\dfrac{\ln(x+1)}{\ln x}\right)^{x\ln x}$ ;
7. $\lim_{x\to\pi/2} \dfrac{\ln\left(\frac{2x}{\pi}\right)}{\cos x}$ ;
8. $\lim_{x\to+\infty} x^2\left(e^{\frac{1}{x+1}} - e^{\frac{1}{x}}\right)$.

### Exercice 10
À quelle condition sur $f$ et $g$ a-t-on $e^f \underset{a}{\sim} e^g$ ?

### Exercice 11
Soient $f$ et $g$ équivalentes au voisinage de $a$ et strictement positives. Montrer que si $f$ admet en $a$ une limite dans $\overline{\mathbb{R}}$ différente de $1$, alors $\ln f \underset{a}{\sim} \ln g$.

### Exercice 12
- Limite en $+\infty$ de $\sqrt[3]{x^3 + x^2} - \sqrt[3]{x^3 - x^2}$ ;
- équivalent en $+\infty$ de $\sqrt{x^2 + \sqrt{x^4+1}} - x\sqrt{2}$ ;
- limite en $0$ de $\dfrac{\tan(ax) - \sin(ax)}{\tan(bx) - \sin(bx)}$ ;
- limite en $\frac{\pi}{4}$ de $\left(x - \frac{\pi}{4}\right)\tan\left(x + \frac{\pi}{4}\right)$ ;
- limite en $\frac{\pi}{4}$ de $\dfrac{\cos x - \sin x}{(4x - \pi)\tan x}$ ;
- équivalent en $0$ de $\dfrac{\tan(x - x\cos x)}{\sin x + \cos x - 1}$ ;
- limite en $0$ de $x^{\frac{1}{1 + 2\ln x}}$ ;
- limite en $\frac{1}{2}$ de $(2x^2 - 3x + 1)\tan(\pi x)$ ;
- équivalent en $+\infty$ de $\dfrac{\sqrt{1+x^2}}{\sin(1/x)}\ln\left(\dfrac{x}{x+1}\right)$.

## Partie III — Développements limités

### Exercice 13
Ordres pour lesquels ces fonctions admettent un DL en $0$ :
1. $x \mapsto \sqrt{x}$ ;
2. $x \mapsto x^{17/4}$ ;
3. $x \mapsto |x|^n$.

### Exercice 14
1. $f(x) = 0$ si $x \le 0$, $f(x) = \exp\left(-\frac{1}{x}\right)$ sinon. Calculer pour tout $n \in \mathbb{N}$ le DL de $f$ en $0$. Quelles conclusions en tirer ? (Le DL est nul à tout ordre sans que $f$ soit nulle.)
2. $g(0) = 0$ et $g(x) = x^3\sin\left(\frac{1}{x}\right)$ si $x \ne 0$. Montrer que $g$ a un DL d'ordre 2 en $0$ mais n'a pas de dérivée seconde en $0$.

### Exercice 15
Soit $f(x) = (\cos x)^{1/x}$ pour $x \in \left]-\frac{\pi}{2}, \frac{\pi}{2}\right[ \setminus \{0\}$.
1. Montrer que $f$ est [[Prolongement par continuité|prolongeable par continuité]] en $0$.
2. Déterminer un DL de $f$ en $0$ à l'ordre 2.
3. Étudier la [[Dérivabilité|dérivabilité]] du prolongement.

### Exercice 16
$f(x) = \dfrac{x^3}{1 + x^6}$. Calculer $f^{(n)}(0)$ pour tout $n \in \mathbb{N}$ (par le DL et l'unicité des coefficients de Taylor).

### Exercice 17
1. $DL_3(0)$ de $f_1(x) = x^4 - x^2 + 1$ ;
2. $DL_3(2)$ de $f_1(x) = x^4 - x^2 + 1$ ;
3. $DL_3(1)$ de $f_2(x) = (\sqrt{x} - 1)\ln x$.

### Exercice 18
DL en $0$ :
1. $f_1(x) = \tan x$, ordre 4 ;
2. $f_2(x) = \dfrac{\ln(1+x)}{\sin x}$, ordre 3 ;
3. $f_5(x) = \sqrt{1 + \sqrt{1 + x^2}}$, ordre 4.

### Exercice 19
DL en $0$ :
1. $\exp(\sin x)$, ordre 3 ;
2. $\sin(\tan x)$, ordre 3 ;
3. $(\ln(1+x))^2$, ordre 3 ;
4. $\exp(\cos x)$, ordre 4 ;
5. $\sin^6 x$, ordre 9.

### Exercice 20
1. $DL_2(1)$ de $f_1(x) = \cos(\ln x)$ ;
2. $DL_3\left(\frac{\pi}{4}\right)$ de $f_2(x) = \ln(\tan x)$ ;
3. $DL_2(1)$ de $f_3(x) = \dfrac{\sqrt{x} - 1}{\ln x}$.

### Exercice 21
Limites :
1. $\lim_{x\to0} (\cos x)^{1/x^2}$ ;
2. $\lim_{x\to0} \left(\dfrac{1+x}{1-x}\right)^{1/x}$ ;
3. $\lim_{x\to e} \dfrac{\sqrt{x} - \sqrt{e}}{\ln x - 1}$ ;
4. $\lim_{x\to0} \dfrac{(1+3x)^{1/3} - 1 - \sin x}{1 - \cos x}$ ;
5. $\lim_{x\to0} \left(\dfrac{1}{x} - \dfrac{\ln(1+x)}{x^2}\right)$ ;
6. $\lim_{x\to0} \dfrac{1}{x^2}\ln\left(\dfrac{\sin x}{x}\right)$.

### Exercice 22 — étude locale
Étudier au voisinage de $1$ la fonction $g(x) = x + 2\sqrt{x} - \sqrt{2 + 2x}$ : [[Tangente à une courbe|tangente]], position de la courbe par rapport à la tangente, allure de la courbe.

### Exercice 23 — arctan
$f(x) = \arctan x$ est $\mathcal{C}^\infty$ sur $\mathbb{R}$, de dérivée $f'(x) = \frac{1}{1+x^2}$.
1. Donner un DL d'ordre 5 de $f$ en $0$.
2. Montrer que $\forall x > 0$, $\arctan x + \arctan\frac{1}{x} = \frac{\pi}{2}$.
3. En déduire un développement asymptotique d'ordre 3 de $f$ au voisinage de $+\infty$.

### Exercice 24 — asymptotes
Les courbes suivantes ont-elles une asymptote en $+\infty$ ? Position, s'il y a lieu :
1. $y = \sqrt{x(x+1)}$ ;
2. $y = \sqrt{\dfrac{x^3}{x-1}}$ ;
3. $y = (x^2 - 1)\ln\left(\dfrac{x+1}{x-1}\right)$ ;
4. $y = (x+1)\arctan(1 + 2/x)$ ;
5. $y = x\arctan x\,e^{1/x}$ ;
6. $y = e^{2/x}\sqrt{1+x^2}\arctan x$ ;
7. $y = \sqrt{x^2 - x}\exp\left(\dfrac{1}{x+1}\right)$.

## Plan en un coup d'œil

**I. Comparaison de suites (ex. 1 à 6)**
- Ex. 1 : vrai ou faux sur $o$, $O$ et $\sim$ (par exemple « $u_n \sim v_n$ implique $u_n - v_n \to 0$ » est faux).
- Ex. 2 à 4 : équivalents simples de suites et limites déduites.
- Ex. 5 : $\sum_{k=0}^n k! \sim n!$.
- Ex. 6 : si $s_n \to 0$ et $s_n + s_{n+1} \sim 1/n$, alors $s_n \sim 1/(2n)$ quand $(s_n)$ est décroissante ; contre-exemple sans monotonie.

**II. Comparaison de fonctions (ex. 7 à 12)** : limites par équivalents, formes $1^\infty$, conditions pour $e^f \sim e^g$ et $\ln f \sim \ln g$.

**III. Développements limités (ex. 13 à 24)** : ordre maximal d'un DL et contre-exemples ($e^{-1/x}$, $x^3\sin(1/x)$), DL en $0$ et en un point $a \ne 0$, composées, limites par DL, étude locale, développement asymptotique d'$\arctan$, asymptotes obliques.

## À retenir

Le TD suit le cours en trois temps : équivalents, limites par équivalents, DL. Règle du corrigé : $u_n \sim v_n \iff u_n = v_n + o(v_n)$, et on n'additionne jamais des équivalents.

## Points à vérifier

1. Exercice 18 : les fonctions sont numérotées $f_1$, $f_2$, $f_5$ (pas de $f_3$, $f_4$) : le TD a sans doute été raccourci d'une version plus longue.
2. Exercice 17 : la même fonction $f_1$ sert pour les DL en $0$ et en $2$.

## Liens

[[Comparaison asymptotique]], [[Développement limité]], [[Limite et continuité]], [[Dérivabilité]], [[Fonction de classe Ck]].
