---
type: concept
tags:
  - year1
  - year3
aliases:
  - développements limités
  - DL
  - Taylor-Young
  - formule de Taylor
  - partie régulière
  - DL usuels
matieres:
  - Analyse Maths
  - Analyse
  - Analyse dans Rn
  - Séries
sources:
  - "[[5 - Analyse Maths|chp5 (Analyse)]]"
  - "[[Raw/Year 1/Analyse Maths/Exos/TD5-AnalyseAsymptotiqueCorrection (1).pdf|TD5-AnalyseAsymptotiqueCorrection (1).pdf]]"
  - "[[0 - Revision chapter|Chp0 - Revision chapter]]"
maj: 2026-11-07
---

$f$ admet un DL d'ordre $n$ en $a$ si $f(x) = a_0 + a_1(x - a) + \dots + a_n(x - a)^n + o((x - a)^n)$, le polynôme étant la partie régulière. Il est unique, et on se ramène à 0 en posant $h = x - a$.

- **Existence** : si $f \in \mathcal{C}^n$, Taylor-Young donne $f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k + o((x - a)^n)$. Continuité ⇔ DL₀ et dérivabilité ⇔ DL₁.
- **Troncature** : un DL d'ordre $n$ en donne un à tout ordre $p \le n$.
- **Parité** : en 0, une fonction paire n'a que des termes pairs, une fonction impaire que des termes impairs.
- **Équivalent et signe** : si $a_p$ est le premier coefficient non nul, alors $f(x) \sim a_p(x - a)^p$. Au voisinage de $a$, $f$ a donc son signe.
- **Primitivation** : un DLₙ de $f'$ donne un DLₙ₊₁ de $f$, en intégrant terme à terme et en ajoutant $f(a)$.
- **Opérations en 0** : combinaison linéaire, produit (troncature du produit), composition si $f \to 0$, quotient si $g$ a une limite non nulle.
- **En l'infini** : on étudie $u \mapsto f(1/u)$ en 0. Cela permet de trouver une [[Asymptote oblique|asymptote oblique]], où $f(x) - ax - b \to 0$.

**DL usuels en 0** :

- $\frac{1}{1 - x} = 1 + x + x^2 + \dots + x^n + o(x^n)$
- $e^x = 1 + x + \frac{x^2}{2} + \dots + \frac{x^n}{n!} + o(x^n)$
- $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$
- $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2}x^2 + \dots + o(x^n)$
- $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots + o(x^{2n+1})$
- $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots + o(x^{2n})$
- $\text{Arctan } x = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots + o(x^{2n+1})$
- $\tan x = x + \frac{x^3}{3} + o(x^3)$

Le chapitre 0 de Séries reprend la liste des DL usuels : $e^x$, $\cos$, $\sin$, $\cosh$, $\sinh$, $(1+x)^\alpha$, $\sqrt{1+x}$, $1/(1 \mp x)$, $\ln(1 \mp x)$, $\tan$, $\arctan$ (voir aussi [[Série entière]] et [[Reste de Taylor]]).

Notion parente : [[Comparaison asymptotique]]. Voir aussi : [[Asymptote oblique]], [[Tangente à une courbe]], [[Fonction de classe Ck]], [[Fonctions trigonométriques réciproques]], [[Série entière]], [[Reste de Taylor]], [[Dérivabilité]], [[Différentielle]]

**Piège** : un DL d'ordre $n$ n'implique pas $n$ dérivées. $x^3\sin(1/x)$ a un DL d'ordre 2 en 0 sans être deux fois dérivable en 0 (corrigé du TD5) : $\mathcal{C}^n \Rightarrow$ DL$_n$, sans réciproque.

## Erreurs du cours

- [[0 - Revision chapter|Chp0 - Revision chapter]] (Séries) écrit $\sin x = x - \frac{x^3}{5!} + \frac{x^5}{5!} + \dots$ et $\sinh x = x + \frac{x^3}{5!} + \frac{x^5}{5!} + \dots$ ; il faut $\frac{x^3}{3!}$ dans les deux.
- Le même chapitre écrit $\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \dots + (-1)^{n-1}\frac{1 \cdot 3 \cdots (2n-3)}{2^n n!} + o(x^n)$ ; il manque $x^n$ au dernier terme : $(-1)^{n-1}\frac{1 \cdot 3 \cdots (2n-3)}{2^n n!}x^n$.
- Le même chapitre écrit $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} + \dots + (-1)^n\frac{x^n}{n} + o(x^n)$ ; il faut $(-1)^{n-1}\frac{x^n}{n}$, comme dans [[5 - Analyse Maths|chp5 (Analyse)]].
- [[5 - Analyse Maths|chp5 (Analyse)]], remarque sur le quotient, écrit les formes normalisées $f(x) = x^{n_1}(a_{p_1} + \dots)$ et $g(x) = x^{n_2}(b_{p_2} + \dots)$ ; il faut $x^{p_1}$ et $x^{p_2}$ en facteur, puisque le quotient s'écrit ensuite $x^{p_1 - p_2}h(x)$.

Résumés : [[5 - Analyse Maths|chp5]], [[0 - Revision chapter]]
