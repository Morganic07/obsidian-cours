---
type: concept
aliases: [sampling distribution, loi d'échantillonnage, distribution d'échantillonnage de la moyenne, erreur type de la moyenne, standard error of the mean, facteur de correction pour population finie]
matieres: [Statistics]
sources: ["[[Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-06
---

Une statistique change d'un échantillon à l'autre : c'est une variable aléatoire, et sa loi est sa **distribution d'échantillonnage**. Elle donne l'espérance de l'estimateur (donc son biais) et sa variance (donc sa précision).

**Moyenne** : $E(\bar{X}) = \mu$ et $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$ (erreur type de la moyenne), estimée par $s/\sqrt{n}$ si $\sigma$ est inconnu. **Proportion** : $E(\hat{P}) = p$, $\mathrm{SD}(\hat{P}) = \sqrt{p(1-p)/n}$.

**Population finie de taille $N$** : on multiplie l'écart-type par $\sqrt{(N-n)/(N-1)}$.

**Variance, loi normale** : $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ ([[Loi du khi-deux]]). **Moyenne, loi normale** : $(\bar{X} - \mu)/(S/\sqrt{n}) \sim t_{n-1}$ ([[Loi de Student]]).

Liens : [[Estimateur]], [[Théorème central limite]], [[Échantillonnage]], [[Tirage avec et sans remise]]

## À vérifier

- [[Chp4 Part 1 - Inferential statistics]] écrit « So far, we have worked with the assumption of a finite population » avant d'introduire le facteur de correction : il faut lire « infinie ».

Résumés : [[Chp4 Part 1 - Inferential statistics (résumé)]], [[Chp4 Part3 - Inferential statistics (résumé)]]
