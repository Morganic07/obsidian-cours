---
type: source
sources: ["[[Chp1 - Convergent, divergent and positive terms SERIES]]"]
maj: 2026-11-05
---

Résumé de [[Chp1 - Convergent, divergent and positive terms SERIES]], dans [[Year 3 - Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Définition d'une [[Série numérique]], séries de référence (géométrique, télescopique, harmonique, de Riemann) et critères pour les séries à termes positifs.

## Contenu, dans l'ordre du cours

- **Série** : suite des sommes partielles $S_n = \sum_{k=0}^n a_k$. Convergente si $(S_n)$ converge, sa limite est la somme.
- **Géométrique** $\sum ar^n$ : converge si et seulement si $|r| < 1$, de somme $\frac{a}{1-r}$. Preuve par $S_n = a\frac{1 - r^{n+1}}{1-r}$.
- **Télescopique** $\sum (a_n - a_{n-1})$ : $S_n = a_n - a_0$, converge si et seulement si $(a_n)$ converge, de somme $\ell - a_0$. Exercice : $\sum \frac{1}{n(n+1)}$.
- **Harmonique** $\sum \frac{1}{n}$ : diverge, par l'absurde avec $S_{2n} - S_n \ge \frac{1}{2}$.
- **Condition nécessaire** : série convergente implique $a_n \to 0$. Réciproque fausse (harmonique). Contraposée : si $a_n \not\to 0$, la série diverge.
- **Reste** $R_n = S - S_n$ : tend vers 0 pour une série convergente.
- **Opérations** : combinaison linéaire de séries convergentes convergente. Convergente plus divergente diverge ; divergente plus divergente peut converger ou diverger.
- **Termes positifs** : convergence équivaut à $(S_n)$ majorée. Sinon $S_n \to +\infty$. Comparaison $a_n \le b_n$, puis $a_n = O(b_n)$, $a_n = o(b_n)$ (exemples : $e^{-n^2} = o(1/n^2)$, $\frac{1}{n} = o(\frac{\ln n}{\sqrt n})$), limite $a_n/b_n \to c \in\, ]0, +\infty[$ (même nature), et équivalents $a_n \sim b_n$.
- **Comparaison série-intégrale** : $f$ continue, positive, décroissante, alors $\sum f(n)$ et $\int^{+\infty} f$ ont la même nature, avec les encadrements $S_n - a_1 \le \int_1^n f \le S_{n-1}$ (deux figures d'aires de rectangles).
- **Encadrement du reste** : $\int_{n+1}^{+\infty} f \le R_n \le \int_n^{+\infty} f$. Exemple $\sum \frac{1}{n^3}$ avec $n = 20$ : $S_{20} = 1.20087$ et $1.20197 \le S \le 1.20212$.
- **Séries de Riemann** $\sum \frac{1}{n^p}$ : convergent si et seulement si $p > 1$. Corollaire : $n^p a_n \to 0$ avec $p > 1$ implique convergence ; $n^p a_n \to +\infty$ avec $p \le 1$ implique divergence.
- La note se termine sur le titre « Alternating series », traité dans [[Chp2 - Alternating and absolutly convergent series (résumé)|le chapitre 2]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Borne basse de l'exemple $\sum 1/n^3$** : $S_{20} + \frac{1}{2 \cdot 21^2} = 1.20087 + 0.00113 \approx 1.20200$, et non 1.20197 (recalcul : $S_{20} = 1.200868$, borne basse $1.202002$, borne haute $1.202118$). La borne haute 1.20212 est juste (complément).
2. **Remarque sur le reste** : la somme $\sum_{k \ge n+1} a_n$ est écrite avec $a_n$ au lieu de $a_k$ (alerte de la transcription, coquille).
3. **Hypothèses des comparaisons** : $a_n \le b_n$ est supposé pour tout $n$, alors que « à partir d'un certain rang » suffit ; de même pour $O$ et $o$ (complément).
4. **Dernière ligne de la preuve de la limite $c$** : coupée sur l'image.
5. **Série de Riemann, cas $p \le 0$** : le cours énonce le résultat pour tout réel $p$ ; il est vrai, la condition nécessaire $a_n \to 0$ suffit à conclure pour $p \le 0$.
