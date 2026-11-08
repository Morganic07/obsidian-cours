---
type: concept
tags: [year3]
aliases: [SUS, échelle SUS, questionnaire SUS]
sources: ["[[Raw/Year 3/Affordance/Présentation Tests Utilisateurs ID3.pptx|Présentation Tests Utilisateurs ID3.pptx]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le *System Usability Scale* (SUS) est un questionnaire standardisé qui mesure l'[[Utilisabilité|utilisabilité]] perçue d'un produit ou d'un système. Il a été conçu par John Brooke en 1986 (publié en 1996) et reste l'une des [[Échelles UX|échelles UX]] les plus utilisées, car il est court, gratuit et indépendant de la technologie évaluée.

Il compte dix affirmations notées sur une échelle de Likert de 1 (pas du tout d'accord) à 5 (tout à fait d'accord). Elles alternent : les items impairs sont formulés positivement (« J'ai trouvé ce système facile à utiliser »), les items pairs négativement (« J'ai trouvé ce système inutilement complexe »). Cette alternance limite les réponses machinales.

**Calcul du score** : pour chaque item impair, on retient $\text{note} - 1$ ; pour chaque item pair, $5 - \text{note}$. Chaque contribution vaut donc de 0 à 4, et leur somme de 0 à 40. On la multiplie par 2,5 :

$$
\text{SUS} = 2{,}5 \times \left[ \sum_{i \in \{1,3,5,7,9\}} (x_i - 1) + \sum_{i \in \{2,4,6,8,10\}} (5 - x_i) \right] \in [0, 100]
$$

où $x_i$ est la note donnée à l'item $i$.

**Interprétation** : le score va de 0 à 100 mais n'est pas un pourcentage. La moyenne observée sur un grand nombre d'études tourne autour de 68 : un score supérieur indique une utilisabilité perçue au-dessus de la moyenne, un score inférieur un produit à améliorer. Le score se lit surtout en comparaison (deux versions, deux produits concurrents, avant et après une refonte).

**Usage** : on le fait remplir à la fin d'un [[Test utilisateur|test utilisateur]], une fois toutes les tâches réalisées. C'est une mesure subjective (ce que le participant ressent), qui complète les mesures objectives de performance (taux de réussite, temps, erreurs).

## Dans le cours

Le cours ne le nomme pas : la passation d'un test utilisateur recueille la perception globale du participant « avec un outil standardisé », sans dire lequel ([[Raw/Year 3/Affordance/Présentation Tests Utilisateurs ID3.pptx|Présentation Tests Utilisateurs ID3.pptx]]). Le SUS est l'outil le plus courant pour cet usage.

Notion parente : [[Échelles UX]]. Voir aussi : [[Test utilisateur]], [[Utilisabilité]], [[Questionnaire]].

Résumés : [[1 - UX]]
