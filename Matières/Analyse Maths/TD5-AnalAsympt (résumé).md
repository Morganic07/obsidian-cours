---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Analyse Maths/Exos/TD5-AnalAsympt.pdf|TD5-AnalAsympt]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/Exos/TD5-AnalAsympt.pdf|TD5-AnalAsympt]] (5 pages, énoncés seuls, version 2020-2021 « CPI 1 »), dans [[Analyse Maths (matière)]]. Son corrigé est résumé dans [[TD5-AnalyseAsymptotiqueCorrection (1) (résumé)]]. Le TD accompagne le cours [[Cours/Year 1/Analyse Maths/Cours/chp5|chp5 (Analyse)]] : voir [[chp5 - Analyse Maths (résumé)|son résumé]].

## Plan (24 exercices en trois parties)

**I. Comparaison de suites (ex. 1 à 6)**
- Ex. 1 : vrai ou faux sur $o$, $O$ et $\sim$ (par exemple « $u_n \sim v_n$ implique $u_n - v_n \to 0$ » est faux).
- Ex. 2 à 4 : équivalents simples de suites ($\ln(1 + 1/n)$, $\ln(n + \sqrt{n^2+1})$, $\sqrt{1 + \sqrt n}$, $\sqrt{n^3+2n^2} - \sqrt{n^3+n^2}$, $\sin(\frac{n^2+n+1}{n+1}\pi)$, $(1+\sqrt n)^{-\sqrt n}$, etc.) et limites déduites.
- Ex. 5 : $\sum_{k=0}^n k! \sim n!$.
- Ex. 6 : si $s_n \to 0$ et $s_n + s_{n+1} \sim 1/n$, alors $s_n \sim 1/(2n)$ quand $(s_n)$ est décroissante ; contre-exemple sans monotonie.

**II. Comparaison de fonctions (ex. 7 à 12)**
- Limites par équivalents : $\frac{\sin x}{x + 3x^2}$, $\frac{\sin x^4}{x(\tan x - \sin x)}$, $\sqrt{4x+1}\,\ln(1 - \frac{\sqrt{x+1}}{x+2})$, $\frac{e^{4x^2} - 1}{\ln\cos x}$, etc.
- Formes $1^\infty$ : $(\ln(e+x))^{1/x}$, $(\ln(1 + e^{-x}))^{1/x}$.
- Ex. 10 et 11 : conditions pour que $e^f \sim e^g$ et pour que $\ln f \sim \ln g$ ; ex. 12 : limites et équivalents plus techniques en $+\infty$, en $0$ ou en $\pi/4$.

**III. Développements limités (ex. 13 à 24)**
- Ex. 13 et 14 : ordre maximal d'un DL ($\sqrt x$, $x^{17/4}$, $|x|^n$) ; contre-exemples : $e^{-1/x}$ (DL nul à tout ordre sans que la fonction soit nulle) et $x^3\sin(1/x)$ (DL d'ordre 2 sans dérivée seconde).
- Ex. 15 à 20 : prolongement et DL de $(\cos x)^{1/x}$, dérivées successives de $x^3/(1+x^6)$ en $0$ par son DL, DL en un point $a \ne 0$, DL de $\tan$, $\ln(1+x)/\sin x$, composées ($e^{\sin x}$, $\sin(\tan x)$, $\sin^6 x$ à l'ordre 9), DL de $\cos(\ln x)$, $\ln(\tan x)$ en $\pi/4$.
- Ex. 21 : limites par DL ($(\cos x)^{1/x^2}$, $\frac{1+x}{1-x}$ à la puissance $1/x$, etc.).
- Ex. 22 à 24 : étude locale (tangente et position), DL de $\arctan$ et développement asymptotique en $+\infty$, recherche d'asymptotes obliques et de la position de la courbe (sept fonctions).

## À retenir

Le TD suit le cours en trois temps : équivalents, limites par équivalents, DL. Règle du corrigé : $u_n \sim v_n \iff u_n = v_n + o(v_n)$, et on n'additionne jamais des équivalents.

## Liens

[[Comparaison asymptotique]], [[Développement limité]], [[Limite et continuité]], [[Dérivabilité]], [[Fonction de classe Ck]].
