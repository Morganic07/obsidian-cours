---
type: source
tags:
  - year1
sources:
  - "[[Cours/Year 1/Analyse Maths/Cours/chp5|chp5 (Analyse)]]"
maj: 2026-11-05
---

Résumé de [[Cours/Year 1/Analyse Maths/Cours/chp5|chp5 (Analyse)]], dans [[Analyse Maths (matière)]]. En cas d'écart, le cours et ses images font foi.

Dans cette note, plusieurs formules en image sont décalées par rapport au texte qu'elles complètent, par exemple « Alors : » après sa formule. C'est un effet de la mise en page d'origine.

## Contenu, dans l'ordre du cours

- **[[Comparaison asymptotique]] de suites** : $u_n = O(v_n)$ si $u_n/v_n$ est bornée, $u_n = o(v_n)$ si $u_n/v_n \to 0$, et $u_n \sim v_n$ si $u_n/v_n \to 1$. Échelle : $\frac{1}{n!} \ll q^{-n} \ll \frac{1}{n^\alpha} \ll \ln^\beta n \ll n^\alpha \ll q^n \ll n! \ll n^n$.
- **Règles sur les équivalents** : ils se multiplient, se divisent et s'élèvent à une puissance constante. Ils ne s'ajoutent pas, ne se soustraient pas et ne se composent pas à gauche sans justification. Deux suites équivalentes ont même signe et même limite.
- **Fonctions** : mêmes définitions au voisinage de $a$. Si $f$ est dérivable et $f'(a) \neq 0$, alors $f(x) - f(a) \sim f'(a)(x - a)$. Le cours donne les équivalents classiques en 0.
- **[[Développement limité]]** : $f(x) = a_0 + \dots + a_n(x - a)^n + o((x - a)^n)$. Il est unique, se tronque, et ne garde que les termes pairs ou impairs si $f$ l'est. Le premier terme non nul donne un équivalent et le signe.
- **Existence** : formule de Taylor-Young pour $f \in \mathcal{C}^n$. Continuité ⇔ DL₀ et dérivabilité ⇔ DL₁, mais $\mathcal{C}^n$ ⇒ DLₙ sans réciproque.
- **Opérations** : combinaison, produit, composition, quotient et primitivation.
- **En l'infini** : DL de $u \mapsto f(1/u)$ en 0, et asymptote oblique.
- **DL usuels** : $\frac{1}{1 - x}$, $\ln(1 + x)$, $e^x$, $(1 + x)^\alpha$, $\sin x$, $\cos x$, Arctan $x$, $\tan x$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Fausses alertes des transcriptions** : deux mentions « À vérifier » de cette note sont à ignorer. $\frac{1}{n^\alpha} = o(\ln^\beta n)$ est bien vrai, car le quotient tend vers 0. « En tronquant à l'ordre $p$ » est bien correct. Le seul défaut réel est $(\alpha, \beta) \in \mathbb{R}$, à lire $\mathbb{R}^2$.
2. **Quotient de DL** : les formes normalisées mettent en facteur $x^{n_1}$ et $x^{n_2}$. Le quotient utilisant $x^{p_1 - p_2}$, il faut lire $x^{p_1}$ et $x^{p_2}$ (complément).
3. **Signe** : « $f$ est du même signe strict que le premier terme non nul » vaut seulement au voisinage de $a$.
4. **Composition par ln** : « lim g (+∞) ≠ 1 » porte sur la limite au point étudié, pas seulement en $+\infty$ (complément).
