---
type: concept
tags:
  - year3
aliases:
  - IA open source
  - close source
  - IA propriétaire
  - modèle open source
  - open weights
  - poids ouverts
sources:
  - "[[1 - IA|Cours 1]]"
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un modèle d'IA est **propriétaire** quand son éditeur n'en publie ni les paramètres ni le code : on ne l'utilise qu'à travers son application ou son API. Il est **ouvert** à des degrés divers :

- **Open source au sens strict** : le modèle (ses paramètres), le code et de quoi le reproduire (les données d'entraînement ou une description détaillée de ces données) sont publiés sous une licence qui permet de l'utiliser, l'étudier, le modifier et le redistribuer. L'Open Source Initiative en a donné une définition en 2024 (Open Source AI Definition, OSAID 1.0).
- **Poids ouverts** (*open weights*) : seuls les paramètres appris sont publiés, parfois sous une licence restrictive (limites d'usage commercial, conditions d'utilisation). C'est le cas de la plupart des modèles dits « ouverts » (DeepSeek, Llama, une partie des modèles Mistral).

Intérêts d'un modèle ouvert : exécution locale (par exemple avec l'outil Ollama), confidentialité des données qui ne quittent pas la machine, adaptation par ajustement fin (*fine-tuning*). Limite : il faut une machine puissante (mémoire de la carte graphique) pour faire tourner les grands modèles.

## Dans le cours

[[1 - IA|Cours 1 (IA)]] classe OpenAI, Midjourney, Anthropic et Google (Gemini) parmi les modèles propriétaires (« close source »), et DeepSeek et Mistral parmi les modèles « open source » ; les modèles à poids ouverts de Google forment la famille Gemma. Hugging Face n'est pas un modèle mais une plateforme qui héberge et distribue des modèles ouverts (et des jeux de données). [[Erreurs du cours#^e-modele-d-ia-proprietaire-ou-ouvert|✎]]

Notion parente : [[Licences libres]]. Voir aussi : [[Intelligence artificielle]], [[Creative Commons]], [[Communs numériques]].

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]

Source : [[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]].
