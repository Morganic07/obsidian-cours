---
type: concept
tags: [year1]
aliases: [théorème de d'Alembert-Gauss, d'Alembert-Gauss, fundamental theorem of algebra, corps algébriquement clos, algébriquement clos]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le théorème fondamental de l'algèbre, ou théorème de d'Alembert-Gauss, affirme que tout [[Polynôme|polynôme]] non constant à coefficients complexes admet au moins une racine dans $\mathbb{C}$.

**Conséquence : factorisation complète.** Par récurrence sur le degré (une racine $z_1$ permet d'écrire $P(z) = (z - z_1)Q(z)$ avec $\deg Q = n - 1$), un polynôme de degré $n \ge 1$ de coefficient dominant $a$ s'écrit
$$P(z) = a(z - z_1)(z - z_2)\cdots(z - z_n),$$
où les $z_k$ ne sont pas forcément distincts. $P$ a donc exactement $n$ racines **comptées avec leur multiplicité**. On dit que $\mathbb{C}$ est **algébriquement clos**. $\mathbb{R}$ ne l'est pas : $x^2 + 1$ n'a aucune racine réelle.

**Polynômes à coefficients réels.** Si $P$ est à coefficients réels et $P(z) = 0$, alors $P(\bar z) = \overline{P(z)} = 0$ : les racines non réelles vont par paires conjuguées. En regroupant $(x - z)(x - \bar z) = x^2 - 2\,\mathrm{Re}(z)\,x + |z|^2$, qui est à coefficients réels et à discriminant négatif, on obtient : tout polynôme réel se factorise dans $\mathbb{R}$ en produit de facteurs de degré 1 et de facteurs de degré 2 à discriminant strictement négatif. En particulier, un polynôme réel de degré impair a au moins une racine réelle.

**Le cas du cours.** Pour le trinôme $az^2 + bz + c$ ($a \ne 0$), on a toujours $az^2 + bz + c = a(z - z_1)(z - z_2)$ dans $\mathbb{C}$ ; si les coefficients sont réels et $\Delta < 0$, $z_1$ et $z_2$ sont conjugués ([[Équation du second degré]]).

Le théorème garantit l'existence des racines, mais ne donne pas de méthode pour les calculer : au-delà du degré 4, il n'existe pas de formule générale par radicaux (théorème d'Abel-Ruffini).

## Dans le cours

Le cours ne le nomme pas : seul le trinôme du second degré est traité, dans [[5 - Complexes]]. Le théorème apparaît dans les compléments de cette fiche.

Voir aussi : [[Polynôme]], [[Équation du second degré]], [[Nombre complexe]], [[Racine n-ième de l'unité]].

Résumés : [[5 - Complexes]]
