---
type: concept
aliases: [analyse asymptotique, équivalent, équivalents, croissances comparées, négligeable, dominée, grand O, petit o]
matieres: [Analyse Maths, Séries]
sources: ["[[Cours/Year 1/Analyse Maths/Cours/chp5|chp5 (Analyse)]]"]
maj: 2026-11-05
---

Trois façons de comparer deux suites ou deux fonctions, au voisinage d'un point ou de l'infini :

- **Dominée**, $u_n = O(v_n)$ : $u_n/v_n$ est bornée.
- **Négligeable**, $u_n = o(v_n)$ : $u_n/v_n \to 0$. Cela implique $u_n = O(v_n)$.
- **Équivalente**, $u_n \sim v_n$ : $u_n/v_n \to 1$. C'est équivalent à $u_n - v_n = o(v_n)$, et c'est une relation réflexive, symétrique et transitive.

**Croissances comparées**, en $+\infty$ : $\frac{1}{n!} \ll q^{-n} \ll \frac{1}{n^\alpha} \ll \ln^\beta n \ll n^\alpha \ll q^n \ll n! \ll n^n$, avec $q > 1$ et $\alpha, \beta > 0$.

**Règles sur les équivalents** :

- Ils se multiplient, se divisent et s'élèvent à une puissance constante.
- Ils ne s'ajoutent pas, ne se soustraient pas, et ne se composent pas à gauche sans justification.
- Composition à droite permise : si $f \sim_a g$ et $\phi \to a$, alors $f \circ \phi \sim g \circ \phi$.
- Pour ln : $f \sim g$ et limite de $g$ différente de 1 donnent $\ln f \sim \ln g$. Pour exp : il faut $f - g \to 0$.
- Deux expressions équivalentes ont même signe et même limite.

**Équivalents classiques en 0** : $e^x - 1$, $\ln(1 + x)$, $\sin x$, $\tan x$, $\arcsin x$, $\arctan x$, sh $x$, th $x$ sont tous $\sim x$. De plus, $(1 + x)^\alpha - 1 \sim \alpha x$ et $1 - \cos x \sim x^2/2$. Un polynôme équivaut à son terme de plus haut degré en $+\infty$, et à son terme de plus bas degré en 0.

En algorithmique, le $O$ sert à exprimer la complexité : voir [[Complexité algorithmique]].

Liens : [[Développement limité]], [[Limite et continuité]], [[Dérivabilité]], [[Complexité algorithmique]]

Le chapitre 0 de Séries rappelle $f \sim g \iff f - g = o(g)$. Le corrigé du TD5 insiste : on n'additionne jamais des équivalents, et $e^f \sim e^g$ si et seulement si $f - g \to 0$.

Résumés : [[Sources/Year 1/Analyse Maths/chp5 (résumé)|chp5 (résumé)]], [[Chp0 - Revision chapter (résumé)]], [[TD5-AnalyseAsymptotiqueCorrection (1) (résumé)]]
