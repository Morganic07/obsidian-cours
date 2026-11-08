---
type: concept
tags: [year3]
aliases: [RLHF, reinforcement learning from human feedback, alignement (IA), alignement des IA]
sources: ["[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'apprentissage par renforcement à partir de retours humains (RLHF, *reinforcement learning from human feedback*) est une étape d'ajustement d'un [[Grand modèle de langage|grand modèle de langage]] après son pré-entraînement, qui lui apprend à produire les réponses que des humains préfèrent. Elle se déroule en quatre temps :

1. **Ajustement supervisé** : le modèle pré-entraîné est entraîné sur des exemples de bonnes réponses rédigés par des humains (questions et réponses modèles).
2. **Collecte des préférences** : pour une même question, le modèle produit plusieurs réponses, que des annotateurs comparent et classent de la meilleure à la moins bonne.
3. **Modèle de récompense** : un second modèle apprend, à partir de ces classements, à prédire quelle réponse un humain préférerait ; il attribue un score à toute réponse.
4. **Renforcement** : le modèle de langage est entraîné par [[Apprentissage par renforcement|apprentissage par renforcement]] à maximiser ce score, en général avec une pénalité qui l'empêche de trop s'éloigner du modèle de départ.

C'est l'un des outils de l'**alignement** : rendre le modèle utile, honnête et inoffensif selon les critères fixés par son éditeur. Les consignes données aux annotateurs, avec le prompt système (instructions cachées ajoutées avant chaque conversation), influencent donc les positions du modèle autant que son corpus d'entraînement : voir [[Biais politique des IA]].

## Dans le cours

Le cours ne la nomme pas. La note sur l'orientation politique des IA, dans [[1 - IA]], parle de la manière dont les chercheurs « recadrent » l'IA pendant l'entraînement : c'est ce recadrage que désigne l'alignement, présenté dans les compléments de la fiche.

Voir aussi : [[Apprentissage par renforcement]], [[Grand modèle de langage]], [[Biais politique des IA]], [[Entraînement et inférence]], [[Prompt (IA)]], [[Hallucination (IA)]]

Résumés : [[1 - IA]]
