---
type: concept
aliases: [intégrale double, intégrales doubles, intégrales multiples, théorème de Fubini, Fubini]
matieres: [Analyse]
sources: ["[[raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples]]"]
maj: 2026-11-06
---

Une intégrale multiple étend l'[[Intégrale]] d'une variable à une fonction de plusieurs variables, sur un domaine de $\mathbb{R}^2$ ou $\mathbb{R}^n$. Source : [[Chp9-intégrales multiples (résumé)]].

## Domaines

- **Pavé** : produit de segments $\prod [a_i, b_i]$.
- **Compact élémentaire** de 1er type : $a \le x \le b$ et $y_1(x) \le y \le y_2(x)$. De 2e type : les rôles de $x$ et $y$ sont échangés.

## Calcul

- **Fubini** : pour $f$ continue sur un pavé, on intègre dans l'ordre que l'on veut, et le résultat est le même.
- Sur un compact élémentaire, l'ordre est imposé par la description du domaine : les bornes de l'intégrale intérieure dépendent de la variable extérieure. Pour un type 1, on intègre en $y$ puis en $x$.
- L'aire d'un domaine est $\iint_D 1\,dx\,dy$.

## Changement de variable

Pour une bijection $\varphi$ de $\Delta$ sur $D$ : $\iint_D f\,dx\,dy = \iint_\Delta f(\varphi(u,v))\,|J_\varphi|\,du\,dv$, où $J_\varphi$ est le déterminant de la [[Matrice jacobienne]].

- Polaires (disques, cercles) : $x = r\cos\theta$, $y = r\sin\theta$.
- Elliptiques : $x = ar\cos\theta$, $y = br\sin\theta$, jacobien $abr$.

Voir aussi [[Dérivée partielle]], [[Difféomorphisme]], [[Year 2 - Analyse]].
