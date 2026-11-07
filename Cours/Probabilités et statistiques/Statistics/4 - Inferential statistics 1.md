---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : chapitre 4, partie 1. Estimer un paramètre à partir d'un échantillon et juger la qualité de l'estimation (biais, variance, convergence). Le chapitre introduit la [[Distribution d'échantillonnage]] et la [[Loi des grands nombres]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

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

![[Chp4 Part 1 - Inferential statistics - image19.png]]

*Figure : (1) quatre cibles croisant biais faible ou fort et variance faible ou forte ; (2) trois densités d'estimateurs : (a) exact mais pas précis, (b) précis mais pas exact, (c) exact et précis.*

### Convergence d'un estimateur

**Définition** : soit $X_1, \dots, X_n$ un échantillon aléatoire d'une loi qui dépend d'un paramètre $\theta$. $\hat{\theta}$ est un estimateur **convergent** (*consistent*) de $\theta$ si $\hat{\theta} \to \theta$ quand $n \to \infty$, au sens où

1. $E[(\hat{\theta} - \theta)^2] \to 0$ quand $n \to \infty$, ou
2. $P(|\hat{\theta} - \theta| \ge \varepsilon) \to 0$ quand $n \to \infty$, pour tout $\varepsilon > 0$.

Le sens 1 entraîne le sens 2. Il existe des cas inhabituels (typiquement une variance infinie) où 1 échoue alors que 2 reste vrai. Voir [[Convergence en probabilité]].

### Cas de la moyenne d'échantillon

- La moyenne d'échantillon est un estimateur **sans biais** de la moyenne de la population : elle est exacte.
- Sa **précision** s'améliore quand $n$ augmente.
- Elle est **convergente** : $E[(\hat{\theta} - \theta)^2] \to 0$ quand $n \to \infty$, avec ici $\hat{\theta} = \bar{X}$ et $\theta = \mu$ (le cours reprend la notation générique).

## Distribution d'échantillonnage

On considère plusieurs échantillons d'une population. Sur chacun, on calcule une statistique qui varie d'un échantillon à l'autre : la statistique est donc une variable aléatoire, dont la loi s'appelle la **[[Distribution d'échantillonnage|distribution d'échantillonnage]]** de la statistique ([[Échantillonnage]]).

- Statistique « moyenne d'échantillon » : elle suit la distribution d'échantillonnage de la moyenne.
- Statistique « écart-type » : il suit la distribution d'échantillonnage de l'écart-type.
- De même pour la variance, la médiane, la proportion, etc.

Pour chaque distribution d'échantillonnage, on calcule moyenne, écart-type, variance… On en déduit l'espérance de l'estimateur (biaisé ou non : exactitude) et sa variance (précision).

![[Chp4 Part 1 - Inferential statistics - image2.png]]

*Figure : panneau A, estimateur sans biais : la distribution de $\hat{\theta}$ est centrée sur $\theta$ ; panneau B, estimateur biaisé : elle est centrée sur $E(\hat{\theta}) \neq \theta$, l'écart étant le biais.*

### Distribution d'échantillonnage de la moyenne

- Si $\sigma$ est connu, l'écart-type de $\bar{X}$, ou **erreur type de la moyenne** (*standard error of the mean*), est $\mathrm{SD}(\bar{X}) = \dfrac{\sigma}{\sqrt{n}}$.
- Si $\sigma$ est inconnu, on l'estime avec l'écart-type d'échantillon : $\mathrm{SD}(\bar{X}) \approx \dfrac{s}{\sqrt{n}}$.

![[Chp4 Part 1 - Inferential statistics - image11.png]]

*Figure : à gauche, population normale et lois de $\bar{X}$ pour $n = 4$ et $n = 10$, de plus en plus étroites ; à droite, le [[Théorème central limite]] illustré : population asymétrique, loi de $\bar{X}$ un peu asymétrique pour $n$ petit, approximativement normale pour $n$ grand.*

## Loi des grands nombres et autres théorèmes

### Loi des grands nombres

([[Loi des grands nombres]], *law of large numbers*, LLN)

Si $X_1, \dots, X_n$ est un échantillon aléatoire d'une loi de moyenne $\mu$ et de variance **finie**, alors $\bar{X}$ converge vers $\mu$ :

1. en moyenne quadratique : $E[(\bar{X} - \mu)^2] \to 0$ quand $n \to \infty$ ;
2. en probabilité : $P(|\bar{X} - \mu| \ge \varepsilon) \to 0$ quand $n \to \infty$, pour tout $\varepsilon > 0$.

### Approximations normales justifiées par le TCL

La [[Loi normale|loi normale]] approche raisonnablement la [[Loi binomiale|loi binomiale]] pour $n$ grand, car la binomiale est **additive** : une variable binomiale est une somme de variables iid. D'autres lois additives ([[Stabilité des lois par somme]]) : Poisson, binomiale négative, gamma et, bien sûr, normale. Le TCL justifie en particulier les approximations normales de :

- la [[Loi de Poisson]], quand $\mu$ est grand ;
- la [[Loi binomiale négative]], quand $r$ est grand ;
- la loi gamma, quand $\alpha$ est grand.

Voir aussi [[Approximation normale]].

### Corollaire du TCL (proportions)

Soit un événement $A$ de probabilité $p = P(A)$, $X$ le nombre de fois où $A$ se produit en $n$ répétitions indépendantes, et $\hat{P} = \hat{P}(A) = X/n$. Alors

1. $\mu_{\hat{P}} = E(\hat{P}) = p$ ;
2. $\sigma_{\hat{P}} = \mathrm{SD}(\hat{P}) = \sqrt{\dfrac{p(1-p)}{n}}$ ;
3. quand $n$ augmente, la loi de $\hat{P}$ tend vers une loi normale.

En pratique, on considère $\hat{P}$ approximativement normale si $np \ge 10$ et $n(1-p) \ge 10$.

### Loi des grands nombres pour les proportions

Si les $X_i$ sont iid de Bernoulli($p$), on écrit $\bar{X} = \hat{P}$, et $\mu = E(X_i) = p$. La proportion d'échantillon $\hat{P}$ converge vers la « vraie » proportion $p$ :

1. en moyenne quadratique : $E[(\hat{P} - p)^2] \to 0$ ;
2. en probabilité : $P(|\hat{P} - p| \ge \varepsilon) \to 0$ pour tout $\varepsilon > 0$.

En langage statistique : $\bar{X}$ est un estimateur convergent de $\mu$, et $\hat{P}$ un estimateur convergent de $p$.

### Population finie de taille $N$

Quand la population a une taille finie $N$, on modifie les formules (facteur de correction $\sqrt{(N-n)/(N-1)}$) :

| | Population finie | Population infinie |
|---|---|---|
| Moyenne $\bar{x}$ | $E(\bar{x}) = \mu$, $\sigma_{\bar{x}} = \sqrt{\dfrac{N-n}{N-1}}\left(\dfrac{\sigma}{\sqrt{n}}\right)$ | $\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$ |
| Proportion $\bar{p}$ | $E(\bar{p}) = p$, $\sigma_{\bar{p}} = \sqrt{\dfrac{N-n}{N-1}}\sqrt{\dfrac{p(1-p)}{n}}$ | $\sigma_{\bar{p}} = \sqrt{\dfrac{p(1-p)}{n}}$ |

## Lois stables par somme

(Section titrée dans la note « Specific RV distribution ???? TROUVER UN MEILLEUR TITRE » ; voir [[Stabilité des lois par somme]].)

- **Poisson** : si $X_1, \dots, X_n$ sont des [[Loi de Poisson|variables de Poisson]] indépendantes de moyennes $\mu_i$, alors $Y = X_1 + \dots + X_n$ suit une loi de Poisson de moyenne $\mu_1 + \dots + \mu_n$.
- **Exponentielle** : si $X_1, \dots, X_n$ sont des [[Loi exponentielle|exponentielles]] indépendantes de même paramètre $\lambda$, alors $Y = X_1 + \dots + X_n$ suit une loi gamma de paramètres $\alpha = n$ et $\beta = 1/\lambda$.
- **Binomiale** : si $X_1, \dots, X_n$ sont des binomiales indépendantes, $X_i \sim \mathrm{Bin}(n_i, p)$ ($n_i \in \mathbb{N}$, $p \in [0, 1]$), alors $Y = X_1 + \dots + X_n \sim \mathrm{Bin}(\sum n_i, p)$ (la note écrit $\mathrm{Bin}(n_j, q)$, voir « Erreurs du cours »).
- **Gamma** : si $X \sim \Gamma(\alpha_1, \beta)$ et $Y \sim \Gamma(\alpha_2, \beta)$ sont indépendantes, de même $\beta$, alors $X + Y \sim \Gamma(\alpha_1 + \alpha_2, \beta)$.

La note se termine par un rappel personnel : « Rajouter dans le cours réponse de la question e) de l'exercice 1 » ; l'exercice n'est pas dans la note.

## Erreurs du cours

- [[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]] écrit « Y ∼ Bin(n_j , q) » pour la somme de binomiales indépendantes $X_i \sim \mathrm{Bin}(n_i, p)$ ; il faut $Y \sim \mathrm{Bin}(n_1 + \dots + n_n,\ p)$ : $q$ n'est pas défini et $n_j$ n'est pas la somme.
- [[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]] écrit « So far, we have worked with the assumption of a finite population » ; il faut « infinite population » : la section introduit justement la correction pour une population finie de taille $N$.
