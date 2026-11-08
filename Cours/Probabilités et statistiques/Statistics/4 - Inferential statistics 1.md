---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : chapitre 4, partie 1. Estimer un paramètre à partir d'un échantillon et juger la qualité de l'estimation (biais, variance, convergence). Le chapitre introduit la [[Distribution d'échantillonnage]] et la [[Loi des grands nombres]]. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Estimation des paramètres

- **Statistique** (*statistic*) : nombre calculé à partir de l'échantillon, associé à la caractéristique étudiée ; « en gros », toute fonction des observations d'un échantillon aléatoire.
- **Paramètre** (*parameter*) : caractéristique numérique de toute la population, que l'on peut estimer par une statistique. Voir [[Paramètre et statistique]].

**Définition** : une **estimation ponctuelle** (*point estimate*) d'un paramètre $\theta$ est un nombre unique qui peut passer pour une valeur sensée de $\theta$. On l'obtient en choisissant une statistique adaptée et en calculant sa valeur sur les données. Cette statistique s'appelle l'**[[Estimateur|estimateur ponctuel]]** (*point estimator*) de $\theta$.

En ingénierie, on doit souvent estimer :

| Paramètre | Estimation raisonnable |
|---|---|
| Moyenne $\mu$ d'une population | $\hat{\mu} = \bar{x}$, la [[Moyenne empirique\|moyenne d'échantillon]] |
| Variance $\sigma^2$ (ou écart-type $\sigma$) | $\hat{\sigma}^2 = s^2$, la [[Variance et écart-type d'échantillon\|variance d'échantillon]] |
| Proportion $p$ d'une classe d'intérêt | $\hat{p} = x/n$, où $x$ est le nombre d'individus de la classe dans un échantillon de taille $n$ |
| Différence de moyennes $\mu_1 - \mu_2$ | $\hat{\mu}_1 - \hat{\mu}_2 = \bar{x}_1 - \bar{x}_2$, sur deux échantillons indépendants |
| Différence de proportions $p_1 - p_2$ | $\hat{p}_1 - \hat{p}_2$, sur deux échantillons indépendants |

Ces estimateurs sont sans biais : $E(\bar{X}) = \mu$, $E(\hat{P}) = p$ et $E(S^2) = \sigma^2$, grâce au dénominateur $n - 1$ de $s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$. En effet $E\big[\sum (X_i - \bar{X})^2\big] = (n-1)\sigma^2$ : les écarts sont mesurés à $\bar{X}$, calculée sur les mêmes données, qui colle donc plus aux observations que $\mu$. Diviser par $n$ donne un estimateur biaisé, d'espérance $\frac{n-1}{n}\sigma^2$ (biais $-\sigma^2/n$). En revanche, $S$ est un estimateur légèrement biaisé de $\sigma$ (il le sous-estime en moyenne), bien que $S^2$ soit sans biais pour $\sigma^2$. [[Complément hors du cours|ⓘ]]

Pour les autres paramètres, deux méthodes générales fournissent un estimateur : [[Complément hors du cours|ⓘ]]

- la **[[Méthode des moments|méthode des moments]]** : égaler les moments théoriques ($E(X)$, $E(X^2)$…), qui dépendent du paramètre, aux moments d'échantillon ($\bar{x}$, $\frac{1}{n}\sum x_i^2$…), puis résoudre en $\theta$ ; [[Complément hors du cours|ⓘ]]
- le **[[Maximum de vraisemblance|maximum de vraisemblance]]** : retenir la valeur du paramètre qui rend les données observées les plus probables, c'est-à-dire qui maximise la [[Vraisemblance|vraisemblance]] $L(\theta) = \prod_i f(x_i; \theta)$, en pratique son logarithme ; [[Complément hors du cours|ⓘ]]
- exemple, échantillon de [[Loi exponentielle|loi exponentielle]] de paramètre $\lambda$ : comme $E(X) = 1/\lambda$, la méthode des moments donne $\hat{\lambda} = 1/\bar{x}$ ; le maximum de vraisemblance aussi, car $\ln L(\lambda) = n\ln\lambda - \lambda\sum x_i$ a une dérivée $n/\lambda - \sum x_i$ nulle pour $\lambda = n/\sum x_i = 1/\bar{x}$. [[Complément hors du cours|ⓘ]]

### Trois critères pour choisir un estimateur

1. **Exactitude** (*accuracy*) : pas de tendance systématique à surestimer ou sous-estimer le paramètre d'un échantillon à l'autre ; en moyenne, l'estimateur donne la valeur du paramètre : il n'a pas de **biais**.
2. **Précision** (*precision*) : la **variance** de l'estimateur calculé sur différents échantillons est faible.
3. **Convergence** (*consistency*) : quand la taille de l'échantillon augmente, l'estimateur **converge** vers le paramètre.

### Exactitude et précision

**Définition** : $\hat{\theta}$ est un **estimateur sans biais** (*unbiased*) de $\theta$ si $E(\hat{\theta}) = \theta$ pour toute valeur possible de $\theta$. La différence $E(\hat{\theta}) - \theta$ est le **biais** de $\hat{\theta}$ (nul s'il est sans biais).

L'**erreur type** (*standard error*) de $\hat{\theta}$ est son écart-type, $\sigma_{\hat{\theta}} = \sqrt{V(\hat{\theta})}$. Si elle contient des paramètres inconnus, on y substitue leurs estimations : c'est l'**erreur type estimée**, notée $\hat{\sigma}_{\hat{\theta}}$ ou $s_{\hat{\theta}}$.

**Définition** : l'**erreur quadratique moyenne** (*mean squared error*, MSE) de $\hat{\theta}$ est $E[(\hat{\theta} - \theta)^2]$.

**Proposition** : pour tout estimateur $\hat{\theta}$ de $\theta$,
$$\text{MSE} = V(\hat{\theta}) + [E(\hat{\theta}) - \theta]^2 = \text{variance de l'estimateur} + (\text{biais})^2.$$
En particulier, pour un estimateur sans biais, MSE et variance sont égales.

Preuve : on écrit $\hat{\theta} - \theta = [\hat{\theta} - E(\hat{\theta})] + [E(\hat{\theta}) - \theta]$ et on développe le carré. Le double produit a une espérance nulle, car $E[\hat{\theta} - E(\hat{\theta})] = 0$ et le second crochet est une constante ; il reste $V(\hat{\theta}) + (\text{biais})^2$. [[Complément hors du cours|ⓘ]]

La MSE permet de comparer un estimateur biaisé à un estimateur sans biais : un léger biais peut être compensé par une variance plus faible. Pour un échantillon normal, $\frac{1}{n}\sum (X_i - \bar{X})^2$, biaisé, a une MSE de $\frac{2n-1}{n^2}\sigma^4$, plus petite que celle de $S^2$, $\frac{2}{n-1}\sigma^4$. C'est le [[Compromis biais-variance|compromis biais-variance]], que l'on retrouve en apprentissage automatique ([[Surapprentissage]]). [[Complément hors du cours|ⓘ]]

Parmi les estimateurs sans biais, on retient celui de plus petite variance (estimateur sans biais de variance minimale). Pour une population normale, c'est $\bar{X}$ pour $\mu$ : la médiane d'échantillon, sans biais elle aussi par symétrie, a pour $n$ grand une variance environ $\pi/2 \approx 1{,}57$ fois plus grande. [[Complément hors du cours|ⓘ]]

![[Chp4 Part 1 - Inferential statistics - image19.png]]

*Figure : (1) quatre cibles croisant biais faible ou fort et variance faible ou forte ; (2) trois densités d'estimateurs : (a) exact mais pas précis, (b) précis mais pas exact, (c) exact et précis.*

### Convergence d'un estimateur

**Définition** : soit $X_1, \dots, X_n$ un échantillon aléatoire d'une loi qui dépend d'un paramètre $\theta$. $\hat{\theta}$ est un estimateur **convergent** (*consistent*) de $\theta$ si $\hat{\theta} \to \theta$ quand $n \to \infty$, au sens où

1. $E[(\hat{\theta} - \theta)^2] \to 0$ quand $n \to \infty$, ou
2. $P(|\hat{\theta} - \theta| \ge \varepsilon) \to 0$ quand $n \to \infty$, pour tout $\varepsilon > 0$.

Le sens 1 entraîne le sens 2. Il existe des cas inhabituels (typiquement une variance infinie) où 1 échoue alors que 2 reste vrai. Voir [[Convergence en probabilité]].

Le sens 1 entraîne le sens 2 par l'inégalité de Markov appliquée à $(\hat{\theta} - \theta)^2$, de la même famille que celle de [[Espérance et variance|Bienaymé-Tchebychev]] : $P(|\hat{\theta} - \theta| \ge \varepsilon) \le E[(\hat{\theta} - \theta)^2]/\varepsilon^2$. Avec la décomposition de la MSE, on obtient un critère pratique : un estimateur dont le biais et la variance tendent vers 0 quand $n \to \infty$ est convergent. [[Complément hors du cours|ⓘ]]

### Cas de la moyenne d'échantillon

- La moyenne d'échantillon est un estimateur **sans biais** de la moyenne de la population : elle est exacte.
- Sa **précision** s'améliore quand $n$ augmente.
- Elle est **convergente** : $E[(\hat{\theta} - \theta)^2] \to 0$ quand $n \to \infty$, avec ici $\hat{\theta} = \bar{X}$ et $\theta = \mu$ (le cours reprend la notation générique).
- Calcul : $\bar{X}$ étant sans biais, $E[(\bar{X} - \mu)^2] = V(\bar{X}) = \sigma^2/n$, qui tend vers 0. [[Complément hors du cours|ⓘ]]

## Distribution d'échantillonnage

On considère plusieurs échantillons d'une population. Sur chacun, on calcule une statistique qui varie d'un échantillon à l'autre : la statistique est donc une variable aléatoire, dont la loi s'appelle la **[[Distribution d'échantillonnage|distribution d'échantillonnage]]** de la statistique ([[Échantillonnage]]).

- Statistique « moyenne d'échantillon » : elle suit la distribution d'échantillonnage de la moyenne.
- Statistique « écart-type » : il suit la distribution d'échantillonnage de l'écart-type.
- De même pour la variance, la médiane, la proportion, etc.

Pour chaque distribution d'échantillonnage, on calcule moyenne, écart-type, variance… On en déduit l'espérance de l'estimateur (biaisé ou non : exactitude) et sa variance (précision).

Quand la loi d'une statistique est trop difficile à calculer, on l'approche par simulation : tirer un grand nombre d'échantillons et tracer l'histogramme des valeurs obtenues. Faute de connaître la population, on rééchantillonne avec remise les données observées elles-mêmes : c'est le [[Bootstrap|bootstrap]], qui donne une erreur type ou un intervalle de confiance sans formule. [[Complément hors du cours|ⓘ]]

![[Chp4 Part 1 - Inferential statistics - image2.png]]

*Figure : panneau A, estimateur sans biais : la distribution de $\hat{\theta}$ est centrée sur $\theta$ ; panneau B, estimateur biaisé : elle est centrée sur $E(\hat{\theta}) \neq \theta$, l'écart étant le biais.*

### Distribution d'échantillonnage de la moyenne

- Si $\sigma$ est connu, l'écart-type de $\bar{X}$, ou **erreur type de la moyenne** (*standard error of the mean*), est $\mathrm{SD}(\bar{X}) = \dfrac{\sigma}{\sqrt{n}}$.
- Si $\sigma$ est inconnu, on l'estime avec l'écart-type d'échantillon : $\mathrm{SD}(\bar{X}) \approx \dfrac{s}{\sqrt{n}}$.
- Exemple : $\sigma = 15$ et $n = 25$ donnent $\mathrm{SD}(\bar{X}) = 15/5 = 3$ ; il faut $n = 100$ pour descendre à $1{,}5$. Ne pas confondre l'écart-type $s$, qui mesure la dispersion des observations, et l'erreur type $s/\sqrt{n}$, qui mesure la précision de la moyenne. [[Complément hors du cours|ⓘ]]

![[Chp4 Part 1 - Inferential statistics - image11.png]]

*Figure : à gauche, population normale et lois de $\bar{X}$ pour $n = 4$ et $n = 10$, de plus en plus étroites ; à droite, le [[Théorème central limite]] illustré : population asymétrique, loi de $\bar{X}$ un peu asymétrique pour $n$ petit, approximativement normale pour $n$ grand.*

## Loi des grands nombres et autres théorèmes

### Loi des grands nombres

([[Loi des grands nombres]], *law of large numbers*, LLN)

Si $X_1, \dots, X_n$ est un échantillon aléatoire d'une loi de moyenne $\mu$ et de variance **finie**, alors $\bar{X}$ converge vers $\mu$ :

1. en moyenne quadratique : $E[(\bar{X} - \mu)^2] \to 0$ quand $n \to \infty$ ;
2. en probabilité : $P(|\bar{X} - \mu| \ge \varepsilon) \to 0$ quand $n \to \infty$, pour tout $\varepsilon > 0$.

Preuve du point 2 par l'inégalité de [[Espérance et variance|Bienaymé-Tchebychev]] : $P(|\bar{X} - \mu| \ge \varepsilon) \le \dfrac{V(\bar{X})}{\varepsilon^2} = \dfrac{\sigma^2}{n\varepsilon^2} \to 0$. [[Complément hors du cours|ⓘ]]

C'est la **loi faible** des grands nombres ; la **loi forte** affirme que $\bar{X}$ converge vers $\mu$ avec probabilité 1, et ne demande qu'une moyenne finie. La loi des grands nombres fonde l'interprétation fréquentiste de la probabilité (sur de nombreuses répétitions, la fréquence d'un événement tend vers sa probabilité) et les méthodes de Monte-Carlo, qui estiment une espérance par la moyenne de nombreuses simulations. Elle ne prévoit aucune « compensation » des écarts passés : après une série de pile, face n'est pas plus probable au lancer suivant (erreur du joueur). [[Complément hors du cours|ⓘ]]

### Approximations normales justifiées par le TCL

La [[Loi normale|loi normale]] approche raisonnablement la [[Loi binomiale|loi binomiale]] pour $n$ grand, car la binomiale est **additive** : une variable binomiale est une somme de variables iid. D'autres lois additives ([[Stabilité des lois par somme]]) : Poisson, binomiale négative, gamma et, bien sûr, normale. Le TCL justifie en particulier les approximations normales de :

- la [[Loi de Poisson]], quand $\mu$ est grand ;
- la [[Loi binomiale négative]], quand $r$ est grand ;
- la loi gamma, quand $\alpha$ est grand.

Voir aussi [[Approximation normale]].

Pour approcher une loi discrète (binomiale, Poisson) par une loi continue, on applique la **[[Approximation normale|correction de continuité]]** : la valeur entière $x$ est représentée par l'intervalle $[x - 0{,}5 ;\ x + 0{,}5]$. Pour $X \sim \mathrm{Bin}(n, p)$, $P(X \le x) \approx \Phi\left(\dfrac{x + 0{,}5 - np}{\sqrt{np(1-p)}}\right)$. Exemple : $n = 100$, $p = 0{,}5$, donc $np = 50$ et $\sqrt{np(1-p)} = 5$ ; $P(X \le 55) \approx \Phi(5{,}5/5) = \Phi(1{,}1) \approx 0{,}864$, très proche de la valeur exacte ($0{,}864$), alors que sans correction $\Phi(1) \approx 0{,}841$. [[Complément hors du cours|ⓘ]]

### Corollaire du TCL (proportions)

Soit un événement $A$ de probabilité $p = P(A)$, $X$ le nombre de fois où $A$ se produit en $n$ répétitions indépendantes, et $\hat{P} = \hat{P}(A) = X/n$. Alors

1. $\mu_{\hat{P}} = E(\hat{P}) = p$ ;
2. $\sigma_{\hat{P}} = \mathrm{SD}(\hat{P}) = \sqrt{\dfrac{p(1-p)}{n}}$ ;
3. quand $n$ augmente, la loi de $\hat{P}$ tend vers une loi normale.

En pratique, on considère $\hat{P}$ approximativement normale si $np \ge 10$ et $n(1-p) \ge 10$.

Les points 1 et 2 découlent de $\hat{P} = X/n$ avec $X \sim \mathrm{Bin}(n, p)$ : $E(\hat{P}) = np/n = p$ et $V(\hat{P}) = np(1-p)/n^2 = p(1-p)/n$. Le point 3 est le TCL appliqué à $X$, somme de $n$ variables de Bernoulli. [[Complément hors du cours|ⓘ]]

### Loi des grands nombres pour les proportions

Si les $X_i$ sont iid de Bernoulli($p$), on écrit $\bar{X} = \hat{P}$, et $\mu = E(X_i) = p$. La proportion d'échantillon $\hat{P}$ converge vers la « vraie » proportion $p$ :

1. en moyenne quadratique : $E[(\hat{P} - p)^2] \to 0$ ;
2. en probabilité : $P(|\hat{P} - p| \ge \varepsilon) \to 0$ pour tout $\varepsilon > 0$.

En langage statistique : $\bar{X}$ est un estimateur convergent de $\mu$, et $\hat{P}$ un estimateur convergent de $p$.

### Population finie de taille $N$

Jusqu'ici, la population était supposée infinie. [[Erreurs du cours#^e-4-inferential-statistics-1|✎]] Quand la population a une taille finie $N$, on modifie les formules (facteur de correction $\sqrt{(N-n)/(N-1)}$) :

| | Population finie | Population infinie |
|---|---|---|
| Moyenne $\bar{x}$ | $E(\bar{x}) = \mu$, $\sigma_{\bar{x}} = \sqrt{\dfrac{N-n}{N-1}}\left(\dfrac{\sigma}{\sqrt{n}}\right)$ | $\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$ |
| Proportion $\bar{p}$ | $E(\bar{p}) = p$, $\sigma_{\bar{p}} = \sqrt{\dfrac{N-n}{N-1}}\sqrt{\dfrac{p(1-p)}{n}}$ | $\sigma_{\bar{p}} = \sqrt{\dfrac{p(1-p)}{n}}$ |

Le facteur vient du [[Tirage avec et sans remise|tirage sans remise]] : pour une proportion, le nombre d'individus de la classe dans l'échantillon suit une [[Loi hypergéométrique|loi hypergéométrique]], de variance $np(1-p)\frac{N-n}{N-1}$. Il vaut 1 pour $n = 1$ et 0 pour $n = N$ : l'échantillon est alors toute la population, et $\bar{x} = \mu$ sans erreur. Il reste proche de 1, donc négligeable, quand $n/N \le 0{,}05$ ([[3 - More on probability]]). [[Complément hors du cours|ⓘ]]

Conséquence : la précision dépend de la taille $n$ de l'échantillon, presque pas de celle de la population. Un échantillon aléatoire de 1 000 personnes estime une proportion avec la même précision dans une ville de 100 000 habitants que dans un pays de 60 millions. [[Complément hors du cours|ⓘ]]

## Lois stables par somme

(Section titrée dans la note « Specific RV distribution ???? TROUVER UN MEILLEUR TITRE » ; voir [[Stabilité des lois par somme]].)

- **Poisson** : si $X_1, \dots, X_n$ sont des [[Loi de Poisson|variables de Poisson]] indépendantes de moyennes $\mu_i$, alors $Y = X_1 + \dots + X_n$ suit une loi de Poisson de moyenne $\mu_1 + \dots + \mu_n$.
- **Exponentielle** : si $X_1, \dots, X_n$ sont des [[Loi exponentielle|exponentielles]] indépendantes de même paramètre $\lambda$, alors $Y = X_1 + \dots + X_n$ suit une loi gamma de paramètres $\alpha = n$ et $\beta = 1/\lambda$.
- **Binomiale** : si $X_1, \dots, X_n$ sont des binomiales indépendantes, $X_i \sim \mathrm{Bin}(n_i, p)$ ($n_i \in \mathbb{N}$, $p \in [0, 1]$), alors $Y = X_1 + \dots + X_n \sim \mathrm{Bin}(\sum n_i, p)$. [[Erreurs du cours#^e-4-inferential-statistics-1|✎]]
- **Gamma** : si $X \sim \Gamma(\alpha_1, \beta)$ et $Y \sim \Gamma(\alpha_2, \beta)$ sont indépendantes, de même $\beta$, alors $X + Y \sim \Gamma(\alpha_1 + \alpha_2, \beta)$.

Ces résultats se démontrent avec les [[Fonction génératrice des moments|fonctions génératrices des moments]] ([[3 - More on probability]]) : pour la binomiale, $\prod_i (1 - p + pe^t)^{n_i} = (1 - p + pe^t)^{\sum n_i}$. La condition « même $p$ » (ou même $\lambda$, même $\beta$) est indispensable : deux binomiales de paramètres $p$ différents ont une somme qui n'est pas binomiale. Une somme de [[Loi du khi-deux|khi-deux]] indépendants est aussi un khi-deux, dont les degrés de liberté s'additionnent ([[4 - Inferential statistics 3]]). [[Complément hors du cours|ⓘ]]

La note se termine par un rappel personnel : « Rajouter dans le cours réponse de la question e) de l'exercice 1 » ; l'exercice n'est pas dans la note.
