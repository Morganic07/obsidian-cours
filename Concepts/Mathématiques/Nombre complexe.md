---
type: concept
tags: [year1]
aliases: [nombres complexes, module et argument, conjugué d'un complexe, forme algébrique, module d'un complexe, argument d'un complexe]
matieres: [Outil Maths, Analyse Maths]
sources: ["[[5 - Complexes|Chapitre 5 - Complexes]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

Un complexe s'écrit sous forme algébrique $z = a + ib$ avec $i^2 = -1$. Somme $(a + a') + i(b + b')$, produit $(aa' - bb') + i(ab' + a'b)$, inverse $\frac{1}{z} = \frac{a - ib}{a^2 + b^2}$. Conjugué $\bar{z} = a - ib$, compatible avec somme, produit, inverse, quotient et puissance, et $z\bar{z} = a^2 + b^2 = |z|^2$. Module $|z| = \sqrt{a^2 + b^2}$ ([[Inégalité triangulaire]]), argument défini modulo $2\pi$. La conjugaison $z \mapsto \bar{z}$ sert d'exemple d'application au chapitre 4 ([[4 - pdf]]).

- **Trinôme** $az^2 + bz + c$ ([[Polynôme]]) : toujours résoluble dans $\mathbb{C}$ ; si $\Delta < 0$, racines conjuguées $\frac{-b \mp i\sqrt{-\Delta}}{2a}$.
- **Forme trigonométrique** ([[Forme trigonométrique et exponentielle]]) : $z = |z|(\cos\theta + i\sin\theta)$, $\theta = \arg(z)$ modulo $2\pi$. Module multiplicatif, arguments additifs pour un produit.
- **Forme exponentielle** : $z = |z|e^{i\theta}$.
- **Moivre** : $z^n = |z|^n(\cos n\theta + i\sin n\theta)$. **Euler** : $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$.
- **Géométrie** ([[Affixe]]) : $|z_B - z_A| = AB$, $\arg(z_B - z_A) = (\vec{u}; \overrightarrow{AB})$.

**En analyse** : le module et les parties réelle et imaginaire servent aux [[Suite complexe|suites complexes]] ([[0 - rappels pdf]], [[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]]). Le contrôle d'Outils math demande la forme exponentielle de $e^{i\pi/3}e^{-i\pi/4}$, les valeurs exactes de $\cos(\pi/12)$ et $\sin(\pi/12)$, la résolution de $z^2 + z + 1 = 0$ et une relation $|z| = |z'|$ ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

Le cours écrit à tort $|\cos\theta + \sin\theta| = 1$ (il manque le $i$) et $\cos 2x = 1 - \sin^2 x$ (il faut $1 - 2\sin^2 x$).

Résumés : [[5 - Complexes]], [[4 - pdf]], [[0 - rappels pdf]]
