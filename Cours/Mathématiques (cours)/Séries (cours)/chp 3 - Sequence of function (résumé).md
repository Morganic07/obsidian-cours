---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp3 : Sequence of function.docx|Chp3 - Sequence of function]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Séries/Chp3 : Sequence of function.docx|Chp3 - Sequence of function]], dans [[Séries (index)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Toutes les images de la note sont des énoncés (texte et formules) : leur contenu est recopié ci-dessous, aucune n'est une figure.

## Idée générale

Deux modes de convergence pour une suite de fonctions, et la raison d'être du second : permettre d'échanger limite et continuité, limite et intégrale, limite et dérivée. Voir [[Convergence uniforme]] et [[Interversion de limites]].

## Convergence simple (*pointwise convergence*)

**Définition.** Soit $(f_n)$ une suite de fonctions d'une partie non vide $X \subset \mathbb{R}$ dans $\mathbb{R}$. $(f_n)$ converge simplement sur $X$ si, pour tout $x \in X$, la suite $(f_n(x))$ converge. On définit alors la **limite simple** $f$ par
$$\forall x \in X,\ f(x) = \lim_{n\to+\infty} f_n(x).$$
De façon équivalente :
$$\forall x \in X,\ \forall \epsilon > 0,\ \exists N \in \mathbb{N},\ (n \ge N \Rightarrow |f_n(x) - f(x)| \le \epsilon).$$

**Remarque.** $N$ dépend de $x$ et de $\epsilon$.

**Théorème.** Si $(f_n) \to f$ et $(g_n) \to g$ simplement sur $X$ et $\lambda \in \mathbb{R}$, alors $(f_n + \lambda g_n) \to f + \lambda g$ simplement sur $X$.

**Questions du cours.** Quelles relations entre $(f_n)$ et sa limite ?
1. Si les $f_n$ sont continues, la limite l'est-elle ?
2. Si les $f_n$ et $f$ sont dérivables, a-t-on $\lim f_n' = f'$ ?
3. Si les $f_n$ et $f$ sont intégrables sur $[a, b]$, a-t-on $\lim \int_a^b f_n = \int_a^b f$ ?

Toutes ces questions portent sur l'**interversion de limites** (*limit switching*). Pour la première, la convergence simple d'une suite de fonctions continues n'implique pas la continuité de la limite. Pour résoudre ces questions, on introduit la convergence uniforme.

## Convergence uniforme

**Définition.** $(f_n)$ converge uniformément vers $f$ sur $X$ si
$$\forall \epsilon > 0,\ \exists N \in \mathbb{N},\ (n \ge N) \Rightarrow \forall x \in X,\ |f_n(x) - f(x)| < \epsilon.$$

**Remarques.**
1. $N$ ne dépend que de $\epsilon$ et est le même pour tout $x \in X$, contrairement à la convergence simple.
2. La convergence uniforme implique la convergence simple ; la réciproque est fausse.
3. Par exemple, si $N = 100$, la convergence uniforme signifie que $f_{100}, f_{101}, f_{102}, \ldots$ sont contenues dans le « tube » $[f - \epsilon, f + \epsilon]$.

**Théorème.** La combinaison linéaire $f_n + \lambda g_n$ de deux suites uniformément convergentes converge uniformément vers $f + \lambda g$.

### Norme uniforme (*supremum norm*)

**Définition.** Pour $f$ bornée sur $X$ :
$$\|f\|_\infty = \sup_{x \in X} |f(x)|.$$
Voir [[Norme]].

**Proposition (condition nécessaire et suffisante).** $(f_n)$ converge uniformément vers $f$ sur $X$ si et seulement si
$$\lim_{n\to+\infty} \|f_n - f\|_\infty = 0.$$

**Proposition (condition suffisante).** Si $(f_n)$ converge simplement vers $f$ et s'il existe une suite $(a_n)$ de réels positifs telle que
$$\forall n,\ \forall x \in X,\ |f_n(x) - f(x)| \le a_n \quad\text{et}\quad \lim a_n = 0,$$
alors $(f_n)$ converge uniformément vers $f$ sur $X$.

**Théorème.** Si chaque $f_n$ est bornée et si $(f_n)$ converge uniformément vers $f$ sur $X$, alors $f$ est bornée sur $X$.

## Point limite et interversion de limites

**Définition.** Soit $X \subset \mathbb{R}$. $a \in \mathbb{R}$ est un [[Point limite]] de $X$ si
$$\forall \epsilon > 0,\ \exists x \in\, ]a-\epsilon, a+\epsilon[\, \cap X.$$
Si $X = [b, +\infty[$ ou $]b, +\infty[$, $+\infty$ est un point limite de $X$ ; si $X = ]-\infty, c]$ ou $]-\infty, c[$, $-\infty$ en est un.

**Théorème (interversion des limites).** Soit $f_n : X \to \mathbb{R}$ et $a$ un point limite de $X$. On suppose :
- pour tout $n$, il existe $\ell_n \in \mathbb{R}$ tel que $\lim_{x\to a} f_n(x) = \ell_n$ ;
- $(f_n)$ converge uniformément sur $X$ vers $f$.

Alors $(\ell_n)$ converge vers une limite $\ell$, et $\ell = \lim_{x\to a} f(x)$, soit
$$\lim_{n\to+\infty}\left(\lim_{x\to a} f_n(x)\right) = \lim_{x\to a}\left(\lim_{n\to+\infty} f_n(x)\right).$$

## Continuité en un point et sur un ensemble

**Corollaire.** Soit $x_0 \in X$. Si les $f_n$ sont continues en $x_0$ et si $(f_n)$ converge uniformément vers $f$ sur $X$, alors $f$ est continue en $x_0$.

**Corollaire.** Une limite uniforme sur $X$ de fonctions continues sur $X$ est continue sur $X$. Voir [[Limite et continuité]].

## Interversion limite-intégrale

**Théorème.** Soient $a < b$, des fonctions $f_n$ définies sur $[a, b]$ et $f : [a, b] \to \mathbb{R}$. Si
1. chaque $f_n$ est continue sur $[a, b]$,
2. $(f_n)$ converge uniformément vers $f$ sur $[a, b]$,

alors $f$ est continue sur $[a, b]$ et
$$\lim_{n\to+\infty} \int_a^b f_n(t)\,dt = \int_a^b \lim_{n\to+\infty} f_n(t)\,dt = \int_a^b f(t)\,dt.$$

**Contre-exemple (par contraposée).** La suite suivante converge simplement vers la fonction nulle :
$$f_n(x) = \begin{cases} n^2 x & \text{si } x \in [0, \frac{1}{n}] \\ -n^2 x + 2n & \text{si } x \in [\frac{1}{n}, \frac{2}{n}] \\ 0 & \text{si } x \in [\frac{2}{n}, 1] \end{cases} \qquad (x \in [0, 1])$$
C'est un « triangle » de hauteur $n$ en $x = \frac{1}{n}$. Pour tout $n$, $\int_0^1 f_n = 1$, alors que $\int_0^1 f = 0$ : la convergence n'est donc pas uniforme sur $[0, 1]$.

L'interversion limite-intégrale peut cependant être vraie sans convergence uniforme : le théorème ne donne qu'une condition suffisante.

## Interversion limite-dérivée

**Théorème.** Soit $(f_n)$ une suite de fonctions dérivables d'un intervalle $I$ dans $\mathbb{R}$ telle que
1. il existe $x_0 \in I$ tel que $(f_n(x_0))$ converge,
2. $(f_n')$ converge uniformément sur $I$ vers $g : I \to \mathbb{R}$.

Alors $(f_n)$ converge uniformément sur $I$ vers une fonction $f$ dérivable, et $f' = g$ : $(\lim f_n)' = \lim f_n'$. La note qualifie ces hypothèses de « bonne condition pour l'utiliser ».

**Définition.** $f : I \to \mathbb{R}$ est de [[Fonction de classe Ck|classe $\mathcal{C}^1$]] si elle est dérivable et de dérivée continue.

**Théorème (version $\mathcal{C}^1$).** Mêmes hypothèses avec des $f_n$ de classe $\mathcal{C}^1$ : $(f_n)$ converge uniformément sur $I$ vers une fonction $f$ de classe $\mathcal{C}^1$, et $f' = g$.

## Résumé : méthodes

### Étudier une suite de fonctions

1. Trouver la limite simple. Il faut parfois distinguer des valeurs particulières de $x$ (bornes de l'intervalle d'étude, par exemple). Tracer les premières fonctions aide.
2. Pour la convergence uniforme, utiliser le critère de la norme uniforme, qui est une condition nécessaire et suffisante. En général, on passe par la dérivée pour calculer $\|f_n - f\|_\infty$.

### Montrer que la convergence n'est pas uniforme

Par contraposée de théorèmes :
1. les $f_n$ sont bornées et la limite ne l'est pas ;
2. les $f_n$ sont continues et la limite ne l'est pas ;
3. les $f_n$ sont continues et $\lim \int_a^b f_n \ne \int_a^b \lim f_n$.

### Utiliser le théorème d'interversion limite-dérivée

Il permet de montrer que la suite des dérivées ne converge pas uniformément. Vérifier :
1. les $f_n$ sont dérivables ;
2. il existe $x_0 \in I$ tel que $(f_n(x_0))$ converge ;
3. ou bien la limite de $(f_n)$ n'est pas dérivable, ou bien $(\lim f_n)' \ne \lim f_n'$.

### Erreurs courantes

Aucune de ces propriétés n'implique la convergence uniforme de $(f_n)$ :
1. la limite est bornée ;
2. la limite est continue ;
3. $\lim \int_a^b f_n = \int_a^b \lim f_n$.

Aucune de ces propriétés n'implique la convergence uniforme de $(f_n')$ :
1. la limite est dérivable ;
2. $(\lim f_n)' = \lim f_n'$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Point limite** : la définition « $\forall \epsilon, \exists x \in\, ]a - \epsilon, a + \epsilon[\, \cap X$ » n'exclut pas $x = a$ (alerte de la transcription). La définition usuelle demande $x \ne a$, sans quoi tout point de $X$ serait point limite (complément).
2. **Ensemble d'arrivée du contre-exemple** : $f_n : [0,1] \to [0,1]$, alors que $f_n(1/n) = n$ dépasse 1 pour $n \ge 2$. L'ensemble d'arrivée devrait être $\mathbb{R}$ (complément, sans conséquence sur le raisonnement).
3. **« Necessary and convergent condition »** : lire « necessary and sufficient », par cohérence avec la proposition sur la norme uniforme (alerte confirmée).
4. **« Defined on $f$ »** pour la norme uniforme : lire $X$. **« From $X \subset \mathbb{R}$ to $X$ »** dans la condition suffisante : lire $\mathbb{R}$. Coquilles signalées par la transcription.
5. **Note sur l'intégrale** : le théorème conclut aussi que $f$ est continue, ce qui découle du résultat de continuité plus haut.
6. **Contre-exemple pour $n = 1$** : la formule donne $2/n = 2 > 1$, donc le dernier morceau $[2/n, 1]$ n'a de sens que pour $n \ge 2$ (complément, sans conséquence).
7. **« $N \in N$ »** dans la définition de la convergence uniforme, et « a subset non-empty subset » : coquilles signalées par la transcription.
