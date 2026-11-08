---
type: concept
tags: [year2]
aliases: [intégrale impropre, improper integral, intégrales généralisées, intégrales impropres]
sources: ["[[Raw/Year 2/Analyse/chp7/Chap7-Integration.docx|Chap7-Integration]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'[[Intégrale|intégrale]] sur un segment s'étend à un intervalle non borné ou à une fonction non bornée près d'une borne, par passage à la limite.

- **Borne infinie** : pour $f$ continue sur $[a, +\infty[$,
$$\int_a^{+\infty} f(t)\,dt = \lim_{x \to +\infty} \int_a^x f(t)\,dt$$
si cette limite existe et est finie : on dit que l'intégrale **converge** ; sinon elle **diverge**.
- **Fonction non bornée en une borne** : pour $f$ continue sur $]a, b]$, $\int_a^b f = \lim_{x \to a^+} \int_x^b f$ sous la même condition.
- **Deux bornes « impropres »** : sur $]a, b[$ (bornes éventuellement infinies), on coupe en un point $c$ et l'on demande que $\int_a^c f$ et $\int_c^b f$ convergent **toutes les deux** ; la valeur ne dépend pas de $c$. Ainsi $\int_{-\infty}^{+\infty} t\,dt$ diverge, même si $\int_{-x}^{x} t\,dt = 0$ pour tout $x$.

**Intégrales de référence** :
$$\int_1^{+\infty} \frac{dt}{t^\alpha} \text{ converge} \iff \alpha > 1, \qquad \int_0^1 \frac{dt}{t^\alpha} \text{ converge} \iff \alpha < 1, \qquad \int_0^{+\infty} e^{-t}\,dt = 1.$$
Pour $\alpha \neq 1$, $\int_1^x t^{-\alpha}\,dt = \frac{x^{1-\alpha} - 1}{1 - \alpha}$, qui a une limite finie en $+\infty$ si et seulement si $\alpha > 1$ (la limite vaut alors $\frac{1}{\alpha - 1}$) ; pour $\alpha = 1$, $\ln x \to +\infty$.

**Critères pour $f \geq 0$** (la fonction $x \mapsto \int_a^x f$ est alors croissante, donc converge si et seulement si elle est majorée) :
- **Comparaison** : si $0 \le f \le g$ au voisinage de la borne et si $\int g$ converge, alors $\int f$ converge ; si $\int f$ diverge, $\int g$ diverge.
- **Équivalents** : si $f \sim g$ au voisinage de la borne ([[Comparaison asymptotique]]), avec $g \ge 0$, les deux intégrales sont de même nature.
- Exemple : $\frac{1}{1 + t^2} \le \frac{1}{t^2}$ sur $[1, +\infty[$, donc $\int_1^{+\infty} \frac{dt}{1+t^2}$ converge ; en fait $\int_0^{+\infty} \frac{dt}{1+t^2} = \lim_{x\to+\infty} \arctan x = \frac{\pi}{2}$.

**Convergence absolue** : si $\int |f|$ converge, alors $\int f$ converge. La réciproque est fausse : $\int_1^{+\infty} \frac{\sin t}{t}\,dt$ converge sans converger absolument.

**Usages** : densités de probabilité d'une variable continue ($\int_{-\infty}^{+\infty} f = 1$, par exemple pour la [[Loi normale]]), [[Fonction Gamma]] $\Gamma(x) = \int_0^{+\infty} t^{x-1}e^{-t}\,dt$, et [[Comparaison série-intégrale]] (pour $f$ positive décroissante, $\sum f(n)$ et $\int_1^{+\infty} f$ sont de même nature).

## Dans le cours

Le cours ne la traite pas : le chapitre 7 reste sur les segments et les fonctions continues. Elle est seulement nommée dans les compléments de [[1 - Integration]].

Voir aussi : [[Intégrale]], [[Comparaison série-intégrale]], [[Fonction Gamma]], [[Comparaison asymptotique]], [[Loi normale]].

Résumés : [[1 - Integration]]
