---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]], dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]. Les tableaux de formules de la note sont en partie vides : les formules figurent dans les transcriptions qui suivent, et sont recopiées ici. Les passages ajoutés finissent par ⓘ.

## Idée générale

Les nombres complexes, de la forme algébrique à la forme exponentielle, avec leur géométrie du plan. Voir [[Nombre complexe]]. Dans tout le chapitre, $z = a + ib$ et $z' = a' + ib'$ avec $a, b, a', b'$ réels.

## Les bases

$$i = \sqrt{-1}, \qquad i^2 = -1.$$

L'écriture $i = \sqrt{-1}$ est un raccourci : le symbole $\sqrt{\ }$ n'est défini que pour les réels positifs, et $-i$ vérifie aussi $(-i)^2 = -1$. Seule l'égalité $i^2 = -1$ définit $i$ sans ambiguïté ; appliquer sans précaution $\sqrt{x}\sqrt{y} = \sqrt{xy}$ donnerait $-1 = i \cdot i = \sqrt{-1}\sqrt{-1} = \sqrt{1} = 1$. [[Complément hors du cours|ⓘ]]

**Vocabulaire.** Dans $z = a + ib$ (forme algébrique, unique), $a = \mathrm{Re}(z)$ est la **partie réelle** et $b = \mathrm{Im}(z)$ la **partie imaginaire** (un réel, sans le $i$). $z$ est réel si $b = 0$, **imaginaire pur** si $a = 0$. Deux complexes sont égaux si et seulement s'ils ont même partie réelle et même partie imaginaire : c'est ce qui permet d'« identifier » les deux membres d'une égalité. [[Complément hors du cours|ⓘ]]

Les puissances de $i$ se répètent de 4 en 4 : $i^0 = 1$, $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$ ; donc $i^n$ ne dépend que du reste de $n$ dans la division par 4 (par exemple $i^{2026} = i^2 = -1$, car $2026 = 4 \times 506 + 2$). [[Complément hors du cours|ⓘ]]

| Opération | Formule |
|---|---|
| Somme | $z + z' = (a + a') + i(b + b')$ |
| Produit | $z \times z' = (aa' - bb') + i(ab' + a'b)$ |
| Inverse | $\dfrac1z = \dfrac{a - ib}{a^2 + b^2}$ |

La formule de l'inverse (pour $z \ne 0$) vient de la multiplication du numérateur et du dénominateur par le conjugué $a - ib$, ce qui rend le dénominateur réel : $\dfrac{1}{a + ib} = \dfrac{a - ib}{(a + ib)(a - ib)} = \dfrac{a - ib}{a^2 + b^2}$. Même méthode pour un quotient : $\dfrac{z}{z'} = \dfrac{z\,\overline{z'}}{|z'|^2}$. Exemple : $\dfrac{1 + 2i}{3 - i} = \dfrac{(1 + 2i)(3 + i)}{9 + 1} = \dfrac{1 + 7i}{10}$. [[Complément hors du cours|ⓘ]]

### Conjugué

$$\bar z = a - ib.$$

| Opération | Propriété du conjugué |
|---|---|
| Somme | $\overline{z + z'} = \bar z + \overline{z'}$ |
| Produit | $\overline{zz'} = \bar z \times \overline{z'}$ [[Erreurs du cours#^e-5-complexes\|✎]] |
| Inverse ($z' \ne 0$) | $\overline{\left(\dfrac{1}{z'}\right)} = \dfrac{1}{\overline{z'}}$ |
| Quotient ($z' \ne 0$) | $\overline{\left(\dfrac{z}{z'}\right)} = \dfrac{\bar z}{\overline{z'}}$ |
| Puissance | $\overline{z^n} = \bar z^{\,n}$ |

Et $z\bar z = a^2 + b^2 = |z|^2$.

Le conjugué donne aussi les parties réelle et imaginaire : $\mathrm{Re}(z) = \dfrac{z + \bar z}{2}$ et $\mathrm{Im}(z) = \dfrac{z - \bar z}{2i}$. D'où deux critères souvent utilisés : $z$ est réel si et seulement si $\bar z = z$, imaginaire pur si et seulement si $\bar z = -z$. Géométriquement, $\bar z$ est le symétrique de $z$ par rapport à l'axe des abscisses. [[Complément hors du cours|ⓘ]]

## Polynôme complexe du second degré

Le trinôme $az^2 + bz + c$ a **toujours** des solutions dans $\mathbb{C}$. Avec $\Delta = b^2 - 4ac$ (voir [[Équation du second degré]]) :

| Cas | Racines |
|---|---|
| $\Delta > 0$ | $z_1 = \dfrac{-b - \sqrt\Delta}{2a}$, $z_2 = \dfrac{-b + \sqrt\Delta}{2a}$ (réelles) |
| $\Delta = 0$ | $z_1 = z_2 = \dfrac{-b}{2a}$ (racine double) |
| $\Delta < 0$ | $z_1 = \dfrac{-b - i\sqrt{-\Delta}}{2a}$, $z_2 = \overline{z_1} = \dfrac{-b + i\sqrt{-\Delta}}{2a}$ (conjuguées) |

Donc le trinôme se factorise toujours par
$$az^2 + bz + c = a(z - z_1)(z - z_2).$$

Ce tableau suppose $a, b, c$ **réels** ($a \ne 0$) : c'est pour cela que les deux racines sont conjuguées quand $\Delta < 0$. Si les coefficients sont complexes, on cherche un complexe $\delta$ tel que $\delta^2 = \Delta$, et les racines sont $\dfrac{-b \pm \delta}{2a}$. [[Complément hors du cours|ⓘ]]

En développant $a(z - z_1)(z - z_2)$ et en identifiant, on obtient dans tous les cas $z_1 + z_2 = -\dfrac{b}{a}$ et $z_1 z_2 = \dfrac{c}{a}$ : utile pour vérifier ses racines, ou en trouver une seconde quand on en connaît une. [[Complément hors du cours|ⓘ]]

Exemple : $z^2 + z + 1 = 0$. $\Delta = 1 - 4 = -3 < 0$, donc $z_1 = \dfrac{-1 - i\sqrt3}{2}$ et $z_2 = \dfrac{-1 + i\sqrt3}{2}$. Vérification : $z_1 + z_2 = -1$ et $z_1 z_2 = \dfrac{1 + 3}{4} = 1$. Ces deux racines sont notées $j^2$ et $j$, avec $j = e^{2i\pi/3}$ (voir plus bas les racines de l'unité). [[Complément hors du cours|ⓘ]]

Le résultat se généralise : tout polynôme non constant à coefficients complexes a au moins une racine dans $\mathbb{C}$, donc un polynôme de degré $n$ se factorise en $n$ facteurs du premier degré ([[Théorème fondamental de l'algèbre]], ou théorème de d'Alembert-Gauss). C'est ce qui fait de $\mathbb{C}$ un corps « algébriquement clos », contrairement à $\mathbb{R}$, où $x^2 + 1$ n'a pas de racine. [[Complément hors du cours|ⓘ]]

## Forme trigonométrique

![[Chapitre 5 - Complexes - image44.png]]
*Figure : plan complexe ; le point $M(z)$ de coordonnées $(a, b)$, le module $|z| = OM$ (segment rouge) et l'argument $\arg(z)$ (angle bleu depuis l'axe des abscisses).*

- **Module** : $|z| = OM = \sqrt{a^2 + b^2}$.
- **Argument** : $\arg(z) = (\vec u\,;\overrightarrow{OM})\ [2\pi]$, défini modulo $2\pi$.
- **[[Forme trigonométrique et exponentielle|Forme trigonométrique]]** (il y a une infinité de formes trigonométriques pour un nombre complexe, à cause du modulo $2\pi$) :
$$z = |z|(\cos\theta + i\sin\theta), \qquad \theta = \arg(z),$$
avec
$$\cos\theta = \frac{a}{\sqrt{a^2 + b^2}}, \qquad \sin\theta = \frac{b}{\sqrt{a^2 + b^2}}.$$

L'argument n'est défini que pour $z \ne 0$ (le point $O$ ne définit aucune direction). Parmi tous ses arguments, on appelle souvent **argument principal** celui qui est dans $]-\pi, \pi]$. [[Complément hors du cours|ⓘ]]

Méthode pour passer à la forme trigonométrique : calculer $|z|$, puis $\cos\theta$ et $\sin\theta$, et reconnaître un angle remarquable (les **deux** valeurs sont nécessaires : $\cos\theta$ seul ne distingue pas $\theta$ de $-\theta$). Exemple : $z = 1 + i$, $|z| = \sqrt2$, $\cos\theta = \sin\theta = \dfrac{1}{\sqrt2} = \dfrac{\sqrt2}{2}$, donc $\theta = \dfrac{\pi}{4}$ et $1 + i = \sqrt2\left(\cos\dfrac\pi4 + i\sin\dfrac\pi4\right)$. [[Complément hors du cours|ⓘ]]

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

Le cours note aussi : $\forall\theta,\ |\cos\theta + i\sin\theta| = 1$. [[Erreurs du cours#^e-5-complexes|✎]]

## Géométrie dans le plan complexe

Rappels (voir [[Affixe]]) :
- $\overrightarrow{AB}$ a pour affixe $z_B - z_A$ ;
- $\vec u + \vec v$ a pour affixe $z_u + z_v$ ;
- $k\vec u$ a pour affixe $kz_u$.

| Module | Argument (modulo $2\pi$) |
|---|---|
| $\lvert z_B - z_A\rvert = AB$ | $\arg(z_B - z_A) = (\vec u\,;\overrightarrow{AB})$ |
| $\left\lvert\dfrac{z_B - z_C}{z_A - z_C}\right\rvert = \dfrac{CB}{CA}$ | $\arg\left(\dfrac{z_B - z_C}{z_A - z_C}\right) = (\overrightarrow{CA}\,;\overrightarrow{CB})$ |

Conséquences pratiques de ce tableau, pour $A$, $B$, $C$ distincts et $Z = \dfrac{z_B - z_C}{z_A - z_C}$ : [[Complément hors du cours|ⓘ]]

- $A$, $B$, $C$ sont **alignés** si et seulement si $Z$ est réel (l'angle vaut $0$ ou $\pi$) ; [[Complément hors du cours|ⓘ]]
- $(CA) \perp (CB)$ si et seulement si $Z$ est imaginaire pur (l'angle vaut $\pm\frac\pi2$) ; [[Complément hors du cours|ⓘ]]
- le triangle $ABC$ est isocèle en $C$ si et seulement si $|Z| = 1$, et équilatéral si de plus $Z = e^{\pm i\pi/3}$. [[Complément hors du cours|ⓘ]]
- L'ensemble des points $M$ d'affixe $z$ tels que $|z - z_A| = r$ est le cercle de centre $A$ et de rayon $r$ ; celui des points tels que $|z - z_A| = |z - z_B|$ est la médiatrice de $[AB]$. [[Complément hors du cours|ⓘ]]

## Forme exponentielle

$$z = |z|e^{i\theta}, \qquad \theta = \arg(z),$$
$$e^{i\theta} = \cos\theta + i\sin\theta, \qquad e^{-i\theta} = \cos\theta - i\sin\theta.$$

$e^{i\theta}$ est le point du cercle de centre $O$ et de rayon 1 (cercle trigonométrique) repéré par l'angle $\theta$ : $|e^{i\theta}| = 1$. Valeurs à connaître : $e^{i0} = 1$, $e^{i\pi/2} = i$, $e^{i\pi} = -1$, $e^{-i\pi/2} = -i$. La troisième donne l'**identité d'Euler** $e^{i\pi} + 1 = 0$, souvent citée parce qu'elle relie $e$, $i$, $\pi$, $0$ et $1$. [[Complément hors du cours|ⓘ]]

La forme exponentielle rend le produit géométrique : multiplier par $re^{i\alpha}$ multiplie les distances à $O$ par $r$ et fait tourner de l'angle $\alpha$ autour de $O$. Multiplier par $i = e^{i\pi/2}$, c'est tourner d'un quart de tour. Plus généralement, l'image de $M(z)$ par la rotation de centre $\Omega(\omega)$ et d'angle $\alpha$ a pour affixe $z' = \omega + e^{i\alpha}(z - \omega)$. [[Complément hors du cours|ⓘ]]

### Propriétés

$$e^{i\theta} \times e^{i\theta'} = e^{i(\theta + \theta')}, \qquad \left(e^{i\theta}\right)^n = e^{in\theta}, \qquad \frac{e^{i\theta}}{e^{i\theta'}} = e^{i(\theta - \theta')}, \qquad \frac{1}{e^{i\theta}} = e^{-i\theta} = \overline{e^{i\theta}}.$$

Exemple d'usage (calcul de valeurs exactes) : $e^{i\pi/3}e^{-i\pi/4} = e^{i\pi/12}$. En forme algébrique, le même produit vaut $\left(\dfrac12 + i\dfrac{\sqrt3}{2}\right)\left(\dfrac{\sqrt2}{2} - i\dfrac{\sqrt2}{2}\right) = \dfrac{\sqrt2 + \sqrt6}{4} + i\,\dfrac{\sqrt6 - \sqrt2}{4}$. En identifiant les parties réelle et imaginaire : $\cos\dfrac{\pi}{12} = \dfrac{\sqrt6 + \sqrt2}{4}$ et $\sin\dfrac{\pi}{12} = \dfrac{\sqrt6 - \sqrt2}{4}$. [[Complément hors du cours|ⓘ]]

### Conseil du cours : revoir les formules de trigonométrie

Voir [[Formules trigonométriques]] :
- $\cos(x + y) = \cos x\cos y - \sin x\sin y$
- $\cos(x - y) = \cos x\cos y + \sin x\sin y$
- $\sin(x + y) = \sin x\cos y + \cos x\sin y$
- $\sin(x - y) = \sin x\cos y - \cos x\sin y$
- $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$ [[Erreurs du cours#^e-5-complexes|✎]]
- $\sin 2x = 2\sin x\cos x$

## Formule de Moivre et formules d'Euler

**Moivre** :
$$z^n = |z|^n(\cos n\theta + i\sin n\theta).$$

Pour $|z| = 1$, elle s'écrit $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$, c'est-à-dire $\left(e^{i\theta}\right)^n = e^{in\theta}$, vraie pour tout entier $n \in \mathbb{Z}$. Usage type : développer le membre de gauche avec le binôme puis identifier. Pour $n = 2$ : $(\cos\theta + i\sin\theta)^2 = \cos^2\theta - \sin^2\theta + 2i\sin\theta\cos\theta$, d'où $\cos 2\theta = \cos^2\theta - \sin^2\theta$ et $\sin 2\theta = 2\sin\theta\cos\theta$ : on retrouve les formules de duplication. Pour $n = 3$, avec la ligne « 1 3 3 1 » : $\cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta = 4\cos^3\theta - 3\cos\theta$. [[Complément hors du cours|ⓘ]]

**Racines $n$-ièmes de l'unité.** Les solutions de $z^n = 1$ ($n \ge 1$) sont les $n$ complexes $\omega_k = e^{2ik\pi/n}$, $k = 0, 1, \dots, n - 1$ : avec $z = re^{i\theta}$, l'équation impose $r^n = 1$, donc $r = 1$, et $n\theta \equiv 0\ [2\pi]$. Leurs points forment un polygone régulier à $n$ côtés inscrit dans le cercle trigonométrique, et leur somme est nulle pour $n \ge 2$. Pour $n = 3$ : $1$, $j = e^{2i\pi/3}$, $j^2 = \bar j$, avec $1 + j + j^2 = 0$. Voir [[Racine n-ième de l'unité]]. [[Complément hors du cours|ⓘ]]

Conseil du cours : revoir le triangle de Pascal (voir [[Formule de Pascal]], [[Formule du binôme de Newton]]), utile pour développer $(\cos\theta + i\sin\theta)^n$. Triangle donné par le cours : [[Erreurs du cours#^e-5-complexes|✎]]

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
```

**Euler** :
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}.$$

Ces formules servent notamment à la [[Linéarisation trigonométrique]].

Elles s'obtiennent en additionnant ou en soustrayant $e^{i\theta} = \cos\theta + i\sin\theta$ et $e^{-i\theta} = \cos\theta - i\sin\theta$. Linéariser, c'est transformer une puissance de $\cos$ ou de $\sin$ en somme de $\cos(k\theta)$ et $\sin(k\theta)$, par exemple pour la primitiver. Exemple : $\cos^2\theta = \left(\dfrac{e^{i\theta} + e^{-i\theta}}{2}\right)^2 = \dfrac{e^{2i\theta} + 2 + e^{-2i\theta}}{4} = \dfrac{1 + \cos 2\theta}{2}$. La démarche est l'inverse de celle de Moivre, qui va de $\cos n\theta$ vers les puissances. [[Complément hors du cours|ⓘ]]

Les complexes ont été introduits au XVIe siècle par les algébristes italiens pour résoudre les équations du troisième degré, où des racines carrées de nombres négatifs apparaissent en cours de calcul même quand les solutions sont réelles. On les emploie aujourd'hui en électricité (impédances en courant alternatif, où l'on note $j$ au lieu de $i$ pour ne pas confondre avec l'intensité), en traitement du signal ([[Série de Fourier|séries de Fourier]]) et en physique des ondes. [[Complément hors du cours|ⓘ]]
