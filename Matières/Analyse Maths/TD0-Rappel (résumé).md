---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de TD0-Rappel ([[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel.pdf]]) (2 pages, sans corrigé), dans [[Analyse Maths (matière)]]. TD d'accompagnement de [[Chap0-Rappels-etc (résumé)]]. Version 2020-2021 (PréING1, département de mathématiques).

Le document ne donne que les énoncés : aucune correction. Les « pistes » ci-dessous sont des méthodes ajoutées pour réviser, pas des corrections du TD. Aucune figure (seule image : le logo).

## Vue d'ensemble

| Ex. | Thème | Piste de méthode (ajoutée) |
|---|---|---|
| 1 | Inégalités classiques | Passer tout d'un côté et reconnaître un carré, ou développer $(x-y)^2 \ge 0$ |
| 2 | Encadrement et minimum d'une fraction rationnelle | Forme canonique : $x^2+2x+2 = (x+1)^2+1 \ge 1$ |
| 3 | Encadrements de combinaisons | Règles d'addition, de produit, d'inverse (attention aux signes) |
| 4 | Signe de $x$ quand $\lvert x-a\rvert < \lvert a\rvert$ | Inégalité triangulaire |
| 5 | Inéquations avec valeurs absolues et racines | Distinguer des cas, élever au carré en vérifiant les signes, tableau de signes |
| 6 | Sommes et produits | Télescopage avec $(k+1)^2 - k^2 = 2k+1$ ; $(k+1)^3 - k^3$ pour obtenir $\sum k^2$ |
| 7 | Somme de coefficients binomiaux | Formule de Pascal en cascade |
| 8 | Domaine de définition | Signe d'un quotient |
| 9 | Formules de trigonométrie | À partir de $\sin(x+y)$, $\cos(x+y)$ |
| 10 | Valeurs en $\pi/12$ | $\pi/12 = \pi/3 - \pi/4$ |
| 11 | Équations trigonométriques | Factoriser, formules de duplication |

## Exercice 1 : inégalités

Voir [[Règles de calcul sur les inégalités]].

Montrer les inégalités suivantes.

1. $\forall x \in\, ]0, +\infty[,\ x + \dfrac{1}{x} \ge 2$
2. $\forall x, y \in \mathbb{R},\ xy \le \dfrac{1}{2}(x^2 + y^2)$
3. $\forall x, y \in \mathbb{R},\ xy \le \left(\dfrac{x+y}{2}\right)^2$
4. $\forall x, y, z \in \mathbb{R},\ x^2 + y^2 + z^2 \ge xy + yz + zx$

## Exercice 2 : fraction rationnelle

1. Démontrer que $\forall x \in \mathbb{R},\ 0 < \dfrac{x^2+2x+4}{x^2+2x+2} \le 3$.
2. Soit $f : \mathbb{R} \to \mathbb{R},\ x \mapsto \dfrac{x^2+2x+3}{x^2+2x+2}$. **Sans étudier les variations de $f$**, trouver le minimum de $f$ sur $\mathbb{R}$.

## Exercice 3 : encadrements

Soit $x, y, z$ trois réels tels que $0 < a \le x \le b$, $d \le y \le c < 0$, $0 < e \le z \le f$. Déterminer un encadrement de :

1. $4x - 2y$
2. $\dfrac{x-y}{z}$

## Exercice 4 : signe

Soit $a$ et $x$ deux réels, avec $a \ne 0$ et $\lvert x - a\rvert < \lvert a\rvert$. Montrer que $x$ est non nul et de même signe que $a$. Voir [[Valeur absolue]], [[Inégalité triangulaire]].

## Exercice 5 : inéquations

Résoudre dans $\mathbb{R}$ :

1. $\lvert x + 1\rvert < 0{,}1$
2. $\lvert x - 2\rvert > 10$
3. $\lvert x\rvert < \lvert x + 1\rvert$
4. $\lvert 2x - 1\rvert < \lvert x - 1\rvert$
5. $\big\lvert\, \lvert x + 3\rvert - 1 \,\big\rvert \le 2$
6. $\dfrac{x-1}{x+2} \ge 3$
7. $\sqrt{x - 3} - \sqrt{2x + 1} \le 4$
8. $\sqrt{x^2 - 2x + 3} \le x - 1$

## Exercice 6 : sommes et produits

Calculer :

1. $\displaystyle\sum_{i=1}^{n} 2$
2. $\displaystyle\prod_{i=1}^{n} 3$
3. $\displaystyle\sum_{k=1}^{n} (2a_{k+1} - 3a_k + a_{k-1})$
4. $\displaystyle\sum_{k=1}^{n} k$ (voir [[Somme des premiers entiers]])
5. En remarquant que $(k+1)^2 - k^2 = 2k + 1$, montrer que $\displaystyle\sum_{k=0}^{n-1} (2k+1) = \sum_{k=1}^{n} (2k-1) = n^2$.
6. Montrer que
$$\sum_{k=0}^{n} (k+1)^3 - \sum_{k=0}^{n} k^3 = 3\sum_{k=0}^{n} k^2 - \frac{(n+1)(3n+2)}{2}.$$
Énoncé recopié tel quel ; le signe « − » semble être une coquille (voir le point 1 à vérifier).
En déduire $\displaystyle\sum_{k=0}^{n} k^2$.

## Exercice 7 : coefficients binomiaux

Soit $p, n \in \mathbb{N}^*$ avec $p < n$. Montrer que
$$\binom{n}{p+1} = \binom{p}{p} + \binom{p+1}{p} + \cdots + \binom{n-1}{p}.$$

Voir [[Coefficient binomial]], [[Dénombrement]], [[Récurrence]].

## Exercice 8 : domaine de définition

Calculer le domaine de définition de $x \mapsto \sqrt{\dfrac{\ln\lvert x\rvert}{x}}$.

## Exercice 9 : formules de trigonométrie

À partir des formules de $\sin(x+y)$, $\cos(x+y)$ et de $\sin^2 x + \cos^2 x = 1$, démontrer (voir [[Formules trigonométriques]]) :

1. $\sin x + \sin y = 2 \sin\left(\dfrac{x+y}{2}\right) \cos\left(\dfrac{x-y}{2}\right)$
2. $\cos x - \cos y = -2 \sin\left(\dfrac{x+y}{2}\right) \sin\left(\dfrac{x-y}{2}\right)$
3. $\tan(x+y) = \dfrac{\tan x + \tan y}{1 - \tan x \tan y}$
4. $\cos x = \dfrac{1-t^2}{1+t^2}$ et $\sin x = \dfrac{2t}{1+t^2}$, où $t = \tan\left(\dfrac{x}{2}\right)$

## Exercice 10 : valeurs en $\pi/12$

Calculer $\cos\dfrac{\pi}{12}$, $\sin\dfrac{\pi}{12}$ et $\tan\dfrac{\pi}{12}$.

## Exercice 11 : équations trigonométriques

Résoudre, d'inconnue $x \in \mathbb{R}$ (voir [[Équation trigonométrique]]) :

1. $\sin x + \sin 2x = 0$
2. $\cos x = \sqrt{3} \sin x$
3. $\tan 2x = 3 \tan x$

## À retenir

Les pièges du Chap 0 reviennent ici : ne jamais soustraire des inégalités, élever au carré seulement quand les deux membres sont positifs, distinguer le signe d'un quotient.

## Points à vérifier

1. **Exercice 6.6** (page du PDF vérifiée) : l'énoncé écrit $3\sum k^2 - \frac{(n+1)(3n+2)}{2}$. Or $(k+1)^3 - k^3 = 3k^2 + 3k + 1$, ce qui donne $3\sum_{k=0}^{n} k^2 + 3\frac{n(n+1)}{2} + (n+1) = 3\sum k^2 + \frac{(n+1)(3n+2)}{2}$, avec un « + ». L'énoncé semble contenir une coquille de signe (complément, non corrigé dans l'énoncé recopié).
2. **Exercice 3** : les bornes de $y$ sont notées $d \le y \le c < 0$ (lettre $d$ avant $c$), tel quel dans l'énoncé.

## Liens

[[Récurrence]], [[Dénombrement]], [[Chap0-Rappels-etc (résumé)]].
