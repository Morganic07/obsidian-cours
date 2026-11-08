---
type: concept
tags:
  - year1
  - year2
  - year3
aliases:
  - analyse asymptotique
  - équivalents
  - négligeable
  - dominée
  - grand O
  - petit o
  - domination
  - négligeabilité
  - little o
  - big O
  - notations de Landau
  - big O notation
matieres:
  - Analyse Maths
  - Séries
  - Analyse
sources:
  - "[[5 - Analyse Maths|chp5 (Analyse)]]"
  - "[[Raw/Year 1/Analyse Maths/Exos/TD5-AnalyseAsymptotiqueCorrection (1).pdf|TD5-AnalyseAsymptotiqueCorrection (1).pdf]]"
  - "[[0 - Revision chapter|Chp0 - Revision chapter]]"
  - "[[Raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1).pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Cours/chp5.docx|chp5 (Analyse)]]"
maj: 2026-11-08
---

Trois façons de comparer deux suites ou deux fonctions, au voisinage d'un point ou de l'infini :

- **Dominée**, $u_n = O(v_n)$ : $u_n/v_n$ est bornée.
- **Négligeable**, $u_n = o(v_n)$ : $u_n/v_n \to 0$. Cela implique $u_n = O(v_n)$.
- **Équivalente**, $u_n \sim v_n$ : $u_n/v_n \to 1$. C'est équivalent à $u_n - v_n = o(v_n)$, et c'est une relation réflexive, symétrique et transitive. Page dédiée : [[Équivalent (comparaison asymptotique)]].

Le cours donne des règles d'addition et de multiplication pour $o$ et $O$, ainsi que leur transitivité, et les mêmes définitions pour les fonctions au voisinage de $a$. Il note aussi « $o(x) = o(y) \neq o(y) = o(x)$ » : le signe $=$ de ces notations ne se lit que de gauche à droite.

*Exemple (complément, hors du cours)* : $o(n^2) = o(n^3)$ est vrai (une suite négligeable devant $n^2$ l'est devant $n^3$), mais $o(n^3) = o(n^2)$ est faux : $n^{5/2} = o(n^3)$ sans être $o(n^2)$, puisque $n^{5/2}/n^2 = \sqrt{n} \to +\infty$. Ces notations, $O$ et $o$, sont appelées **notations de Landau**.

**[[Croissances comparées]]**, en $+\infty$ : $\frac{1}{n!} \ll q^{-n} \ll \frac{1}{n^\alpha} \ll \ln^\beta n \ll n^\alpha \ll q^n \ll n! \ll n^n$, avec $q > 1$ et $\alpha, \beta > 0$.

**Règles sur les équivalents** :

- Ils se multiplient, se divisent et s'élèvent à une puissance constante.
- Ils ne s'ajoutent pas, ne se soustraient pas, et ne se composent pas à gauche sans justification.
- Composition à droite permise : si $f \sim_a g$ et $\phi \to a$, alors $f \circ \phi \sim g \circ \phi$.
- Pour ln : $f \sim g$ et limite de $g$ différente de 1 donnent $\ln f \sim \ln g$. Pour exp : il faut $f - g \to 0$.
- Deux expressions équivalentes ont même signe et même limite.

**Équivalents classiques en 0** : $e^x - 1$, $\ln(1 + x)$, $\sin x$, $\tan x$, $\arcsin x$, $\arctan x$, sh $x$, th $x$ sont tous $\sim x$ (par exemple $e^x - 1 \underset{0}{\sim} x$). De plus, $(1 + x)^\alpha - 1 \sim \alpha x$ et $1 - \cos x \sim x^2/2$. [[Erreurs du cours#^e-comparaison-asymptotique|✎]] Un polynôme équivaut à son terme de plus haut degré en $+\infty$, et à son terme de plus bas degré en 0.

En algorithmique, le $O$ sert à exprimer la complexité : c'est la même notation $O$ qui sert en informatique, appliquée au nombre d'opérations en fonction de la taille $n$ de l'entrée ; voir [[Complexité algorithmique]]. La [[Formule de Stirling]] donne l'équivalent de $n!$ qui précise sa place dans l'échelle des croissances comparées.

Le chapitre 0 de Séries rappelle les trois définitions ($f/g \to 0$, $f/g$ borné, $f/g \to 1$), $f \sim g \iff f - g = o(g)$, les équivalents usuels en 0 et les croissances comparées ; le chapitre 1 s'en sert pour le [[Critère de comparaison]]. Le corrigé du TD5 insiste : on n'additionne jamais des équivalents, et $e^f \sim e^g$ si et seulement si $f - g \to 0$.

En Analyse de deuxième année, le TD7 demande de montrer $I_n \sim I_{n+1}$ et de trouver un équivalent de $I_n$ pour les [[Intégrales de Wallis]].

Voir aussi : [[Équivalent (comparaison asymptotique)]], [[Croissances comparées]], [[Développement limité]], [[Critère de comparaison]], [[Limite et continuité]], [[Dérivabilité]], [[Complexité algorithmique]], [[Formule de Stirling]]

Résumés : [[5 - Analyse Maths|chp5]], [[0 - Revision chapter]], [[1 - Convergent, divergent and positive terms SERIES]]
