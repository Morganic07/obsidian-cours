---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 3 : Important discrete distributions.docx|Chp 3 - Important discrete distributions]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 3 : Important discrete distributions.docx|Chp 3 - Important discrete distributions]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Toutes les images du chapitre sont des énoncés ou des formules : elles sont recopiées ci-dessous, aucune n'est intégrée. Les passages ajoutés finissent par ⓘ.

## Idée générale

Catalogue des lois discrètes usuelles, avec leur fonction de masse (*pmf*), leur espérance et leur variance ([[Espérance et variance]]).

## Récapitulatif

| Loi | Paramètres | $P(X = x)$ | Valeurs | $E(X)$ | $V(X)$ |
|---|---|---|---|---|---|
| Bernoulli | $p$ | $p$ si $x=1$, $1-p$ si $x=0$ | $\{0,1\}$ | $p$ | $p(1-p)$ |
| [[Loi binomiale\|Binomiale]] | $n, p$ | $\binom{n}{x}p^x(1-p)^{n-x}$ | $0,\dots,n$ | $np$ | $np(1-p)$ |
| [[Loi de Poisson\|Poisson]] | $\lambda > 0$ | $e^{-\lambda}\lambda^x/x!$ | $0,1,2,\dots$ | $\lambda$ | $\lambda$ |
| [[Loi hypergéométrique\|Hypergéométrique]] | $n, M, N$ | $\binom{M}{x}\binom{N-M}{n-x}/\binom{N}{n}$ | — | $n\frac{M}{N}$ | $\frac{N-n}{N-1}\,n\frac{M}{N}\left(1-\frac{M}{N}\right)$ |
| [[Loi binomiale négative\|Binomiale négative]] | $r, p$ | $\binom{x-1}{r-1}p^r(1-p)^{x-r}$ | $r, r+1,\dots$ | $r/p$ | $r(1-p)/p^2$ |

Pour reconnaître la loi dans un énoncé, se demander ce que l'on compte : [[Complément hors du cours|ⓘ]]
- un seul essai à deux issues → **Bernoulli** ; [[Complément hors du cours|ⓘ]]
- le nombre de succès en $n$ essais indépendants **fixés à l'avance**, ou tirés **avec remise** → **binomiale** ; [[Complément hors du cours|ⓘ]]
- le nombre de succès en $n$ tirages **sans remise** dans une population finie → **hypergéométrique** ; [[Complément hors du cours|ⓘ]]
- le nombre d'**essais** nécessaires pour atteindre $r$ succès (le nombre d'essais n'est plus fixé) → **binomiale négative**, et [[Loi géométrique|géométrique]] pour $r = 1$ ; [[Complément hors du cours|ⓘ]]
- le nombre d'événements **rares** survenant dans un intervalle de temps ou d'espace (appels à un standard par heure, pannes par mois, coquilles par page), sans nombre maximal → **Poisson**. [[Complément hors du cours|ⓘ]]

## Variable de Bernoulli et loi binomiale

### Variable de Bernoulli (*Bernoulli RV*)

Si $X$ est la [[Variable aléatoire|variable aléatoire]] qui représente le résultat d'un essai, on écrit $X = 1$ pour un succès et $X = 0$ pour un échec. Alors :
$$P\{X = 0\} = 1 - p, \qquad P\{X = 1\} = p$$
$$E(X) = p, \qquad E(X^n) = p, \qquad V(X) = p(1-p)$$

Ces trois formules se vérifient directement. $E(X) = 0 \cdot (1-p) + 1 \cdot p = p$. Comme $0^n = 0$ et $1^n = 1$, $X^n = X$ pour tout $n \ge 1$, d'où $E(X^n) = E(X) = p$. Enfin, par la formule raccourcie ([[Espérance et variance]]), $V(X) = E(X^2) - E(X)^2 = p - p^2 = p(1-p)$, maximale pour $p = 1/2$ (elle vaut alors $1/4$) et nulle quand l'issue est certaine ($p = 0$ ou $1$). [[Complément hors du cours|ⓘ]]

### Expérience binomiale (*binomial experiment*)

Une expérience est binomiale si et seulement si :
1. elle consiste en une suite de $n$ petites expériences appelées **essais** (*trials*), $n$ étant fixé avant l'expérience ;
2. chaque essai a deux issues possibles : succès (S) ou échec (F) ;
3. $p(S) = p$, $p(F) = 1 - p$ ;
4. les essais sont indépendants.

### Loi binomiale (*binomial distribution*)

Si $X$ représente le nombre de succès en $n$ essais, avec probabilité de succès $p$, $X$ est une **variable binomiale de paramètres** $(n, p)$, et :
$$P\{X = i\} = \binom{n}{i} p^i (1-p)^{n-i}, \quad i = 0, 1, \dots, n$$

D'où vient la formule : une suite précise de $n$ essais comportant $i$ succès et $n - i$ échecs (par exemple SS…SF…F) a la probabilité $p^i(1-p)^{n-i}$, par indépendance des essais. Il y a autant de telles suites que de façons de choisir la place des $i$ succès parmi les $n$ essais, soit le [[Coefficient binomial|coefficient binomial]] $\binom{n}{i} = \frac{n!}{i!(n-i)!}$. Les probabilités somment bien à 1 : par la [[Formule du binôme de Newton|formule du binôme]], $\sum_{i=0}^{n}\binom{n}{i}p^i(1-p)^{n-i} = (p + 1 - p)^n = 1$, d'où le nom de la loi. On note souvent $X \sim \mathcal{B}(n, p)$ ou $\mathrm{Bin}(n, p)$. [[Complément hors du cours|ⓘ]]

**Théorème.** La *pmf* de la variable binomiale associée à une expérience binomiale s'appelle loi binomiale :
$$b(x; n, p) = \begin{cases} \dbinom{n}{x} p^x (1-p)^{n-x} & x = 0, 1, 2, \dots, n \\ 0 & \text{sinon} \end{cases}$$
$$E(X) = np, \qquad V(X) = np(1-p)$$

Ces moments s'obtiennent sans calcul de somme : $X = X_1 + \dots + X_n$, où $X_k$ vaut 1 si le $k$-ième essai est un succès, 0 sinon. Les $X_k$ sont des variables de Bernoulli de paramètre $p$, et [[Indépendance de variables aléatoires|indépendantes]]. Par linéarité de l'espérance, $E(X) = \sum E(X_k) = np$ ; par indépendance, les variances s'ajoutent : $V(X) = \sum V(X_k) = np(1-p)$. [[Complément hors du cours|ⓘ]]

Exemple : on lance 10 fois une pièce équilibrée ; le nombre $X$ de « pile » suit $\mathcal{B}(10, 1/2)$. $P(X = 5) = \binom{10}{5}/2^{10} = 252/1024 \approx 0{,}246$, $E(X) = 5$ et $V(X) = 2{,}5$. [[Complément hors du cours|ⓘ]]

## Loi de Poisson (*Poisson distribution*)

Une variable de Poisson approche une variable binomiale de paramètres $(n, p)$ quand $n$ est grand et $p$ petit.

**Théorème (limite).** Si, dans la *pmf* binomiale $b(x; n, p)$, on fait $n \to \infty$ et $p \to 0$ de sorte que $np \to \mu > 0$, alors $b(x; n, p) \to p(x; \mu)$, la loi de Poisson :
$$p(x; \mu) = \frac{e^{-\mu}\mu^x}{x!}, \qquad x = 0, 1, 2, \dots$$

Idée de la preuve : on pose $p = \mu/n$ et on réécrit la masse binomiale en trois facteurs : [[Complément hors du cours|ⓘ]]
$$b(x; n, p) = \underbrace{\frac{n(n-1)\cdots(n-x+1)}{n^x}}_{\to\,1}\cdot\frac{\mu^x}{x!}\cdot\underbrace{\left(1 - \frac{\mu}{n}\right)^{n}}_{\to\,e^{-\mu}}\cdot\underbrace{\left(1 - \frac{\mu}{n}\right)^{-x}}_{\to\,1}$$
Le premier facteur est un produit de $x$ termes $\frac{n-k}{n}$ qui tendent chacun vers 1 ($x$ est fixé), et $(1 - \mu/n)^n \to e^{-\mu}$ est la limite classique de l'exponentielle. [[Complément hors du cours|ⓘ]]

En pratique, on remplace donc $\mathcal{B}(n, p)$ par la loi de Poisson de paramètre $\mu = np$ quand le nombre d'essais est grand et le succès rare : c'est la **loi des événements rares**. Exemple : sur une page de 500 mots, chaque mot contient une coquille avec probabilité $0{,}002$, indépendamment des autres ; le nombre de coquilles suit approximativement une Poisson de paramètre $500 \times 0{,}002 = 1$, d'où $P(\text{aucune coquille}) \approx e^{-1} \approx 0{,}368$. [[Complément hors du cours|ⓘ]]

**Définition.** Une variable aléatoire à valeurs dans $\{0, 1, 2, 3, \dots\}$ est une **variable de Poisson de paramètre $\lambda > 0$** si
$$P\{X = i\} = e^{-\lambda}\frac{\lambda^i}{i!}, \qquad i = 0, 1, \dots$$
$$E[X] = \lambda, \qquad \mathrm{Var}(X) = \lambda$$

Les probabilités somment à 1 grâce à la [[Série entière|série]] de l'exponentielle, $\sum_{i \ge 0} \lambda^i/i! = e^{\lambda}$. La même série donne l'espérance : $E[X] = \sum_{i \ge 1} i\,e^{-\lambda}\frac{\lambda^i}{i!} = \lambda e^{-\lambda}\sum_{i \ge 1}\frac{\lambda^{i-1}}{(i-1)!} = \lambda$. Le paramètre $\lambda$ est donc le **nombre moyen d'événements** dans l'intervalle considéré ; il est proportionnel à la longueur de l'intervalle (si l'on reçoit en moyenne 4 appels par heure, on en reçoit en moyenne 2 par demi-heure). [[Complément hors du cours|ⓘ]]

Espérance et variance égales sont la signature de la loi de Poisson : sur des données de comptage, une variance nettement supérieure à la moyenne (**surdispersion**) indique que le modèle de Poisson ne convient pas. Quand le nombre d'événements par unité de temps suit une Poisson de paramètre $\lambda$ (dans le modèle du processus de Poisson), le temps d'attente entre deux événements suit une [[Loi exponentielle|loi exponentielle]] de même paramètre $\lambda$ (voir [[5 - Continuous random variable]]). [[Complément hors du cours|ⓘ]]

## Loi hypergéométrique (*hypergeometric distribution*)

Contexte : [[Tirage avec et sans remise|tirage sans remise]] dans une population finie, avec succès/échec, et dépendance entre les tirages.

**Théorème.** Si $X$ est le nombre de succès dans un échantillon aléatoire de taille $n$ tiré d'une population de $M$ succès et $(N - M)$ échecs, la loi de $X$, dite hypergéométrique, est :
$$P(X = x) = h(x; n, M, N) = \frac{\dbinom{M}{x}\dbinom{N-M}{n-x}}{\dbinom{N}{n}}$$

Lecture de la formule ([[Dénombrement]]) : le dénominateur compte tous les échantillons possibles de $n$ éléments parmi $N$, supposés équiprobables ; le numérateur, ceux qui contiennent exactement $x$ succès (choisis parmi les $M$) et $n - x$ échecs (choisis parmi les $N - M$). Les valeurs possibles, laissées en blanc dans le tableau, vont de $\max(0,\, n - (N - M))$ à $\min(n,\, M)$ : on ne peut tirer ni plus de succès qu'il n'y en a, ni plus d'échecs qu'il n'y en a. [[Complément hors du cours|ⓘ]]

Exemple : un lot de 20 pièces contient 5 défectueuses ; on en contrôle 4 au hasard, sans remise. $P(X = 1) = \binom{5}{1}\binom{15}{3}/\binom{20}{4} = 5 \times 455/4845 \approx 0{,}470$, et $E(X) = 4 \times 5/20 = 1$. [[Complément hors du cours|ⓘ]]

**Proposition.** L'espérance et la variance de $X$, de *pmf* $h(x; n, M, N)$, sont :
$$E(X) = n \cdot \frac{M}{N}, \qquad \mathrm{Var}(X) = \left(\frac{N-n}{N-1}\right) \cdot n \cdot \frac{M}{N}\left(1 - \frac{M}{N}\right)$$

Avec $p = M/N$, la proportion de succès dans la population, ce sont les moments de la binomiale $\mathcal{B}(n, p)$, sauf le facteur $\frac{N-n}{N-1} \le 1$, appelé **facteur de correction pour population finie** : tirer sans remise réduit la variabilité, car chaque tirage renseigne sur ce qui reste. Quand $N$ est grand devant $n$, ce facteur est proche de 1, retirer un élément ne change presque pas la composition de la population, et l'on approche l'hypergéométrique par la binomiale $\mathcal{B}(n, M/N)$ (règle pratique courante : $n/N \le 0{,}05$). C'est ce qui justifie de traiter un sondage dans une grande population comme des tirages indépendants ([[Tirage avec et sans remise]]). [[Complément hors du cours|ⓘ]]

## Loi binomiale négative (*negative binomial distribution*)

Contexte (note) : nombre total d'essais nécessaires pour obtenir $r$ succès, $r$-ième succès compris, essais indépendants, probabilité de succès $p$. [[Erreurs du cours#^e-3-important-discrete-distributions|✎]]

**Proposition.** La *pmf* de la variable binomiale négative $X$, de paramètres $r$ = nombre de succès voulus et $p = P(S)$, est :
$$nb(x; r, p) = \binom{x-1}{r-1} p^r (1-p)^{x-r}, \qquad x = r, r+1, r+2, \dots$$

D'où vient la formule : $X = x$ signifie que le $x$-ième essai est un succès (le $r$-ième) et que les $x - 1$ essais précédents contiennent exactement $r - 1$ succès. Le second événement a la probabilité binomiale $\binom{x-1}{r-1}p^{r-1}(1-p)^{x-r}$, le premier la probabilité $p$, et ils sont indépendants : leur produit donne $nb(x; r, p)$. [[Complément hors du cours|ⓘ]]

Certains manuels appellent $X$ le nombre d'**échecs** avant le $r$-ième succès ; $X$ prend alors les valeurs $0, 1, 2, \dots$, sa masse est $\binom{x+r-1}{r-1}p^r(1-p)^x$ et son espérance $r(1-p)/p$ (la variance ne change pas). Vérifier la convention d'un énoncé avant d'appliquer les formules. [[Complément hors du cours|ⓘ]]

**Loi géométrique, cas $r = 1$.** Le nombre d'essais jusqu'au **premier** succès suit la [[Loi géométrique|loi géométrique]] de paramètre $p$ : [[Complément hors du cours|ⓘ]]
$$P(X = x) = (1-p)^{x-1}p, \quad x = 1, 2, \dots \qquad E(X) = \frac{1}{p}, \qquad \mathrm{Var}(X) = \frac{1-p}{p^2}$$
Il faut $x - 1$ échecs puis un succès. Par exemple, avec un dé, le nombre de lancers pour obtenir le premier 6 a pour espérance $1/(1/6) = 6$. Une binomiale négative de paramètres $(r, p)$ est la somme de $r$ géométriques indépendantes (attente du 1ᵉʳ succès, puis du 2ᵉ, etc.), ce qui explique $E(X) = r/p$ et $\mathrm{Var}(X) = r(1-p)/p^2$. [[Complément hors du cours|ⓘ]]

La loi géométrique est **sans mémoire** : $P(X > s + t \mid X > s) = P(X > t)$, puisque $P(X > k) = (1-p)^k$. Avoir déjà échoué $s$ fois ne rapproche pas du succès ; c'est l'erreur du joueur qui croit qu'un numéro « doit » sortir après une longue absence. C'est la seule loi discrète sans mémoire, l'équivalent discret de la loi exponentielle. [[Complément hors du cours|ⓘ]]

**Proposition.** Si $X$ suit une binomiale négative de paramètres $r$ et $p$ :
$$E(X) = \frac{r}{p}, \qquad \mathrm{Var}(X) = \frac{r(1-p)}{p^2}$$

Le chapitre ne contient ni exemple ni exercice.
