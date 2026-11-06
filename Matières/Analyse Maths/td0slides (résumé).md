---
type: source
tags: [year1]
sources: [".raw/Year 1/Analyse Maths/Exos/td0slides.pdf"]
maj: 2026-11-06
---

Résumé de td0slides (`.raw/Year 1/Analyse Maths/Exos/td0slides.pdf`) (85 diapositives, texte, « Analyse 1, premier semestre 2026-2027 »), dans [[Analyse Maths (matière)]]. Ce sont les diapositives corrigées du TD0 « Inégalités, sigma et fonctions trigonométriques ». Les énoncés sont ceux de [[TD0-Rappel (résumé)]] (ordre légèrement différent), avec la solution rédigée pas à pas. Cours associé : [[Chap0-Rappels-etc (résumé)]]. Quelques diapositives ont été vérifiées en image.

## Exercices et méthodes de résolution

| Ex. | Sujet | Méthode du corrigé |
|---|---|---|
| 1 | Inégalités classiques ($x + 1/x \ge 2$, $xy \le \frac12(x^2+y^2)$, $x^2+y^2+z^2 \ge xy+yz+zx$, $\frac{x^2+2x+4}{x^2+2x+2} \in ]0,3]$) | Partir de $(x-1)^2 \ge 0$ ou $(x-y)^2 \ge 0$ ; additionner trois inégalités ; positivité par discriminant ou par forme canonique ; majoration d'un quotient en passant tout d'un côté |
| 2 | $xy \le ((x+y)/2)^2$ ; minimum de $\frac{x^2+2x+2}{x^2+2x+3}$ | $f = 1 - \frac{1}{(x+1)^2 + 2} \ge \frac12$, atteint en $x = -1$ : on prouve la minoration puis on montre qu'elle est atteinte |
| 3 | Encadrer $4x - 2y$ et $(x-y)/z$ | Multiplier par $-2$ renverse l'ordre ; ne pas multiplier des encadrements dont les bornes sont de signes différents |
| 4 | Domaine de $\sqrt{\ln\lvert x\rvert / x}$ | Condition de la racine : $\ln\lvert x\rvert / x \ge 0$, étude du signe selon $x$ et $\lvert x\rvert \lessgtr 1$ ; domaine $[-1, 0[\ \cup [1, +\infty[$ |
| 5 | $\lvert x - a\rvert < \lvert a\rvert$ entraîne $x$ de même signe que $a$ | Encadrement $-\lvert a\rvert < x - a < \lvert a\rvert$ puis cas $a > 0$ et $a < 0$ |
| 6 | Inéquations avec valeurs absolues et racines | Deux méthodes : cas selon le signe, ou élévation au carré ($x^2 \le a^2 \iff \lvert x\rvert \le \lvert a\rvert$). Pour une racine : $\sqrt{u} \le v \iff u \ge 0$, $v \ge 0$, $u \le v^2$. Solutions : $]-1{,}1;-0{,}9[$, $]-\infty,-8[ \cup ]12,+\infty[$, $]-\frac12,+\infty[$, $]0, \frac23[$ |
| 7 | Sommes et produits : $\sum 2$, $\prod 3$, somme géométrique, télescopage | Sortir les constantes, formule de la somme géométrique, réécriture en $u_{k+1} - u_k$ |
| 8 | $\sum \binom nk 5^k$, $\sum (-3)^k\binom nk$, $\sum k\binom nk$ | Binôme de Newton ; $k\binom nk = n\binom{n-1}{k-1}$ pour la dernière |
| 9, 10 | Produits en factorielles ($\prod k^2 = (n!)^2$) ; $\prod 3^k = 3^{n(n+1)/2}$ ; $\prod \frac{k}{k+2}$ | Regrouper, puis télescoper les quotients |
| 11 | $\binom{n}{p+1} = \sum_{k=p}^{n-1}\binom kp$ | Pascal appliqué en cascade et télescopage |
| 12, 13 | $\sin x + \sin y$ et $\cos x - \cos y$ en produit ; $\cos$, $\sin$, $\tan$ de $\pi/12$ | Formules d'addition ; $\pi/12 = \pi/4 - \pi/6$ |
| 14 | Équations trigonométriques : $\sin x + \sin 2x = 0$, $\cos x = \sqrt3 \sin x$, $\tan 2x = 3\tan x$ | Factoriser ($\sin x\,(1 + 2\cos x) = 0$, solutions $k\pi$, $\pm 2\pi/3 + 2k\pi$) ; diviser par $\cos x$ après avoir exclu $\cos x = 0$ ; poser $t = \tan x$ avec condition de définition |

Le document se termine par des exercices supplémentaires à chercher : $\frac{3}{x-1} \le \frac{5}{2x+1}$, $\frac{x^2 - 6x + 8}{x - 1} < 0$, $\sum 3^k$, $\cos^2 x - \cos x = 0$, $\tan x = 1$, $\tan(\frac\pi4(\sin x + 1)) = 1$.

## Pièges mis en avant

- Résoudre sans préciser le domaine (racine, quotient, tangente).
- Diviser par une quantité qui peut s'annuler.
- Multiplier ou soustraire des inégalités sans tenir compte des signes.
- Après élévation au carré, vérifier que les solutions du problème d'origine sont bien conservées.

## Liens

[[Récurrence]], [[Dénombrement]], [[Norme]].
