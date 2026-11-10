---
type: concept
tags: [year4]
aliases: [Contrastive Language-Image Pre-training]
sources: ["[[Raw/Year 4/SHS/Prise de note SHS.docx|Prise de note SHS.docx]]"]
maj: 2026-11-10
---

**Définition (complément, hors du cours)** : CLIP (*Contrastive Language-Image Pre-training*) est un modèle publié par OpenAI en 2021, entraîné sur environ 400 millions de paires image-texte à rapprocher les représentations d'une image et de la phrase qui la décrit, et à éloigner celles des paires qui ne vont pas ensemble. Il sait ainsi mesurer à quel point une légende correspond à une image, sans avoir été entraîné sur des catégories fixées à l'avance. Ce score sert à filtrer des [[Jeu de données d'entraînement|jeux de données]] collectés sur le web et à guider des modèles de génération d'images ([[IA générative]]).

## Dans le cours

Nommé dans [[6 - design libre]] : [[LAION-5B]] est formé de paires image-texte filtrées à l'aide de CLIP.

Voir aussi : [[Apprentissage profond]], [[LAION-5B]].

Résumés : [[6 - design libre]]
