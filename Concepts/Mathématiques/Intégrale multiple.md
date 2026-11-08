---
type: concept
tags: [year2]
aliases: [intégrale double, intégrales doubles, intégrales multiples, intégrale triple, intégrales triples, théorème de Fubini, Fubini, intégrale double sur un pavé, "aire d'une figure", double integral, multiple integral]
matieres: [Analyse]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-08
---

Une intégrale multiple étend l'[[Intégrale]] d'une variable à une fonction de plusieurs variables, sur un domaine de $\mathbb{R}^2$ ou $\mathbb{R}^n$. Source : [[2 - intégrales multiples]].

**Interprétation (complément, hors du cours)** : pour $f \ge 0$ continue sur $D$, $\iint_D f\,dx\,dy$ est le volume du solide compris entre le domaine $D$ du plan $(xOy)$ et la surface $z = f(x,y)$. Avec $f = 1$, on retrouve l'aire de $D$.

## Propriétés (complément, hors du cours)

Comme l'intégrale simple, l'intégrale double est :
- **linéaire** : $\iint_D (\lambda f + \mu g) = \lambda\iint_D f + \mu\iint_D g$ ;
- **positive** et donc croissante : $f \ge 0$ sur $D$ entraîne $\iint_D f \ge 0$, et $f \le g$ entraîne $\iint_D f \le \iint_D g$ ; en particulier $\left|\iint_D f\right| \le \iint_D |f|$ ;
- **additive par rapport au domaine** : si $D = D_1 \cup D_2$ avec $D_1 \cap D_2$ d'aire nulle (une frontière commune), $\iint_D f = \iint_{D_1} f + \iint_{D_2} f$. C'est ce qui justifie de découper un domaine compliqué en compacts élémentaires.

## Domaines

- **Pavé** : produit de segments $\prod [a_i, b_i]$.
- **Compact élémentaire** de 1er type : $a \le x \le b$ et $y_1(x) \le y \le y_2(x)$. De 2e type : les rôles de $x$ et $y$ sont échangés.

## Calcul

- **Fubini** : pour $f$ continue sur un pavé $P = [a,b]\times[c,d]$, $\iint_P f\,dx\,dy = \int_c^d\left(\int_a^b f\,dx\right)dy = \int_a^b\left(\int_c^d f\,dy\right)dx$ : on intègre dans l'ordre qui arrange, et le résultat est le même.
- Sur un compact élémentaire, l'ordre est imposé par la description du domaine : les bornes de l'intégrale intérieure dépendent de la variable extérieure. Pour un type 1, on intègre en $y$ puis en $x$.
- L'aire d'une figure $D$ est $A(D) = \iint_D 1\,dx\,dy$.
- **Variables séparées sur un pavé (complément, hors du cours)** : si $f(x,y) = g(x)h(y)$ avec $g$, $h$ continues, Fubini donne $\iint_{[a,b]\times[c,d]} g(x)h(y)\,dx\,dy = \left(\int_a^b g(x)\,dx\right)\left(\int_c^d h(y)\,dy\right)$. Ce n'est vrai que sur un pavé : sur un compact élémentaire, les bornes dépendent de l'autre variable.
- **Intervertir l'ordre d'intégration (complément, hors du cours)** : on redécrit le même domaine dans l'autre type. Exemple : $\int_0^1\int_y^1 e^{x^2}\,dx\,dy$ ne se calcule pas dans cet ordre ($e^{x^2}$ n'a pas de primitive explicite). Le domaine $\{0 \le y \le 1,\ y \le x \le 1\}$ s'écrit aussi $\{0 \le x \le 1,\ 0 \le y \le x\}$, d'où
$$\int_0^1\int_y^1 e^{x^2}\,dx\,dy = \int_0^1\left(\int_0^x dy\right)e^{x^2}\,dx = \int_0^1 x\,e^{x^2}\,dx = \left[\tfrac12 e^{x^2}\right]_0^1 = \frac{e-1}{2}.$$

## Intégrales triples (complément, hors du cours)

Tout s'étend à $\mathbb{R}^3$ : $\iiint_V f\,dx\,dy\,dz$ se calcule par Fubini en trois intégrales emboîtées, et le volume d'un solide $V$ est $\mathrm{Vol}(V) = \iiint_V 1\,dx\,dy\,dz$. Les changements de variables usuels sont les [[Coordonnées cylindriques]] ($dx\,dy\,dz = r\,dr\,d\theta\,dz$) et les [[Coordonnées sphériques]] ($x = r\sin\varphi\cos\theta$, $y = r\sin\varphi\sin\theta$, $z = r\cos\varphi$, $dx\,dy\,dz = r^2\sin\varphi\,dr\,d\varphi\,d\theta$, avec $\varphi \in [0,\pi]$ l'angle mesuré depuis l'axe $Oz$). Exemple : le volume de la boule de rayon $R$ vaut $\int_0^{2\pi}\int_0^{\pi}\int_0^R r^2\sin\varphi\,dr\,d\varphi\,d\theta = 2\pi \cdot 2 \cdot \frac{R^3}{3} = \frac43\pi R^3$.

## Changement de variable

Pour une bijection $\varphi$ de $\Delta$ sur $D$ : $\iint_D f\,dx\,dy = \iint_\Delta f(\varphi(u,v))\,|J_\varphi|\,du\,dv$, où $J_\varphi$ est le déterminant de la [[Matrice jacobienne]].

**Hypothèse exacte (complément, hors du cours)** : $\varphi$ doit être un [[Difféomorphisme]] de classe $C^1$ de l'intérieur de $\Delta$ sur l'intérieur de $D$ ; il peut cesser d'être bijectif sur les bords, qui sont d'aire nulle (c'est le cas des polaires en $r = 0$ ou $\theta = 2\pi$). $|J_\varphi(u,v)|$ est le facteur local de dilatation des aires : un petit rectangle d'aire $du\,dv$ est envoyé sur un quasi-parallélogramme d'aire $|J_\varphi|\,du\,dv$.

- Polaires (disques, cercles) : $x = r\cos\theta$, $y = r\sin\theta$. Les notes n'écrivent pas le jacobien polaire (vérifié sur la page 3). Calcul (complément, hors du cours) : $J = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta + r\sin^2\theta = r$, d'où $dx\,dy = r\,dr\,d\theta$. Application classique : l'[[Intégrale de Gauss]] $\int_{-\infty}^{+\infty} e^{-x^2}dx = \sqrt\pi$, obtenue en passant son carré en polaires.
- Elliptiques : $x = ar\cos\theta$, $y = br\sin\theta$, jacobien $abr$.

Notion parente : [[Intégrale]]. Voir aussi : [[Pavé]], [[Compact élémentaire]], [[Coordonnées polaires]], [[Coordonnées elliptiques]], [[Coordonnées cylindriques]], [[Coordonnées sphériques]], [[Intégrale de Gauss]], [[Changement de variable dans une intégrale]], [[Matrice jacobienne]], [[Dérivée partielle]], [[Difféomorphisme]], [[Cours/Mathématiques/Analyse/_index|Analyse]].

Résumé : [[2 - intégrales multiples]]
