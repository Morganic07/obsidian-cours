---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de td1slides ([[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]) (101 diapositives, texte, « Analyse 1, premier semestre 2026-2027 »), dans [[Analyse Maths (index)]]. Ce sont les diapositives corrigées du TD1 « Réels ». Elles reprennent les exercices de [[TD1-numbres-reels (résumé)]] et en ajoutent (partie entière, dénombrement d'entiers). Cours associé : [[chp 1 - reels (résumé)]].

Les diapositives ne contiennent aucune figure : seulement du texte, des calculs et deux tableaux de signe, recopiés ici. Les exercices marqués « À faire chez soi » ou « Pour aller plus loin » sont corrigés eux aussi. Les barres de période des écritures décimales sont perdues à l'extraction du texte ; elles sont rétablies ici d'après les calculs des corrigés.

## Exercice 1 : rationnels, décimaux, irrationnels

**Énoncé** : les nombres suivants sont-ils rationnels ? décimaux ? irrationnels ? $1/3$, $1/15$, $1/25$, $1/125$, $0{,}\overline{3}$, $\sqrt{2}$, $0{,}\overline{123456789}$…

**Rappel** : un [[Nombre rationnel|rationnel]] $r$ est **décimal** s'il s'écrit $r = \dfrac{p}{10^n}$, $p \in \mathbb{Z}$, $n \in \mathbb{N}$ ; autrement dit, il s'écrit exactement avec un nombre fini de chiffres après la virgule.

**Proposition** : un nombre est rationnel si et seulement s'il admet une écriture décimale périodique ou finie.

**Corrigé** :

| Nombre | Écriture décimale | Conclusion |
|---|---|---|
| $1/3$ | $0{,}\overline{3}$ | rationnel, écriture périodique |
| $1/15$ | $0{,}0\overline{6}$ | rationnel, écriture périodique |
| $1/25$ | $4/10^2 = 0{,}04$ | rationnel, décimal (écriture finie) |
| $1/125$ | $8/10^3 = 0{,}008$ | rationnel, décimal (écriture finie) |
| $0{,}\overline{3}$ | $= 1/3$ | rationnel, écriture périodique |
| $\sqrt{2}$ | — | irrationnel ([[Irrationalité de √2]]) |
| $0{,}\overline{123456789}$ | périodique | rationnel |

## Exercice 2 : fraction d'un développement périodique

**Énoncé** : écrire sous la forme $p/q$ les rationnels de développements $3{,}\overline{14}$, $0{,}\overline{9}$, $3{,}14\overline{9}$.

### Première méthode : série géométrique

Pour $a \ne 1$ ([[Suite géométrique]]) :
$$\sum_{k=0}^{n} a^k = \frac{1 - a^{n+1}}{1 - a}, \qquad \text{et si } 0 \le a < 1 : \quad \sum_{k=0}^{\infty} a^k = \lim_{n \to \infty}\sum_{k=0}^{n} a^k = \frac{1}{1-a}.$$

- $3{,}\overline{14} = 3 + \dfrac{14}{100} + \dfrac{14}{100^2} + \dfrac{14}{100^3} + \dots = 3 + \dfrac{14}{100}\displaystyle\sum_{k=0}^{+\infty}\left(\frac{1}{100}\right)^k = 3 + \frac{14}{100}\cdot\frac{100}{99} = 3 + \frac{14}{99} = \frac{311}{99}$.
- $3{,}14\overline{9} = \dfrac{314}{100} + \dfrac{9}{10^3} + \dfrac{9}{10^4} + \dots = \dfrac{314}{100} + \dfrac{9}{10^3}\cdot\dfrac{10}{9} = \dfrac{314}{100} + \dfrac{1}{100} = \dfrac{315}{100}$.
- (À faire chez soi) $0{,}\overline{9} = \dfrac{9}{10}\displaystyle\sum_{k=0}^{+\infty}\left(\frac{1}{10}\right)^k = \frac{9}{10}\cdot\frac{10}{9} = 1$.

### Autre méthode : décaler et soustraire

1. Faire apparaître la partie périodique juste après la virgule (multiplier par $10^k$).
2. Décaler d'une période (multiplier par $10^{\text{longueur de la période}}$).
3. Soustraire : les parties décimales s'annulent.

- $r = 3{,}14\overline{9}$ : $100r = 314{,}\overline{9}$ (1) ; $100 \times 10r = 3149{,}\overline{9}$ (2) ; (2) − (1) : $900r = 3149 - 314 = 2835$, donc $r = \dfrac{2835}{900} = \dfrac{315}{100}$.
- $r = 3{,}\overline{14}$ : la période commence juste après la virgule (3) ; $100r = 314{,}\overline{14}$ (4) ; (4) − (3) : $99r = 311$, donc $r = \dfrac{311}{99}$.

## Exercice 3 : $\ln 3 / \ln 2$ est irrationnel

**Rappels** : pour $a, b > 0$, $\ln(ab) = \ln a + \ln b$ ; $\ln(a^p) = p\ln a$ ; $\ln(a/b) = \ln a - \ln b$ ; $\exp(\ln a) = a$.

**Preuve** ([[Raisonnement par l'absurde|par l'absurde]]) : supposons $\dfrac{\ln 3}{\ln 2} = \dfrac{p}{q}$ avec $p \in \mathbb{Z}$, $q \in \mathbb{Z}^*$. Alors
$$p\ln 2 = q\ln 3 \iff \ln 2^p = \ln 3^q \iff 2^p = 3^q.$$
Contradiction ; donc $\ln 3/\ln 2$ est irrationnel (justification de la contradiction : voir les points à vérifier).

## Exercice 4 (pour aller plus loin) : rationnels et irrationnels

**Énoncé** : (1) si $r \in \mathbb{Q}$ et $x \notin \mathbb{Q}$, alors $r + x \notin \mathbb{Q}$, et si $r \ne 0$, $r \cdot x \notin \mathbb{Q}$ ; (2) $\sqrt{2} \notin \mathbb{Q}$ ; (3) en déduire qu'entre deux rationnels il y a toujours un irrationnel.

**Rappels** : $\mathbb{Q}$ est stable par somme et produit : $\dfrac{p}{q} + \dfrac{p'}{q'} = \dfrac{pq' + p'q}{qq'} \in \mathbb{Q}$ et $\dfrac{p}{q}\cdot\dfrac{p'}{q'} = \dfrac{pp'}{qq'} \in \mathbb{Q}$.

**Corrigé** (par l'absurde) :

- Si $r + x \in \mathbb{Q}$, alors $x = (x + r) - r \in \mathbb{Q}$ : contradiction.
- Si $r \cdot x \in \mathbb{Q}$ ($r \ne 0$), alors $x = (r \cdot x)\cdot\dfrac{1}{r} \in \mathbb{Q}$ : contradiction.
- Entre $r < r'$ rationnels : $i = r + \dfrac{\sqrt{2}}{2}(r' - r)$. Comme $0 < \sqrt{2}/2 < 1$, $0 < \frac{\sqrt{2}}{2}(r' - r) < r' - r$, donc $r < i < r'$. Et $i$ est irrationnel : rationnel + (rationnel non nul × irrationnel). Voir [[Densité de ℚ dans ℝ]].

La preuve de $\sqrt{2} \notin \mathbb{Q}$ n'est pas détaillée dans les diapositives.

## Exercice 5 : quantificateurs

Pour $A \subset \mathbb{R}$ ([[Quantificateur]], [[Majorant et minorant]]) :

| Propriété | Écriture |
|---|---|
| 10 est un majorant de $A$ | $\forall x \in A,\ x \le 10$ |
| $m$ est un minorant de $A$ | $\forall x \in A,\ x \ge m$ |
| $P$ n'est pas un majorant de $A$ | $\exists x \in A,\ x > P$ |
| $A$ est majoré | $\exists M \in \mathbb{R},\ \forall x \in A,\ x \le M$ |
| $A$ n'est pas minoré | $\forall m \in \mathbb{R},\ \exists x \in A,\ x < m$ |
| $A$ est borné | $\exists M \in \mathbb{R},\ \exists m \in \mathbb{R},\ \forall x \in A,\ m \le x \le M$ |
| $A$ n'est pas borné | $\forall M \in \mathbb{R},\ \forall m \in \mathbb{R},\ \exists x \in A,\ x < m \text{ ou } M < x$ |

## Exercice 6 : un ensemble défini par une inéquation

**Énoncé** : $I = \left\{x \in \mathbb{R}^* : -2 < x + \dfrac{1}{2x} \le 2\right\}$. (1) Montrer que $I$ est la réunion de deux intervalles. (2) Déterminer majorants, minorants, bornes, plus grand et plus petit élément.

**Inégalité de droite** : $x + \dfrac{1}{2x} \le 2 \iff \dfrac{2x^2 - 4x + 1}{2x} \le 0$.

| $x$ | $-\infty$ | | $0$ | | $1 - \frac{\sqrt2}{2}$ | | $1 + \frac{\sqrt2}{2}$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|---|---|
| $2x^2 - 4x + 1$ | | $+$ | | $+$ | 0 | $-$ | 0 | $+$ | |
| $2x$ | | $-$ | 0 | $+$ | | $+$ | | $+$ | |
| quotient | | $-$ | ‖ | $+$ | 0 | $-$ | 0 | $+$ | |

$$S_d = \,]-\infty, 0[\, \cup \left[1 - \frac{\sqrt{2}}{2},\ 1 + \frac{\sqrt{2}}{2}\right].$$

**Inégalité de gauche** : $x + \dfrac{1}{2x} > -2 \iff \dfrac{2x^2 + 4x + 1}{2x} > 0$.

| $x$ | $-\infty$ | | $-1 - \frac{\sqrt2}{2}$ | | $-1 + \frac{\sqrt2}{2}$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|---|---|
| $2x^2 + 4x + 1$ | | $+$ | 0 | $-$ | 0 | $+$ | | $+$ | |
| $2x$ | | $-$ | | $-$ | | $-$ | 0 | $+$ | |
| quotient | | $-$ | 0 | $+$ | 0 | $-$ | ‖ | $+$ | |

$$S_g = \left]-1 - \frac{\sqrt{2}}{2},\ -1 + \frac{\sqrt{2}}{2}\right[ \cup\, ]0, +\infty[.$$

**Conclusion** :
$$I = S_g \cap S_d = \left]-1 - \frac{\sqrt{2}}{2},\ -1 + \frac{\sqrt{2}}{2}\right[ \cup \left[1 - \frac{\sqrt{2}}{2},\ 1 + \frac{\sqrt{2}}{2}\right].$$

- $I$ n'a pas de minimum ; $\max I = 1 + \frac{\sqrt{2}}{2}$ ;
- $\inf I = -1 - \frac{\sqrt{2}}{2}$ ; $\sup I = \max I = 1 + \frac{\sqrt{2}}{2}$ ([[Borne supérieure]], [[Plus grand élément]]) ;
- $x$ est un minorant $\iff x \le -1 - \frac{\sqrt{2}}{2}$ ; $x$ est un majorant $\iff x \ge 1 + \frac{\sqrt{2}}{2}$.

## Exercice 7 : bornes de trois ensembles

**Énoncé** : $A = \left\{1 + \frac{1}{n} : n \in \mathbb{N}^*\right\}$, $B = \left\{\frac{1}{p} - \frac{1}{q} : p, q \in \mathbb{N}^*\right\}$, $C = \{x \in \mathbb{R} : x^2 < 2\}$. Majorés, minorés ? Bornes ? Plus petit, plus grand élément ?

### Ensemble $C$

$x \in C \iff x^2 < 2 \iff -\sqrt{2} < x < \sqrt{2}$, donc $C = \,]-\sqrt{2}, \sqrt{2}[$ ([[Intervalle réel]]) : $\sup C = \sqrt{2}$, $\inf C = -\sqrt{2}$. Comme $\pm\sqrt{2} \notin C$, $C$ n'a ni minimum ni maximum.

### Ensemble $A$

Pour tout $n \in \mathbb{N}^*$ : $0 < \frac{1}{n} \le 1$, donc $1 < 1 + \frac{1}{n} \le 2$.

- $2 = 1 + \frac{1}{1} \in A$, donc $\max A = \sup A = 2$.
- $A$ est minoré par 1, et $\lim_{n\to+\infty}(1 + \frac{1}{n}) = 1$ : candidat naturel pour $\inf A$.

**Méthode 1 (caractérisation)** : il faut montrer que 1 est le plus grand des minorants, c'est-à-dire $\forall m > 1,\ \exists x \in A,\ x < m$. Soit $m > 1$ ; on cherche $n$ avec $1 + \frac{1}{n} < m \iff \frac{1}{m-1} < n$. Comme $\mathbb{N}$ n'est pas majoré ([[Propriété d'Archimède]]), un tel $n$ existe ; $x = 1 + \frac{1}{n} \in A$ et $x < m$. Donc $\inf A = 1$, et comme $1 \notin A$, $A$ n'a pas de minimum.

**Méthode 2 (par l'absurde)** : 1 est un minorant, donc $1 \le \inf A$. Si $1 < \inf A$, posons $n = E\left(\frac{1}{\inf A - 1}\right) + 1$ ([[Partie entière]]). Alors $\frac{1}{\inf A - 1} < n$, d'où $\inf A > 1 + \frac{1}{n}$, alors que $1 + \frac{1}{n} \in A$ : contradiction.

**Méthode 3 (par la limite)** : $a_n = 1 + \frac{1}{n} \in A$, donc $a_n \ge \inf A$ ; par passage à la limite (la limite préserve les inégalités larges), $1 \ge \inf A$. Avec $1 \le \inf A$ : $\inf A = 1$.

### Ensemble $B$

$0 < \frac{1}{p} \le 1$ et $-1 \le -\frac{1}{q} < 0$, donc $-1 < \frac{1}{p} - \frac{1}{q} < 1$ : $B$ est majoré par 1 et minoré par $-1$.

- $\inf B = -1$ : avec $q = 1$, $\frac{1}{p} - 1 \in B$, donc $\frac{1}{p} - 1 \ge \inf B$ ; à la limite $-1 \ge \inf B$. Comme $-1 \le \inf B$, $\inf B = -1$ ; $-1 \notin B$ : pas de minimum.
- $\sup B = 1$ : avec $p = 1$, $1 - \frac{1}{q} \in B$, donc $1 - \frac{1}{q} \le \sup B$ ; à la limite $1 \le \sup B$. Comme $1 \ge \sup B$, $\sup B = 1$ ; $1 \notin B$ : pas de maximum.

## Exercice 8 : $\dfrac{mn}{(m+n)^2}$

**Énoncé** : (1) montrer que $\forall n, m \in \mathbb{N}^*$, $0 < \dfrac{mn}{(m+n)^2} \le \dfrac{1}{4}$. (2) En déduire que $A = \left\{\dfrac{mn}{(m+n)^2} : n, m \in \mathbb{N}^*\right\}$ a une borne supérieure et une borne inférieure, et les déterminer.

**Encadrement** : $mn > 0$ et $(m+n)^2 > 0$ donnent l'inégalité de gauche. À droite :
$$\frac{1}{4} - \frac{mn}{(m+n)^2} = \frac{(m+n)^2 - 4mn}{4(m+n)^2} = \frac{m^2 - 2mn + n^2}{4(m+n)^2} = \frac{(m-n)^2}{4(m+n)^2} \ge 0.$$
$A$ est non vide, minoré par 0, majoré par $\frac14$ : $\inf A$ et $\sup A$ existent.

**Borne supérieure** : pour $m = n = 1$, $\frac{1 \cdot 1}{(1+1)^2} = \frac{1}{4} \in A$, donc $\max A = \sup A = \frac{1}{4}$.

**Borne inférieure** : 0 est un minorant ; montrons $\forall a > 0,\ \exists x \in A,\ x < a$.

- *Méthode 1* : on impose $m = 1$ et on cherche $n$ tel que $\frac{n}{(1+n)^2} < a \iff \frac{(n+1)^2}{n} > \frac{1}{a} \iff n + 2 + \frac{1}{n} > \frac{1}{a}$ (5). Comme $n + 2 + \frac1n > n + 2$, il suffit que $\frac{1}{a} - 2 < n$, ce qui existe car $\mathbb{N}$ n'est pas majoré. Donc $\inf A = 0$.
- *Méthode 2 (absurde)* : si $0 < \inf A$, soit $n = E\left(\frac{1}{\inf A}\right) + 1$ ; alors $\inf A > \frac{1}{n} = \frac{n}{n^2} > \frac{n}{(n+1)^2} \in A$ : contradiction.
- *Méthode 3 (limite)* : $a_n = \frac{n}{(n+1)^2} \in A$ (avec $m = 1$), $a_n \ge \inf A$, et à la limite $0 \ge \inf A$ ; donc $\inf A = 0$.

## Exercice 9 : $\sup A \le \inf B$

**Énoncé** : $A$ et $B$ non vides, avec $x \le y$ pour tout $x \in A$, $y \in B$. Montrer que $\sup A$ et $\inf B$ existent et que $\sup A \le \inf B$.

**Corrigé** :

- tout élément de $B$ majore $A$ (non vide) : $\sup A$ existe ; tout élément de $A$ minore $B$ : $\inf B$ existe ;
- $\sup A$ étant le plus petit des majorants de $A$, $\sup A \le y$ pour tout $y \in B$ ;
- donc $\sup A$ minore $B$, et comme $\inf B$ est le plus grand des minorants, $\sup A \le \inf B$.

## Exercice 10 : $-A$ et $A + B$

**Énoncé** : (1) $A$ non vide borné, $-A = \{-x : x \in A\}$ : montrer que $-A$ est borné et $\sup(-A) = -\inf A$. (2) $A, B$ non vides bornés, $A + B = \{x + y : x \in A, y \in B\}$ : montrer que $A + B$ est borné et que $\sup(A+B) = \sup A + \sup B$, $\inf(A+B) = \inf A + \inf B$.

### $\sup(-A) = -\inf A$

- $-A$ non vide ($a \in A \Rightarrow -a \in -A$) ; si $m \le x \le M$ sur $A$, alors $-M \le -x \le -m$ : $-A$ est borné.
- Pour tout $x \in A$, $\inf A \le x \Rightarrow -x \le -\inf A$ : $-\inf A$ majore $-A$, donc $\sup(-A) \le -\inf A$.
- Pour tout $y \in -A$, $y \le \sup(-A) \Rightarrow -\sup(-A) \le -y$ : $-\sup(-A)$ minore $A$, donc $-\sup(-A) \le \inf A$, soit $\sup(-A) \ge -\inf A$.
- Par double inégalité : $\sup(-A) = -\inf A$.

### $\sup(A + B) = \sup A + \sup B$

- $A + B$ non vide ; $m_1 + m_2 \le a + b \le M_1 + M_2$ : borné, donc sup et inf existent.
- $a \le \sup A$ et $b \le \sup B$ donnent $a + b \le \sup A + \sup B$ : $\sup(A+B) \le \sup A + \sup B$.
- On fixe $b \in B$ : pour tout $a \in A$, $a + b \le \sup(A+B)$, donc $a \le \sup(A+B) - b$ ; d'où $\sup A \le \sup(A+B) - b$.
- Vrai pour tout $b$ : $b \le \sup(A+B) - \sup A$, donc $\sup B \le \sup(A+B) - \sup A$, soit $\sup A + \sup B \le \sup(A+B)$.

### $\inf(A + B) = \inf A + \inf B$

Même démarche : $\inf A + \inf B \le a + b$ donne $\inf A + \inf B \le \inf(A+B)$ ; à $b$ fixé, $\inf(A+B) - b \le a$ pour tout $a$, donc $\inf(A+B) - b \le \inf A$, puis $\inf(A+B) - \inf A \le b$ pour tout $b$, donc $\inf(A+B) \le \inf A + \inf B$.

## Exercice 11 : inclusion, réunion, intersection

**Énoncé** : $A$, $B$ bornés. Montrer : (1) $A \subset B \Rightarrow \sup A \le \sup B$ ; (2) $A \subset B \Rightarrow \inf B \le \inf A$ ; (3) $\sup(A \cup B) = \max(\sup A, \sup B)$ ; (4) $\inf(A \cap B) \ge \max(\inf A, \inf B)$.

**Corrigé** :

1. Tout $x \in A$ est dans $B$, donc $x \le \sup B$ : $\sup B$ majore $A$, d'où $\sup A \le \sup B$.
2. De même $\inf B \le x$ pour tout $x \in A$ : $\inf B$ minore $A$, d'où $\inf B \le \inf A$.
3. $A, B \subset A \cup B$ et la question 1 donnent $\max(\sup A, \sup B) \le \sup(A \cup B)$. Réciproquement, si $x \in A$, $x \le \sup A \le \max(\dots)$ ; si $x \in B$, $x \le \sup B \le \max(\dots)$ : le max majore $A \cup B$, d'où l'égalité par double inégalité.
4. $A \cap B \subset A$ et $A \cap B \subset B$ ; la question 2 donne $\inf A \le \inf(A \cap B)$ et $\inf B \le \inf(A \cap B)$.

## Exercice 12 (à faire chez soi) : $\{1/n\}$

$B = \{1/n : n \in \mathbb{N}^*\}$. Pour tout $n$, $1 \le n \Rightarrow 0 < \frac{1}{n} \le 1$ : $B$ est majoré par 1, minoré par 0.

- $1 = \frac{1}{1} \in B$, donc $\max B = \sup B = 1$.
- $\frac{1}{n} \ge \inf B$, et à la limite $0 \ge \inf B$ ; avec $0 \le \inf B$ : $\inf B = 0$. Comme $0 \notin B$, pas de plus petit élément.

## Exercice 13 (à faire chez soi) : $\sup\{|x - y|\}$

**Énoncé** : $A$ non vide borné, $B = \{|x - y| : (x, y) \in A^2\}$. (1) $B$ est majoré. (2) $\sup B = \sup A - \inf A$.

**Corrigé** :

- $|a - a| = 0 \in B$ : $B$ non vide. Pour $x, y \in A$ : $\inf A \le x \le \sup A$ et $-\sup A \le -y \le -\inf A$, donc $\inf A - \sup A \le x - y \le \sup A - \inf A$, soit $|x - y| \le \sup A - \inf A$ ([[Valeur absolue]]). Donc $\sup B \le \sup A - \inf A$.
- À $y \in A$ fixé : $|x - y| \le \sup B \Rightarrow x \le \sup B + y$ pour tout $x$, donc $\sup A \le \sup B + y$, soit $\sup A - \sup B \le y$ pour tout $y \in A$. Donc $\sup A - \sup B \le \inf A$, c'est-à-dire $\sup A - \inf A \le \sup B$.
- Double inégalité : $\sup B = \sup A - \inf A$.

## Exercice 14 (à faire chez soi) : produit $A \cdot B$

**Énoncé** : $A \cdot B = \{xy : x \in A, y \in B\}$. A-t-on toujours $\sup(A \cdot B) = \sup A \cdot \sup B$ ? Quelle hypothèse ajouter ?

**Contre-exemple** : $A = [-3, -1]$, $B = [1, 4]$. $\sup A \cdot \sup B = (-1) \cdot 4 = -4$. Or $1 \le -x \le 3$ et $1 \le y \le 4$, donc (encadrements positifs) $1 \le -xy \le 12$, soit $A \cdot B = [-12, -1]$ et $\sup(A \cdot B) = -1 \ne -4$.

**Hypothèse suffisante** : $A$ et $B$ parties majorées non vides de $\mathbb{R}_+$.

- $A \cdot B$ est non vide et majoré ($0 \le a \le M_1$, $0 \le b \le M_2 \Rightarrow ab \le M_1M_2$).
- $ab \le \sup A \cdot \sup B$ : donc $\sup(A \cdot B) \le \sup A \cdot \sup B$.
- Inégalité inverse, par cas : si $b = 0$, $\sup A \cdot b = 0 \le \sup(A \cdot B)$ ; si $b > 0$, $a \le \frac{\sup(A \cdot B)}{b}$ pour tout $a$, donc $\sup A \cdot b \le \sup(A \cdot B)$. Puis : si $\sup A = 0$, c'est immédiat ; si $\sup A > 0$, $b \le \frac{\sup(A \cdot B)}{\sup A}$ pour tout $b$, donc $\sup A \cdot \sup B \le \sup(A \cdot B)$.
- Conclusion : $\sup(A \cdot B) = \sup A \cdot \sup B$.

## Exercice 15 (à faire chez soi) : réunion et intersection (bis)

1. $\inf(A \cup B) = \min(\inf A, \inf B)$ : par l'exercice 11, question 2, $\inf(A \cup B) \le \inf A$ et $\le \inf B$ ; réciproquement, tout $x \in A \cup B$ vérifie $\min(\inf A, \inf B) \le x$, donc le min minore $A \cup B$. Double inégalité.
2. $\sup(A \cap B) \le \min(\sup A, \sup B)$ : par l'exercice 11, question 1, $\sup(A \cap B) \le \sup A$ et $\le \sup B$.

## Exercice 16 : la partie entière est croissante

**Définition** : pour $x \in \mathbb{R}$, $E(x) := \max\{n \in \mathbb{Z} : n \le x\}$ ([[Partie entière]]). D'où
$$x - 1 < E(x) \le x < E(x) + 1.$$

**Corrigé** : soient $x \le y$. $E(x) \le x \le y$, donc $E(x)$ est un entier inférieur ou égal à $y$ ; comme $E(y)$ est le plus grand de ces entiers, $E(x) \le E(y)$ ([[Application monotone]]).

$E$ n'est pas strictement croissante : $x = 1{,}5 < y = 1{,}9$ mais $E(x) = E(y) = 1$.

## Exercice 17 : propriétés de la partie entière

### $E(x) + E(y) \le E(x+y) \le E(x) + E(y) + 1$

- $E(x) + E(y) \le x + y$ ; par croissance, $E(E(x) + E(y)) \le E(x+y)$, et comme $E(x) + E(y) \in \mathbb{Z}$, $E(E(x) + E(y)) = E(x) + E(y)$.
- $E(x+y) \le x + y < E(x) + 1 + E(y) + 1$ ; l'inégalité est stricte entre entiers, donc $E(x+y) \le E(x) + E(y) + 1$.

### $E(x) + E(-x)$

- Si $x \in \mathbb{Z}$ : $E(x) = x$, $E(-x) = -x$, somme nulle.
- Sinon $E(x) < x < E(x) + 1$, donc $-E(x) - 1 < -x < -E(x)$, et $E(-x) = -E(x) - 1$.

$$E(x) + E(-x) = \begin{cases} 0 & \text{si } x \in \mathbb{Z} \\ -1 & \text{sinon} \end{cases}$$

### $E(x) = E\left(\dfrac{E(nx)}{n}\right)$ pour $n \in \mathbb{N}^*$

$E(x) \le x < E(x) + 1$ ; en multipliant par $n$, $nE(x) \le nx < nE(x) + n$. Par croissance de $E$ : $nE(x) = E(nE(x)) \le E(nx) < nE(x) + n$. En divisant par $n$ : $E(x) \le \frac{E(nx)}{n} < E(x) + 1$. Donc $E(x)$ est le plus grand entier inférieur ou égal à $\frac{E(nx)}{n}$.

## Exercice 18 (à faire chez soi) : dénombrer des entiers

**Énoncé** : $n \in \mathbb{N}$, $x \ge 0$ réel. Combien d'entiers naturels (1) entre 1 et $n$, entre 1 et $x$ ; (2) entre 0 et $n$, entre 0 et $x$ ; (3) pairs, impairs entre 0 et $x$ ; (4) multiples de 3 entre 0 et $x$ ? (5) Combien de couples $(x, y) \in \mathbb{N}^2$ solutions de $x + 2y = n$ ? (6) De combien de façons payer 10 euros avec des pièces de 10 et 20 centimes ?

**Corrigé** ([[Dénombrement]]) :

| Question | Raisonnement | Réponse |
|---|---|---|
| 1 | $1 \le k \le x \iff 1 \le k \le E(x)$ | $n$ ; $E(x)$ |
| 2 | | $n + 1$ ; $E(x) + 1$ |
| 3 | $0 \le 2k \le x \iff 0 \le k \le \frac{x}{2}$ ; $0 \le 2k + 1 \le x \iff 0 \le k \le \frac{x-1}{2}$ | pairs : $E\left(\frac{x}{2}\right) + 1$ ; impairs : $E\left(\frac{x-1}{2}\right) + 1$ |
| 4 | $0 \le 3k \le x \iff 0 \le k \le \frac{x}{3}$ | $E\left(\frac{x}{3}\right) + 1$ |
| 5 | $x = n - 2y \in \mathbb{N} \iff 0 \le 2y \le n$ | $E\left(\frac{n}{2}\right) + 1$ couples |
| 6 | $10x + 20y = 1000 \iff x + 2y = 100$ | $E\left(\frac{100}{2}\right) + 1 = 51$ façons |

## Exercice 19 (à faire chez soi) : équations avec partie entière

1. $(5E(x) + 2)(3E(x) + 6) = 0 \iff E(x) = -\frac{2}{5}$ ou $E(x) = -\frac{6}{3} = -2$. $E(x)$ est entier, donc $E(x) = -\frac25$ est impossible. Donc $E(x) = -2 \iff x \in [-2, -1[$.
2. $(2E(x) + 1)^2 < 4 \iff |2E(x) + 1| < 2 \iff -\frac{3}{2} < E(x) < \frac{1}{2} \iff -1 \le E(x) \le 0$. Le corrigé conclut « $\iff -1 < x < 1$ », $S_2 = \,]-1; 1[$ (voir les points à vérifier : l'ensemble correct est $[-1, 1[$).

## Exercice 20 (pour aller plus loin) : formule d'Hermite

**Énoncé** : montrer que pour $n \in \mathbb{N}^*$, $x \in \mathbb{R}$ ([[Identité d'Hermite]]) :
$$\sum_{k=0}^{n-1} E\left(x + \frac{k}{n}\right) = E(nx).$$
On pose $f(x) = \sum_{k=0}^{n-1} E\left(x + \frac{k}{n}\right) - E(nx)$. (1) $f$ est périodique de période $\frac1n$. (2) Calculer $f$ sur $\left[0, \frac1n\right[$. (3) Conclure.

**Corrigé** :

1. $f\left(x + \frac1n\right) = \sum_{k=0}^{n-1} E\left(x + \frac{k+1}{n}\right) - E(nx + 1)$. Or $E(nx) + 1 \le nx + 1 < E(nx) + 2$, donc $E(nx + 1) = E(nx) + 1$. Avec le [[Changement d'indice|changement d'indice]] $l = k + 1$ :
$$f\left(x + \tfrac1n\right) = \sum_{l=1}^{n} E\left(x + \tfrac{l}{n}\right) - E(nx) - 1 = E(x + 1) + \sum_{l=1}^{n-1} E\left(x + \tfrac{l}{n}\right) - E(nx) - 1$$
$$= E(x) + \sum_{l=1}^{n-1} E\left(x + \tfrac{l}{n}\right) - E(nx) = \sum_{l=0}^{n-1} E\left(x + \tfrac{l}{n}\right) - E(nx) = f(x).$$
$f$ est donc [[Fonction périodique|périodique]] de période $\frac1n$.
2. Si $0 \le x < \frac1n$ et $0 \le k \le n - 1$ : $0 \le nx < 1$ et $0 \le x + \frac{k}{n} < \frac1n + 1 - \frac1n = 1$, donc $E(nx) = 0$ et $E\left(x + \frac{k}{n}\right) = 0$ : $f(x) = 0$.
3. Par périodicité, $f = 0$ sur $\mathbb{R}$, d'où la formule.

## Inégalité de Cauchy-Schwarz (pour aller plus loin)

**Énoncé** : pour $n \in \mathbb{N}^*$ et $a_1, \dots, a_n, b_1, \dots, b_n \in \mathbb{R}$ ([[Inégalité de Cauchy-Schwarz]]) :
$$\sum_{k=1}^{n} a_kb_k \le \sqrt{\sum_{k=1}^{n} a_k^2}\ \sqrt{\sum_{k=1}^{n} b_k^2}.$$
Indication : considérer $f(x) = \sum_{k=1}^{n}(a_k + b_kx)^2$.

**Corrigé** : on développe
$$f(x) = \underbrace{\sum a_k^2}_{c} + \underbrace{2\sum a_kb_k}_{b}\,x + \underbrace{\sum b_k^2}_{a}\,x^2,$$
de discriminant $\Delta = b^2 - 4ac = 4\left(\sum a_kb_k\right)^2 - 4\left(\sum a_k^2\right)\left(\sum b_k^2\right)$. Or $f(x) \ge 0$ pour tout $x$ : ce trinôme du second degré de signe constant a un discriminant $\Delta \le 0$ ([[Équation du second degré]]). D'où $\left(\sum a_kb_k\right)^2 \le \left(\sum a_k^2\right)\left(\sum b_k^2\right)$, puis l'inégalité en prenant la racine carrée.

## Exercice 22 (pour aller plus loin) : moyennes et inégalité de Bernoulli

### Inégalité arithmético-géométrique

**Énoncé** : $0 < x \le y$, $A = \frac{x+y}{2}$ (moyenne arithmétique), $G = \sqrt{xy}$ (géométrique), $H = \dfrac{1}{\frac12\left(\frac1x + \frac1y\right)}$ (harmonique). Montrer ([[Inégalité arithmético-géométrique]]) :
$$x \le H \le G \le A \le y.$$

**Corrigé** :

- $A \le y$ : $y = \frac{y}{2} + \frac{y}{2} \ge \frac{x}{2} + \frac{y}{2} = A$.
- $G \le A$ : $A - G = \frac{x}{2} - \sqrt{xy} + \frac{y}{2} = \frac12\left((\sqrt{x})^2 - 2\sqrt{xy} + (\sqrt{y})^2\right) = \frac12(\sqrt{x} - \sqrt{y})^2 \ge 0$.
- $H \le G$ : on applique $G \le A$ à $\frac1x$ et $\frac1y$ : $\frac{1}{\sqrt{xy}} = \sqrt{\frac1x \cdot \frac1y} \le \frac12\left(\frac1x + \frac1y\right)$, d'où $H \le \sqrt{xy} = G$.
- $x \le H$ : comme $0 < x \le y$, $\frac1y \le \frac12\left(\frac1x + \frac1y\right) \le \frac1x$ ; en passant à l'inverse, $x \le H \le y$.

### Inégalité de Bernoulli

**Énoncé** : $a \ge 0$, $n \in \mathbb{N}$, $P(n) : (1 + a)^n \ge 1 + na$ ([[Inégalité de Bernoulli]]).

**Corrigé** ([[Récurrence]] sur $n$, $a$ fixé) :

- *Initialisation* : $(1 + a)^1 = 1 + a \ge 1$ ; $P(1)$ est vraie, $P(0)$ aussi.
- *Hérédité* : si $(1 + a)^n \ge 1 + na$, alors
$$(1 + a)^{n+1} = (1 + a)^n(1 + a) \ge (1 + na)(1 + a) = 1 + (n+1)a + na^2 \ge 1 + (n+1)a,$$
car $na^2 \ge 0$.
- Conclusion : pour tout $a \ge 0$ et tout $n \in \mathbb{N}$, $(1 + a)^n \ge 1 + na$.

## Exercice 23 (pour aller plus loin) : nombre de chiffres

**Énoncé** : tout entier $n \ge 1$ s'écrit de manière unique $n = a_0 + 10a_1 + \dots + 10^pa_p$, avec $a_i \in \{0, \dots, 9\}$ et $a_p \ne 0$. Déterminer $p$ en fonction de $n$.

**Corrigé** : $n = 10^p\left(a_010^{-p} + a_110^{-p+1} + \dots + a_p\right)$, donc
$$\log_{10}(n) = p + \log_{10}\left(a_010^{-p} + a_110^{-p+1} + \dots + a_p\right).$$
La parenthèse est $< 10$ (et $\ge 1$ car $a_p \ge 1$), donc son logarithme est dans $[0, 1[$ par croissance du logarithme. D'où
$$p = E(\log_{10} n),$$
et $n$ a $p + 1$ chiffres.

## Points à vérifier

- **Exercice 19, question 2** : le corrigé écrit $-1 \le E(x) \le 0 \iff -1 < x < 1$ et conclut $S_2 = ]-1;1[$. L'ensemble correct est $[-1, 1[$ : $E(x) = -1$ correspond à $x \in [-1, 0[$, et $x = -1$ est bien solution. La même erreur figure dans le corrigé du DS1 de 2021 : voir [[DS1-correction-2021 (résumé)]].
- **Exercice 3** : le corrigé conclut « contradiction » à $2^p = 3^q$ sans la justifier. Il faut dire que $p$ et $q$ sont des entiers strictement positifs (car $\ln 3/\ln 2 > 0$) et que $2^p$ est pair alors que $3^q$ est impair (complément).
- **Exercice 7, méthode 1** : le corrigé écrit « L'entier $m$ ne peut donc pas être un minorant de $B$ » ; il s'agit du réel $m$ et de l'ensemble $A$.
- **Exercice 13** : le corrigé écrit « $A$ est minoré par $\sup(A+B) - \sup(A)$ » ; il faut lire $\sup(A) - \sup(B)$, comme la ligne précédente (coquille recopiée de l'exercice 10).
- **Exercice 17, $E(-x)$** : « $-E(x) - 1$ est le plus grand entier relatif inférieur ou égal à $E(-x)$ » ; il faut lire « inférieur ou égal à $-x$ ».
- **Exercice 23** : le corrigé n'écrit que la majoration de la parenthèse par 10 ; il faut aussi qu'elle soit $\ge 1$ (car $a_p \ge 1$) pour que son logarithme soit positif et que la partie entière vaille $p$ (complément).
- **Numérotation** : les diapositives numérotent 22 à la fois l'inégalité arithmético-géométrique et celle de Bernoulli, et ne numérotent pas Cauchy-Schwarz (exercice 21 implicite). Le résumé précédent de ce fichier regroupait autrement les exercices 11 à 15.
- **Exercice 4, question 2** : la preuve de $\sqrt{2} \notin \mathbb{Q}$ n'apparaît pas dans les diapositives.

## Liens

[[Borne supérieure]], [[Relation d'ordre]], [[Récurrence]], [[Produit scalaire]], [[Dénombrement]].
