---
type: concept
tags:
  - year3
aliases:
  - Simpson's paradox
  - Simpson paradox
  - facteur de confusion
  - confounding factor
  - variable cachée
  - stratifier
  - stratification par groupe
matieres:
  - Data analysis (Thanos)
sources:
  - "[[3 - Paradoxe de Simpson (résumé)|Cours 3 - Paradoxe de Simpson]]"
maj: 2026-11-06
---

Une tendance observée sur les données globales s'inverse quand on sépare les données en sous-groupes. Elle vient d'une **variable cachée** (facteur de confusion) qui influence les résultats et répartit inégalement les cas entre les groupes.

**Exemple du cours** : un traitement de tumeurs. Au total, les médicaments réussissent à 76 % et la chirurgie à 66 %. Mais selon la taille de la tumeur, la chirurgie fait mieux dans les deux catégories (63 % contre 49 % pour les grosses, 90 % contre 82 % pour les petites). La chirurgie reçoit surtout les grosses tumeurs, plus difficiles : la variable cachée est la gravité.

**Conduite à tenir** : ne pas se fier à une moyenne globale sans regarder les sous-groupes, stratifier (séparer les données par groupe) et visualiser en colorant par groupe, ce qui fait apparaître le facteur de confusion, et utiliser une régression multivariée qui ajuste sur les variables cachées (voir [[Régression linéaire]]).

Résumé : [[3 - Paradoxe de Simpson (résumé)]]
