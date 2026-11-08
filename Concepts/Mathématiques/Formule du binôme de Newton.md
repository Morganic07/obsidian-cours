---
type: concept
tags: [year1]
aliases: [binôme de Newton, formule du binôme]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]", "[[Raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé.pdf]]", "[[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]]"]
maj: 2026-11-08
---

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k},$$

démontrée par récurrence au chapitre 0 d'analyse. Avec $a = b = 1$ on obtient $2^n$ ; avec $a = 1, b = -1$, on obtient $0$ pour $n \ge 1$ (la somme vaut 1 pour $n = 0$). [[Erreurs du cours#^e-formule-du-binome-de-newton|✎]] Les DS s'en servent pour des sommes comme $\sum (-1)^k\binom{n}{k} / 3^{k+1}$.

**Outil Maths** : le cours ne développe pas la formule. L'exercice 19 de la feuille 1 demande d'exprimer $(a+b)^n$ avec les $\binom{n}{k}$, puis de calculer $\sum_{k=0}^{n} \binom{n}{k}$ et $\sum_{k=0}^{n} \binom{n}{k}(-1)^k$. L'exercice 18 demande de prouver, pour tous $n, p, k \in \mathbb{N}$ avec $n \ge p \ge k$, $\binom{n}{k}\binom{n-k}{p-k} = \binom{p}{k}\binom{n}{p}$. [[Erreurs du cours#^e-formule-du-binome-de-newton|✎]]

## Compléments (complément, hors du cours)

**Idée de l'hérédité** : on suppose la formule vraie au rang $n$ et l'on développe
$$(a+b)^{n+1} = (a+b)(a+b)^n = \sum_{k=0}^{n}\binom nk a^{k+1}b^{n-k} + \sum_{k=0}^{n}\binom nk a^k b^{n+1-k}.$$
Dans la première somme, on [[Changement d'indice|décale l'indice]] ($j = k+1$) : elle devient $\sum_{j=1}^{n+1}\binom n{j-1}a^jb^{n+1-j}$. On isole les termes extrêmes ($a^{n+1}$ et $b^{n+1}$), puis on regroupe les deux sommes de $1$ à $n$ avec la [[Formule de Pascal]] $\binom n{j-1}+\binom nj = \binom{n+1}j$, ce qui donne la formule au rang $n+1$.

**Domaine de validité** : la formule vaut pour des réels, des complexes, et plus généralement pour deux éléments d'un anneau qui commutent ($ab = ba$). Elle est fausse pour deux [[Matrice|matrices]] qui ne commutent pas : $(A+B)^2 = A^2 + AB + BA + B^2$, qui ne vaut $A^2 + 2AB + B^2$ que si $AB = BA$.

**Petits cas** : $n = 2$ et $n = 3$ donnent les identités remarquables
$$(a+b)^2 = a^2+2ab+b^2, \qquad (a+b)^3 = a^3+3a^2b+3ab^2+b^3,$$
dont les coefficients sont les lignes $1\ 2\ 1$ et $1\ 3\ 3\ 1$ du triangle de Pascal. Avec $b$ remplacé par $-b$, les signes alternent : $(a-b)^3 = a^3-3a^2b+3ab^2-b^3$.

**Formule voisine** (factorisation de $a^n - b^n$) : pour $n \ge 1$,
$$a^n - b^n = (a-b)\sum_{k=0}^{n-1}a^k b^{n-1-k},$$
par exemple $a^2-b^2 = (a-b)(a+b)$ et $a^3-b^3 = (a-b)(a^2+ab+b^2)$. Avec $a = q$ et $b = 1$, c'est la somme d'une [[Suite géométrique]].

Notion parente : [[Dénombrement]]. Voir aussi : [[Coefficient binomial]], [[Récurrence]], [[Formule de Leibniz]], [[Formule de Pascal]], [[Changement d'indice]], [[Suite géométrique]].

Résumés : [[0 - Rappels-etc]]
