---
type: source
tags: [year3]
sources: ["[[Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-05
---

Résumé de [[Chp4 Part 1 - Inferential statistics]], dans [[Statistics (matière)]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Estimer un paramètre à partir d'un échantillon et juger la qualité de l'estimation : biais, variance, convergence. Le chapitre introduit la [[Distribution d'échantillonnage]] et la [[Loi des grands nombres]].

## Contenu, dans l'ordre du cours

- **Statistique et paramètre** : une statistique est toute fonction des observations d'un échantillon aléatoire. Un paramètre est une caractéristique numérique de la population.
- **[[Estimateur]]** : une estimation ponctuelle de $\theta$ est un nombre calculé à partir d'une statistique, qui est l'estimateur de $\theta$. Choix usuels : $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = s^2$, $\hat{p} = x/n$, $\hat{\mu}_1 - \hat{\mu}_2 = \bar{x}_1 - \bar{x}_2$, $\hat{p}_1 - \hat{p}_2$.
- **Trois critères** : exactitude (pas de biais, $E(\hat{\theta}) = \theta$), précision (variance faible), convergence. Biais $= E(\hat{\theta}) - \theta$. **Erreur type** (standard error) : $\sigma_{\hat{\theta}} = \sqrt{V(\hat{\theta})}$, estimée si elle contient des paramètres inconnus. **Erreur quadratique moyenne** : $\mathrm{MSE} = E[(\hat{\theta} - \theta)^2] = V(\hat{\theta}) + (\text{biais})^2$ ; pour un estimateur sans biais, MSE et variance coïncident. Cibles à quatre cases : biais faible ou fort, variance faible ou forte.
- **Convergence (consistance)** : $\hat{\theta}$ est consistant si $E[(\hat{\theta} - \theta)^2] \to 0$, ou si $P(|\hat{\theta} - \theta| \ge \varepsilon) \to 0$ pour tout $\varepsilon > 0$. Le premier sens entraîne le second, la réciproque tombant en défaut quand la variance est infinie. La moyenne empirique est sans biais, de plus en plus précise avec $n$, et consistante.
- **Distribution d'échantillonnage** : une statistique varie d'un échantillon à l'autre, c'est donc une variable aléatoire dont la loi s'appelle sa distribution d'échantillonnage. On en déduit l'espérance (biais) et la variance (précision). Pour la moyenne, $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$ (erreur type de la moyenne), estimée par $s/\sqrt{n}$ si $\sigma$ est inconnu.
- **[[Loi des grands nombres]]** : si les $X_i$ forment un échantillon d'une loi de moyenne $\mu$ et de variance finie, $\bar{X} \to \mu$ en moyenne quadratique et en probabilité. Le [[Théorème central limite]] justifie des approximations normales de la binomiale ($n$ grand), de la Poisson ($\mu$ grand), de la binomiale négative ($r$ grand) et de la gamma ($\alpha$ grand), qui sont des lois additives.
- **Corollaire du TCL** : pour $\hat{P} = X/n$, $E(\hat{P}) = p$, $\mathrm{SD}(\hat{P}) = \sqrt{p(1-p)/n}$, et $\hat{P}$ est approximativement normale si $np \ge 10$ et $n(1-p) \ge 10$. Même loi des grands nombres pour les proportions : $\hat{P}$ est consistant.
- **Population finie de taille $N$** : $E(\bar{x}) = \mu$ et $\sigma_{\bar{x}} = \sqrt{\frac{N-n}{N-1}}\frac{\sigma}{\sqrt{n}}$ ; $E(\bar{p}) = p$ et $\sigma_{\bar{p}} = \sqrt{\frac{N-n}{N-1}}\sqrt{\frac{p(1-p)}{n}}$ ; sans le facteur de correction si la population est infinie.
- **Lois stables par somme** : somme de Poisson indépendantes de moyennes $\mu_i$ = Poisson de moyenne $\sum \mu_i$ ; somme de $n$ exponentielles de paramètre $\lambda$ = gamma $(\alpha = n, \beta = 1/\lambda)$ ; somme de gammas de même $\beta$ = gamma $(\alpha_1 + \alpha_2, \beta)$ ; somme de binomiales de même $p$ = binomiale.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Somme de binomiales** : la note écrit $Y \sim \mathrm{Bin}(n_j, q)$. Le résultat attendu est $\mathrm{Bin}(\sum n_i, p)$ : $q$ n'est pas défini et $n_j$ n'est pas la somme (complément). Les $X_i \sim \mathrm{Bin}(n_i, p)$ ont un même $p$, comme dans l'hypothèse.
2. **Population finie** : la note dit « So far, we have worked with the assumption of a finite population », alors que tout ce qui précède suppose une population infinie (complément).
3. **$\bar{p}$ ou $\hat{p}$** : la barre de $E(\bar{p})$ est peut-être un chapeau, image floue. Cette alerte de la transcription tombe sur une simple notation, qui n'est pas ambiguë ici.
4. **Titre provisoire** : la section « Specific RV distribution ???? TROUVER UN MEILLEUR TITRE » porte une note personnelle. Elle regroupe les lois stables par somme.
5. **Rappels de l'étudiant** : « Rajouter dans le cours réponse de la question e) de l'exercice 1 » est un rappel personnel, non repris dans le wiki.
