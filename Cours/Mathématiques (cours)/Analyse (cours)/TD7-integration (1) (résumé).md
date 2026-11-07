---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de TD7-integration ([[Raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1).pdf]]) (3 pages, texte, sans corrigé), dans [[Analyse (index)]]. Il accompagne le cours [[chp 7 - Integration (résumé)]]. L'en-tête du PDF porte « TD 6 », « 2020-2021 », « PréIng 1 » : c'est le TD d'intégration de l'ancien programme.

Le document ne contient que les énoncés : aucune correction, sauf le résultat de l'exercice 6. Il n'a pas de figure (la seule image est le logo). Les « pistes » ci-dessous ne sont pas dans le TD : elles renvoient aux résultats du cours.

## Énoncés

### Exercice 1 — fonction en escalier
Soit $f$ définie sur $[0,4]$ par
$$f(x) = \begin{cases} -1 & \text{si } x = 0 \\ 1 & \text{si } 0 < x < 1 \\ 3 & \text{si } x = 1 \\ -2 & \text{si } 1 < x \le 2 \\ 4 & \text{si } 2 < x \le 4. \end{cases}$$
1. Calculer $\int_0^4 f(t)\,dt$.
2. Pour $x \in [0,4]$, calculer $F(x) = \int_0^x f(t)\,dt$.
3. Montrer que $F$ est continue sur $[0,4]$. $F$ est-elle dérivable sur $[0,4]$ ?

*Piste :* $f$ est en escalier ; ses valeurs aux points isolés ne changent pas l'intégrale. $F$ est continue même si $f$ ne l'est pas, mais dérivable seulement là où $f$ est continue.

### Exercice 2 — intégrales par morceaux
Calculer :
1. $\int_1^3 |2t - 5|\,dt$ ;
2. $\int_0^\pi \sqrt{E(t)}\,dt$ ($E$ : [[Partie entière|partie entière]]) ;
3. $\int_0^\pi \min(2, t)\,dt$ ;
4. $\int_{-1}^2 t|t|\,dt$.

*Piste :* découper en intervalles où la fonction intégrée a une expression simple ([[Relation de Chasles]]).

### Exercice 3 — vrai ou faux sur $F(x) = \int_0^x f$
Soit $f : \mathbb{R} \to \mathbb{R}$ continue et $F(x) = \int_0^x f(t)\,dt$. Vrai ou faux :
1. $F$ est continue sur $\mathbb{R}$.
2. $F$ est dérivable sur $\mathbb{R}$ de dérivée $f$.
3. Si $f$ est croissante sur $\mathbb{R}$, $F$ est croissante sur $\mathbb{R}$.
4. Si $f$ est positive sur $\mathbb{R}$, $F$ est positive sur $\mathbb{R}$.
5. Si $f$ est positive sur $\mathbb{R}$, $F$ est croissante sur $\mathbb{R}$.
6. Si $f$ est $T$-périodique, $F$ est $T$-périodique.
7. Si $f$ est paire, $F$ est impaire.

*Piste :* théorème fondamental de l'analyse ($F' = f$). Attention au signe de $F$ pour $x < 0$ et au fait que $\int_0^T f$ n'est pas forcément nulle.

### Exercice 4 — cas d'égalité
Déterminer les fonctions $f$ continues sur $[a,b]$ telles que
$$\int_a^b f(t)\,dt = (b-a)\sup_{[a,b]} |f|.$$

*Piste :* majoration $\int f \le \int |f| \le (b-a)\sup|f|$, puis « fonction continue positive d'intégrale nulle est nulle ».

### Exercice 5 — moyenne d'une fonction
Soit $f \in \mathcal{C}^0(\mathbb{R})$ et $g : \mathbb{R}^* \to \mathbb{R}$, $x \mapsto \frac{1}{x}\int_0^x f(t)\,dt$.
1. Montrer que $g$ se [[Prolongement par continuité|prolonge par continuité]] en $0$.
2. On suppose $f$ $T$-périodique. Montrer que $\forall k \in \mathbb{N}$, $\int_{kT}^{(k+1)T} f(t)\,dt = \int_0^T f(t)\,dt$.
3. Écrire $g(x) = \frac{1}{x}\int_0^{nT} f(t)\,dt + \frac{1}{x}\int_{nT}^x f(t)\,dt$ pour un entier $n$ bien choisi, et en déduire que $g$ admet une limite en $+\infty$.

*Piste :* (1) dérivée en $0$ de $F(x) = \int_0^x f$ ; (2) [[Parité et périodicité d'une intégrale|périodicité de l'intégrale]].

### Exercice 6 — changement de variable
$$I = \int_0^{\ln 2} \sqrt{e^x - 1}\,dx.$$
Effectuer le [[Changement de variable dans une intégrale|changement de variable]] $u = \sqrt{e^x - 1}$ et calculer $I$.

**Résultat (donné par le TD) :** $I = 2 - \dfrac{\pi}{2}$.

### Exercice 7 — primitives
1. $\displaystyle\int \frac{dx}{\sqrt{2+x} + \sqrt[3]{2+x}}$, avec $t = \sqrt[6]{2+x}$ ;
2. $\displaystyle\int (\arcsin x)^2\,dx$ ;
3. $\displaystyle\int x^2\sqrt{1 + x^3}\,dx$.

### Exercice 8 — primitives
$$\int e^x \cos x\,dx \;;\quad \int \frac{\ln x}{x^n}\,dx\ (n \in \mathbb{N}) \;;\quad \int x \arctan x\,dx \;;\quad \int (x^2 + x + 1)\,e^x\,dx.$$

*Piste :* [[Intégration par parties|intégrations par parties]], éventuellement répétées.

### Exercice 9
Soit $I_n = \int_0^1 (1 - t^2)^n\,dt$.
1. Établir une relation de récurrence entre $I_n$ et $I_{n+1}$.
2. Calculer $I_n$.
3. En déduire $\displaystyle\sum_{k=0}^{n} \frac{(-1)^k}{2k+1}\binom{n}{k}$.

*Piste :* pour (3), développer $(1-t^2)^n$ par la [[Formule du binôme de Newton]].

### Exercice 10 — [[Intégrales de Wallis]]
Soit $I_n = \int_0^{\pi/2} \sin^n t\,dt$.
1. Établir une relation de récurrence entre $I_n$ et $I_{n+2}$.
2. En déduire $I_{2p}$ et $I_{2p+1}$.
3. Montrer que $(I_n)_{n \in \mathbb{N}}$ est décroissante et strictement positive.
4. En déduire que $I_n \sim I_{n+1}$.
5. Calculer $n I_n I_{n+1}$.
6. Donner un [[Équivalent (comparaison asymptotique)|équivalent]] simple de $I_n$.

### Exercice 11
Soit $I_n = \int_0^1 \frac{x^n}{1+x}\,dx$.
1. En majorant la fonction intégrée, montrer que $I_n \to 0$.
2. Calculer $I_n + I_{n+1}$.
3. Déterminer $\displaystyle\lim_{n\to+\infty} \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k}$.

### Exercice 12 — fractions rationnelles
[[Décomposition en éléments simples|Décomposer]] puis calculer les primitives de :
1. $\dfrac{x^3}{x^2 - 4}$ ;
2. $\dfrac{4x}{(x-2)^2}$ ;
3. $\dfrac{3t + 1}{t^2 - 2t + 10}$ ;
4. $\dfrac{1}{t^3 + 1}$.

### Exercice 13 — sommes de Riemann
Calculer :
$$\lim_{n\to\infty} \prod_{k=1}^{n}\left(1 + \frac{k^2}{n^2}\right)^{1/n} \;;\quad \lim_{n\to\infty} n\sum_{k=1}^{n} \frac{e^{-n/k}}{k^2} \;;\quad \lim_{n\to\infty} \sum_{k=1}^{n} \frac{n+k}{n^2+k^2} \;;\quad \lim_{n\to\infty} \sum_{k=1}^{n-1} \frac{1}{\sqrt{n^2-k^2}}.$$

*Piste :* reconnaître une [[Somme de Riemann]] $\frac{1}{n}\sum f(k/n)$ ; pour le produit, passer au logarithme.

### Exercice 14
1. $\displaystyle\lim_{n\to\infty} \frac{1 + \sqrt{2} + \sqrt{3} + \dots + \sqrt{n}}{n\sqrt{n}}$ ;
2. $\displaystyle\lim_{n\to\infty} \sum_{p=1}^{n} \frac{n}{n^2 + p^2}$.

### Exercice 15
Sans calculer les intégrales, montrer que $\displaystyle\int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \cos^n x\,dx$.

*Piste :* changement de variable $t = \frac{\pi}{2} - x$.

### Exercice 16 — calculs d'intégrales
$$\int_0^1 \frac{t}{\sqrt{1-t^2}}\,dt, \qquad \int_0^a \sqrt{a^2 - t^2}\,dt, \qquad \int_0^\pi t^2 \sin t\,dt, \qquad \int_{1-\frac{\pi^2}{4}}^{1} \cos\sqrt{1-t}\,dt.$$

*Piste :* primitive directe ($u'/\sqrt{u}$), $t = a\sin u$, deux intégrations par parties, $u = \sqrt{1-t}$.

## Thèmes, en un coup d'œil

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

## Points à vérifier

1. Le fichier s'appelle « TD7 » mais son en-tête dit « TD 6 » (2020-2021, PréIng 1) : la numérotation ne correspond pas à celle du chapitre 7 du cours actuel.
2. Exercice 8 : $\int \frac{\ln x}{x^n}\,dx$ est donné pour $n \in \mathbb{N}$ ; le cas $n = 1$ se traite à part (primitive $\frac{(\ln x)^2}{2}$).
