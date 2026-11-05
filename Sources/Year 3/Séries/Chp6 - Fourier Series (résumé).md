---
type: source
sources: ["[[Chp6 - Fourier Series]]"]
maj: 2026-11-05
---

Résumé de [[Chp6 - Fourier Series]], dans [[Year 3 - Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Associer à une fonction $2\pi$-périodique une série trigonométrique, puis dire quand elle converge vers la fonction. Voir [[Série de Fourier]].

## Contenu, dans l'ordre du cours

- **Série de Fourier** : $a_0 + \sum_{n \ge 1}(a_n\cos nx + b_n\sin nx)$.
- **Fonction continue par morceaux** : intervalle découpé en un nombre fini de morceaux où elle est continue avec limites finies à droite et à gauche.
- **Périodicité $2\pi$** et propriété $\int_a^{a+2\pi} f = \int_b^{b+2\pi} f$, en particulier $\int_{-\pi}^{\pi} = \int_0^{2\pi}$.
- **Coefficients** : $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f$, $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx$, $b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\,dx$. La définition associe une série à $f$ sans dire que $f$ en est la somme.
- **Phénomène de Gibbs** : sur une fonction créneau, les sommes partielles $S_1, S_3, \ldots, S_{15}$ approchent mieux la fonction mais dépassent près des sauts.
- **Fonction paire** : $b_n = 0$, $a_0 = \frac{1}{\pi}\int_0^\pi f$, $a_n = \frac{2}{\pi}\int_0^\pi f\cos nx$. **Fonction impaire** : $a_n = 0$, $b_n = \frac{2}{\pi}\int_0^\pi f\sin nx$.
- **Convergence simple** : si $f$ et $f'$ sont continues par morceaux, la série converge, vers $f(x)$ aux points de continuité et vers $\frac{1}{2}(f(x^+) + f(x^-))$ aux sauts.
- **Convergence normale** : si $f$ est continue et $f'$ continue par morceaux, la série converge normalement vers $f$.
- **Égalité de Parseval** : $a_0^2 + \frac{1}{2}\sum (a_n^2 + b_n^2) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f^2$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Aucune formule n'est fausse (relues avec la convention $a_0$ = valeur moyenne).

1. **Convention de $a_0$** : ici $a_0$ est la moyenne de $f$ (et la série commence par $a_0$ et non $a_0/2$). Cela change les formules de Parseval et de parité par rapport à la convention $a_0/2$ (complément, pas une erreur).
2. **Périodicité pour la convergence normale** : le cours ne précise pas que $f$ continue et périodique suppose $f(-\pi) = f(\pi)$ ; c'est implicite dans « $2\pi$-périodique et continue sur $\mathbb{R}$ » (complément).
3. **Fautes de frappe** : « number if intervals », « do the square wave », « over shoot » (alertes de la transcription).
4. Aucun exemple de calcul de coefficients n'est dans la note.
