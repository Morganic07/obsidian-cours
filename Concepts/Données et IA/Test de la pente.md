---
type: concept
tags: [year3]
aliases: [test of the slope, test de significativité de la pente, test sur la pente]
sources: ["[[Cours 10 - linear regression]]", "[[probabilité statistiques utilitaire]]"]
maj: 2026-11-06
---

En régression linéaire simple, on teste $H_0 : \beta_1 = 0$ (pas de relation linéaire) contre $H_a : \beta_1 \ne 0$. Statistique : $t = \dfrac{\hat\beta_1}{S_{\hat\beta_1}}$, avec $S_{\hat\beta_1} = \dfrac{s}{\sqrt{SS_{xx}}}$, où $s$ est l'[[Erreur standard de la régression]], et $df = n - 2$ ([[Cours 10 - linear regression]]).

L'aide-mémoire de Statistics donne aussi, pour la corrélation, $t_{n-2} = \dfrac{r\sqrt{n-2}}{\sqrt{1-r^2}}$ ([[probabilité statistiques utilitaire]]).

Notion parente : [[Régression linéaire]]. Voir aussi : [[Test t]], [[Loi de Student]], [[Erreur standard de la régression]].

Résumés : [[Cours 10 - linear regression (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
