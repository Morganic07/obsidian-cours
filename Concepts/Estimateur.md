---
type: concept
aliases: [estimator, point estimate, estimation ponctuelle, biais d'un estimateur, unbiased estimator, estimateur sans biais, erreur quadratique moyenne, mean squared error, MSE, standard error, erreur type, estimateur consistant, consistent estimator]
matieres: [Statistics]
sources: ["[[Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-05
---

Une statistique est une fonction des observations d'un échantillon. Un **estimateur** $\hat{\theta}$ d'un paramètre $\theta$ est une statistique choisie pour l'estimer ; sa valeur sur les données est l'estimation ponctuelle. Choix usuels : $\bar{x}$ pour $\mu$, $s^2$ pour $\sigma^2$, $\hat{p} = x/n$ pour $p$, différences de moyennes ou de proportions pour deux populations.

**Critères** :
- exactitude : biais $= E(\hat{\theta}) - \theta$, nul pour un estimateur sans biais ;
- précision : variance de l'estimateur faible ;
- convergence (consistance) : $E[(\hat{\theta} - \theta)^2] \to 0$ ou $P(|\hat{\theta} - \theta| \ge \varepsilon) \to 0$ quand $n \to \infty$.

**Erreur type** : $\sigma_{\hat{\theta}} = \sqrt{V(\hat{\theta})}$. **MSE** : $E[(\hat{\theta} - \theta)^2] = V(\hat{\theta}) + (\text{biais})^2$, égale à la variance pour un estimateur sans biais. La moyenne empirique est sans biais et consistante.

Liens : [[Distribution d'échantillonnage]], [[Loi des grands nombres]], [[Intervalle de confiance]], [[Variance et écart-type d'échantillon]]

Résumé : [[Chp4 Part 1 - Inferential statistics (résumé)]]
