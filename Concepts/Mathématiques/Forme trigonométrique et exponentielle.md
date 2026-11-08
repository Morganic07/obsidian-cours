---
type: concept
tags: [year1]
aliases: [forme trigonométrique, forme exponentielle, formule de Moivre, formules d'Euler, identité d'Euler, Euler's identity, exponential form]
sources: ["[[5 - Complexes|Chapitre 5 - Complexes]]", "[[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]]"]
maj: 2026-11-08
---

Forme trigonométrique : $z = |z|(\cos\theta + i\sin\theta)$ avec $\theta = \arg z$, $\cos\theta = a/|z|$, $\sin\theta = b/|z|$ ; il y en a une infinité pour un même complexe. Forme exponentielle : $z = |z|e^{i\theta}$, avec $e^{i\theta} = \cos\theta + i\sin\theta$ ; pour tout $\theta$, $|\cos\theta + i\sin\theta| = 1$. [[Erreurs du cours#^e-forme-trigonometrique-et-exponentielle|✎]]

Propriétés : $|zz'| = |z||z'|$, $\arg(zz') = \arg z + \arg z'$ [$2\pi$], $\arg(-z) = \arg z + \pi$, $\arg \bar z = -\arg z$ ; « les formules de arg sont similaires aux formules de logarithme népérien ».

Formule de Moivre : $z^n = |z|^n(\cos n\theta + i\sin n\theta)$. Formules d'Euler : $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$.

## Compléments (hors du cours)

**Cercle trigonométrique.** Pour tout réel $\theta$, $|e^{i\theta}| = \sqrt{\cos^2\theta + \sin^2\theta} = 1$ : $e^{i\theta}$ est le point du cercle trigonométrique d'angle $\theta$. Valeurs à connaître : $e^{i\pi/2} = i$, $e^{i\pi} = -1$, $e^{2i\pi} = 1$, d'où l'**identité d'Euler** $e^{i\pi} + 1 = 0$.

**Exemple de mise sous forme exponentielle.** $|1 + i| = \sqrt2$, $\cos\theta = \sin\theta = \frac{1}{\sqrt2}$, donc $\theta = \frac{\pi}{4}$ et $1 + i = \sqrt2\,e^{i\pi/4}$.

**Interprétation géométrique.** Multiplier $z$ par $re^{i\alpha}$ ($r > 0$) multiplie le module par $r$ et ajoute $\alpha$ à l'argument : c'est la composée de l'[[Homothétie]] de centre $O$ et de rapport $r$ et de la rotation de centre $O$ et d'angle $\alpha$. La rotation de centre $\Omega$ d'affixe $\omega$ et d'angle $\alpha$ s'écrit
$$z' = \omega + e^{i\alpha}(z - \omega).$$

**Usage de la formule de Moivre.** Pour exprimer $\cos n\theta$ ou $\sin n\theta$ en fonction de $\cos\theta$ et $\sin\theta$, on développe $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ avec la [[Formule du binôme de Newton]], puis on identifie parties réelle et imaginaire. Pour $n = 3$ :
$$(\cos\theta + i\sin\theta)^3 = \cos^3\theta - 3\cos\theta\sin^2\theta + i(3\cos^2\theta\sin\theta - \sin^3\theta),$$
d'où, avec $\sin^2\theta = 1 - \cos^2\theta$, $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$ et $\sin 3\theta = 3\sin\theta - 4\sin^3\theta$.

**Valeurs exactes par produit d'exponentielles.** $e^{i\pi/3}e^{-i\pi/4} = e^{i\pi/12}$. En développant le membre de gauche, $\left(\frac12 + i\frac{\sqrt3}{2}\right)\left(\frac{\sqrt2}{2} - i\frac{\sqrt2}{2}\right) = \frac{\sqrt2 + \sqrt6}{4} + i\,\frac{\sqrt6 - \sqrt2}{4}$, d'où
$$\cos\frac{\pi}{12} = \frac{\sqrt6 + \sqrt2}{4}, \qquad \sin\frac{\pi}{12} = \frac{\sqrt6 - \sqrt2}{4}.$$

Notion parente : [[Nombre complexe]]. Voir aussi : [[Formules trigonométriques]], [[Formule de Pascal]], [[Fonctions trigonométriques]], [[Formule du binôme de Newton]], [[Homothétie]].

Résumés : [[5 - Complexes]]
