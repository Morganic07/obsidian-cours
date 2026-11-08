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
maj: 2026-11-08
---

[[1 - IA|Cours 1 (IA)]] distingue trois types de prompts pour la génération d'images :

- le prompt de texte détaillé : style, éclairage, objectif, résolution ;
- le prompt avec image de référence, par exemple une planche de style dans Gemini ;
- le prompt en fichier JSON, que les IA comprendraient mieux et qu'une IA peut rédiger : éclairage, arrière-plan, composition, profil de couleur, sujet, paramètres de génération, dont un `negative_prompt`. Dans l'exemple, chaque clé s'écrit entre guillemets doubles droits (`"technical_specs": {`) ; le texte mêle « A old man », un débardeur et des détails féminins (« her », bikini), alors que l'image montre un homme jeune en t-shirt. [[Erreurs du cours#^e-prompt-ia|✎]]

Voir aussi : [[Modèle de diffusion]], [[Droit d'auteur et IA]], [[Token (IA)]].

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]
