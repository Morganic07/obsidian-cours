---
type: concept
tags: [year4]
aliases: [puissance d'un nombre, puissance entière, puissances entières, x puissance n]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp4/4.5.c|4.5.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : pour un nombre $x$ et un entier naturel $n \ge 1$, la puissance $n$-ième de $x$ est le produit de $n$ facteurs égaux à $x$ :

$$x^n = \underbrace{x \times x \times \dots \times x}_{n \text{ facteurs}}$$

$x$ est la **base** et $n$ l'**exposant**. Par convention $x^0 = 1$ (produit vide, élément neutre de la multiplication, voir [[Symboles somme et produit]]), et pour $x \neq 0$, $x^{-n} = \dfrac{1}{x^n}$. La définition peut aussi s'écrire par [[Récurrence|récurrence]] : $x^0 = 1$ et $x^{n+1} = x^n \times x$.

Règles de calcul, pour des exposants entiers (et $x, y \neq 0$ si un exposant est négatif) :

| Règle | Exemple |
|---|---|
| $x^m \times x^n = x^{m+n}$ | $2^3 \times 2^4 = 2^7 = 128$ |
| $\dfrac{x^m}{x^n} = x^{m-n}$ | $10^5 / 10^2 = 10^3$ |
| $(x^m)^n = x^{mn}$ | $(2^3)^2 = 2^6 = 64$ |
| $(xy)^n = x^n y^n$ | $6^2 = 2^2 \times 3^2 = 36$ |

Les puissances de 10 servent à la notation scientifique ($3 \times 10^8$ m/s), les puissances de 2 en informatique : un [[Octet|octet]] a $2^8 = 256$ valeurs, un `int` de 32 bits va de $-2^{31}$ à $2^{31} - 1$ ([[Numération binaire]], [[Complément à deux]]). La suite $(x^n)$ est une [[Suite géométrique|suite géométrique]] de raison $x$ ; la notion s'étend aux exposants rationnels ($x^{1/2} = \sqrt{x}$, [[Racine carrée]]) puis réels ($x^a = e^{a \ln x}$ pour $x > 0$).

Le calcul effectif de $x^n$, par multiplications successives ou par une méthode plus rapide, est traité dans [[Exponentiation]].

## Dans le cours

- [[tp4]] : le programme 4.5 calcule $2^3$ par multiplications successives dans une boucle, en affichant chaque étape ; l'[[Accumulateur (programmation)|accumulateur]] `result` part de 1 et vaut $x^i$ après le tour $i$ ([[Invariant de boucle]]).

Voir aussi : [[Exponentiation]], [[Exponentiation rapide]], [[Suite géométrique]], [[Échelle logarithmique]].
