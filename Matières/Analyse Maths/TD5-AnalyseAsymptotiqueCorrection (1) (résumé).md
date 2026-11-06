---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Analyse Maths/Exos/TD5-AnalyseAsymptotiqueCorrection (1).pdf|TD5-AnalyseAsymptotiqueCorrection]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/Exos/TD5-AnalyseAsymptotiqueCorrection (1).pdf|TD5-AnalyseAsymptotiqueCorrection]] (32 pages, texte, « Analyse II 2021/2022 »), dans [[Analyse Maths (matière)]]. C'est le corrigé détaillé du TD d'analyse asymptotique dont l'énoncé 2020-2021 est dans [[TD5-AnalAsympt (résumé)]]. Cette version compte 5 affirmations à l'exercice 1 au lieu de 4. Le résumé donne les méthodes et les pièges, pas les corrections complètes. Cours associé : [[chp5 - Analyse Maths (résumé)|chp5 (résumé)]].

## Méthodes de résolution

**Équivalents de suites et de fonctions**
- Règle d'or : $u \sim v \iff u = v + o(v)$.
- Pour un équivalent d'un produit, d'un quotient ou d'une puissance, on remplace chaque facteur par son équivalent. Pour une **somme ou une différence**, on ne peut pas remplacer terme à terme : on factorise le terme dominant, ou on passe par la forme $\sqrt{1+u} = 1 + u/2 + o(u)$ puis on regroupe, ou on multiplie par la quantité conjuguée (ex. 2.4 : $\sqrt{n^3+2n^2} - \sqrt{n^3+n^2} \sim \sqrt n / 2$).
- Piège de l'ex. 2.3 : $\sqrt{1 + u} - 1 \sim u/2$ exige $u \to 0$. Pour $\sqrt{1 + \sqrt n}$, on a simplement $1 + \sqrt n \sim \sqrt n$, donc $w_n \sim n^{1/4}$.
- Pour un logarithme : $\ln(n + \sqrt{n^2+1}) = \ln n + \ln(1 + \sqrt{1 + 1/n^2})$, où le second terme tend vers $\ln 2$, négligeable devant $\ln n$.

**Vrai ou faux (ex. 1)**
- $o$ implique $O$ (un quotient qui converge est borné) ; $O$ dans les deux sens n'implique pas $\sim$ (contre-exemple $1$ et $2$) ; $u_n \sim v_n$ donne $u_n - v_n = o(v_n)$ mais pas $u_n - v_n \to 0$ (contre-exemple $n+1$ et $n$) ; $3^n/n = O(2^n)$ est faux car $(3/2)^n/n \to +\infty$ par croissances comparées.

**Ex. 5 et 6 (suites)**
- $\sum_{k=0}^n k! \sim n!$ : retirer les deux derniers termes et majorer les $n-1$ autres par $n(n-1)$ fois $1/(n(n-1))$ chacun, puis gendarmes. Piège : « chaque terme tend vers 0 » ne suffit pas pour que la somme tende vers 0.
- Ex. 6 : encadrer $2n\,s_n$ entre $n(s_n + s_{n+1})$ et $n(s_{n-1} + s_n)$ grâce à la décroissance, puis gendarmes ; le contre-exemple $\frac1{2n} + \frac{(-1)^n}{\sqrt n}$ vérifie les hypothèses sauf la monotonie.

**Équivalents de fonctions**
- Ex. 10 : $e^f \sim e^g$ en $a$ si et seulement si $f - g \to 0$. Donc $f \sim g$ n'implique pas $e^f \sim e^g$ (exemple $x^2 + x$ et $x^2$ en $+\infty$).
- Ex. 11 : $f \sim g$, strictement positives, avec $\lim f \ne 1$, alors $\ln f \sim \ln g$ : on écrit $\frac{\ln f - \ln g}{\ln f} = \ln\frac{f}{g} \cdot \frac{1}{\ln f}$. La condition $\lim f \ne 1$ est nécessaire.
- Ex. 7 à 9 et 12 : se ramener aux équivalents usuels ($\sin x \sim x$, $1 - \cos x \sim x^2/2$, $\tan x - \sin x \sim x^3/2$, $\ln(1+u) \sim u$), changer de variable pour les limites en un point $a \ne 0$, passer à l'exponentielle pour les formes $1^\infty$.

**Développements limités**
- Ex. 13 : $\sqrt x$ n'a qu'un DL d'ordre 0 en 0 (continue, non dérivable).
- Ex. 14 : $e^{-1/x}$ ($0$ pour $x \le 0$) est négligeable devant toute puissance de $x$ : son DL est nul à tout ordre sans que la fonction soit nulle. Donc des DL égaux à tout ordre n'impliquent pas des fonctions égales. $x^3 \sin(1/x)$ a un DL d'ordre 2 (nul) mais pas de dérivée seconde en 0 : **un DL d'ordre $n$ n'implique pas que $f$ soit $n$ fois dérivable** (le sens réciproque, Taylor-Young, est le bon).
- Ex. 16 : développer $x^3/(1 + x^6) = \sum (-1)^k x^{3+6k}$, puis identifier avec Taylor par unicité : $f^{(n)}(0) = (-1)^{(n-3)/6}\, n!$ si $n \equiv 3 \pmod 6$, et $0$ sinon.
- Ex. 17 à 20 : DL en un point $a \ne 0$ par $x = a + h$ ; composée par substitution ; produit en tronquant à l'ordre voulu ; quotient par $1/(1+u)$.
- Ex. 22 : tangente = partie d'ordre $\le 1$ du DL ; position = signe du premier terme non nul suivant (ici $-\frac{3}{16}(x-1)^2 \le 0$ : la courbe est sous sa tangente).
- Ex. 23 : DL de $\arctan$ par intégration du DL de $1/(1+x^2)$ ; $\arctan x + \arctan(1/x) = \pi/2$ pour $x > 0$ donne le développement asymptotique en $+\infty$.
- Ex. 24 : asymptote oblique en $+\infty$ : écrire $f(x) = ax + b + \frac{c}{x} + o(1/x)$ par DL en $u = 1/x$ ; la position est donnée par le signe de $c$ (ex. $\sqrt{x(x+1)} = x + \frac12 - \frac{1}{8x} + \dots$ : courbe sous l'asymptote $y = x + 1/2$).

## Liens

[[Comparaison asymptotique]], [[Développement limité]], [[Limite et continuité]], [[Dérivabilité]], [[Fonction de classe Ck]], [[Suite numérique]].
