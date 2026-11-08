---
type: concept
tags: [year1]
aliases: [moyenne arithmétique, moyenne géométrique, moyenne harmonique, inégalité AM-GM, AM-GM inequality]
matieres: [Analyse Maths]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]"]
maj: 2026-11-08
---

Pour $0 < x \le y$, avec la moyenne arithmétique $A = \frac{x+y}{2}$, la moyenne géométrique $G = \sqrt{xy}$ et la moyenne harmonique $H$ définie par $\frac1H = \frac12\left(\frac1x + \frac1y\right)$ :

$$x \le H \le G \le A \le y.$$

**Méthode** : partir du carré $(\sqrt x - \sqrt y)^2 \ge 0$. Le TD s'en sert aussi pour montrer $0 < \frac{mn}{(m+n)^2} \le \frac14$.

**Preuve à deux termes (complément, hors du cours)** : pour $a, b \ge 0$,
$$\frac{a+b}{2} - \sqrt{ab} = \frac{a + b - 2\sqrt{ab}}{2} = \frac{(\sqrt a - \sqrt b)^2}{2} \ge 0,$$
donc $\frac{a+b}{2} \ge \sqrt{ab}$, avec égalité si et seulement si $\sqrt a = \sqrt b$, c'est-à-dire $a = b$.

**Lien avec le chapitre 0 (complément, hors du cours)** : l'exemple 2 de [[0 - Rappels-etc]], $x + \frac1x \ge 2$ pour $x > 0$, en est le cas $a = x$, $b = \frac1x$ : $\frac{x + 1/x}{2} \ge \sqrt{x \cdot \frac1x} = 1$, avec égalité si et seulement si $x = 1$.

Voir aussi : [[Inégalité de Bernoulli]].

Résumés : [[0 - Rappels-etc]] ; rapprochement (complément hors du cours) : [[0 - rappels pdf]]
