---
type: concept
tags:
  - year3
aliases:
  - modèles de diffusion
  - diffusion model
  - diffusion models
  - Stable Diffusion
  - prompt négatif
  - negative prompt
sources:
  - "[[1 - IA|Cours 1]]"
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : famille de modèles génératifs d'[[Apprentissage profond|apprentissage profond]], surtout utilisée pour produire des images.

- **Entraînement** : on ajoute progressivement du bruit gaussien à des images réelles, en de nombreuses petites étapes, jusqu'à obtenir un bruit pur ; le réseau apprend à inverser chaque étape, c'est-à-dire à prédire le bruit ajouté pour le retirer.
- **Génération** : le modèle part d'un bruit pur et le débruite pas à pas ; à chaque étape, il est guidé par le [[Prompt (IA)|prompt]] (texte traduit en vecteur par un encodeur de texte).
- **Stable Diffusion** (2022) est un modèle de diffusion *latent* : il travaille non sur les pixels mais dans un espace latent, version compressée de l'image, puis décode le résultat. Ce gain de calcul le rend utilisable sur une carte graphique grand public.
- **Prompt négatif** : texte décrivant ce qu'on ne veut pas ; à chaque étape, le débruitage est poussé à s'éloigner de ce qu'il décrit.

## Dans le cours

Nommé dans [[1 - IA|Cours 1 (IA)]] sans définition : famille de l'apprentissage profond (2020), à laquelle le schéma du cours rattache Stable Diffusion et Midjourney.

Notion parente : [[Apprentissage profond]]. Voir aussi : [[Prompt (IA)]].

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]
