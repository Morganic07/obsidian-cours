---
type: concept
tags: [year2]
aliases: [inversion locale, théorème d'inversion globale, inverse function theorem]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-08
---

**Énoncé (complément, hors du cours)** : soit $U$ un ouvert de $\mathbb{R}^p$, $\varphi : U \to \mathbb{R}^p$ de classe $\mathcal{C}^1$ et $a \in U$ tel que le jacobien $\det J_\varphi(a) \ne 0$. Il existe un ouvert $U' \ni a$ et un ouvert $V' \ni \varphi(a)$ tels que $\varphi$ réalise un $\mathcal{C}^1$-[[Difféomorphisme|difféomorphisme]] de $U'$ sur $V'$. De plus
$$J_{\varphi^{-1}}(\varphi(a)) = J_\varphi(a)^{-1}.$$

- **Le résultat est local** : un jacobien partout non nul ne donne pas la bijectivité globale. Les coordonnées polaires $(\rho, \theta) \mapsto (\rho\cos\theta, \rho\sin\theta)$ ont pour jacobien $\rho \ne 0$ sur $\mathbb{R}_+^* \times \mathbb{R}$, mais ne sont pas injectives ($\theta$ et $\theta + 2\pi$ ont la même image) : il faut restreindre $\theta$, par exemple à $]-\pi, \pi[$, pour obtenir un difféomorphisme.
- **Version globale** : si $\varphi : U \to \mathbb{R}^p$ est de classe $\mathcal{C}^1$, injective, et de jacobien partout non nul, alors $\varphi(U)$ est un ouvert et $\varphi$ est un $\mathcal{C}^1$-difféomorphisme de $U$ sur $\varphi(U)$.
- La formule sur les jacobiennes généralise $(f^{-1})'(f(a)) = 1/f'(a)$ en une variable.

## Dans le cours

Le cours ne le nomme pas. Ses propriétés 13 (caractérisation rapide d'un difféomorphisme) et 14 (jacobien non nul ⇒ différentielle bijective) en sont proches : la propriété 13 suppose la bijection globale, que le théorème d'inversion locale ne fournit pas. Il apparaît dans les compléments de [[4 - Calcul différentiel du premier ordre]].

Voir aussi : [[Difféomorphisme]], [[Matrice jacobienne]], [[Coordonnées polaires]], [[Différentielle]].

Résumés : [[4 - Calcul différentiel du premier ordre]]
