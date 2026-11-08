---
type: concept
tags: [year1]
aliases: [suites géométriques, somme géométrique, geometric sequence]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une suite $(u_n)$ est géométrique de raison $q$ si $u_{n+1} = q\,u_n$ pour tout $n$ ; par récurrence, $u_n = u_0\,q^n$ (et plus généralement $u_n = u_p\,q^{n-p}$).

**Somme géométrique (complément, hors du cours)** : pour $q \ne 1$,
$$\sum_{k=0}^{n} q^k = 1 + q + \dots + q^n = \frac{1-q^{n+1}}{1-q},$$
et la somme vaut $n+1$ si $q = 1$. Preuve par télescopage (voir [[Somme télescopique]]) :
$$(1-q)\sum_{k=0}^{n} q^k = \sum_{k=0}^{n}\left(q^k - q^{k+1}\right) = 1 - q^{n+1}.$$
C'est le cas $a = q$, $b = 1$ de la factorisation $a^{n+1} - b^{n+1} = (a-b)\sum_{k=0}^{n} a^k b^{n-k}$ (voir [[Formule du binôme de Newton]]). Pour une suite géométrique quelconque : $\sum_{k=0}^{n} u_k = u_0\,\frac{1-q^{n+1}}{1-q}$, soit « premier terme $\times \frac{1 - q^{\text{nombre de termes}}}{1-q}$ ».

**Limite de $q^n$ pour $q$ réel (complément, hors du cours)** : $q^n \to 0$ si $|q| < 1$ ; $q^n = 1$ si $q = 1$ ; $q^n \to +\infty$ si $q > 1$ ; pas de limite si $q \le -1$ (pour $q = -1$, la suite vaut alternativement $1$ et $-1$). Pour $|q| < 1$, la somme géométrique tend donc vers $\frac{1}{1-q}$ : c'est la [[Série numérique|série]] géométrique, convergente si et seulement si $|q| < 1$.

**Exemple du polycopié** ([[0 - rappels pdf]]) : $S_n = S \times (1{,}1)^n$ est géométrique de raison $1{,}1$ ; comme $1{,}1 > 1$ et $S > 0$, elle est strictement croissante et tend vers $+\infty$.

**Contrepoint : la [[Suite arithmétique]] (complément, hors du cours)** : $u_{n+1} = u_n + r$, d'où $u_n = u_0 + nr$, et $\sum_{k=0}^{n} u_k = \frac{(n+1)(u_0 + u_n)}{2}$ (nombre de termes $\times$ moyenne du premier et du dernier). On ajoute une constante à chaque pas pour une suite arithmétique, on multiplie par une constante pour une suite géométrique.

td0slides rappelle la formule de la somme géométrique (pour une raison $a \ne 1$). td1slides l'utilise pour écrire un développement décimal périodique sous forme de fraction (voir [[Nombre rationnel]]).

Dans le TDSuites, $w_n = v_n - u_n$ est géométrique, et la comparaison à une suite géométrique justifie le critère $u_{n+1}/u_n \to l$.

Notion parente : [[Suite numérique]]. Voir aussi : [[Série numérique]], [[Critère de d'Alembert et de Cauchy]], [[Suite arithmétique]], [[Somme télescopique]], [[Formule du binôme de Newton]].

Résumés : [[0 - Revision chapter]], [[1 - Convergent, divergent and positive terms SERIES]], [[0 - Rappels-etc]], [[0 - rappels pdf]]
