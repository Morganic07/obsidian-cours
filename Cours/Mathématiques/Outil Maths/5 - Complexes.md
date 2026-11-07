---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]], dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]. En cas d'écart, le cours et ses images font foi. Les tableaux de formules de la note sont en partie vides : les formules figurent dans les transcriptions qui suivent, et sont recopiées ici.

## Idée générale

Les nombres complexes, de la forme algébrique à la forme exponentielle, avec leur géométrie du plan. Voir [[Nombre complexe]]. Dans tout le chapitre, $z = a + ib$ et $z' = a' + ib'$ avec $a, b, a', b'$ réels.

## Les bases

$$i = \sqrt{-1}, \qquad i^2 = -1.$$

| Opération | Formule |
|---|---|
| Somme | $z + z' = (a + a') + i(b + b')$ |
| Produit | $z \times z' = (aa' - bb') + i(ab' + a'b)$ |
| Inverse | $\dfrac1z = \dfrac{a - ib}{a^2 + b^2}$ |

### Conjugué

$$\bar z = a - ib.$$

| Opération | Propriété du conjugué |
|---|---|
| Somme | $\overline{z + z'} = \bar z + \overline{z'}$ |
| Produit | $\overline{zz'} = \bar z \times \overline{z'}$ |
| Inverse ($z' \ne 0$) | $\overline{\left(\dfrac{1}{z'}\right)} = \dfrac{1}{\overline{z'}}$ |
| Quotient ($z' \ne 0$) | $\overline{\left(\dfrac{z}{z'}\right)} = \dfrac{\bar z}{\overline{z'}}$ |
| Puissance | $\overline{z^n} = \bar z^{\,n}$ |

Et $z\bar z = a^2 + b^2 = |z|^2$.

## Polynôme complexe du second degré

Le trinôme $az^2 + bz + c$ a **toujours** des solutions dans $\mathbb{C}$. Avec $\Delta = b^2 - 4ac$ (voir [[Équation du second degré]]) :

| Cas | Racines |
|---|---|
| $\Delta > 0$ | $z_1 = \dfrac{-b - \sqrt\Delta}{2a}$, $z_2 = \dfrac{-b + \sqrt\Delta}{2a}$ (réelles) |
| $\Delta = 0$ | $z_1 = z_2 = \dfrac{-b}{2a}$ (racine double) |
| $\Delta < 0$ | $z_1 = \dfrac{-b - i\sqrt{-\Delta}}{2a}$, $z_2 = \overline{z_1} = \dfrac{-b + i\sqrt{-\Delta}}{2a}$ (conjuguées) |

Donc le trinôme se factorise toujours par
$$az^2 + bz + c = a(z - z_1)(z - z_2).$$

## Forme trigonométrique

![[Chapitre 5 - Complexes - image44.png]]
*Figure : plan complexe ; le point $M(z)$ de coordonnées $(a, b)$, le module $|z| = OM$ (segment rouge) et l'argument $\arg(z)$ (angle bleu depuis l'axe des abscisses).*

- **Module** : $|z| = OM = \sqrt{a^2 + b^2}$.
- **Argument** : $\arg(z) = (\vec u\,;\overrightarrow{OM})\ [2\pi]$, défini modulo $2\pi$.
- **[[Forme trigonométrique et exponentielle|Forme trigonométrique]]** (il y a une infinité de formes trigonométriques pour un nombre complexe, à cause du modulo $2\pi$) :
$$z = |z|(\cos\theta + i\sin\theta), \qquad \theta = \arg(z),$$
avec
$$\cos\theta = \frac{a}{\sqrt{a^2 + b^2}}, \qquad \sin\theta = \frac{b}{\sqrt{a^2 + b^2}}.$$

### Propriétés du module et de l'argument

| Module | Argument (modulo $2\pi$) |
|---|---|
| $z\bar z = a^2 + b^2 = \lvert z\rvert^2$ | $\arg(-z) = \arg(z) + \pi$ ; $\arg(\bar z) = -\arg(z)$ |
| $\lvert -z\rvert = \lvert\bar z\rvert = \lvert z\rvert$ | $\arg(-z) = \arg(z) + \pi$ ; $\arg(\bar z) = -\arg(z)$ |
| $\lvert z \times z'\rvert = \lvert z\rvert \times \lvert z'\rvert$ | $\arg(zz') = \arg(z) + \arg(z')$ |
| $\left\lvert\dfrac1z\right\rvert = \dfrac{1}{\lvert z\rvert}$ | $\arg\left(\dfrac1z\right) = -\arg(z)$ |
| $\left\lvert\dfrac{z}{z'}\right\rvert = \dfrac{\lvert z\rvert}{\lvert z'\rvert}$ | $\arg\left(\dfrac{z}{z'}\right) = \arg(z) - \arg(z')$ |
| $\lvert z^n\rvert = \lvert z\rvert^n$ | $\arg(z^n) = n\arg(z)$ |
| $\lvert z + z'\rvert \le \lvert z\rvert + \lvert z'\rvert$ ([[Inégalité triangulaire]]) | Nota bene du cours : les formules de $\arg$ ressemblent à celles du logarithme népérien |

Le cours écrit aussi : $\forall\theta,\ |\cos\theta + \sin\theta| = 1$ (formule fausse telle qu'écrite, voir « Erreurs du cours » : il faut $|\cos\theta + i\sin\theta| = 1$).

## Géométrie dans le plan complexe

Rappels (voir [[Affixe]]) :
- $\overrightarrow{AB}$ a pour affixe $z_B - z_A$ ;
- $\vec u + \vec v$ a pour affixe $z_u + z_v$ ;
- $k\vec u$ a pour affixe $kz_u$.

| Module | Argument (modulo $2\pi$) |
|---|---|
| $\lvert z_B - z_A\rvert = AB$ | $\arg(z_B - z_A) = (\vec u\,;\overrightarrow{AB})$ |
| $\left\lvert\dfrac{z_B - z_C}{z_A - z_C}\right\rvert = \dfrac{CB}{CA}$ | $\arg\left(\dfrac{z_B - z_C}{z_A - z_C}\right) = (\overrightarrow{CA}\,;\overrightarrow{CB})$ |

## Forme exponentielle

$$z = |z|e^{i\theta}, \qquad \theta = \arg(z),$$
$$e^{i\theta} = \cos\theta + i\sin\theta, \qquad e^{-i\theta} = \cos\theta - i\sin\theta.$$

### Propriétés

$$e^{i\theta} \times e^{i\theta'} = e^{i(\theta + \theta')}, \qquad \left(e^{i\theta}\right)^n = e^{in\theta}, \qquad \frac{e^{i\theta}}{e^{i\theta'}} = e^{i(\theta - \theta')}, \qquad \frac{1}{e^{i\theta}} = e^{-i\theta} = \overline{e^{i\theta}}.$$

### Conseil du cours : revoir les formules de trigonométrie

Voir [[Formules trigonométriques]] :
- $\cos(x + y) = \cos x\cos y - \sin x\sin y$
- $\cos(x - y) = \cos x\cos y + \sin x\sin y$
- $\sin(x + y) = \sin x\cos y + \cos x\sin y$
- $\sin(x - y) = \sin x\cos y - \cos x\sin y$
- $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$ (le cours écrit « $1 - \sin^2 x$ », voir « Erreurs du cours »)
- $\sin 2x = 2\sin x\cos x$

## Formule de Moivre et formules d'Euler

**Moivre** :
$$z^n = |z|^n(\cos n\theta + i\sin n\theta).$$

Conseil du cours : revoir le triangle de Pascal (voir [[Formule de Pascal]], [[Formule du binôme de Newton]]), utile pour développer $(\cos\theta + i\sin\theta)^n$. Triangle donné par le cours :

```
1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
```

**Euler** :
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}.$$

Ces formules servent notamment à la [[Linéarisation trigonométrique]].

## Erreurs du cours

- [[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]] écrit « $\forall\theta,\ |\cos\theta + \sin\theta| = 1$ » (vérifié sur l'image) ; il faut « $|\cos\theta + i\sin\theta| = 1$ ». Pour $\theta = \pi/4$, la formule du cours donne $\sqrt 2$.
- [[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]] écrit « $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - \sin^2 x$ » (vérifié sur l'image) ; il faut « $1 - 2\sin^2 x$ » pour la dernière égalité.
- [[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]] donne un triangle de Pascal sans la ligne « 1 1 » entre « 1 » et « 1 2 1 » (vérifié sur l'image) ; le reste du triangle est juste.
- [[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]] écrit, ligne « produit » du tableau du conjugué, « $\overline{zz'} = \bar z \times \overline{z'} = a^2 + b^2$ » (vérifié sur l'image) ; la dernière égalité est fausse en général : c'est $z\bar z = a^2 + b^2$.
