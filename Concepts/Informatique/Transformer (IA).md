---
type: concept
tags:
  - year3
aliases:
  - architecture transformer
  - transformers 2017
  - Attention Is All You Need
matieres:
  - IA
sources:
  - "[[1 - IA|Cours 1]]"
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : architecture de [[Réseau de neurones|réseau de neurones]] présentée par des chercheurs de Google en 2017 dans l'article « Attention Is All You Need ». Son mécanisme d'**attention** permet à chaque [[Token (IA)|token]] de la séquence de pondérer l'importance de tous les autres tokens pour construire sa représentation. Dans l'attention dite « produit scalaire normalisé », chaque token produit une requête $Q$, une clé $K$ et une valeur $V$, et :

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V$$

où $d_k$ est la dimension des clés. Plusieurs attentions calculées en parallèle forment l'attention multi-têtes ; un encodage de position ajoute l'ordre des tokens, que l'attention seule ignore.

Le transformer remplace les [[Réseau de neurones récurrent|réseaux récurrents]], qui lisent la séquence token par token : il traite toute la séquence d'un coup, ce qui se parallélise bien sur GPU et permet d'entraîner des modèles bien plus grands.

- **GPT** (Generative Pre-trained Transformer, OpenAI, 2018) : n'utilise que le décodeur, prédit le token suivant pour générer du texte.
- **BERT** (Google, 2018) : n'utilise que l'encodeur et lit le texte dans les deux sens, pour le comprendre (classement, recherche).

C'est la base des [[Grand modèle de langage|grands modèles de langage]].

## Dans le cours

Nommé dans [[1 - IA|Cours 1 (IA)]] sans définition : famille de l'apprentissage profond (2017), à laquelle le schéma du cours rattache BERT et GPT.

Notion parente : [[Apprentissage profond]].

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]
