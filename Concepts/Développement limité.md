---
type: concept
aliases: [développements limités, DL, Taylor-Young, formule de Taylor]
matieres: [Analyse Maths, Analyse, Analyse dans Rn, Séries]
sources: ["[[Cours/Year 1/Analyse Maths/Cours/chp5|chp5 (Analyse)]]"]
maj: 2026-11-05
---

$f$ admet un DL d'ordre $n$ en $a$ si $f(x) = a_0 + a_1(x - a) + \dots + a_n(x - a)^n + o((x - a)^n)$. Il est unique, et on se ramène à 0 en posant $h = x - a$.

- **Existence** : si $f \in \mathcal{C}^n$, Taylor-Young donne $f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k + o((x - a)^n)$. Continuité ⇔ DL₀ et dérivabilité ⇔ DL₁.
- **Troncature** : un DL d'ordre $n$ en donne un à tout ordre $p \le n$.
- **Parité** : en 0, une fonction paire n'a que des termes pairs, une fonction impaire que des termes impairs.
- **Équivalent et signe** : si $a_p$ est le premier coefficient non nul, alors $f(x) \sim a_p(x - a)^p$. Au voisinage de $a$, $f$ a donc son signe.
- **Primitivation** : un DLₙ de $f'$ donne un DLₙ₊₁ de $f$, en intégrant terme à terme et en ajoutant $f(a)$.
- **Opérations en 0** : combinaison linéaire, produit (troncature du produit), composition si $f \to 0$, quotient si $g$ a une limite non nulle.
- **En l'infini** : on étudie $u \mapsto f(1/u)$ en 0. Cela permet de trouver une asymptote oblique, où $f(x) - ax - b \to 0$.

**DL usuels en 0** :

- $\frac{1}{1 - x} = 1 + x + x^2 + \dots + x^n + o(x^n)$
- $e^x = 1 + x + \frac{x^2}{2} + \dots + \frac{x^n}{n!} + o(x^n)$
- $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$
- $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2}x^2 + \dots + o(x^n)$
- $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots + o(x^{2n+1})$
- $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots + o(x^{2n})$
- $\text{Arctan } x = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots + o(x^{2n+1})$
- $\tan x = x + \frac{x^3}{3} + o(x^3)$

Liens : [[Comparaison asymptotique]], [[Dérivabilité]], [[Fonction de classe Ck]], [[Différentielle]]

> [!warning] Écart dans le cours
> [[Chp0 - Revision chapter]] écrit $\sin$ et $\sinh$ avec $5!$ au lieu de $3!$ : voir son résumé.

**Piège** : un DL d'ordre $n$ n'implique pas $n$ dérivées. $x^3\sin(1/x)$ a un DL d'ordre 2 en 0 sans être deux fois dérivable en 0 (corrigé du TD5).

Résumés : [[Sources/Year 1/Analyse Maths/chp5 (résumé)|chp5 (résumé)]], [[Chp0 - Revision chapter (résumé)]], [[TD5-AnalyseAsymptotiqueCorrection (1) (résumé)]], [[Contrôles (résumé)]]
