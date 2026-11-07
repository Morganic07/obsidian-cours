---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp0 : Revision chapter.docx|Chp0 - Revision chapter]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Séries/Chp0 : Revision chapter.docx|Chp0 - Revision chapter]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Toutes les images de la note sont des énoncés (texte et formules) : leur contenu est recopié ci-dessous, aucune n'est une figure.

## Idée générale

Rappels sur les suites et les comparaisons asymptotiques, utiles pour toute la matière. Les notions de petit $o$, grand $O$ et équivalent sont aussi traitées dans [[Comparaison asymptotique]], et les développements usuels dans [[Développement limité]].

## Suites (*sequences*)

**Définition.** Une [[Suite numérique|suite de réels]] est une liste infinie de nombres écrits dans un ordre donné :
$$a_0, a_1, a_2, \ldots, a_n, \ldots$$
On peut la voir comme une fonction de $\mathbb{N}$ dans $\mathbb{R}$.

**Remarques.**
1. Une suite ne commence pas forcément à 0 : pour $a_n = \frac{1}{n}$, on a $n \ge 1$.
2. Une suite peut être définie par une formule : $a_n = \ln(n+1)$.
3. Une suite peut être définie par récurrence : $a_0$ donné et $\forall n \ge 1,\ a_n = \frac{a_{n-1}+1}{2}$.

## Convergence des suites

**Définition (convergence vers $\ell$).** $(a_n)$ converge vers $\ell \in \mathbb{R}$ si
$$\forall \epsilon > 0,\ \exists N \in \mathbb{N},\ \forall n \ge N,\ |a_n - \ell| < \epsilon.$$

**Définition (suite convergente).** $(a_n)$ converge si
$$\exists \ell \in \mathbb{R},\ \forall \epsilon > 0,\ \exists N \in \mathbb{N},\ \forall n \ge N,\ |a_n - \ell| < \epsilon.$$

**Définition (limites infinies).**
1. $(a_n)$ tend vers $+\infty$ si $\forall A \in \mathbb{R}^+,\ \exists N \in \mathbb{N},\ \forall n \ge N,\ a_n \ge A$.
2. $(a_n)$ tend vers $-\infty$ si $\forall B \in \mathbb{R}^+,\ \exists N \in \mathbb{N},\ \forall n \ge N,\ a_n \le -B$.

**Exercice.** Étudier les suites $a_n = \frac{n^2}{\sqrt{n^3+4n}}$ pour $n \ge 1$, et $a_n = -n^2 + 2n - 4$ pour $n \ge 0$. Le cours ne donne pas la correction.

**Définition (convergente / divergente).** La suite est **convergente** s'il existe $\ell \in \mathbb{R}$ tel qu'elle converge vers $\ell$. Sinon elle est **divergente** : elle tend vers $+\infty$, ou vers $-\infty$, ou n'admet pas de limite $\ell \in \mathbb{R}$. Voir [[Convergence d'une suite]].

## Suite géométrique

**Définition.** Une [[Suite géométrique]] est une suite de nombres non nuls où chaque terme, après le premier, s'obtient en multipliant le précédent par un nombre fixe non nul, la raison (*common ratio*). Forme générale :
$$a,\ ar,\ ar^2,\ \ldots,\ ar^n,\ \ldots \qquad r \ne 0,\ a \in \mathbb{R}.$$

## Limite d'une suite définie par une fonction

**Théorème.** Soit $f : \mathbb{R} \to \mathbb{R}$ et $a_n = f(n)$. Alors
$$\lim_{x\to+\infty} f(x) = \ell \ \Rightarrow\ \lim_{n\to+\infty} a_n = \ell.$$

**Remarque.** La limite en $\pm\infty$ d'une fraction rationnelle est celle du quotient de ses termes de plus haut degré.

## Opérations sur les limites (*limit laws*)

Soient $(a_n)$, $(b_n)$ deux suites convergentes et $c$ une constante.

1. $\lim (a_n + b_n) = \lim a_n + \lim b_n$.
2. $\lim (a_n - b_n) = \lim a_n - \lim b_n$.
3. $\lim c\,a_n = c \lim a_n$.
4. $\lim c = c$.
5. $\lim (a_n b_n) = \lim a_n \times \lim b_n$.
6. Si $\lim b_n \ne 0$, alors $\lim \dfrac{a_n}{b_n} = \dfrac{\lim a_n}{\lim b_n}$.
7. Si $p > 0$ et $\forall n,\ a_n > 0$, alors $\lim (a_n)^p = \left[\lim a_n\right]^p$.

## Théorème d'encadrement (*squeeze theorem*)

**Théorème.** Soient $(a_n)$, $(b_n)$, $(c_n)$ telles que $\exists n_0,\ \forall n \ge n_0,\ a_n \le b_n \le c_n$. Alors
$$\lim a_n = \lim c_n = \ell \ \Rightarrow\ \lim b_n = \ell.$$
Voir [[Théorème des gendarmes]].

## Valeur absolue

**Théorème.** Si $\lim |a_n| = 0$, alors $\lim a_n = 0$.

## Fonctions continues

**Théorème.** Si $\lim a_n = \ell$ et si $f$ est continue en $\ell$, alors $\lim f(a_n) = f(\ell)$.

## Suites monotones

**Définition.**
1. $(a_n)$ est croissante (*increasing*) si $\forall n,\ a_n \le a_{n+1}$.
2. $(a_n)$ est décroissante (*decreasing*) si $\forall n,\ a_n \ge a_{n+1}$.
3. $(a_n)$ est monotone si elle est croissante ou décroissante.

## Suites bornées

**Définition.**
1. $(a_n)$ est majorée (*bounded above*) s'il existe $M$ tel que $\forall n,\ a_n \le M$.
2. $(a_n)$ est minorée (*bounded below*) s'il existe $m$ tel que $\forall n,\ m \le a_n$.
3. Majorée et minorée : la suite est bornée (*bounded*).

**Théorème.** Toute suite convergente est bornée.

**Théorème** (voir [[Théorème de la limite monotone]]).
1. Toute suite croissante et majorée converge.
2. Toute suite décroissante et minorée converge.
3. Toute suite bornée et monotone converge.

## Suites adjacentes

**Définition.** $(a_n)$ et $(b_n)$ sont [[Suites adjacentes|adjacentes]] si l'une est croissante, l'autre décroissante, et $\lim (b_n - a_n) = 0$.

**Théorème.** Deux suites adjacentes convergent et ont la même limite.

## Voisinage (*neighborhood*)

**Définition.** Soit $a \in \overline{\mathbb{R}} = \mathbb{R} \cup \{\pm\infty\}$. Un voisinage de $a$, noté $\nu(a)$, est une partie de $\mathbb{R}$ contenant un intervalle de la forme :
1. $]a - \epsilon, a + \epsilon[$ avec $\epsilon > 0$, si $a \in \mathbb{R}$ ;
2. $]A, +\infty[$ si $a = +\infty$ ;
3. $]-\infty, A[$ si $a = -\infty$.

Une propriété est vraie « près de $a$ » si elle est vraie sur un voisinage de $a$. Voir [[Boule et voisinage]].

## Petit $o$ et grand $O$

**Hypothèse commune.** $a \in \overline{\mathbb{R}}$, $f$ et $g$ définies sur $\nu(a)$, à valeurs réelles ; $g$ ne s'annule pas sur $\nu(a)$, sauf éventuellement en $a$, et dans ce cas $f(a) = 0$.

**Définition (petit $o$, fonctions).** $f$ est un petit $o$ de $g$ près de $a$ si
$$\lim_{x \to a} \frac{f(x)}{g(x)} = 0, \qquad \text{noté } f \underset{a}{=} o(g).$$

**Définition (petit $o$, suites).** Si $(v_n)$ ne s'annule pas à partir d'un certain rang, $u_n \underset{+\infty}{=} o(v_n)$ si $\lim \frac{u_n}{v_n} = 0$.

**Théorème (croissances comparées).** Soit $(a, b) \in \mathbb{R}^2$. Voir [[Croissances comparées]].
1. Si $a < b$ :
   1. $x^a \underset{+\infty}{=} o(x^b)$ ;
   2. $x^b \underset{0^+}{=} o(x^a)$.
2. Pour tous $a > 0$, $b > 0$ :
   1. $\lim_{x \to +\infty} \frac{x^b}{e^{ax}} = 0$, soit $x^b \underset{+\infty}{=} o(e^{ax})$ ;
   2. $\lim_{x \to +\infty} \frac{(\ln x)^b}{x^a} = 0$, soit $(\ln x)^b \underset{+\infty}{=} o(x^a)$ ;
   3. $\lim_{x \to -\infty} |x|^b e^{ax} = 0$, soit $e^{ax} \underset{-\infty}{=} o\left(\frac{1}{|x|^b}\right)$ ;
   4. $\lim_{x \to 0^+} x^a |\ln x|^b = 0$, soit $|\ln x|^b \underset{0^+}{=} o\left(\frac{1}{x^a}\right)$.

**Définition (grand $O$, fonctions).** Sous la même hypothèse, $f \underset{a}{=} O(g)$ si $\frac{f}{g}$ est bornée près de $a$.

**Définition (grand $O$, suites).** Si $(v_n)$ ne s'annule pas à partir d'un certain rang, $u_n \underset{+\infty}{=} O(v_n)$ si $\frac{u_n}{v_n}$ est bornée près de $+\infty$ :
$$\exists K > 0,\ \exists N,\ \forall n \ge N,\ \left|\frac{u_n}{v_n}\right| \le K \quad\Longleftrightarrow\quad \exists K > 0,\ \exists N,\ \forall n \ge N,\ |u_n| \le K|v_n|.$$

## Équivalents (*asymptotic equivalence*)

**Définition (fonctions).** Sous la même hypothèse, $f$ est équivalente à $g$ près de $a$ si
$$\lim_{x \to a} \frac{f(x)}{g(x)} = 1, \qquad \text{noté } f \underset{a}{\sim} g.$$
Voir [[Équivalent (comparaison asymptotique)]].

**Définition (suites).** Si $(v_n)$ ne s'annule pas à partir d'un certain rang, $u_n \underset{+\infty}{\sim} v_n$ si $\lim \frac{u_n}{v_n} = 1$.

**Proposition (équivalents usuels).**
1. Un polynôme est équivalent en $\pm\infty$ à son terme de plus haut degré.
2. Un polynôme est équivalent en 0 à son terme de plus bas degré.
3. $e^x - 1 \underset{0}{\sim} x$ (écrit « $= 1$ » dans le cours, voir « Erreurs du cours »).
4. $\ln(1+x) \underset{0}{\sim} x$.
5. $(1+x)^\alpha - 1 \underset{0}{\sim} \alpha x$.
6. $\sin x \underset{0}{\sim} x$.
7. $1 - \cos x \underset{0}{\sim} \frac{x^2}{2}$.
8. $\tan x \underset{0}{\sim} x$.

**Propriétés.**
1. Si $f \underset{a}{\sim} g$, alors ou bien $f$ et $g$ ont une limite en $a$ et c'est la même, ou bien aucune des deux n'a de limite en $a$.
2. $f \underset{a}{\sim} g \Leftrightarrow f - g \underset{a}{=} o(g)$.
3. $f \underset{a}{=} o(g) \Leftrightarrow f + g \underset{a}{\sim} g$.
4. Si $f \underset{a}{\sim} g$, alors $f$ et $g$ ont le même signe près de $a$.

**Proposition (liens entre les notations).**
1. $f \underset{a}{=} o(g) \Rightarrow f \underset{a}{=} O(g)$.
2. $f \underset{a}{\sim} g \Rightarrow f \underset{a}{=} O(g)$.

## Développements limités usuels (*common Taylor expansions*)

Tous en 0. Formules recopiées du cours ; les coquilles signalées sont indiquées entre crochets et détaillées dans « Erreurs du cours ».

1. $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^n}{n!} + o(x^n)$.
2. $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + \dots + (-1)^n \frac{x^{2n}}{(2n)!} + o(x^{2n})$.
3. $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} + \dots + (-1)^n \frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+1})$ [le cours écrit $5!$ sous $x^3$].
4. $\cosh x = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots + \frac{x^{2n}}{(2n)!} + o(x^{2n})$.
5. $\sinh x = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots + \frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+1})$ [le cours écrit $5!$ sous $x^3$].
6. $(1+x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \dots + \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n + o(x^n)$.
7. $\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \dots + (-1)^{n-1}\frac{1 \cdot 3 \cdots (2n-3)}{2^n n!} + o(x^n)$ [terme général tel quel dans le cours, incomplet].
8. $\frac{1}{1-x} = 1 + x + x^2 + x^3 + \dots + x^n + o(x^n)$.
9. $\frac{1}{1+x} = 1 - x + x^2 - x^3 + \dots + (-1)^n x^n + o(x^n)$.
10. $\ln(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \dots - \frac{x^n}{n} + o(x^n)$.
11. $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} + \dots + (-1)^{n} \frac{x^n}{n} + o(x^n)$ [le cours écrit $(-1)^n$ ; il faut $(-1)^{n+1}$].
12. $\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + o(x^7)$.
13. $\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} + \dots + (-1)^n \frac{x^{2n+1}}{2n+1} + o(x^{2n+1})$.

## Erreurs du cours

- [[Raw/Year 3/Séries/Chp0 : Revision chapter.docx|Chp0 - Revision chapter]] écrit les équivalents usuels 3 à 8 avec le signe « $=$ » et un « 0 » dessous (vérifié sur l'image) ; il faut le signe $\underset{0}{\sim}$. Le point 3 écrit en outre « $e^x - 1 \underset{0}{=} 1$ » ; il faut « $e^x - 1 \underset{0}{\sim} x$ ».
- [[Raw/Year 3/Séries/Chp0 : Revision chapter.docx|Chp0 - Revision chapter]] écrit, dans les développements de $\sin x$ et de $\sinh x$, « $\frac{x^3}{5!}$ » (vérifié sur l'image) ; il faut « $\frac{x^3}{3!}$ ». Le [[5 - power series|chapitre 5]] écrit la série de $\sin$ correctement.
- [[Raw/Year 3/Séries/Chp0 : Revision chapter.docx|Chp0 - Revision chapter]] écrit le terme général de $\sqrt{1+x}$ « $(-1)^{n-1}\frac{1 \cdot 3 \cdots (2n-3)}{2^n n!}$ » (vérifié sur l'image) : il y manque $x^n$, et ce signe donne $+\frac{x^2}{8}$ pour $n = 2$ alors que le cours écrit $-\frac{x^2}{8}$.
- [[Raw/Year 3/Séries/Chp0 : Revision chapter.docx|Chp0 - Revision chapter]] écrit le terme général de $\ln(1+x)$ « $(-1)^n \frac{x^n}{n}$ » (vérifié sur l'image) ; il faut « $(-1)^{n+1} \frac{x^n}{n}$ », pour retrouver $x - \frac{x^2}{2} + \dots$ La série correcte figure au [[5 - power series|chapitre 5]].
