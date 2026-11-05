---
type: source
sources: ["[[Chp0 - Revision chapter]]"]
maj: 2026-11-05
---

Résumé de [[Chp0 - Revision chapter]], dans [[Year 3 - Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Rappels sur les suites et les comparaisons asymptotiques, utiles pour toute la matière. Les notions de petit $o$, grand $O$ et équivalent sont aussi traitées dans [[Comparaison asymptotique]], et les développements usuels dans [[Développement limité]].

## Contenu, dans l'ordre du cours

- **Suite** : liste infinie, fonction de $\mathbb{N}$ dans $\mathbb{R}$, définie par formule ou récurrence.
- **Convergence** : vers $\ell$ si $\forall \epsilon > 0, \exists N, \forall n \ge N, |a_n - \ell| < \epsilon$. Vers $\pm\infty$ avec $A$ ou $B$. Convergente s'il existe une limite réelle, divergente sinon (tend vers $\pm\infty$ ou n'a pas de limite). Exercices posés : $\frac{n^2}{\sqrt{n^3 + 4n}}$ et $-n^2 + 2n - 4$.
- **Suite géométrique** $a, ar, ar^2, \ldots$ avec $r \ne 0$.
- **Limite par une fonction** : $\lim_{x \to +\infty} f(x) = \ell \Rightarrow \lim a_n = \ell$ pour $a_n = f(n)$. Pour une fraction rationnelle, on garde les termes de plus haut degré.
- **Opérations sur les limites** : somme, différence, produit, quotient (limite du dénominateur non nulle), puissance $p > 0$ pour des termes positifs.
- **Théorème d'encadrement**, **valeur absolue** ($|a_n| \to 0 \Rightarrow a_n \to 0$), **fonction continue** ($f(a_n) \to f(\ell)$).
- **Suites monotones et bornées** : toute suite convergente est bornée ; croissante majorée, décroissante minorée, ou monotone bornée, implique convergente.
- **Suites adjacentes** : l'une croissante, l'autre décroissante, $b_n - a_n \to 0$ ; elles convergent vers la même limite.
- **Voisinage** $\nu(a)$ pour $a \in \overline{\mathbb{R}}$.
- **Petit $o$ et grand $O$** : $f = o(g)$ si $f/g \to 0$ ; $f = O(g)$ si $f/g$ est borné près de $a$. Pour les suites, $|u_n| \le K|v_n|$ à partir d'un rang. Croissances comparées : $x^a = o(x^b)$ en $+\infty$ si $a < b$, $x^b = o(e^{ax})$, $(\ln x)^b = o(x^a)$, et les versions en $-\infty$ et $0^+$.
- **Équivalent** : $f \sim g$ si $f/g \to 1$. Équivalents usuels en 0 : $e^x - 1$, $\ln(1+x)$, $\sin x$, $\tan x \sim x$ ; $(1+x)^\alpha - 1 \sim \alpha x$ ; $1 - \cos x \sim x^2/2$. Un polynôme est équivalent à son terme de plus haut degré en $\pm\infty$ et à son terme de plus bas degré en 0. Conséquences : mêmes limites ou aucune, même signe, $f \sim g \Leftrightarrow f - g = o(g)$, $f = o(g) \Leftrightarrow f + g \sim g$. Le petit $o$ et l'équivalent impliquent le grand $O$.
- **Développements limités usuels** : $e^x$, $\cos$, $\sin$, $\cosh$, $\sinh$, $(1+x)^\alpha$, $\sqrt{1+x}$, $\frac{1}{1 \mp x}$, $\ln(1 \mp x)$, $\tan$, $\arctan$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Équivalents** : le point 3 et le point 4 sont écrits « $e^x - 1 = 1$ » et « $\ln(1+x) = x$ » avec un « 0 » sous le signe égal. Le signe est probablement un $\sim$ rendu comme un égal, et le point 3 devrait donner $x$ et non 1 (complément). **À corriger avant un examen.**
2. **Développements de $\sin$ et $\sinh$** : le terme en $x^3$ est écrit avec $5!$ au lieu de $3!$, dans les deux formules (alerte de la transcription, confirmée par la formule, complément). **À corriger avant un examen.** Dans le chapitre 5, la série de $\sin$ est écrite correctement avec $3!$.
3. **$\sqrt{1+x}$** : le terme général est incomplet (pas de $x^n$) et son signe ne correspond pas à $-x^2/8$ (complément).
4. **$\ln(1+x)$** : le terme général $(-1)^n x^n / n$ donne le signe opposé aux premiers termes ; il faudrait $(-1)^{n+1}$ (complément). La série correcte figure au [[Chp5 - power series (résumé)|chapitre 5]].
5. **Dernier terme de $\arctan$** : coupé en bas de l'image.
6. **Indice des suites** : $(a_n)_{\in\mathbb{N}}$ sans $n$, plusieurs fois, et « $g$does », « as $a$ tends to » : coquilles de rédaction sans conséquence.
7. **Hypothèse du quotient** : la règle 6 sur les limites suppose aussi $b_n \ne 0$ à partir d'un certain rang (complément).
