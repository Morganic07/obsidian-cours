---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de AnalyseID1 ([[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]) (95 pages), dans [[Cours/Mathématiques/Analyse Maths/_index|Analyse Maths]]. C'est le polycopié complet du cours d'Analyse I (PréING1, 2020-2021) : cinq chapitres de cours, chacun suivi de sa feuille de TD. Il regroupe donc des documents résumés ailleurs :

| Chapitre | Pages | Résumé détaillé |
|---|---|---|
| 0. Rappels, sigma et pi, trigonométrie | 1 à 14 | [[0 - Rappels-etc]], [[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel]] ; trigonométrie ci-dessous |
| 1. L'ensemble $\mathbb{R}$ | 15 à 24 | [[1 - Ensemble des Reels]], [[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels]] |
| 2. Suites numériques | 25 à 43 | ci-dessous ; TD dans [[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]] |
| 3. Limites et continuité | 44 à 60 | ci-dessous, avec le TD3 |
| 4. Dérivabilité | 61 à 72 | [[4 - dérivabilité]] |
| 5. Analyse asymptotique | 73 à 95 | [[5 - Analyse Maths\|chp5]], [[Raw/Year 1/Analyse Maths/Exos/TD5-AnalAsympt.pdf|TD5-AnalAsympt]] |

Les chapitres 0 à 3 ont été lus en image (le polycopié est en grande partie fait de captures). Pour les chapitres 1, 4 et 5 et les rappels du chapitre 0, la fiche renvoie aux résumés dédiés ; elle détaille ici la trigonométrie, les chapitres 2 et 3 et le TD3. Les figures sont recadrées dans `Cours/Mathématiques/Analyse Maths/images/`.

## Chapitre 0 : rappels (pages 1 à 14)

Les pages 1 à 7 sont les rappels sur les équations et inéquations, la valeur absolue, les puissances et racines, le principe des substitutions, les symboles $\sum$ et $\prod$, les coefficients binomiaux et la formule du binôme : voir [[0 - Rappels-etc]]. Les pages 13-14 sont le TD0 : voir [[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel]].

### Rappel de trigonométrie (pages 8 à 12)

**Définition 1 (cosinus et sinus).** Sur le cercle unité de centre $O$, orienté dans le sens direct (inverse des aiguilles d'une montre), soit $N(a, b)$ un point du cercle et $x$ une mesure en radians de l'angle $(\overrightarrow{OI}, \overrightarrow{ON})$. Alors $\cos x = a$ (abscisse de $N$) et $\sin x = b$ (ordonnée). Voir [[Fonctions trigonométriques]].

La mesure en **radians** d'un angle est la longueur de l'arc qu'il intercepte sur le cercle unité. Un tour complet mesure $2\pi$, donc $\pi\ \text{rad} = 180°$ : un angle de $d$ degrés mesure $\frac{d\pi}{180}$ radians ($90° = \frac{\pi}{2}$, $60° = \frac{\pi}{3}$, $45° = \frac{\pi}{4}$, $30° = \frac{\pi}{6}$). [[Complément hors du cours|ⓘ]]

![[AnalyseID1 - p8.jpg]]

*Figure : le cercle trigonométrique ; $\cos x$ et $\sin x$ sont les coordonnées du point $N$.*

**Remarque.** Comme $-1 \le a, b \le 1$ et $a^2 + b^2 = 1$ :
$$-1 \le \cos x \le 1, \qquad -1 \le \sin x \le 1, \qquad \cos^2 x + \sin^2 x = 1.$$

**Notation (modulo).** Pour $\theta \in \mathbb{R}$, $x \equiv y\ [\theta]$ (« $x$ égal à $y$ modulo $\theta$ ») s'il existe $k \in \mathbb{Z}$ tel que $x = y + k\theta$. Voir [[Congruence modulo n]].

![[AnalyseID1 - p9a.jpg]]

*Figure : cercle trigonométrique avec les angles remarquables (en degrés et en radians) et les coordonnées des points associés.*

**Proposition 1 (propriétés).**
- $\sin$ et $\cos$ sont $2\pi$-périodiques : $\sin(x + 2\pi) = \sin x$, $\cos(x + 2\pi) = \cos x$.
- $\sin$ est impaire, $\sin(-x) = -\sin x$ ; $\cos$ est paire, $\cos(-x) = \cos x$ (voir [[Fonction paire et impaire]]).

![[AnalyseID1 - p9b.jpg]]

*Figure 1 du cours : parité des fonctions trigonométriques, lue sur le cercle ($\cos(-x) = \cos x$, $\sin(-x) = -\sin x$).*

**Proposition 2 (résolution d'équations).** Pour tous $x, y \in \mathbb{R}$ (voir [[Équation trigonométrique]]) :
$$\sin x = \sin y \iff x \equiv y\ [2\pi] \text{ ou } x \equiv \pi - y\ [2\pi],$$
$$\cos x = \cos y \iff x \equiv y\ [2\pi] \text{ ou } x \equiv -y\ [2\pi].$$

**Proposition 3 (transformations affines).**
$$\sin(x+\pi) = -\sin x,\quad \sin(\pi - x) = \sin x,\quad \cos(x + \pi) = -\cos x,\quad \cos(\pi - x) = -\cos x,$$
$$\sin\left(x + \tfrac{\pi}{2}\right) = \cos x,\quad \sin\left(\tfrac{\pi}{2} - x\right) = \cos x,\quad \cos\left(x + \tfrac{\pi}{2}\right) = -\sin x,\quad \cos\left(\tfrac{\pi}{2} - x\right) = \sin x.$$

**Exemple.** Résoudre $\sin x = \cos x$.
$$\sin x = \cos x \iff \sin x = \sin\left(\tfrac{\pi}{2} - x\right) \iff x \equiv \tfrac{\pi}{2} - x\ [2\pi] \text{ ou } x \equiv \pi - \left(\tfrac{\pi}{2} - x\right)\ [2\pi].$$
La seconde donne $0 \equiv \frac{\pi}{2}\ [2\pi]$, impossible ; la première donne $2x \equiv \frac{\pi}{2}\ [2\pi]$, soit $x \equiv \frac{\pi}{4}\ [\pi]$. Donc $S = \{\frac{\pi}{4} + k\pi,\ k \in \mathbb{Z}\}$.

**Proposition 4 (formules d'addition).** Voir [[Formules trigonométriques]].
$$\sin(x + y) = \sin x\cos y + \cos x \sin y, \qquad \cos(x+y) = \cos x \cos y - \sin x \sin y,$$
$$\sin(x - y) = \sin x\cos y - \cos x \sin y, \qquad \cos(x-y) = \cos x \cos y + \sin x \sin y.$$
Pour $x = y$, **formules de duplication** :
$$\sin 2x = 2\sin x\cos x, \qquad \cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x.$$

**Proposition 5 (formules de produit)**, obtenues en additionnant les formules d'addition (voir [[Linéarisation trigonométrique]]) :
$$\cos x\cos y = \tfrac12\big(\cos(x+y) + \cos(x-y)\big),\quad \sin x \sin y = \tfrac12\big(\cos(x-y) - \cos(x+y)\big),\quad \sin x\cos y = \tfrac12\big(\sin(x+y) + \sin(x-y)\big).$$

Lues dans l'autre sens, avec $p = x + y$ et $q = x - y$ (donc $x = \frac{p+q}{2}$, $y = \frac{p-q}{2}$), ces formules donnent les **formules de factorisation**, qui transforment une somme en produit (utile pour résoudre $\cos p = \cos q$ ou étudier un signe) : [[Complément hors du cours|ⓘ]]
$$\cos p + \cos q = 2\cos\tfrac{p+q}{2}\cos\tfrac{p-q}{2},\qquad \cos p - \cos q = -2\sin\tfrac{p+q}{2}\sin\tfrac{p-q}{2},$$
$$\sin p + \sin q = 2\sin\tfrac{p+q}{2}\cos\tfrac{p-q}{2},\qquad \sin p - \sin q = 2\cos\tfrac{p+q}{2}\sin\tfrac{p-q}{2}.$$

**Définition 2 (tangente).** Sur
$$\left]-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right[ + \pi\mathbb{Z} = \left\{x \in \mathbb{R} : \forall k \in \mathbb{Z},\ x \ne \tfrac{\pi}{2} + k\pi\right\},\qquad \tan x = \frac{\sin x}{\cos x}.$$

**Proposition 6 (propriétés de la tangente).**
- $\tan x = \tan y \iff x \equiv y\ [\pi]$ ; en particulier $\tan$ est $\pi$-périodique.
- $\tan$ est impaire : $\tan(-x) = -\tan x$.
- En divisant $\cos^2 x + \sin^2 x = 1$ par $\cos^2 x$ : $1 + \tan^2 x = \dfrac{1}{\cos^2 x}$, expression qui est aussi la dérivée de $\tan$. [[Complément hors du cours|ⓘ]]
- Addition et duplication :
$$\tan(x+y) = \frac{\tan x + \tan y}{1 - \tan x\tan y}, \qquad \tan(x - y) = \frac{\tan x - \tan y}{1 + \tan x \tan y}, \qquad \tan 2x = \frac{2\tan x}{1 - \tan^2 x}.$$

![[AnalyseID1 - p12.jpg]]

*Figure 2 du cours : la tangente, longueur lue sur la droite verticale $x = 1$, au point $T$ où la droite $(OM)$ la coupe.*

**Valeurs remarquables.**

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|---|---|---|---|---|---|
| $\sin x$ | $0$ | $\frac12$ | $\frac{1}{\sqrt2}$ | $\frac{\sqrt3}{2}$ | $1$ |
| $\cos x$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $0$ |
| $\tan x$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | non définie |

## Chapitre 1 : l'ensemble $\mathbb{R}$ (pages 15 à 24)

Voir [[1 - Ensemble des Reels]] (cours) et [[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels]] (TD).

## Chapitre 2 : suites numériques (pages 25 à 43)

Voir aussi [[Suite numérique]].

### I. Définitions

**Définition 1.** Une **suite** est une application $u : \mathbb{N} \to \mathbb{R}$. Pour $n \in \mathbb{N}$, $u(n)$ se note $u_n$, le $n$-ième **terme** ou **terme général**. La suite se note $u$, $(u_n)_{n\in\mathbb{N}}$ ou $(u_n)$ ; une suite définie à partir d'un rang $n_0$ se note $(u_n)_{n\ge n_0}$.

**Exemples 1.** $(\sqrt n)_{n\ge0}$ : $0, 1, \sqrt2, \sqrt3, \ldots$ ; $((-1)^n)_{n\ge0}$ : $+1, -1, +1, \ldots$ ; $S_n = S \times (1{,}1)^n$ (suite de l'introduction) ; [[Suite de Fibonacci]] $F_0 = F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$ : $1, 1, 2, 3, 5, 8, 13, \ldots$ ; $\left(\frac{1}{n^2}\right)_{n\ge1}$ : $1, \frac14, \frac19, \frac{1}{16}, \ldots$

**Suites arithmétiques et géométriques.** Une suite est **arithmétique** de raison $r$ si $u_{n+1} = u_n + r$, d'où $u_n = u_0 + nr$ et $\sum_{k=0}^{n} u_k = (n+1)\frac{u_0 + u_n}{2}$ ; elle est [[Suite géométrique|géométrique]] de raison $q$ si $u_{n+1} = q\,u_n$, d'où $u_n = u_0\,q^n$ et, pour $q \ne 1$, $\sum_{k=0}^{n} q^k = \frac{1 - q^{n+1}}{1 - q}$. La suite $(S_n)$ de l'introduction est géométrique de raison $1{,}1$. Pour $q$ réel : $q^n \to 0$ si $|q| < 1$, $q^n = 1$ si $q = 1$, $q^n \to +\infty$ si $q > 1$, et pas de limite si $q \le -1$. [[Complément hors du cours|ⓘ]]

Pour la suite de Fibonacci, le rapport $\frac{F_{n+1}}{F_n}$ tend vers le **nombre d'or** $\varphi = \frac{1 + \sqrt5}{2} \approx 1{,}618$, racine positive de $x^2 = x + 1$. Avec l'autre racine $\psi = \frac{1 - \sqrt5}{2}$, on a la formule explicite (de Binet) $F_n = \frac{\varphi^{n+1} - \psi^{n+1}}{\sqrt5}$ pour la numérotation $F_0 = F_1 = 1$ du cours. [[Complément hors du cours|ⓘ]]

**Définition 2 (majorée, minorée, bornée).**
- $(u_n)$ est **majorée** si $\exists M \in \mathbb{R},\ \forall n,\ u_n \le M$ ;
- **minorée** si $\exists m \in \mathbb{R},\ \forall n,\ u_n \ge m$ ;
- **bornée** si elle est majorée et minorée, ce qui revient à $\exists M \in \mathbb{R},\ \forall n,\ |u_n| \le M$.

![[AnalyseID1 - p25a.jpg]]

*Figure : une suite majorée par $M$ (à gauche) et une suite minorée par $m$ (à droite).*

**Définition 3 (monotonie).** $(u_n)$ est **croissante** si $\forall n,\ u_{n+1} \ge u_n$ ; **strictement croissante** si $u_{n+1} > u_n$ ; **décroissante** si $u_{n+1} \le u_n$ ; **strictement décroissante** si $u_{n+1} < u_n$ ; **monotone** si croissante ou décroissante ; **strictement monotone** si strictement croissante ou strictement décroissante.

![[AnalyseID1 - p25b.jpg]]

*Figure : une suite croissante mais pas strictement croissante (paliers).*

**Remarque.** $(u_n)$ est croissante si et seulement si $\forall n,\ u_{n+1} - u_n \ge 0$. Si les termes sont strictement positifs, elle est croissante si et seulement si $\forall n,\ \frac{u_{n+1}}{u_n} \ge 1$.

**Exemples 2.**
- $(S_n)$ est strictement croissante car $S_{n+1}/S_n = 1{,}1 > 1$.
- $u_n = (-1)^n/n$ ($n \ge 1$) n'est ni croissante ni décroissante ; elle est majorée par $\frac12$ (atteint en $n = 2$) et minorée par $-1$ (atteint en $n = 1$).
- $\left(\frac1n\right)_{n\ge1}$ est strictement décroissante, majorée par 1 (atteint en $n = 1$), minorée par 0 (jamais atteint).

![[AnalyseID1 - p26a.jpg]]

*Figure : premiers termes de $u_n = (-1)^n/n$, alternativement sous et au-dessus de l'axe.*

### II. Limite d'une suite

**Définition 4 (limite finie).** $(u_n)$ a pour **limite** $\ell \in \mathbb{R}$ si
$$\forall \varepsilon > 0\ \ \exists N \in \mathbb{N}\ \ \forall n \in \mathbb{N}\quad (n \ge N \Rightarrow |u_n - \ell| \le \varepsilon).$$
On dit que $u_n$ **tend vers** $\ell$ : $u_n$ est aussi proche que l'on veut de $\ell$ à partir d'un certain rang. Voir [[Convergence d'une suite]].

![[AnalyseID1 - p26b.jpg]]

*Figure : à partir du rang $N$, tous les termes sont dans la bande $[\ell - \varepsilon, \ell + \varepsilon]$.*

**Définition 5 (limites infinies).**
1. $u_n \to +\infty$ si $\forall A > 0\ \exists N\ \forall n\ (n \ge N \Rightarrow u_n \ge A)$.
2. $u_n \to -\infty$ si $\forall A > 0\ \exists N\ \forall n\ (n \ge N \Rightarrow u_n \le -A)$.

**Remarques.**
1. On note $\lim_{n\to+\infty} u_n = \ell$ ou $u_n \xrightarrow[n\to+\infty]{} \ell$.
2. $\lim u_n = -\infty \iff \lim(-u_n) = +\infty$.
3. On abrège en $\forall \varepsilon > 0\ \exists N \in \mathbb{N}\ (n \ge N \Rightarrow |u_n - \ell| \le \varepsilon)$. $N$ dépend de $\varepsilon$, et on ne peut pas échanger « pour tout » et « il existe ».
4. $|u_n - \ell| \le \varepsilon$ signifie $\ell - \varepsilon \le u_n \le \ell + \varepsilon$. On peut aussi définir la limite avec $|u_n - \ell| < \varepsilon$ (inégalité stricte).

**Définition 6.** Une suite est **convergente** si elle admet une limite **finie**, **divergente** sinon (elle tend vers $\pm\infty$ ou n'a pas de limite).

**Proposition 1 (unicité).** Si une suite est convergente, sa limite est unique.
*Preuve par l'absurde* ([[Raisonnement par l'absurde]]) : si $\ell \ne \ell'$ sont deux limites, on choisit $0 < \varepsilon < \frac{|\ell - \ell'|}{2}$ ; il existe $N_1$ et $N_2$ tels que $|u_n - \ell| < \varepsilon$ pour $n \ge N_1$ et $|u_n - \ell'| < \varepsilon$ pour $n \ge N_2$. Avec $N = \max(N_1, N_2)$, l'[[Inégalité triangulaire]] donne $|\ell - \ell'| \le |\ell - u_N| + |u_N - \ell'| < 2\varepsilon < |\ell - \ell'|$, impossible.

**Définition abstraite par les voisinages.** Pour $\ell \in \overline{\mathbb{R}}$, un **voisinage** de $\ell$ est :
- si $\ell \in \mathbb{R}$, tout intervalle $]\ell - \varepsilon, \ell + \varepsilon[$ avec $\varepsilon > 0$ ;
- si $\ell = +\infty$, tout intervalle $]A, +\infty[$ avec $A \in \mathbb{R}$ ;
- si $\ell = -\infty$, tout intervalle $]-\infty, A[$ avec $A \in \mathbb{R}$.

L'idée : un voisinage de $\ell$ contient tous les réels « à proximité immédiate » de $\ell$. Voir [[Boule et voisinage]].

![[AnalyseID1 - p27.jpg]]

*Figure : voisinages de $-\infty$, d'un réel $\ell$ et de $+\infty$ sur la droite réelle.*

**Définition générale.** $(u_n)$ admet $\ell \in \overline{\mathbb{R}}$ pour limite si **pour tout voisinage $\mathcal{V}$ de $\ell$, les $u_n$ appartiennent à $\mathcal{V}$ à partir d'un certain rang**. Cas particuliers : limite finie ($\forall \varepsilon > 0\ \exists N\ \forall n \ge N,\ |u_n - \ell| < \varepsilon$), $+\infty$ ($\forall A > 0\ \exists N\ \forall n \ge N,\ u_n > A$), $-\infty$ ($\forall A < 0\ \exists N\ \forall n \ge N,\ u_n < A$).

**Théorème (convergence et caractère borné).** Toute suite convergente est bornée.
*Preuve* : avec $\varepsilon = 1$, $|u_n - \ell| < 1$ pour $n \ge N$, donc $|u_n| \le |u_n - \ell| + |\ell| \le |\ell| + 1$. Avec $K = \max\{|u_0|, \ldots, |u_{N-1}|, |\ell| + 1\}$, on a $|u_n| \le K$ pour tout $n$.

**Attention.**
- La réciproque est fausse : $(-1)^n$ est bornée (entre $-1$ et 1) sans converger.
- Une suite non bornée n'a pas forcément $\pm\infty$ pour limite : $(-1)^n n$ n'est pas bornée et n'a pas de limite (regarder les indices pairs et impairs).

### III. Opérations sur les limites

**Propriété 7 (somme, produit, limites finies).** Si $u_n \to \ell$ et $v_n \to \ell'$ :
1. pour tout $(\lambda, \mu) \in \mathbb{R}^2$, $\lambda u_n + \mu v_n \to \lambda\ell + \mu\ell'$ ;
2. $u_n v_n \to \ell\ell'$.

*Preuve.* (1) $|\lambda u_n + \mu v_n - (\lambda\ell + \mu\ell')| \le |\lambda||u_n - \ell| + |\mu||v_n - \ell'| \to 0$. (2) $|u_n v_n - \ell\ell'| = |u_n - \ell||v_n| + |v_n - \ell'||\ell| \to 0$, car $(v_n)$ est bornée (convergente).

**Tableaux (limites de somme et de produit).**

| $\lim u_n$ | $\ell$ | $\ell$ | $\ell$ | $+\infty$ | $-\infty$ | $+\infty$ |
|---|---|---|---|---|---|---|
| $\lim v_n$ | $\ell'$ | $+\infty$ | $-\infty$ | $+\infty$ | $-\infty$ | $-\infty$ |
| $\lim(u_n + v_n)$ | $\ell + \ell'$ | $+\infty$ | $-\infty$ | $+\infty$ | $-\infty$ | forme indéterminée |

| $\lim u_n$ | $\ell$ | $\ell \ne 0$ | $\pm\infty$ | $0$ |
|---|---|---|---|---|
| $\lim v_n$ | $\ell'$ | $\pm\infty$ | $\pm\infty$ | $\pm\infty$ |
| $\lim(u_n v_n)$ | $\ell\ell'$ | $\pm\infty$ | $\pm\infty$ | forme indéterminée |

Pour les infinis, la règle des signes donne le signe du produit. Voir [[Forme indéterminée]].

**Propriété 9 (inverse, rapport).**
1. Si $u_n \to \ell \in \mathbb{R}$ et $v_n \to \ell' \in \mathbb{R}^*$, alors $\frac{u_n}{v_n}$ est définie à partir d'un certain rang et tend vers $\frac{\ell}{\ell'}$.
2. Si $|u_n| \to +\infty$, alors $\frac{1}{u_n}$ est définie à partir d'un certain rang et tend vers 0.
3. Si $u_n \to 0$ en étant strictement positive (resp. négative) à partir d'un certain rang, alors $\frac{1}{u_n} \to +\infty$ (resp. $-\infty$).

*Preuve.* (1) $|v_n|$ est minorée par $m > 0$ à partir d'un rang $N$, et $\left|\frac{u_n}{v_n} - \frac{\ell}{\ell'}\right| \le \frac{|u_n - \ell||\ell'| + |v_n - \ell'||\ell|}{m|\ell'|} \to 0$. (2) Pour $\varepsilon > 0$, à partir d'un rang, $|u_n| \ge \frac{1}{\varepsilon}$, donc $\left|\frac{1}{u_n}\right| \le \varepsilon$. (3) Pour $A > 0$, à partir d'un rang, $0 < u_n \le \frac1A$, donc $\frac{1}{u_n} \ge A$.

**Théorème (composition à gauche par une fonction)**, admis pour l'instant car il demande la limite d'une fonction (chapitre 3). Soit $f : I \to \mathbb{R}$, $\ell$ un élément ou une borne de $I$, $L \in \overline{\mathbb{R}}$. Si $u_n \to \ell$ et $\lim_{x\to\ell} f(x) = L$, alors $f(u_n) \to L$.

**Propriété 10 (passage à la limite dans les inégalités larges).** Si $u_n \to \ell$, $v_n \to \ell'$ et $m, M \in \mathbb{R}$ :
1. si $u_n \le M$ à partir d'un certain rang, alors $\ell \le M$ ;
2. si $u_n \ge m$ à partir d'un certain rang, alors $\ell \ge m$ ;
3. si $u_n \le v_n$ à partir d'un certain rang, alors $\ell \le \ell'$.

*Preuve de (3) par l'absurde* : si $\ell > \ell'$, on pose $\varepsilon = \frac{\ell - \ell'}{3}$ ; à partir d'un rang, $\ell - \varepsilon \le u_n \le v_n \le \ell' + \varepsilon$, d'où $\ell - \ell' \le 2\varepsilon = \frac23(\ell - \ell')$, absurde. Les points 1 et 2 s'en déduisent avec des suites constantes.

**Remarque.** Les inégalités strictes deviennent larges par passage à la limite : $\frac{1}{n+1} > 0$ pour tout $n$, mais la limite vaut 0.

### IV. Théorèmes d'existence de limite

**Théorème 11 (encadrement, « gendarmes »).** Si $\exists N,\ \forall n \ge N,\ u_n \le v_n \le w_n$ et si $(u_n)$ et $(w_n)$ convergent vers la même limite $\ell$, alors $(v_n)$ converge et $\lim v_n = \ell$. Voir [[Théorème des gendarmes]].
*Preuve* : à partir d'un rang, $-\varepsilon \le u_n - \ell \le v_n - \ell \le w_n - \ell \le \varepsilon$.

**Exemples.**
- $u_n = \sum_{k=1}^{n} \frac{n}{n^2 + k}$ : $\frac{n}{n+1} = \sum_{k=1}^n \frac{n}{n^2+n} \le u_n \le \sum_{k=1}^n \frac{n}{n^2+1} = \frac{n^2}{n^2+1}$, et les deux bornes tendent vers 1, donc $u_n \to 1$.
- $u_n = \frac{E(nx)}{n}$ : calculer $\lim u_n$ (non corrigé dans le cours ; voir [[Partie entière]]).

**Propriété 12 (minoration, majoration).**
1. Si $u_n \le v_n$ à partir d'un rang et $u_n \to +\infty$, alors $v_n \to +\infty$.
2. Si $u_n \le v_n$ à partir d'un rang et $v_n \to -\infty$, alors $u_n \to -\infty$.

**Exemple.** $u_n = \sum_{k=1}^{n} \frac{1}{\sqrt k} \ge \sum_{k=1}^n \frac{1}{\sqrt n} = \sqrt n \to +\infty$, donc $u_n \to +\infty$.

**Théorème 13 (limite monotone).** Voir [[Théorème de la limite monotone]].
1. Toute suite croissante et majorée converge, vers $\sup\{u_n \mid n \in \mathbb{N}\}$ ; toute suite croissante non majorée tend vers $+\infty$.
2. Toute suite décroissante et minorée converge, vers $\inf\{u_n \mid n \in \mathbb{N}\}$ ; toute suite décroissante non minorée tend vers $-\infty$.

*Preuve* : si $(u_n)$ est majorée, $A = \{u_n\}$ est non vide et majoré, donc a une [[Borne supérieure]] $L$. Pour $\varepsilon > 0$, il existe $u_N > L - \varepsilon$, et par croissance $L - \varepsilon < u_N \le u_n \le L$ pour $n \ge N$. Si elle n'est pas majorée, pour tout $A > 0$ il existe $N$ avec $u_N > A$, et par croissance $u_n > A$ pour $n \ge N$.

**Exemple.** $u_n = \sum_{k=1}^n \frac{1}{k^2}$ est croissante ($u_{n+1} - u_n = \frac{1}{(n+1)^2} \ge 0$) et, puisque $\frac{1}{k^2} \le \frac{1}{k(k-1)}$ pour $k \ge 2$, [[Erreurs du cours#^e-0-rappels-pdf|✎]]
$$u_n \le 1 + \sum_{k=2}^n \frac{1}{k(k-1)} = 1 + \sum_{k=2}^n \left(\frac{1}{k-1} - \frac1k\right) = 2 - \frac1n \le 2.$$
Elle converge donc ; on peut montrer que sa limite vaut $\frac{\pi^2}{6}$.

Le calcul de cette limite est le **problème de Bâle**, résolu par Euler en 1735 : $\sum_{k=1}^{+\infty} \frac{1}{k^2} = \frac{\pi^2}{6} \approx 1{,}645$. Plus généralement, $\sum \frac{1}{k^\alpha}$ converge si et seulement si $\alpha > 1$ (séries de Riemann), alors que $\sum \frac1k$ diverge (voir [[Série numérique]]). [[Complément hors du cours|ⓘ]]

**Définition (suites adjacentes).** $(u_n)$ et $(v_n)$ sont [[Suites adjacentes|adjacentes]] si $(u_n)$ est croissante, $(v_n)$ décroissante et $(v_n - u_n) \to 0$.

**Théorème 14 (suites adjacentes).** Si $(u_n)$ croissante et $(v_n)$ décroissante sont adjacentes :
1. elles convergent vers la même limite $\ell$ ;
2. $\forall n,\ u_n \le \ell \le v_n$.

*Preuve* : $(v_{n+1} - u_{n+1}) - (v_n - u_n) = (v_{n+1} - v_n) - (u_{n+1} - u_n) \le 0$, donc $(v_n - u_n)$ décroît vers 0, d'où $v_n - u_n \ge 0$. Ainsi $u_0 \le u_n \le v_n \le v_0$ : $(u_n)$ croissante majorée par $v_0$, $(v_n)$ décroissante minorée par $u_0$ convergent vers $\ell_1$, $\ell_2$, et $\ell_2 - \ell_1 = \lim(v_n - u_n) = 0$.

**Exemple.** $u_n = \sum_{k=0}^n \frac{1}{k!}$ et $v_n = u_n + \frac{1}{n \cdot n!}$ sont adjacentes :
- $u_{n+1} - u_n = \frac{1}{(n+1)!} \ge 0$ ;
- $v_{n+1} - v_n = \frac{1}{(n+1)!} + \frac{1}{(n+1)(n+1)!} - \frac{1}{n \cdot n!} = -\frac{1}{n(n+1)(n+1)!} \le 0$ ;
- $v_n - u_n = \frac{1}{n \cdot n!} \to 0$.

Leur limite commune est le nombre $e = \exp(1) \approx 2{,}718$. L'encadrement $u_n < e < v_n$ (strict, car $(u_n)$ est strictement croissante et $(v_n)$ strictement décroissante) montre que $e$ est **irrationnel** : si $e = \frac{p}{q}$, en multipliant $u_q < e < u_q + \frac{1}{q \cdot q!}$ par $q!$, l'entier $q!\,e = p\,(q-1)!$ serait strictement compris entre l'entier $q!\,u_q$ et $q!\,u_q + \frac1q \le q!\,u_q + 1$, ce qui est impossible. [[Complément hors du cours|ⓘ]]

### V. Suites extraites (sous-suites)

**Définition.** Une suite extraite (sous-suite) de $(u_n)$ est une suite $(u_{\varphi(n)})$ avec $\varphi : \mathbb{N} \to \mathbb{N}$ strictement croissante. Voir [[Suite extraite]].

**Remarque.** Si $\varphi$ est strictement croissante, $\varphi(n) \ge n$ pour tout $n$ ([[Récurrence]] : $\varphi(0) \ge 0$ ; si $\varphi(n) \ge n$, alors $\varphi(n+1) > \varphi(n) \ge n$, donc $\varphi(n+1) \ge n+1$ car ce sont des entiers).

**Exemples.** $(u_{n+1})$, $(u_{n^2})_{n\ge1}$, $(u_{2^n})$ sont extraites de $(u_n)$ ; $(u_{2n})$ et $(u_{2n+1})$ sont les suites extraites paire et impaire.

![[AnalyseID1 - p34.jpg]]

*Figure : les termes entourés, d'indices $\varphi(0), \varphi(1), \varphi(2), \varphi(3)$, forment une suite extraite.*

**Théorème (limites de suites extraites).** Soit $\ell \in \overline{\mathbb{R}}$.
1. Si $u_n \to \ell$, alors $u_{\varphi(n)} \to \ell$ pour toute $\varphi$ strictement croissante.
2. Si $u_{2n} \to \ell$ et $u_{2n+1} \to \ell$, alors $u_n \to \ell$.

*Preuve.* (1) Pour un voisinage $\mathcal{V}$ de $\ell$, $u_n \in \mathcal{V}$ pour $n \ge N$ ; or $\varphi(n) \ge n \ge N$, donc $u_{\varphi(n)} \in \mathcal{V}$. (2) $u_{2p} \in \mathcal{V}$ pour $p \ge N$ et $u_{2p+1} \in \mathcal{V}$ pour $p \ge N'$ ; avec $n_0 = \max\{2N, 2N'+1\}$, tout $n \ge n_0$ (pair ou impair) vérifie $u_n \in \mathcal{V}$.

**En pratique.** Ce théorème sert surtout à montrer qu'une suite **n'a pas de limite** : il suffit d'exhiber deux suites extraites de limites différentes. Exemple : $(-1)^n$ n'a pas de limite car $(-1)^{2n} \to 1$ et $(-1)^{2n+1} \to -1$.

**[[Théorème de Bolzano-Weierstrass]].** De toute suite réelle **bornée**, on peut extraire une suite convergente (même énoncé pour les suites complexes). Ainsi $(-1)^n$, bornée sans être convergente, a des suites extraites convergentes. C'est un résultat central de l'analyse, qui sert notamment à démontrer le théorème des bornes atteintes du chapitre 3. [[Complément hors du cours|ⓘ]]

### VI. Suites récurrentes $u_{n+1} = f(u_n)$

$f$ est une fonction réelle définie sur un intervalle $I$.

**Remarque.** Une telle relation ne définit pas toujours une suite : avec $u_0 = 1$ et $u_{n+1} = 2 + \sqrt{1 - u_n}$, $u_1 = 2$ et $u_2$ n'existe pas.

**Propriété 17 (existence).** Si $I$ est stable par $f$ ($f(I) \subset I$, voir [[Intervalle stable]]) et $a \in I$, il existe une unique suite vérifiant $u_0 = a$ et $\forall n,\ u_{n+1} = f(u_n)$. Preuve par récurrence.

**Propriété 18 (monotonie).** Soit $f : I \to \mathbb{R}$, $I$ stable, $u_0 = a \in I$, $u_{n+1} = f(u_n)$.
1. Si $f$ est **croissante** sur $I$, $(u_n)$ est monotone : croissante si $f(u_0) - u_0 \ge 0$, décroissante si $f(u_0) - u_0 \le 0$.
2. Si $f$ est **décroissante** sur $I$, les suites extraites $(u_{2n})$ et $(u_{2n+1})$ sont monotones, de monotonies contraires.

![[AnalyseID1 - p35.jpg]]

*Figure : diagramme en escalier pour $f$ croissante ; selon $u_0$, la suite monte (en rouge) ou descend (en vert) le long de la courbe, entre la courbe et la droite $y = x$.*

*Preuve.* (1) Si $f(u_0) - u_0 \ge 0$, $u_1 \ge u_0$, et $u_{n+2} - u_{n+1} = f(u_{n+1}) - f(u_n)$ permet de montrer par récurrence que $(u_n)$ est croissante. (2) $g = f \circ f$ est croissante ; $v_n = u_{2n}$ et $w_n = u_{2n+1}$ vérifient $v_{n+1} = g(v_n)$, $w_{n+1} = g(w_n)$, donc sont monotones par le point 1. Si $(v_n)$ est croissante, $v_n \le v_{n+1}$ et, $f$ étant décroissante, $f(v_n) \ge f(v_{n+1})$, c'est-à-dire $w_n \ge w_{n+1}$ : $(w_n)$ est décroissante (et inversement).

**Remarque.** Pour la monotonie, on peut étudier le signe de $x \mapsto f(x) - x$ sur $I$ : si $f(x) - x \ge 0$ sur $I$, alors $u_{n+1} - u_n = f(u_n) - u_n \ge 0$ et la suite est croissante.

![[AnalyseID1 - p36.jpg]]

*Figure : diagramme en escargot pour $f$ décroissante ; les termes $u_0, u_2, \ldots$ et $u_1, u_3, \ldots$ s'approchent du point fixe de part et d'autre.*

**Propriété 19 (convergence).** Si $f$ est continue sur $I$ et si $(u_n)$ converge vers $\ell$, alors $f(\ell) = \ell$ : $\ell$ est un [[Point fixe]] de $f$. (Preuve par la caractérisation séquentielle de la limite, démontrée au chapitre 3.)

**Exercice.** Étudier la suite définie par $u_{n+1} = \sqrt{1 + u_n}$ et $u_0 \ge -1$. Non corrigé dans le cours.

Piste : $f(x) = \sqrt{1 + x}$ est continue et croissante sur $[-1, +\infty[$, intervalle stable ; un point fixe vérifie $\ell \ge 0$ et $\ell^2 = 1 + \ell$, donc $\ell = \varphi = \frac{1 + \sqrt5}{2}$ (le nombre d'or). Le signe de $f(x) - x$ (positif sur $[-1, \varphi]$, négatif au-delà) montre que la suite est croissante si $u_0 \le \varphi$, décroissante sinon, et bornée par $\varphi$ du même côté : elle converge vers $\varphi$ par le théorème de la limite monotone. [[Complément hors du cours|ⓘ]]

### VII. Suites complexes

On étend aux suites complexes les propriétés des suites réelles qui ne font pas appel à l'ordre de $\mathbb{R}$ (pas de croissance, décroissance, majorant, minorant), en remplaçant la valeur absolue par le module. Voir [[Suite complexe]] et [[Nombre complexe]].

**Définitions.** $(u_n) \in \mathbb{C}^{\mathbb{N}}$ est bornée s'il existe $M > 0$ tel que $\forall n,\ |u_n| \le M$ ; elle converge vers $\ell \in \mathbb{C}$ si $\forall \varepsilon > 0\ \exists N\ \forall n\ (n \ge N \Rightarrow |u_n - \ell| \le \varepsilon)$.

**Remarque.** Il n'existe pas de limite infinie.

**Théorème (parties réelle et imaginaire).** $u_n \to \ell \iff \mathrm{Re}(u_n) \to \mathrm{Re}(\ell)$ et $\mathrm{Im}(u_n) \to \mathrm{Im}(\ell)$.
*Preuve* : $|\mathrm{Re}(u_n) - \mathrm{Re}(\ell)| \le |u_n - \ell|$ (encadrement de suites réelles) ; réciproquement, $|u_n - \ell| = \sqrt{(\mathrm{Re}\,u_n - \mathrm{Re}\,\ell)^2 + (\mathrm{Im}\,u_n - \mathrm{Im}\,\ell)^2} \to 0$.

**En résumé.**

| Ce qui reste valable | Ce qui n'est plus valable |
|---|---|
| unicité de la limite | majorant, minorant |
| une suite convergente est bornée | monotonie |
| opérations sur les limites | limites infinies |
| suites extraites | passage à la limite dans $\le$ |
| | théorème des gendarmes |
| | théorème de la limite monotone |
| | suites adjacentes |

### TD2 - Suites numériques (pages 38 à 43)

Énoncés détaillés dans [[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]]. Plan de la feuille (aucune correction dans le polycopié) :
1. **Généralités** (ex. 1-2) : exemples de suites (croissante majorée, ni croissante ni décroissante, ni majorée ni minorée) ; propriétés « à partir d'un certain rang » avec quantificateurs.
2. **Techniques classiques** (ex. 3-5) : limites de quotients, de différences de racines (quantité conjuguée), de $\frac{a^n - b^n}{a^n + b^n}$, de $1 + a + \dots + a^n$, de $n^{1/n}$, de $\frac{E(nx)}{n}$, de $\sum \frac{1}{\sqrt{n^2 + k}}$…
3. **Définition, opérations, théorèmes d'existence, suites extraites** (ex. 6-21) : convergence par la définition ; vrai-faux sur les limites (ex. 7-8) ; $u_{2n}$, $u_{3n}$, $u_{2n+1}$ convergentes ⇒ $u_n$ converge (ex. 10) ; $\varphi(n) \ge n$ (ex. 11) ; $(1 + x/n)^n \to e^x$ (ex. 12) ; $n!/n^n$ (ex. 13) ; critère du rapport $u_{n+1}/u_n \to \ell$ (ex. 14) ; [[Théorème de Cesàro]] (ex. 15) ; suites adjacentes (ex. 17-19, 32) ; densité de $\mathbb{Q}$ par $\frac{1}{n^2}\sum E(kx)$ (ex. 20) ; [[Constante d'Euler]] $\gamma \approx 0{,}5772$ par $H_n - \ln n$ (ex. 21).
4. **Suites récurrentes** (ex. 22-25) : $u_{n+1} = \sqrt{u_n + 1}$, $u_{n+1} = \frac{1}{u_n} + 1$, $u_0 = 0$, $u_{n+1} = 3 - \sqrt{u_n/2}$ avec $f(x) = 3 - \sqrt{x/2}$, $f(x) = 1 + \frac2x$, $u_{n+1} = \frac12 u_n(u_n^2 - 3u_n + 4)$.
5. **Suites complexes** (ex. 26-29) : limites de suites complexes, $z_{n+1} = \frac13(2z_n - \bar z_n)$, couple $(x_n, y_n)$ via $z_n = x_n + iy_n$, suite géométrique $a^n$ selon $|a|$.
6. **Exercices supplémentaires** (ex. 30-32) : récurrence $a_n = \frac12(a_{n-2} + a_{n-1})$, moyennes arithmétique, géométrique et harmonique.

## Chapitre 3 : limites et continuité de fonctions (pages 44 à 60)

Voir aussi [[Limite et continuité]]. Dans tout le chapitre, $I$ est un intervalle de $\mathbb{R}$ non vide et non réduit à un point ; $\mathring{I} = I \setminus \{\text{extrémités}\}$ (intérieur) et $\bar I = I \cup \{\text{extrémités}\}$. Exemples : $\mathring{[0,2[} = ]0, 2[$, $\overline{]0,2[} = [0,2]$, $\mathring{]1, +\infty[} = ]1, +\infty[$, $\overline{]1, +\infty[} = [1, +\infty[ \cup \{+\infty\}$, $\overline{\mathbb{R}} = \mathbb{R} \cup \{\pm\infty\}$. Voir [[Intérieur et adhérence]].

### I. Limite de fonction

**Définition (limite en un point $a \in \bar I$ réel).** Soit $f : I \to \mathbb{R}$.
- $f(x) \xrightarrow[x\to a]{} \ell \in \mathbb{R}$ si $\forall \varepsilon > 0,\ \exists \eta > 0,\ \forall x \in I,\ |x - a| \le \eta \Rightarrow |f(x) - \ell| \le \varepsilon$.
- $f(x) \to +\infty$ en $a$ si $\forall M > 0,\ \exists \eta > 0,\ \forall x \in I,\ |x - a| \le \eta \Rightarrow f(x) \ge M$.
- $f(x) \to -\infty$ en $a$ si $\forall M < 0,\ \exists \eta > 0,\ \forall x \in I,\ |x - a| \le \eta \Rightarrow f(x) \le M$.

**Remarque.** La distance de $f(x)$ à $\ell$ peut être rendue inférieure à tout $\varepsilon > 0$, pourvu que $x$ soit assez proche de $a$.

**Définition (limite en $+\infty$)**, si $+\infty$ est une extrémité de $I$ :
- $f \to \ell$ : $\forall \varepsilon > 0,\ \exists A > 0,\ \forall x \in I,\ x \ge A \Rightarrow |f(x) - \ell| \le \varepsilon$ ;
- $f \to +\infty$ : $\forall M > 0,\ \exists A > 0,\ \forall x \in I,\ x \ge A \Rightarrow f(x) \ge M$ ;
- $f \to -\infty$ : $\forall N < 0,\ \exists A > 0,\ \forall x \in I,\ x \ge A \Rightarrow f(x) \le N$.

Ici, la distance de $f(x)$ à $\ell$ est inférieure à $\varepsilon$ pourvu que $x$ soit assez grand.

**Définition (limite en $-\infty$)** : même chose avec $\exists B \in \mathbb{R}$ (ou $B < 0$) et $x \le B$ : [[Erreurs du cours#^e-0-rappels-pdf|✎]]
- $f \to \ell$ : $\forall \varepsilon > 0,\ \exists B,\ \forall x \in I,\ x \le B \Rightarrow |f(x) - \ell| \le \varepsilon$ ;
- $f \to +\infty$ : $\forall M > 0,\ \exists B,\ x \le B \Rightarrow f(x) \ge M$ ;
- $f \to -\infty$ : $\forall N < 0,\ \exists B,\ x \le B \Rightarrow f(x) \le N$.

**Remarque.** Pour $\ell \in \mathbb{R}$ : $f(x) \to \ell \iff |f(x) - \ell| \to 0$ ; en particulier $f \to 0 \iff |f| \to 0$.

**Formulation unique avec les voisinages.** Voisinages de $a \in \mathbb{R}$ : $[a - h, a + h]$ avec $h > 0$ ; de $+\infty$ : $[c, +\infty[$ ; de $-\infty$ : $]-\infty, c]$. On note $\mathcal{V}(a)$ l'ensemble des voisinages. $f$ vérifie une propriété $\mathcal{P}$ au voisinage de $a$ s'il existe $V \in \mathcal{V}(a)$ tel que $f$ vérifie $\mathcal{P}$ sur $I \cap V$. Toutes les définitions s'écrivent :
$$f(x) \xrightarrow[x\to a]{} \ell \iff \forall V \in \mathcal{V}(\ell),\ \exists U \in \mathcal{V}(a),\ \forall x \in I,\ x \in U \Rightarrow f(x) \in V.$$

![[AnalyseID1 - p46.jpg]]

*Figure : quatre cas de limite illustrés par voisinages — $\lim_a f = \ell$, $\lim_{+\infty} f = +\infty$, $\lim_{+\infty} f = \ell$, $\lim_a f = +\infty$ ; pour tout voisinage $\mathcal{V}$ de la limite (en bleu) existe un voisinage de $a$ (en rouge) dont l'image y entre.*

**Propriété 1 (unicité de la limite).** Si $f$ admet une limite finie en $a \in \bar I$, elle est unique, notée $\lim_{x\to a} f(x)$.
*Preuve par l'absurde* : avec $\varepsilon = \frac{|\ell_1 - \ell_2|}{3}$ et $\eta_0 = \min(\eta_1, \eta_2)$, pour $|x - a| \le \eta_0$, $|\ell_1 - \ell_2| \le |f(x) - \ell_1| + |f(x) - \ell_2| \le \frac23|\ell_1 - \ell_2|$, donc $\ell_1 = \ell_2$.

### Limites à droite et à gauche

**Définition.** Soit $a \in \mathring I$. $f$ admet une limite à gauche en $a$ si $f_{|I \cap ]-\infty, a[}$ admet une limite en $a$, notée $\lim_{x\to a^-} f(x)$ ou $\lim_{x\to a,\ x<a} f(x)$ ; à droite si $f_{|I \cap ]a, +\infty[}$ en admet une, notée $\lim_{x\to a^+} f(x)$.

**Propriété 3.** Si $f$ admet une limite $\ell$ en $a \in \mathring I$, elle admet une limite à gauche et une limite à droite en $a$, toutes deux égales à $\ell$.

**Définition.** Pour $a \in \mathring I$ et $f : I \setminus \{a\} \to \mathbb{R}$, $f$ admet une limite $\ell \in \overline{\mathbb{R}}$ en $a$ si elle admet une limite à droite et une limite à gauche en $a$ et qu'elles coïncident.

### Propriétés

**Propriété 4.** Si $f$ admet une limite finie en $a \in \bar I$, elle est bornée au voisinage de $a$.
*Preuve* : avec $\varepsilon = 1$, pour $x \in I \cap [a - \eta, a + \eta]$, $|f(x)| \le |f(x) - \ell| + |\ell| \le 1 + |\ell|$.

**Théorème 6 (caractérisation séquentielle de la limite).** Pour $\ell \in \overline{\mathbb{R}}$, $a \in \bar I$ :
$$\lim_{x\to a} f(x) = \ell \iff \left(\forall (u_n) \in I^{\mathbb{N}} \text{ telle que } u_n \to a,\ f(u_n) \to \ell\right).$$
Voir [[Caractérisation séquentielle de la limite]].

*Preuve ($a$, $\ell$ finis).* ⇒ : pour $\varepsilon > 0$, soit $\eta$ de la définition ; comme $u_n \to a$, $|u_n - a| \le \eta$ pour $n \ge N$, donc $|f(u_n) - \ell| \le \varepsilon$. ⇐ par contraposée : si $f$ ne tend pas vers $\ell$, $\exists \varepsilon > 0,\ \forall \eta > 0,\ \exists x \in I,\ |x - a| \le \eta$ et $|f(x) - \ell| > \varepsilon$ ; avec $\eta_n = \frac1n$, on construit $x_n \to a$ telle que $(f(x_n))$ ne converge pas vers $\ell$.

**Méthode.** Pour montrer qu'une fonction n'a pas de limite en $a$, chercher deux suites $(x_n)$ et $(y_n)$ qui tendent vers $a$ et telles que $(f(x_n))$ et $(f(y_n))$ aient deux limites différentes.

### II. Opérations sur les limites de fonctions

**Propriété 7.** Si $f \to \ell$ et $g \to \ell'$ (finies) en $a \in \bar I$ :
1. $\lambda f + \mu g \to \lambda\ell + \mu\ell'$ pour tout $(\lambda, \mu) \in \mathbb{R}^2$ ;
2. $fg \to \ell\ell'$ ;
3. si $\ell' \ne 0$, $\frac{f}{g}$ est définie au voisinage de $a$ et tend vers $\frac{\ell}{\ell'}$.

*Preuve* : par la caractérisation séquentielle et les opérations sur les limites de suites.

**Remarque.** Ces formules s'étendent aux limites infinies, sauf pour les **formes indéterminées** $\infty - \infty$, $0 \times (\pm\infty)$, $\frac{\pm\infty}{\pm\infty}$, $\frac00$.

Pour lever ces formes, on s'appuie sur quelques **limites usuelles** (taux d'accroissement en 0, ce sont des nombres dérivés) et sur les [[Croissances comparées]], avec $\alpha, \beta > 0$ : [[Complément hors du cours|ⓘ]]
$$\lim_{x\to0}\frac{\sin x}{x} = 1,\qquad \lim_{x\to0}\frac{e^x - 1}{x} = 1,\qquad \lim_{x\to0}\frac{\ln(1+x)}{x} = 1,\qquad \lim_{x\to0}\frac{1 - \cos x}{x^2} = \frac12,$$
$$\lim_{x\to+\infty}\frac{(\ln x)^\beta}{x^\alpha} = 0,\qquad \lim_{x\to+\infty}\frac{x^\alpha}{e^{\beta x}} = 0,\qquad \lim_{x\to0^+} x^\alpha\,|\ln x|^\beta = 0.$$

**Propriété 9 (composition des limites).** Si $f : I \to \mathbb{R}$, $g : J \to \mathbb{R}$ avec $f(I) \subset J$, $a \in \bar I$, $\lim_a f = b$ et $\lim_b g = c$, alors $\lim_{x\to a} (g \circ f)(x) = c$. Voir [[Composition de fonctions]].
*Preuve ($a, b, c$ réels)* : $\exists \nu,\ |y - b| \le \nu \Rightarrow |g(y) - c| \le \varepsilon$, puis $\exists \eta,\ |x - a| \le \eta \Rightarrow |f(x) - b| \le \nu$.

**Propriété 10 (passage à la limite dans les inégalités larges).** Si $f \to \ell \in \mathbb{R}$, $g \to \ell' \in \mathbb{R}$ en $a$ et $f \le g$ au voisinage de $a$, alors $\ell \le \ell'$.
*Preuve par l'absurde* avec $\varepsilon = \frac{\ell - \ell'}{3}$, comme pour les suites. Les inégalités strictes deviennent larges par passage à la limite.

### III. Théorèmes d'existence de limites de fonctions

**Théorème 11 (encadrement).** Si $f \le g \le h$ au voisinage de $a$ et $\lim_a f = \lim_a h = \ell$, alors $\lim_a g$ existe et vaut $\ell$.

**Théorème 13 (minoration, majoration).**
1. Si $f \le g$ au voisinage de $a$ et $\lim_a f = +\infty$, alors $\lim_a g = +\infty$.
2. Si $f \le g$ au voisinage de $a$ et $\lim_a g = -\infty$, alors $\lim_a f = -\infty$.

**Théorème 14 (limite monotone).** Soit $-\infty \le a < b \le +\infty$ et $f : ]a, b[ \to \mathbb{R}$.
- $f$ **croissante** : si $f$ est majorée, $\lim_{x\to b} f(x) = \sup_{]a,b[} f$, sinon $\lim_b f = +\infty$ ; si $f$ est minorée, $\lim_{x\to a} f(x) = \inf_{]a,b[} f$, sinon $\lim_a f = -\infty$.
- $f$ **décroissante** : si $f$ est minorée, $\lim_b f = \inf_{]a,b[} f$, sinon $-\infty$ ; si $f$ est majorée, $\lim_a f = \sup_{]a,b[} f$, sinon $+\infty$.

Notation : $\inf_{x\in]a,b[} f(x) = \inf\{f(x) \mid x \in ]a,b[\}$, de même pour $\sup$.

*Preuve (non exigible, $f$ croissante, limite en $b$).* Si $f$ est majorée, $E = \{f(x)\}$ a une borne supérieure $\ell$ ; pour $\varepsilon > 0$, il existe $y_0 = f(x_0) > \ell - \varepsilon$, et pour $x \in [x_0, b[$, $\ell - \varepsilon \le f(x_0) \le f(x) \le \ell$. Si $f$ n'est pas majorée, pour $A > 0$ il existe $x_A$ avec $f(x_A) > A$, et $f(x) \ge f(x_A) > A$ pour $x \in [x_A, b[$.

**Propriété 15.** Si $f : I \to \mathbb{R}$ est monotone et $a \in I$ n'est pas une borne de $I$, $f$ admet des limites finies à gauche et à droite en $a$, et
$$f \text{ croissante} : \lim_{x\to a^-} f(x) \le f(a) \le \lim_{x\to a^+} f(x) ; \qquad f \text{ décroissante} : \lim_{x\to a^+} f(x) \le f(a) \le \lim_{x\to a^-} f(x).$$

**Remarque.** Ces inégalités peuvent être strictes (penser à la partie entière) : $f$ n'est pas forcément continue en $a$. On établit sa continuité en $a$ en prouvant $\lim_{a^-} f = f(a) = \lim_{a^+} f$, les limites existant par monotonie.

### IV. Continuité

**Définition (continuité en un point).** $f : I \to \mathbb{R}$ est continue en $a \in I$ si elle admet une limite finie en $a$, qui vaut alors $f(a)$ :
$$\forall \varepsilon > 0,\ \exists \eta > 0,\ \forall x \in I,\ |x - a| \le \eta \Rightarrow |f(x) - f(a)| \le \varepsilon.$$
*Preuve que la limite vaut $f(a)$* : $a$ appartient à $[a - \eta, a + \eta] \cap I$, donc $|f(a) - \ell| \le \varepsilon$ pour tout $\varepsilon$.

**Remarque.** Géométriquement, une fonction est continue si son graphe se trace « sans lever le crayon ».

**Exemple.** $x \mapsto \sqrt x$ est continue en 2 : pour $x \in \mathbb{R}_+$, $|\sqrt x - \sqrt 2| = \frac{|x - 2|}{\sqrt x + \sqrt 2} \le |x - 2|$ ; avec $\eta = \varepsilon$, $|x - 2| \le \varepsilon \Rightarrow |\sqrt x - \sqrt 2| \le \varepsilon$.

**Définition (continuité à gauche, à droite).** $f$ est continue à gauche (resp. à droite) en $a$ si $f(a)$ est la limite à gauche (resp. à droite) de $f$ en $a$. $f$ est continue en $a$ si et seulement si elle est continue à gauche et à droite en $a$.

**Exemple.** La [[Partie entière]] $x \mapsto \lfloor x \rfloor$ est continue à droite en tout point de $\mathbb{R}$, mais continue à gauche seulement aux points de $\mathbb{R} \setminus \mathbb{Z}$.

![[AnalyseID1 - p52.jpg]]

*Figure : graphe de la partie entière, en marches ; chaque palier contient son extrémité gauche, d'où la continuité à droite.*

**Définition (prolongement par continuité).** Soit $a \in I$ et $f : I \setminus \{a\} \to \mathbb{R}$. $f$ est prolongeable par continuité en $a$ s'il existe $\tilde f : I \to \mathbb{R}$ continue en $a$ telle que $\tilde f_{|I \setminus \{a\}} = f$.

**Propriété 16.** $f$ est prolongeable par continuité en $a$ si et seulement si $f$ admet une limite finie $\ell$ en $a$. Ce prolongement est alors unique :
$$\tilde f(x) = \begin{cases} f(x) & \text{si } x \ne a \\ \ell & \text{si } x = a \end{cases}$$
C'est le prolongement par continuité de $f$ en $a$, souvent noté $f$. Voir [[Prolongement par continuité]].
*Preuve* : ⇒ $\tilde f(a) = \lim_{a^-} \tilde f = \lim_{a^+} \tilde f$, et ces limites sont celles de $f$ ; cela prouve aussi l'unicité. ⇐ la fonction $\tilde f$ ci-dessus convient.

**Propriété 17 (caractérisation séquentielle de la continuité).** $f$ est continue en $a \in I$ si et seulement si, pour toute suite $(x_n)$ d'éléments de $I$ convergeant vers $a$, $f(x_n) \to f(a)$.

**Définition (continuité sur un intervalle).** $f$ est continue sur $I$ si elle est continue en chaque point de $I$. On note $\mathcal{C}^0(I, \mathbb{R})$ ou $\mathcal{C}(I, \mathbb{R})$ l'ensemble des fonctions continues de $I$ dans $\mathbb{R}$.

**Exemples.** $\exp$, $\log$, $x \mapsto x$ sont continues sur $\mathbb{R}$ (sur leur domaine) ; $x \mapsto \sqrt x$ est continue sur $\mathbb{R}_+$.

**Propriété 19 (opérations).** Si $f, g$ sont continues sur $I$ et $(\lambda, \mu) \in \mathbb{R}^2$ :
1. $\lambda f + \mu g$ et $f \times g$ sont continues sur $I$ ;
2. si $g$ ne s'annule pas sur $I$, $\frac{f}{g}$ est continue sur $I$.

**Remarque.** Les polynômes sont continus sur $\mathbb{R}$ ; $\tan$ est continue sur $]-\frac{\pi}{2} + k\pi, \frac{\pi}{2} + k\pi[$ ; une fraction rationnelle $\frac{P}{Q}$ est continue sur $\mathbb{R}$ privé des racines de $Q$ (ses pôles).

**Propriété 20 (composition).** Si $f : I \to \mathbb{R}$ est continue sur $I$, $g : J \to \mathbb{R}$ continue sur $J$ et $f(I) \subset J$, alors $g \circ f$ est continue sur $I$.

**Remarque.** C'est avec ces théorèmes qu'on établit en pratique la continuité d'une fonction, sauf en certains points qui demandent une étude particulière.

### V. Les grands théorèmes de la continuité

**Théorème 21 (valeurs intermédiaires, TVI).** Si $f : I \to \mathbb{R}$ est continue et $(a, b) \in I^2$ vérifie $f(a)f(b) \le 0$, il existe $c$ entre $a$ et $b$ tel que $f(c) = 0$. Voir [[Théorème des valeurs intermédiaires]].

*Preuve par dichotomie* (voir [[Recherche dichotomique]]), avec $a < b$. On construit deux suites adjacentes : $a_0 = a$, $b_0 = b$ ; si $a_n, b_n$ sont construits avec $b_n - a_n = \frac{b-a}{2^n}$ et $f(a_n)f(b_n) \le 0$, on pose $m_n = \frac{a_n + b_n}{2}$ : [[Erreurs du cours#^e-0-rappels-pdf|✎]]
- si $f(a_n)f(m_n) \le 0$ : $a_{n+1} = a_n$, $b_{n+1} = m_n$ ;
- si $f(a_n)f(m_n) > 0$ : $a_{n+1} = m_n$, $b_{n+1} = b_n$.

Dans les deux cas, $f(a_{n+1})f(b_{n+1}) \le 0$ et $b_{n+1} - a_{n+1} = \frac{b-a}{2^{n+1}}$. $(a_n)$ croît, $(b_n)$ décroît, $b_n - a_n \to 0$ : elles sont adjacentes et convergent vers $c \in [a, b]$. Par continuité, en passant à la limite dans $f(a_n)f(b_n) \le 0$, on obtient $f(c)^2 \le 0$, donc $f(c) = 0$.

**Remarque.** $|a_n - c| \le |b_n - a_n| \le \frac{b-a}{2^n} \to 0$ : $a_n$ (ou $b_n$) approche $c$ à $\frac{b-a}{2^n}$ près.

**Propriété 22 (TVI, deuxième forme).** Si $I$ est un intervalle et $f$ est continue sur $I$, alors $f(I)$ est un intervalle : pour tous $a, b \in I$ et tout $y$ entre $f(a)$ et $f(b)$, il existe $c \in [a, b]$ tel que $f(c) = y$.
*Preuve* : appliquer le TVI à $g(x) = f(x) - y$, continue, avec $g(a)$, $g(b)$ de signes contraires.

**Propriété 23 (image d'un segment).** Une fonction continue sur un segment est bornée et atteint ses bornes : si $f : [a, b] \to \mathbb{R}$ est continue, il existe $(c, d) \in [a, b]^2$ tel que $\forall x \in [a, b],\ f(c) \le f(x) \le f(d)$. $c$ et $d$ sont les minimum et maximum globaux de $f$ sur $[a, b]$. Voir [[Théorème des bornes atteintes]].

**Propriété 24.** L'image d'un segment par une fonction continue est un segment : $f([a,b]) = [f(c), f(d)]$ (bornes atteintes, puis TVI).

**Propriété 25 (injectivité et monotonie stricte).** Une fonction continue $f : I \to \mathbb{R}$ est injective sur $I$ si et seulement si elle est strictement monotone. Voir [[Injectivité et surjectivité]].
*Preuve.* ⇐ : si $x \ne y$, $f(x) < f(y)$ ou $f(x) > f(y)$. ⇒ : on montre que $f$ est strictement monotone sur tout $[a, b]$ ; si par exemple $f(a) < f(b)$ et $a \le x < y \le b$, on pose $g(t) = f(tx + (1-t)a) - f(ty + (1-t)b)$ sur $[0, 1]$ ; $g$ est continue et ne s'annule pas (sinon $tx + (1-t)a = ty + (1-t)b$, impossible car $tx + (1-t)a < ty + (1-t)b$), donc garde le signe de $g(0) = f(a) - f(b) < 0$ ; ainsi $g(1) = f(x) - f(y) < 0$.

**Théorème 26 (continuité et bijection).** Toute fonction continue et strictement monotone sur un intervalle $I$ réalise une bijection de $I$ sur l'intervalle $f(I)$. Sa réciproque est continue et strictement monotone sur $f(I)$, de même monotonie que $f$. Voir [[Théorème de la bijection]] et [[Bijection]].
*Preuve* ($f$ croissante, quitte à remplacer $f$ par $-f$) : $f(I)$ est un intervalle, $f$ est injective, donc bijective de $I$ sur $f(I)$. $f^{-1}$ est strictement croissante (si $y < y'$, $f^{-1}(y) < f^{-1}(y')$, sinon on contredit la croissance de $f$). $f^{-1}$ étant monotone, elle a en tout $a \in f(I)$ des limites à gauche et à droite avec $\lim_{a^-} f^{-1} \le f^{-1}(a) \le \lim_{a^+} f^{-1}$ ; si l'une des inégalités était stricte, les valeurs strictement comprises entre $f^{-1}(a)$ et $\lim_{a^+} f^{-1}$ n'auraient pas d'antécédent par $f^{-1}$, ce qui contredit la bijectivité de $f^{-1} : f(I) \to I$.

### TD3 - Limites et continuité (pages 57 à 60)

Aucune correction dans le polycopié.

**1. Généralités sur les fonctions**
- **Ex. 1.** Pour $f : \mathbb{R} \to \mathbb{R}$, écrire avec des quantificateurs ([[Quantificateur]]) : $f$ n'est pas constante ; 2 n'est l'image d'aucun réel ; $f$ prend la même valeur en deux réels opposés ; aucun réel négatif n'est égal à son image.
- **Ex. 2.** (1) $f(x) = \frac{\cos x + 2}{x^2 + 1}$ est-elle bornée (sans étudier ses variations) ? Position de son graphe par rapport à celui de $g(x) = \frac{1}{x^2 + 1}$. (2) $f(x) = \ln\frac{1 - 4x^2}{2}$ : pour quels $x$ le graphe est-il au-dessus de l'axe des abscisses ?

**2. Définition de la limite**
- **Ex. 3.** $f(x) = \frac{2x + 3}{3x - 1}$ sur $\mathbb{R} \setminus \{\frac13\}$ : pour tout $\varepsilon > 0$, trouver $\alpha$ tel que ($x \ne \frac13$ et $|x| \le \alpha$) $\Rightarrow |f(x) + 3| \le \varepsilon$. Conclusion ?
- **Ex. 4.** Montrer par la définition : $\lim_{x\to0}\sqrt{x+1} = 1$ ; $\lim_{x\to0} x^2\cos\frac1x = 0$ ; $\lim_{x\to2}\frac{x+1}{|x-2|} = +\infty$ ; $\lim_{x\to+\infty}\frac{1}{e^x + 1} = 0$.

**3. Propriétés des limites**
- **Ex. 5.** Si $\lim_{x_0} f = u > 0$ ($x_0$ intérieur à $I$), montrer qu'il existe $\alpha > 0$ tel que $0 < |x - x_0| < \alpha \Rightarrow |f(x)| \ge \frac u2$.
- **Ex. 6.** Une fonction [[Fonction périodique|périodique]] sur $\mathbb{R}$ qui a une limite finie en $+\infty$ est constante.
- **Ex. 7.** Si $f \to \ell$ et $g \to \ell'$ en 0, alors $\max(f, g) \to \max(\ell, \ell')$.
- **Ex. 8.** Si $f$, $g$ positives sur $\mathbb{R}_+$ ont la même limite en $+\infty$, a-t-on $\frac{f}{g} \to 1$ ?
- **Ex. 9.** (1) Si $f \to \ell \in \mathbb{R}$ en $+\infty$, montrer (P) : $\forall \varepsilon > 0,\ \exists A,\ \forall x, x' > A,\ |f(x) - f(x')| < \varepsilon$. (2) Écrire la négation de (P). (3) La montrer pour $\sin$ (avec $x = 2n\pi$, $x' = 2n\pi + \frac\pi2$) ; conclure. (4) Quelles fonctions périodiques ont une limite finie en $+\infty$ ?
- **Ex. 10.** Si $g > 0$ sur $\mathbb{R}_+$ et $\frac{f}{g} \to L \ne 0$ en $+\infty$ : $f \to 0 \iff g \to 0$ ; si $L > 0$, $f \to +\infty \iff g \to +\infty$.

**4. Calculs de limites**
- **Ex. 11.** $\lim_{0} x\sin\frac1x$ ; $\lim_{+\infty}\frac{x\cos(e^x)}{x^2 + 1}$ ; $\lim_{+\infty} e^{x - \sin x}$ ; $\lim_0 x E\left(\frac1x\right)$ ; $\lim_{+\infty} x E\left(\frac1x\right)$.
- **Ex. 12.** $\lim_{x\to1}\left(\frac{3}{x^3 - 1} - \frac{2}{x^2 - 1}\right)$ ; $\lim_{+\infty}\left(\sqrt{x^2 + 2x - 1} - x\right)$ ; $\lim_{+\infty}\left(\sqrt{x + \sqrt{x+1}} - \sqrt{x + \sqrt{x - 1}}\right)$.

**5. Continuité**
- **Ex. 13.** (1) $f(x) = \frac{e^{3x} - 1}{x}$ si $x < 0$, $\frac{x^2 + 2x + 3}{x^3 + 1}$ si $x \ge 0$ : $f$ est-elle continue sur $\mathbb{R}$ ? (2) $g(x) = \frac{\sin(ax)}{x}$ si $x < 0$, $\frac{\ln(1 + 3x)}{2x}$ si $x > 0$ : quelle valeur de $a$ rend $g$ prolongeable par continuité en 0 ?
- **Ex. 14.** $g(x) = \frac{\ln x}{x - 1}$ sur $]0, 1[$, $g(1) = 2$, $g(x) = \frac{x+1}{3x - 1}$ pour $x > 1$ : $g$ est-elle continue en 1 ?
- **Ex. 15.** $f(x) = e^{2x+2}$ si $x < -1$, $2x + 3$ si $-1 \le x \le 0$, $x^2 + 2x + 3$ si $x > 0$ : la représenter, montrer qu'elle est continue et strictement croissante, donner sa réciproque.
- **Ex. 16.** Continuité de $f_1(x) = x^2\cos\frac1x$ ($f_1(0) = 0$), $f_2(x) = \sin x\sin\frac1x$ ($f_2(0) = 0$), $f_3(x) = xE(x)$, $f_4(x) = [x - E(x)]^2$, $f_5 = E + f_4$.
- **Ex. 17.** La [[Fonction indicatrice]] de $\mathbb{Q}$ (1 sur $\mathbb{Q}$, 0 sinon) n'est continue en aucun point.
- **Ex. 18.** Trouver les $f$ continues en 0 telles que $f(x) = f(3x)$ ; les $f$ continues en 1 telles que $f(x) = -f(x^2)$.

**6. Grands théorèmes de la continuité**
- **Ex. 19.** (1) $f$ continue sur $[a, b]$ avec $f([a,b]) \subset [a,b]$ a un point fixe (étudier $\varphi(x) = f(x) - x$). (2) $f$ continue sur $[0, 1]$ avec $f(0) = f(1)$ : il existe $c \in [0, \frac12]$ tel que $f(c) = f(c + \frac12)$. (3) Un mobile parcourant à vitesse continue une distance $d$ en une unité de temps parcourt $\frac d2$ pendant un intervalle d'une demi-unité.
- **Ex. 20.** Fonctions continues sur $I$ dont l'image est finie.
- **Ex. 21.** Vrai ou faux pour $f$ continue sur $\mathbb{R}$, puis continue et strictement monotone : l'image d'un intervalle ouvert est un intervalle ouvert ; l'image d'un segment est un segment ; l'image d'une partie bornée est bornée ; l'image réciproque d'un intervalle est un intervalle.
- **Ex. 22.** $f$ continue sur $\mathbb{R}$ ayant des limites finies en $\pm\infty$ est bornée.
- **Ex. 23.** $x^{17} = x^{11} + 1$ a au moins une solution réelle ; tout polynôme de degré impair a une racine réelle.
- **Ex. 24.** Si $f$, $g$ continues sur $I$ vérifient $f(x)^2 = g(x)^2 \ne 0$, alors $f = g$ ou $f = -g$.
- **Ex. 25.** $f$, $g$ continues sur $[0, 1]$, $f(0) = g(1) = 0$, $g(0) = f(1) = 1$ : $\forall \lambda > 0,\ \exists x \in [0, 1],\ f(x) = \lambda g(x)$.
- **Ex. 26.** Nombre de solutions de $\ln x = mx$ selon $m$.
- **Ex. 27.** $f(x) = \frac{e^x}{1 + e^x}$ est continue, bijective ; déterminer $f^{-1}$.
- **Ex. 28.** (1) Si $f$ est strictement croissante, $f \circ f(x) = x \iff f(x) = x$. (2) $f(x) = x^5 + x - 1$ : montrer qu'elle est bijective et résoudre $f(x) = f^{-1}(x)$.

## Chapitre 4 : dérivabilité (pages 61 à 72)

Plan relevé : nombre dérivé et opérations, dérivées usuelles, dérivées successives, classe $\mathcal{C}^n$ et formule de Leibniz, extremum local, Rolle, sens de variation, inégalité des accroissements finis, règle de l'Hôpital. TD4 : dérivabilité de $x|x|$, prolongements, dérivées, raccord $\mathcal{C}^2$, bijection $x\ln x - x$, parité et périodicité des dérivées, dérivées $n$-ièmes, Rolle pour compter les racines, suites $x_{n+1} = f(x_n)$ et point fixe attractif ou répulsif, injectivité locale. Voir [[4 - dérivabilité]] et [[Dérivabilité]].

## Chapitre 5 : analyse asymptotique (pages 73 à 95)

Plan relevé : domination, négligeabilité, équivalence pour les suites puis pour les fonctions, développements limités (généralités, Taylor-Young, opérations, applications). TD5 identique à [[Raw/Year 1/Analyse Maths/Exos/TD5-AnalAsympt.pdf|TD5-AnalAsympt]]. Voir [[5 - Analyse Maths|chp5]], [[Comparaison asymptotique]] et [[Développement limité]].

## Liens

[[Suite numérique]], [[Limite et continuité]], [[Dérivabilité]], [[Développement limité]], [[Comparaison asymptotique]], [[Borne supérieure]], [[Nombre complexe]].