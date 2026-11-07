---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp6 : Fourier Series.docx|Chp6 - Fourier Series]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Séries/Chp6 : Fourier Series.docx|Chp6 - Fourier Series]], dans [[Séries (index)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Les énoncés en image sont recopiés en texte ; seule la figure du phénomène de Gibbs est intégrée.

## Idée générale

Associer à une fonction $2\pi$-périodique une série trigonométrique, puis dire quand elle converge vers la fonction. Voir [[Série de Fourier]].

## Définition

**Définition.** Une série de Fourier (ou série trigonométrique) est
$$a_0 + \sum_{n=1}^{+\infty} (a_n \cos nx + b_n \sin nx),$$
où $(a_n)_{n\ge0}$ et $(b_n)_{n\ge1}$ sont des réels, les **coefficients de Fourier** de la série.

On calcule des séries de Fourier pour une classe de fonctions précise, les fonctions [[Fonction continue par morceaux|continues par morceaux]].

**Définition.** Une fonction est continue par morceaux (*piece-wise continuous*) sur un intervalle si l'intervalle peut être découpé en un nombre fini d'intervalles sur chacun desquels la fonction est continue et admet des limites finies à droite et à gauche. Une telle fonction n'a qu'un nombre fini de discontinuités.

## Séries de Fourier de période $2\pi$

**Définition.** Soit $f$ continue par morceaux sur $\mathbb{R}$. $f$ est [[Fonction périodique|périodique]] de période $2\pi$ ($2\pi$-périodique) si
$$\forall x \in \mathbb{R},\ f(x+2\pi) = f(x).$$

**Remarque.** Si une fonction continue par morceaux est définie sur $[-\pi, \pi[$ ou sur $[0, 2\pi[$, et prolongée hors de cet intervalle par $f(x+2\pi) = f(x)$, alors elle est $2\pi$-périodique.

**Proposition.** Si $f$ est $2\pi$-périodique :
$$\forall a, b \in \mathbb{R},\quad \int_a^{a+2\pi} f(t)\,dt = \int_b^{b+2\pi} f(t)\,dt.$$
En particulier $\int_{-\pi}^{\pi} f = \int_0^{2\pi} f$. Voir [[Parité et périodicité d'une intégrale]].

## Série de Fourier d'une fonction $2\pi$-périodique continue par morceaux

**Définition.** Soit $f$ continue par morceaux et $2\pi$-périodique. Sa série de Fourier est
$$FS(f)(x) = a_0 + \sum_{n=1}^{+\infty} (a_n \cos nx + b_n \sin nx),$$
avec
$$a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\,dx,$$
$$\forall n \ge 1,\quad a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx, \qquad b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\,dx.$$
Ce sont les coefficients de Fourier de $f$.

**Remarque.** Cette définition ne dit pas que $f$ est la somme de sa série de Fourier : elle associe seulement à chaque fonction continue par morceaux et $2\pi$-périodique une série $FS(f)$. Les conditions pour que $f$ en soit la somme viennent plus loin.

## Phénomène de Gibbs

Premières sommes partielles de la série de Fourier d'une fonction créneau (*square wave*) :

![[Chp6 - Fourier Series - image9.png]]

*Figure : sommes partielles $S_1$, $S_3$, $S_5$, $S_7$, $S_{11}$ et $S_{15}$ (en bleu) d'une fonction créneau valant 0 sur $[-\pi, 0[$ et 1 sur $]0, \pi]$ (en rouge).*

Quand $n$ augmente, $S_n$ approche de mieux en mieux la fonction créneau, mais les sommes partielles dépassent (*overshoot*) près des sauts : c'est le **phénomène de Gibbs**. On dirait que $f$ est la somme de sa série de Fourier, sauf aux points où $f$ est discontinue.

## Séries de Fourier des fonctions paires

**Définition.** Soit $I$ un intervalle symétrique par rapport à l'origine. $f$ est [[Fonction paire et impaire|paire]] si $\forall x \in I,\ f(-x) = f(x)$.

**Proposition.** Si $f$ est $2\pi$-périodique, continue par morceaux et paire :
$$a_0 = \frac{1}{\pi}\int_0^{\pi} f(x)\,dx, \qquad \forall n \ge 1,\ a_n = \frac{2}{\pi}\int_0^{\pi} f(x)\cos nx\,dx, \qquad b_n = 0,$$
donc
$$FS(f)(x) = a_0 + \sum_{n=1}^{+\infty} a_n \cos nx.$$

## Séries de Fourier des fonctions impaires

**Définition.** $f$ est impaire si $\forall x \in I,\ f(-x) = -f(x)$.

**Proposition.** Si $f$ est $2\pi$-périodique, continue par morceaux et impaire :
$$\forall n \ge 0,\ a_n = 0, \qquad \forall n \ge 1,\ b_n = \frac{2}{\pi}\int_0^{\pi} f(x)\sin nx\,dx,$$
donc
$$FS(f)(x) = \sum_{n=1}^{+\infty} b_n \sin nx.$$

## Convergence des séries de Fourier

### Convergence simple (théorème de Dirichlet)

**Théorème.** Si $f$ est $2\pi$-périodique et si $f$ et $f'$ sont continues par morceaux sur $[-\pi, \pi]$, la série de Fourier de $f$ converge simplement. Sa somme vaut $f(x)$ en tout point où $f$ est continue. En un point $x$ de discontinuité, elle vaut la moyenne des limites à droite et à gauche :
$$\frac{1}{2}\left(f(x^+) + f(x^-)\right), \qquad f(x^+) = \lim_{t \to x^+} f(t),\quad f(x^-) = \lim_{t \to x^-} f(t).$$
(Le nom « théorème de Dirichlet » n'est pas dans le cours.)

### Convergence normale

**Théorème.** Si $f$ est $2\pi$-périodique, continue, et si $f'$ est continue par morceaux sur $[-\pi, \pi]$, la série de Fourier de $f$ converge normalement vers $f$ (voir [[chp 4 - Series of functions (résumé)|convergence normale]]).

## Égalité de Parseval

**Théorème.** Si $f$ est $2\pi$-périodique et continue par morceaux sur $[-\pi, \pi]$ :
$$a_0^2 + \frac{1}{2}\sum_{n=1}^{+\infty}\left(a_n^2 + b_n^2\right) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)^2\,dx.$$

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Aucune formule n'est fausse (relues avec la convention $a_0$ = valeur moyenne).

1. **Convention de $a_0$** : ici $a_0$ est la moyenne de $f$ (et la série commence par $a_0$ et non $a_0/2$). Cela change les formules de Parseval et de parité par rapport à la convention $a_0/2$ (complément, pas une erreur).
2. **Périodicité pour la convergence normale** : le cours ne précise pas que $f$ continue et périodique suppose $f(-\pi) = f(\pi)$ ; c'est implicite dans « $2\pi$-périodique et continue sur $\mathbb{R}$ » (complément).
3. **Fautes de frappe** : « number if intervals », « do the square wave », « over shoot » (alertes de la transcription).
4. Aucun exemple de calcul de coefficients n'est dans la note : les coefficients de la fonction créneau de la figure ne sont pas donnés.
