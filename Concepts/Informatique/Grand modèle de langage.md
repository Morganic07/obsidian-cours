---
type: concept
tags: [year3]
aliases: [LLM, large language model, large language models, grands modèles de langage]
sources: ["[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un grand modèle de langage (LLM, *large language model*) est un modèle d'[[Apprentissage profond|apprentissage profond]] à architecture [[Transformer (IA)|transformer]], qui compte des milliards de paramètres.

- **Pré-entraînement** : le modèle apprend, sur un immense corpus de texte, à prédire le [[Token (IA)|token]] suivant d'une séquence.
- **Ajustement (alignement)** : il est ensuite entraîné à suivre des instructions et à dialoguer, notamment par apprentissage par renforcement à partir de retours humains (RLHF, *reinforcement learning from human feedback* ; voir [[Apprentissage par renforcement]]) : des humains classent ses réponses, et le modèle est ajusté pour produire celles qu'ils préfèrent.
- **Génération** : il produit sa réponse token par token, en choisissant à chaque pas une suite probable. Il vise donc le plausible, pas le vrai, d'où le risque d'[[Hallucination (IA)|hallucination]].
- **Exemples** : GPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta), Mistral, DeepSeek, Qwen (Alibaba). Certains sont fermés, d'autres diffusent leurs poids (voir [[Modèle d'IA propriétaire ou ouvert]]).
- **Grand public** : ChatGPT, lancé par OpenAI le 30 novembre 2022, a fait connaître ces modèles du grand public.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[1 - IA]] (historique de l'IA, hallucinations), qui cite aussi plusieurs de ces outils (ChatGPT, Gemini, Claude, DeepSeek).

Voir aussi : [[IA générative]], [[Token (IA)]], [[Transformer (IA)]], [[Prompt (IA)]], [[Intelligence artificielle]].

Résumés : [[1 - IA]]
