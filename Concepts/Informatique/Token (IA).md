---
type: concept
tags:
  - year3
aliases:
  - tokens d'image
  - token d'image
  - fenêtre de contexte
  - context window
matieres:
  - IA
sources:
  - "[[1 - IA|Cours 1]]"
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le token est l'unité de base que traite un modèle d'IA. En texte, c'est un mot ou un fragment de mot (en anglais, environ quatre caractères en moyenne, selon OpenAI) ; en image, selon le modèle, c'est un petit carré de l'image (*patch*) ou un code d'un vocabulaire visuel. Un [[Grand modèle de langage|grand modèle de langage]] lit et génère du texte token par token.

- **Fenêtre de contexte** : nombre maximal de tokens qu'un modèle peut prendre en compte d'un coup (la consigne, les documents fournis, la conversation et sa réponse). Au-delà, le début est oublié ou tronqué.
- **Coût** : les services payants facturent à l'usage, au nombre de tokens en entrée et en sortie.

Explication imagée de [[1 - IA|Cours 1 (IA)]] : une IA d'image répartit un nombre fixe de tokens. Un portrait les concentre sur un seul visage ; avec 50 visages, ils se dispersent et chaque visage perd en qualité.

Les « 50 tokens » du cours sont une image (complément, hors du cours) : le nombre réel de tokens d'une image dépend de sa résolution et du modèle, mais l'idée tient, car la quantité de détail disponible reste limitée et se partage entre les éléments représentés.

Voir aussi : [[Prompt (IA)]], [[Grand modèle de langage]], [[Transformer (IA)]].

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]
