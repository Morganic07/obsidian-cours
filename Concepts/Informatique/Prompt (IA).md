---
type: concept
tags:
  - year3
aliases:
  - prompts
  - prompt JSON
  - negative prompt
  - negative_prompt
  - prompt engineering
  - ingénierie de prompt
matieres:
  - IA
sources:
  - "[[1 - IA|Cours 1]]"
maj: 2026-11-07
---

[[1 - IA|Cours 1 (IA)]] distingue trois types de prompts pour la génération d'images :

- le prompt de texte détaillé : style, éclairage, objectif, résolution ;
- le prompt avec image de référence, par exemple une planche de style dans Gemini ;
- le prompt en fichier JSON, que les IA comprendraient mieux et qu'une IA peut rédiger : éclairage, arrière-plan, composition, profil de couleur, sujet, paramètres de génération, dont un `negative_prompt`.

Voir aussi : [[Modèle de diffusion]], [[Droit d'auteur et IA]], [[Token (IA)]].

## Erreurs du cours

- Le prompt JSON d'exemple de [[1 - IA|Cours 1 (IA)]] écrit `« technical_specs": {` ; il faut `"technical_specs": {`, sans quoi le JSON n'est pas valide (vérifié sur l'image). Son texte ne correspond pas non plus à la photo : il parle de « bikini », de « her », de « A old man » et de « tank top », alors que l'image montre un homme jeune en t-shirt.

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]
