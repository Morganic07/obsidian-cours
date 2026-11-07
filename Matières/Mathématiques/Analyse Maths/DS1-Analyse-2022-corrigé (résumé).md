---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de DS1-Analyse-2022-corrigé ([[Raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé.pdf]]) (7 pages, texte), dans [[Analyse Maths (matière)]]. Devoir surveillé n° 1 d'Analyse I (PréING1), jeudi 10 novembre 2022, 1 h 30, sans appareil électronique, 6 exercices à traiter dans l'ordre voulu ; la qualité de la rédaction et la précision des justifications comptent. Le barème est sur 24 points. Il porte sur [[Chap0-Rappels-etc (résumé)]] et [[Chap1-reels (résumé)]]. Voir aussi [[DS1-correction-2021 (résumé)]] pour la version précédente, de même forme.

Le document ne contient aucune figure (seulement le logo de l'école).

## Exercice 1 — Équations trigonométriques (4 points)

Résoudre dans $\mathbb{R}$ (voir [[Équation trigonométrique]]) :

### 1. $\tan x = 2\sin x$ (2 points)

**Ensemble de définition** (celui de la tangente, voir [[Ensemble de définition]]) :
$$D = \mathbb{R} \setminus \left\{ \frac{\pi}{2} + k\pi,\ k \in \mathbb{Z} \right\}.$$

Pour $x \in D$ :
$$\tan x = 2\sin x \iff \frac{\sin x}{\cos x} = 2\sin x \iff \sin x = 2\sin x\cos x \iff \sin x = \sin(2x)$$
$$\iff 2x = x + 2k\pi \ \text{ou}\ 2x = \pi - x + 2k\pi,\ k\in\mathbb{Z} \iff x = 2k\pi \ \text{ou}\ x = \frac{\pi}{3} + \frac{2k\pi}{3}.$$

**Solution** : $\left\{ 2k\pi,\ \dfrac{\pi}{3} + \dfrac{2k\pi}{3},\ k \in \mathbb{Z} \right\}$.

Outils : $\sin(2x) = 2\sin x\cos x$ et $\sin a = \sin b \iff a = b + 2k\pi$ ou $a = \pi - b + 2k\pi$ (voir [[Formules trigonométriques]]).

### 2. $\cos x + \sin x = 1 + \tan x$ (2 points)

Même ensemble de définition $D$. Pour $x \in D$ :
$$\cos x + \sin x = 1 + \frac{\sin x}{\cos x} \iff \cos x + \sin x = \frac{\cos x + \sin x}{\cos x}$$
$$\iff \cos^2 x - \cos x + \cos x \sin x - \sin x = 0 \iff \cos x(\cos x - 1) + \sin x(\cos x - 1) = 0$$
$$\iff (\cos x - 1)(\cos x + \sin x) = 0 \iff \cos x = 1 \ \text{ou}\ \cos x = -\sin x = \cos\left(x + \frac{\pi}{2}\right)$$
$$\iff x = 2k\pi \ \text{ou}\ x = -x - \frac{\pi}{2} + 2k\pi \iff x = 2k\pi \ \text{ou}\ x = -\frac{\pi}{4} + k\pi.$$

**Solution** : $\left\{ 2k\pi,\ -\dfrac{\pi}{4} + k\pi,\ k \in \mathbb{Z} \right\}$.

Méthode : mettre au même dénominateur, puis **factoriser** par $(\cos x - 1)$ plutôt que développer. Pour $\cos a = \cos b$ : $a = b + 2k\pi$ ou $a = -b + 2k\pi$ ; seule la seconde branche donne ici des solutions.

## Exercice 2 — Partie entière (4 points)

$E(x)$ désigne la [[Partie entière]] de $x$ : le plus grand entier inférieur ou égal à $x$, caractérisé par $E(x) \le x < E(x) + 1$.

### 1. Deux égalités à démontrer

**(a)** (1 point)
$$E(-x) = \begin{cases} -E(x) & \text{si } x \in \mathbb{Z},\\ -E(x) - 1 & \text{si } x \in \mathbb{R}\setminus\mathbb{Z}.\end{cases}$$

Preuve :
- si $x \in \mathbb{Z}$ : $E(x) = x$ et $E(-x) = -x$ ;
- si $x \notin \mathbb{Z}$ : $E(x) < x < E(x) + 1$ (inégalités strictes), donc $-E(x) - 1 < -x < -E(x)$, d'où $E(-x) = -E(x) - 1$.

**(b)** (1,5 point)
$$E(2x) = \begin{cases} 2E(x) & \text{si } x - E(x) < \frac12,\\ 2E(x) + 1 & \text{si } x - E(x) \ge \frac12.\end{cases}$$

Preuve : pour tout $x$, $E(x) \le x < E(x) + 1 \Rightarrow 0 \le x - E(x) < 1$. Deux cas :
- si $0 \le x - E(x) < \frac12$ : $E(x) \le x < E(x) + \frac12 \Rightarrow 2E(x) \le 2x < 2E(x) + 1$, donc $E(2x) = 2E(x)$ ;
- si $\frac12 \le x - E(x) < 1$ : $E(x) + \frac12 \le x < E(x) + 1 \Rightarrow 2E(x) + 1 \le 2x < (2E(x)+1) + 1$, donc $E(2x) = 2E(x) + 1$.

Dans les deux cas, on conclut parce que $E(2x)$ est le plus grand entier inférieur ou égal à $2x$.

### 2. Résoudre $E(2x) = 5 + E(-x)$ (1,5 point)

Trois cas (voir [[Raisonnement par disjonction des cas]]) :
- **$x \in \mathbb{Z}$** : $E(2x) = 2x$, $E(-x) = -x$, donc $2x = 5 - x$, $x = 5/3$ : pas un entier, **pas de solution**.
- **$0 < x - E(x) < \frac12$** : $E(2x) = 2E(x)$ et $E(-x) = -E(x) - 1$, donc $2E(x) = 4 - E(x)$, $E(x) = 4/3$ : pas un entier, **pas de solution**.
- **$\frac12 \le x - E(x) < 1$** : $E(2x) = 2E(x) + 1$ et $E(-x) = -E(x) - 1$, donc $2E(x) + 1 = 4 - E(x)$, $E(x) = 1$, soit $x \in [1, 2[$ ; avec la condition $x - 1 \ge \frac12$, on obtient $x \in \left[\frac32, 2\right[$.

**Solution** : $\left[\dfrac32, 2\right[$.

Méthode : traiter $E(x)$ comme une **inconnue entière** ; une valeur non entière élimine le cas.

## Exercice 3 — Inéquations (4 points)

Voir [[Valeur absolue]] et [[Règles de calcul sur les inégalités]].

### 1. $|x - 1| \le |2x + 1| + 1$ (2 points)

On utilise $|a| \le b \iff -b \le a \le b$ :
$$|x-1| \le |2x+1| + 1 \iff -|2x+1| - 1 \le x - 1 \le |2x+1| + 1.$$

- **Cas $2x + 1 \ge 0$** (soit $x \ge -\frac12$) : $-2x - 2 \le x - 1 \le 2x + 2 \iff -\frac13 \le x$ et $-3 \le x$. Solutions dans $\left[-\frac12, +\infty\right[$ : $\left[-\frac13, +\infty\right[$.
- **Cas $2x + 1 < 0$** (soit $x < -\frac12$) : $2x \le x - 1 \le -2x \iff x \le -1$ et $x \le \frac13$. Solutions dans $\left]-\infty, -\frac12\right[$ : $]-\infty, -1]$.

**Solution** : $]-\infty, -1] \cup \left[-\dfrac13, +\infty\right[$.

### 2. $\sqrt{|x + 2|} \le |x - 4|$ (2 points)

Les deux membres sont positifs, on peut élever au carré :
$$\sqrt{|x+2|} \le |x-4| \iff |x+2| \le (x-4)^2 = x^2 - 8x + 16$$
$$\iff -x^2 + 8x - 16 \le x + 2 \le x^2 - 8x + 16 \iff -x^2 + 7x - 18 \le 0 \ \text{et}\ 0 \le x^2 - 9x + 14 = (x-2)(x-7).$$

Le trinôme $-x^2 + 7x - 18$ n'a pas de racine réelle (discriminant $49 - 72 < 0$) et il est donc toujours $\le 0$ : la première condition est toujours vraie (voir [[Équation du second degré]]).

**Solution** : $]-\infty, 2] \cup [7, +\infty[$.

## Exercice 4 — Sommes et produits (4 points)

Voir [[Symboles somme et produit]].

### 1. $\displaystyle\sum_{k=1}^n \left(\frac1k - \frac{1}{n+1-k}\right)$ (1,5 point)

On sépare en deux sommes et on fait le [[Changement d'indice]] $j = n + 1 - k$ dans la seconde : $1 \le k \le n \Rightarrow n \ge n + 1 - k \ge 1$, donc $n \ge j \ge 1$ et
$$\sum_{k=1}^n \frac{1}{n+1-k} = \sum_{j=1}^n \frac1j.$$

**Résultat** : $\displaystyle\sum_{k=1}^n \frac1k - \sum_{j=1}^n \frac1j = 0$.

### 2. $\displaystyle\sum_{k=0}^n \frac{(-1)^k}{2^{2k+1}} \binom nk$ (1 point)

$$\sum_{k=0}^n \frac{(-1)^k}{2^{2k+1}}\binom nk = \frac12 \sum_{k=0}^n \binom nk \frac{(-1)^k}{2^{2k}} = \frac12 \sum_{k=0}^n \binom nk \left(\frac{-1}{4}\right)^k = \frac12 \sum_{k=0}^n \binom nk 1^{n-k}\left(-\frac14\right)^k = \frac12\left(1 - \frac14\right)^n = \frac{3^n}{2^{2n+1}}.$$

Outil : [[Formule du binôme de Newton]] $(a+b)^n = \sum_{k=0}^n \binom nk a^{n-k} b^k$ avec $a = 1$, $b = -\frac14$ (voir [[Coefficient binomial]]).

### 3. Simplifier $\displaystyle\prod_{k=2}^n \left(1 - \frac{1}{k^2}\right)$ (1,5 point)

$$\prod_{k=2}^n \left(1 - \frac1{k^2}\right) = \prod_{k=2}^n \frac{k^2 - 1}{k^2} = \prod_{k=2}^n \frac{(k-1)(k+1)}{k\cdot k} = \prod_{k=2}^n \frac{k-1}{k} \cdot \prod_{k=2}^n \frac{k+1}{k} = \frac1n \cdot \frac{n+1}{2} = \frac{n+1}{2n}.$$

Méthode : factoriser $k^2 - 1$, séparer en deux produits **télescopiques** (voir [[Somme télescopique]]) : $\prod \frac{k-1}{k} = \frac{1}{n}$ et $\prod \frac{k+1}{k} = \frac{n+1}{2}$.

## Exercice 5 — Bornes de deux ensembles (6 points)

$$A = \left\{ x \in \mathbb{R}\setminus\{1\} : \frac{2}{x-1} \le 2x - 5 < 11 \right\}, \qquad B = \left\{ \frac{(-1)^n}{n} + \frac2n : n \in \mathbb{N}^* \right\}.$$

Voir [[Majorant et minorant]], [[Borne supérieure]], [[Plus grand élément]].

### 1. Majorés, minorés ? (1,5 point par ensemble)

**Ensemble $A$** :
$$x \in A \iff 0 \le \frac{(2x-5)(x-1) - 2}{x-1} \ \text{et}\ x < 8 \iff 0 \le \frac{2x^2 - 7x + 3}{x-1} \ \text{et}\ x < 8 \iff 0 \le \frac{(2x-1)(x-3)}{x-1} \ \text{et}\ x < 8.$$

Un tableau de signe donne $x \in \left(\left[\frac12, 1\right[ \cup [3, +\infty[\right) \cap\ ]-\infty, 8[$, donc
$$A = \left[\frac12, 1\right[ \cup [3, 8[.$$

$A$ est majorée par tout réel $\ge 8$ et minorée par tout réel $\le \frac12$.

**Ensemble $B$** : on sépare selon la [[Parité d'un entier|parité]] de $n$ :
- $n$ pair : $(-1)^n = 1$, l'élément vaut $\frac3n$, donc $0 < \frac3n \le \frac32$ (plus grande valeur pour $n = 2$) ;
- $n$ impair : $(-1)^n = -1$, l'élément vaut $\frac1n$, donc $0 < \frac1n \le 1$.

Ainsi $\forall n \in \mathbb{N}^*,\ 0 < \frac{(-1)^n}{n} + \frac2n \le \frac32$ : $B$ est majorée par tout réel $\ge \frac32$ et minorée par tout réel $\le 0$.

### 2. Bornes, plus grand et plus petit élément (1,5 point par ensemble)

**$A$** : $\sup A = 8$ (non atteint : $A$ n'a pas de maximum) et $\min A = \inf A = \frac12$.

**$B$** :
- $\frac32 = \frac{(-1)^2}{2} + \frac22 \in B$ : $\frac32$ est un majorant qui appartient à $B$, donc $\max B = \sup B = \frac32$.
- Pour tout $n$, $\frac{(-1)^n}{n} + \frac2n \ge \inf B$ ; par passage à la limite, $0 = \lim_{n\to+\infty} \left(\frac{(-1)^n}{n} + \frac2n\right) \ge \inf B$. Comme $0$ est un minorant, $0 \le \inf B$. Donc $\inf B = 0$.
- $0 \notin B$ : $B$ n'a **pas de minimum**.

## Exercice 6 — Borne supérieure d'un translaté (3 points)

Soit $A$ une partie non vide et bornée de $\mathbb{R}$ et $x \in \mathbb{R}$. On pose $x + A = \{x + a : a \in A\}$. Montrer que $x + A$ est bornée (1 point) et que
$$\sup(x + A) = x + \sup(A) \quad (2\ \text{points}).$$

**Correction** :
- $A$ majorée et non vide : il existe $M$ tel que $a \le M$ pour tout $a \in A$, donc $a + x \le M + x$ : $A + x$ est majorée et admet une borne supérieure.
- Égalité par **double inégalité** (voir [[Borne supérieure]], plus petit des majorants) :
  - pour $a \in A$, $a \le \sup A \Rightarrow a + x \le \sup A + x$ : $\sup A + x$ majore $A + x$, donc $\sup(A + x) \le \sup A + x$ ;
  - pour $a \in A$, $a + x \le \sup(A + x) \Rightarrow a \le \sup(A + x) - x$ : $\sup(A+x) - x$ majore $A$, et $\sup A$ est le plus petit majorant, donc $\sup A \le \sup(A + x) - x$, soit $\sup A + x \le \sup(A + x)$.
- Conclusion : $\sup(A + x) = \sup(A) + x$.

## Pièges et points de méthode

- Toujours donner l'ensemble de définition avant de transformer une équation avec $\tan$ ou une fraction.
- Un $\sup$ qui n'appartient pas à l'ensemble n'est pas un maximum (cas de $A$ avec $8$ et de $B$ avec $0$).
- Pour un inf non atteint, la preuve classique est : un minorant évident (ici $0$), puis une suite d'éléments de l'ensemble qui tend vers lui. Voir [[Borne supérieure]].
- Avec une partie entière : poser $E(x)$ comme inconnue entière et découper selon la partie fractionnaire $x - E(x)$.
- Élever au carré une inégalité n'est légitime que si les deux membres sont positifs.

## Points à vérifier

Coquilles du corrigé, sans effet sur les résultats :
- Ex. 6 : l'énoncé écrit $x + A = \{x + a : x \in A\}$ au lieu de $a \in A$, et la dernière ligne écrit $\sup(A+B)$ au lieu de $\sup(A+x)$.
- Ex. 5 : la phrase « $A$ est majorée par tout réel supérieur ou égal à $8$ » est correcte, mais l'écriture de $A$ dans le texte extrait a perdu un crochet : l'ensemble est bien $[1/2, 1[ \cup [3, 8[$, ce qui est cohérent avec $\min A = 1/2$.
- Ex. 1.2 : dans le corrigé, la ligne $\cos^2 x - \cos x + \cos x\sin x - \sin x$ n'a pas de « $= 0$ » (rétabli ici).
- Ex. 1 : le corrigé ne vérifie pas que les solutions trouvées appartiennent à $D$ (c'est le cas : aucune n'est de la forme $\frac\pi2 + k\pi$).
- Ex. 6 : on demande de montrer que $x + A$ est **bornée**, mais le corrigé ne montre que la majoration ; la minoration se fait de la même façon ($m \le a \Rightarrow m + x \le a + x$). Le corrigé note aussi indifféremment $x + A$ et $A + x$.
- Ex. 5 (B) : le corrigé écrit « pour tout $n \in \mathbb{N}$ » au lieu de $\mathbb{N}^*$, et un « $\lim_{q\to+\infty}$ » isolé, sans effet.

## Liens

[[Relation d'ordre]], [[Borne supérieure]], [[Récurrence]], [[Dénombrement]] (binôme).
