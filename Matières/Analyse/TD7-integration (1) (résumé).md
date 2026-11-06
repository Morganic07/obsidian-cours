---
type: source
tags: [year2]
sources: [".raw/Year 2/Analyse/chp7/TD7-integration (1).pdf"]
maj: 2026-11-06
---

Résumé de TD7-integration (`.raw/Year 2/Analyse/chp7/TD7-integration (1).pdf`) (3 pages, texte, sans corrigé), dans [[Analyse (matière)]]. Il accompagne le cours [[Chap7-Integration (résumé)]]. L'en-tête du PDF porte « TD 6 », « 2020-2021 », « PréIng 1 » : c'est le TD d'intégration de l'ancien programme.

## Thèmes des 16 exercices

| Exercices | Thème | Méthode attendue |
|---|---|---|
| 1 | Fonction en escalier, $F(x) = \int_0^x f$ : continuité et dérivabilité de $F$ | Calcul par morceaux. $F$ est continue même si $f$ ne l'est pas, mais dérivable seulement là où $f$ est continue |
| 2 | Intégrales avec $\lvert\cdot\rvert$, partie entière $E$, $\min$, $t\lvert t\rvert$ | Découper en intervalles où la fonction est simple |
| 3 | Vrai ou faux sur $F(x) = \int_0^x f$ ($f$ continue) : continuité, dérivée, croissance, positivité, périodicité, parité | Théorème fondamental. Pièges : $f$ croissante ne rend pas $F$ croissante, $f$ périodique ne rend pas $F$ périodique, et $f$ positive rend $F$ croissante |
| 4 | Cas d'égalité $\int_a^b f = (b-a)\sup\lvert f\rvert$ | Cas d'égalité de l'inégalité de la moyenne, avec la propriété « continue positive d'intégrale nulle est nulle » |
| 5 | Moyenne $g(x) = \frac1x\int_0^x f$ : prolongement en $0$, limite en $+\infty$ pour $f$ périodique | Dérivée en 0 de $F$, périodicité de l'intégrale, découpage $\frac1x\int_0^{nT} + \frac1x\int_{nT}^x$ |
| 6 | Changement de variable $u = \sqrt{e^x - 1}$ | Résultat donné : $I = 2 - \pi/2$ |
| 7, 8 | Primitives : racines, $(\arcsin x)^2$, $x^2\sqrt{1+x^3}$, $e^x\cos x$, $\ln x / x^n$, $x\arctan x$, $(x^2+x+1)e^x$ | Changement de variable (indice $t = \sqrt[6]{2+x}$), intégrations par parties répétées |
| 9, 10 | $I_n = \int_0^1 (1-t^2)^n\,dt$ et intégrales de Wallis $\int_0^{\pi/2} \sin^n t\,dt$ | Intégration par parties pour une relation de récurrence, valeurs de $I_{2p}$ et $I_{2p+1}$, décroissance, $I_n \sim I_{n+1}$, $n I_n I_{n+1}$ constant, équivalent de $I_n$ |
| 11 | $I_n = \int_0^1 \frac{x^n}{1+x}\,dx$ | Majoration (limite nulle), $I_n + I_{n+1}$, puis limite de $\sum (-1)^{k+1}/k$ |
| 12 | Décomposition en éléments simples et primitives de fractions rationnelles | $x^3/(x^2-4)$, $4x/(x-2)^2$, $(3t+1)/(t^2-2t+10)$, $1/(t^3+1)$ |
| 13, 14 | Limites de produits et sommes qui sont des sommes de Riemann | Reconnaître $\frac1n \sum f(k/n)$ (voir « Approximation » dans le cours) |
| 15 | $\int_0^{\pi/2} \sin^n = \int_0^{\pi/2} \cos^n$ sans calcul | Changement de variable $t \mapsto \pi/2 - t$ |
| 16 | Intégrales à calculer : $t/\sqrt{1-t^2}$, $\sqrt{a^2-t^2}$, $t^2\sin t$, $\cos\sqrt{1-t}$ | Primitive directe, $t = a\sin u$, deux intégrations par parties, $u = \sqrt{1-t}$ |

## À retenir pour réviser

- Un tiers du TD tourne autour de $F(x) = \int_0^x f$ : bien distinguer ce que donne la continuité de $f$ (le théorème fondamental) de ce qu'on ne peut pas dire sans elle.
- Les intégrales de Wallis et la relation entre $I_n$ et $I_{n+2}$ sont un classique du semestre : on retrouve la même chaîne (récurrence, parité de l'indice, équivalent).
- Les exercices 13 et 14 ne demandent aucun calcul de primitive : tout se ramène à une [[Intégrale]] de la fonction limite.

## Liens

[[Intégrale]], [[Primitive]], [[Comparaison asymptotique]] (équivalent de $I_n$), [[Limite et continuité]], [[Série numérique]] (somme alternée de l'exercice 11).
