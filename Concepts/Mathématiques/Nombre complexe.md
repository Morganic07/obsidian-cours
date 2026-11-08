---
type: concept
tags: [year1]
aliases: [nombres complexes, module et argument, conjugué d'un complexe, forme algébrique, module d'un complexe, argument d'un complexe, partie réelle, partie imaginaire, imaginaire pur, complex number, argument principal]
matieres: [Outil Maths, Analyse Maths]
sources: ["[[5 - Complexes|Chapitre 5 - Complexes]]", "[[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-08
---

Un complexe s'écrit sous forme algébrique $z = a + ib$ avec $i^2 = -1$. Somme $(a + a') + i(b + b')$, produit $(aa' - bb') + i(ab' + a'b)$, inverse $\frac{1}{z} = \frac{a - ib}{a^2 + b^2}$. Conjugué $\bar{z} = a - ib$, compatible avec somme, produit, inverse, quotient et puissance, et $z\bar{z} = a^2 + b^2 = |z|^2$. Module $|z| = \sqrt{a^2 + b^2}$ ([[Inégalité triangulaire]]), argument défini modulo $2\pi$. La conjugaison $z \mapsto \bar{z}$ sert d'exemple d'application au chapitre 4 ([[4 - pdf]]).

- **Trinôme** $az^2 + bz + c$ ([[Polynôme]]) : toujours résoluble dans $\mathbb{C}$ ; si $\Delta < 0$, racines conjuguées $\frac{-b \mp i\sqrt{-\Delta}}{2a}$.
- **Forme trigonométrique** ([[Forme trigonométrique et exponentielle]]) : $z = |z|(\cos\theta + i\sin\theta)$, $\theta = \arg(z)$ modulo $2\pi$. Module multiplicatif, arguments additifs pour un produit.
- **Forme exponentielle** : $z = |z|e^{i\theta}$.
- **Moivre** : $z^n = |z|^n(\cos n\theta + i\sin n\theta)$. **Euler** : $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$.
- **Géométrie** ([[Affixe]]) : $|z_B - z_A| = AB$, $\arg(z_B - z_A) = (\vec{u}; \overrightarrow{AB})$.

**En analyse** : le module et les parties réelle et imaginaire servent aux [[Suite complexe|suites complexes]] ([[0 - rappels pdf]], [[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]]). Le contrôle d'Outils math demande la forme exponentielle de $e^{i\pi/3}e^{-i\pi/4}$, les valeurs exactes de $\cos(\pi/12)$ et $\sin(\pi/12)$, la résolution de $z^2 + z + 1 = 0$ et une relation $|z| = |z'|$ ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

Le complexe $\cos\theta + i\sin\theta$ est de module 1 : $|\cos\theta + i\sin\theta| = 1$. [[Erreurs du cours#^e-nombre-complexe|✎]] Formule de duplication : $\cos 2x = 1 - 2\sin^2 x$. [[Erreurs du cours#^e-nombre-complexe|✎]]

## Compléments (complément, hors du cours)

Ajoutés dans [[5 - Complexes]].

- **Parties réelle et imaginaire** : pour $z = a + ib$ ($a, b$ réels), $\mathrm{Re}(z) = a$ et $\mathrm{Im}(z) = b$ ; la partie imaginaire est un **réel** ($b$, pas $ib$). $z$ est réel si $b = 0$, **imaginaire pur** si $a = 0$.
- **Identification** : deux complexes sont égaux si et seulement s'ils ont même partie réelle et même partie imaginaire. En particulier $a + ib = 0 \iff a = b = 0$.
- **Avec le conjugué** : $\mathrm{Re}(z) = \dfrac{z + \bar z}{2}$, $\mathrm{Im}(z) = \dfrac{z - \bar z}{2i}$ ; $z$ réel $\iff \bar z = z$, $z$ imaginaire pur $\iff \bar z = -z$.
- **Quotient** : on multiplie par le conjugué du dénominateur, $\dfrac{z}{z'} = \dfrac{z\,\overline{z'}}{|z'|^2}$ pour $z' \ne 0$.
- **Argument** : il n'existe que pour $z \ne 0$ ($0$ n'a pas d'argument). L'**argument principal** est l'unique argument dans $]-\pi, \pi]$.
- **Géométrie** : pour trois points distincts $A$, $B$, $C$, $A$, $B$, $C$ sont alignés $\iff \dfrac{z_B - z_C}{z_A - z_C}$ est réel ; $(CA) \perp (CB) \iff$ ce quotient est imaginaire pur. L'argument de ce quotient mesure l'angle $(\overrightarrow{CA}, \overrightarrow{CB})$.
- Pour aller plus loin : [[Racine n-ième de l'unité]] et [[Théorème fondamental de l'algèbre]].

Résumés : [[5 - Complexes]], [[4 - pdf]], [[0 - rappels pdf]]
