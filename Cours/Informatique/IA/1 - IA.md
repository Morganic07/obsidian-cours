---
type: source
tags:
  - year3
sources:
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]], dans [[Cours/Informatique/IA/_index|IA]]. En cas d'écart, le cours et ses images font foi. Les diapositives à texte (listes, tableaux, articles) sont recopiées ; les images d'exemples, le schéma des familles d'IA et la boussole politique sont intégrés.

## Idée générale

Premier cours d'IA, d'orientation pratique : culture générale, façon d'écrire des prompts, grandes familles d'IA, outils, consommation d'énergie, positionnement politique des modèles, et droit d'auteur sur les contenus générés. Beaucoup de chiffres et de noms de produits datent de 2025 et vieillissent vite.

## Éléments de culture générale

Notes de l'étudiant :
- Le terme « [[Intelligence artificielle|intelligence artificielle]] » est proposé à la **[[Conférence de Dartmouth|conférence de Dartmouth]]** en 1956, qui réunit notamment Marvin Minsky, John McCarthy et Claude Shannon.
- « Les IA sont basées sur des **[[TPU]]**, pas des CPU ou GPU » (affirmation de la note).
- **[[Token (IA)|Tokens]] par image** : à chaque requête de génération d'image, l'IA répartit son nombre de tokens. Exemple : pour un portrait, les 50 tokens se concentrent sur la femme ; pour une image de 50 visages, les 50 tokens se répartissent sur les 50 visages, et chaque visage perd en qualité.
- Le domaine de l'IA serait dominé par la Chine, qui ferait aussi revenir ses chercheurs pour travailler pour elle (affirmation de la note).

## Types de prompt

### 1. Prompt textuel détaillé

Exemple de [[Prompt (IA)|prompt]] du cours :

```text
A hyper-realistic close-up portrait of a woman with long hair, looking at the camera,
soft natural morning window light, standing in a modern kitchen. Shot on Sony A7R IV,
85mm f/1.8 lens, incredibly detailed skin texture, cinematic lighting, photorealistic,
8k, depth of field
```

Le prompt décrit le sujet, la pose, la lumière, le lieu, l'appareil et l'objectif, la texture, le style et la résolution.

![[Séance 1 - IA - image19.png]]
*Figure : résultat du prompt — portrait photoréaliste d'une jeune femme en lumière de fenêtre, cuisine floue en arrière-plan.*

### 2. Prompt avec image de référence (sur Gemini)

Prompt : « Dessine-moi une image photo réaliste d'une femme habillée avec les éléments que tu as dans cette planche de style. »

![[Séance 1 - IA - image17.png]]
*Figure : à gauche, la planche de style (sac, lunettes, bijoux dorés, pull col roulé beige, pantalon en cuir, ceinture, col en fourrure, palette taupe / caramel / orange brûlé / marron) ; à droite, la photo générée d'une femme portant la tenue dans la rue.*

### 3. Prompt au format JSON

On peut écrire un prompt sous forme de **fichier JSON**, car les IA le comprennent mieux. On peut utiliser une IA pour rédiger ce JSON.

![[Séance 1 - IA - image13.png]]
*Figure : le prompt JSON et l'image obtenue — un homme en t-shirt blanc et jean, appuyé à la rambarde d'un yacht, mer bleue et île rocheuse au loin.*

Structure du prompt de l'exemple (recopié d'après la transcription, texte tel quel, incohérences comprises) :

```json
{
  "lighting": {
    "source": "Direct, bright sunlight",
    "shadows": "Defined shadows are cast on the deck, the subject's body, and the yacht structure.",
    "direction": "From the upper right, creating strong highlights and deep shadows",
    "intensity": "High contrast, hard light"
  },
  "background": {
    "depth": "Considerable depth of field, with the background elements clearly distinguishable.",
    "setting": "The deck of a luxury yacht on a sunny day.",
    "elements": [
      "White fiberglass yacht structure",
      "Stainless steel railing",
      "Teak wood deck planks",
      "A white staircase on the left leading to an upper deck",
      "Vast blue sea with small waves",
      "A rocky, rugged island or coastline in the distance on the right",
      "Clear blue sky",
      "Another small boat visible on the horizon"
    ]
  },
  "composition": {
    "focus": "Sharp focus on the subject, with a slight blur in the distant background elements.",
    "framing": "The subject is positioned on the left side of the frame, with the yacht's deck and railing leading into the distance on the right. The horizon line is visible in the upper third.",
    "shot_type": "Medium-long shot",
    "camera_angle": "Slightly low-angle, looking up at the subject"
  },
  "color_profile": {
    "mood": "Bright, sunny, and summery.",
    "accent_colors": { "tan": "#D2B48C", "gold": "#FFD700" },
    "color_palette": "A high-contrast palette dominated by the cool blues of the water and sky, contrasted with the stark white of the yacht and tank top, and the warm red of the bikini.",
    "dominant_colors": { "red": "#DC143C", "blue": "#0047AB", "brown": "#A52A2A", "white": "#FFFFFF" }
  },
  "technical_specs": {
    "medium": "Photograph",
    "resolution": "High, with sharp detail",
    "camera_type": "Digital camera",
    "aspect_ratio": "2:3 (portrait orientation)"
  },
  "subject_analysis": {
    "hair": "Dark, shoulder-length, tousled hair with sun-kissed highlights, partially covering her face.",
    "pose": "Standing, leaning slightly against the yacht railing with her right hand on her hip and left hand holding the edge of her white tank top. Her body is angled towards the left, head turned to look over her left shoulder.",
    "clothing": { "top": "A white, teeshirt.", "bottom": "A jeans." },
    "skin_tone": "Fair",
    "expression": "Thoughtful or contemplative, looking towards the distance.",
    "accessories": "A thin gold bracelet on her left wrist.",
    "main_subject": "A old man"
  },
  "artistic_elements": {
    "style": "Candid, naturalistic photography",
    "texture": "Smooth fiberglass, ribbed tank top fabric, wooden deck, rippled water",
    "contrast": "High tonal contrast between the brightly lit areas and the shadowed sections."
  },
  "generation_parameters": {
    "prompt": "A candid photograph of a young man with tousled dark hair, wearing a white tank, leaning against the railing on the deck of a luxury yacht. He is looking over her shoulder towards a rocky island across the blue sea under a clear sky. The sunlight is bright and direct, casting defined shadows. The shot is medium-long and slightly low-angle.",
    "negative_prompt": "Blurry, grainy, artificial lighting, studio setting, text, watermark, painting, illustration, low resolution, overcast."
  }
}
```

Les rubriques à retenir : éclairage (`lighting`), arrière-plan (`background`), composition, profil de couleur (`color_profile`, avec codes hexadécimaux), spécifications techniques, analyse du sujet, éléments artistiques, et paramètres de génération avec un **prompt négatif** (`negative_prompt` : ce qu'on ne veut pas voir). La note contient une seconde capture du même JSON, coupée après la liste `elements`.

## Les différentes IA

### Histoire et familles d'IA

![[Séance 1 - IA - image9.png]]
*Figure : schéma des familles d'IA — précurseurs en haut, approche symbolique à gauche, connexionniste à droite, hybride en bas.*

Contenu du schéma (voir [[Approche symbolique et connexionniste]]) :

- **Précurseurs (1943-1956)** : [[Neurone de McCulloch-Pitts|neurone de McCulloch-Pitts]] (1943), [[Cybernétique]] de Norbert Wiener (1948), [[Test de Turing]] (1950), [[Perceptron]] (1958).
- **IA symbolique (1950-1970)** : [[Logic Theorist]] (1955), [[ELIZA|Eliza]] (1966), [[Système expert|systèmes experts]], [[Deep Blue]] (1997).
- **IA connexionniste (1980…)** : [[Apprentissage automatique|machine learning]] :
  - [[Apprentissage supervisé|supervisé]] → [[Apprentissage profond|deep learning]] :
    - [[Réseau de neurones convolutif|réseaux convolutifs]] ;
    - [[Réseau de neurones récurrent|réseaux récurrents]] ;
    - [[Transformer (IA)|transformers]] (2017) → BERT, GPT ;
    - [[Modèle de diffusion|modèles de diffusion]] (2020) → Stable Diffusion → Midjourney ;
  - [[Apprentissage non supervisé|non supervisé]] ;
  - [[Apprentissage par renforcement|par renforcement]] → [[AlphaGo Zero]] (2017).
- **IA hybride (2000…)** : [[IA hybride|systèmes multimodaux]], neuro-symbolique.

### IA d'image : Midjourney contre les autres

| Midjourney | Nano Banana, ChatGPT, SeeDream |
|---|---|
| Très « créatif », mais très peu de contrôle | Moins « créatif », mais beaucoup de contrôle |

### IA propriétaires et open source

[[Modèle d'IA propriétaire ou ouvert|Logiciels propriétaires contre open source]], selon la diapositive :

| *Close* (propriétaire) | *Open source* |
|---|---|
| OpenAI — https://openai.com/ | DeepSeek — https://www.deepseek.com/ |
| Midjourney — https://www.midjourney.com/ | Mistral — https://mistral.ai/fr/ |
| Anthropic — https://claude.ai/ | Google — https://gemini.google.com/ |
| | Hugging Face — https://huggingface.co/ |

### Outils IA

| Usage | Outils (liens du cours) |
|---|---|
| Images | https://www.midjourney.com/app/ ; https://gemini.google.com/app ; https://www.vizcom.ai/ ; https://www.krea.ai/home ; Seedream ; https://quiver.ai/ |
| Animation | https://seed.bytedance.com/ ; https://klingai.com/global/ ; https://hailuoai.video/ ; https://gemini.google/overview/video-generation |
| Texte | https://chat.openai.com/ ; https://gemini.google.com/app ; https://claude.ai ; https://www.perplexity.ai/ ; https://www.deepseek.com/ |
| 3D | https://www.tripo3d.ai/ ; https://www.meshy.ai/ |
| Son | https://suno.com/ ; https://www.udio.com/ ; https://elevenlabs.io/ ; https://artlist.io/voice-over |
| Divers | https://huggingface.co/ ; https://pinokio.computer/ ; https://notebooklm.google.com/ ; https://www.weavy.ai/ ; https://ollama.com/ |

**Conseils d'usage** (diapositive) :
- générer des images comme avec Midjourney : essayer Meta AI, « qui a les mêmes algorithmes » → https://meta.ai/ ;
- travailler sur une très grande masse de contenus, faire des présentations, des cartes mentales → https://notebooklm.google.com/ ;
- générer des images parfaitement contrôlables (Nano Banana) → https://gemini.google.com/app ;
- outil très précis et professionnel pour designers → https://vizcom.com/ ;
- tester des milliers de nouveaux modèles open source sans les installer → https://huggingface.co/.

### IA à usage malveillant

Les « [[IA malveillante|IA maléfiques]] » (note : par exemple Dark GPT, entraîné sur le darknet). Noms cités par la diapositive :

| | | |
|---|---|---|
| Candy ai | civitai | DarkBert |
| DeepSwap | MyEdit | Dark GPT |
| Onlyfakes | Lensa AI | ReFace |
| FraudGPT | [[Deepfake\|DeepFake]] bot | FakeMe |
| Wolf GPT | Zao | XXXGPT |

## Point énergétique

Voir [[Consommation énergétique de l'IA]].

### Consommation d'énergie pour l'entraînement

| Modèle | Énergie | Équivalent |
|---|---|---|
| DeepSeek-V3 | ~1,95 GWh | ~450 foyers français / an |
| Mistral (Large 2) | ~4,5 GWh | ~1 000 foyers français / an |
| Llama 3 (70B) | ~6,4 GWh | ~1 500 foyers français / an |
| Claude 3.5 | ~35 GWh | ~7 800 foyers français / an |
| GPT-4 | ~50-60 GWh | ~12 000 foyers français / an |
| GPT-5 | ~80-100 GWh | ~20 000 foyers français / an |

### Consommation d'énergie pour l'inférence

Voir [[Entraînement et inférence]].

| Usage | Consommation |
|---|---|
| Recherche Google sans IA | 0,1 - 0,3 Wh / texte |
| DeepSeek-V3 | 0,15 Wh / texte |
| Nano Banana 2 | 0,24 Wh / image |
| Nano Banana (Pro) | 0,8 Wh / image |
| FLUX 2.0 | 1,8 Wh / image |
| GPT-5 (Deep Thinking) | 15 à 20 Wh / texte |
| 1 h de jeu vidéo (PC) | 450 Wh (→ 1 865 images avec Nano Banana 2) |
| 1 h de jeu vidéo (PC 5090) / micro-ondes | 1 090 Wh (→ 4 541 images avec Nano Banana 2) |
| 1 h de PlayStation 5 ou Netflix sur TV | 210 Wh |
| 1 h de route en Tesla à 130 km/h | 23 400 Wh (→ 97 500 images avec Nano Banana 2) |

### Le nucléaire pour les centres de données (articles cités)

- **Microsoft relance la centrale nucléaire de Three Mile Island** : en relançant l'un des deux réacteurs du site, Microsoft mise sur plus de 800 MW d'électricité, jusqu'en 2054, pour alimenter ses data centers.
- **Google commande des mini-réacteurs nucléaires** : six à sept [[Petit réacteur modulaire|petits réacteurs modulaires]] (SMR) pour ses data centers et bureaux américains ; à long terme, ces réacteurs de nouvelle génération devraient coûter moins cher que les centrales traditionnelles.

## Politique des IA

![[Séance 1 - IA - image22.png]]
*Figure : [[Biais politique des IA|positionnement politique des IA]] en 2025, sur une boussole politique (axe vertical autoritaire / libertaire, axe horizontal gauche / droite économique).*

| Quadrant | IA placées |
|---|---|
| Autoritaire de gauche | Qwen-Max (Alibaba), ERNIE Bot 4 (Baidu) |
| Libertaire de gauche (près du centre) | Claude 4, Mistral Large 2, ChatGPT (o1/o3), Gemini 2.5, Llama 3.1 |
| Libertaire de droite | Perplexity (près du centre), Grok 3 (loin, vers le coin) |
| Autoritaire de droite | — |

**Comment mesurer l'orientation d'une IA** (note) : l'orientation dépend du corpus d'entraînement et de la manière dont les chercheurs recadrent l'IA pendant l'entraînement. On lui pose beaucoup de questions (entre 5 000 et 100 000), puis on détermine son spectre politique d'après les mots employés, les tournures de phrase et les idées proposées.

**Biais par origine** (diapositive) :

| Origine | Biais | Particularité |
|---|---|---|
| Californiens (OpenAI, Anthropic, Google) | Le « *safetyism* » puritain : refus de répondre aux questions jugées « sensibles » (médical, légal, survie) par peur du risque juridique | Vision : le monde est riche, connecté et sûr |
| Européens (Mistral AI) | L'efficacité « *no bullshit* » | Souvent moins moralisateurs : ils répondent sans « leçon d'éthique de 3 paragraphes » |
| Asiatiques (Qwen, DeepSeek) | Alignement culturel et politique très spécifique | Excellence technique surprenante en mathématiques et en code |

## IA et copyright

Diapositives d'une avocate spécialisée (voir [[Droit d'auteur et IA]]).

### Création générée par prompts textuels

Prompt de l'exemple :

```text
professional photo, bespectacled cat in a robe reading the Sunday newspaper and smoking a pipe,
foggy, wet, stormy, 70mm, cinematic, highly detailed wood, cinematic lighting, intricate,
sharp focus, medium shot, (centered image composition), (professionally color graded),
((bright soft diffused light)), volumetric fog, hdr 4k, 8k, realistic
```

*Image du cours, non reprise (elle porte le logo nominatif de l'intervenante) : le prompt et son résultat — chat à lunettes, en robe de chambre, fumant la pipe et lisant le journal dans une ambiance brumeuse.*

🔴 Les créations fondées seulement sur des prompts textuels ne peuvent pas être protégées par le copyright : on estime que l'auteur n'a pas assez de contrôle sur le processus créatif.

### Retouches d'un contenu généré

*Image du cours, non reprise (logo nominatif de l'intervenante) : un même paysage peint ; une zone sélectionnée y devient une montgolfière, puis un château.*

🟠 Les outils qui permettent de modifier les outputs (chez Midjourney, *vary region* et *remix mode*) peuvent démontrer, au cas par cas, le contrôle humain du processus créatif.

### Création générée à partir d'éléments de référence

Prompt : « a young cyborg woman (((roses))) flowers coming out of her head, photorealism, cinematic lighting, hyper realism, 8k, hyper detailed. »

*Image du cours, non reprise (logo nominatif de l'intervenante) : trois colonnes — le prompt, l'input (dessin au trait d'un visage fleuri) et l'output (visage photoréaliste dont sortent des roses rouges).*

🟢 La protection par copyright des éléments de référence intégrés dans l'output est possible.
🚩 Seulement si vous êtes titulaire des droits sur ces éléments de référence.

### Se protéger

Le droit sur la protection des outputs est en construction. Pour se protéger :
- ✅ identifier les contenus susceptibles d'être protégés ;
- ✅ conserver des preuves du contrôle du processus créatif (pas uniquement les prompts !).

### Principes et jurisprudence

- **Le droit d'auteur ne protège pas les idées, mais les réalisations de formes.** On protège une création précise, pas une manière de créer. En général, la [[Propriété intellectuelle|propriété intellectuelle]] ne permet pas de réserver des idées, méthodes ou théories, seulement leur traduction dans l'univers sensible des formes.
- **Les images générées sont-elles protégées ?**
  - États-Unis, affaire *Thaler v. Perlmutter* (2023) : un juge a tranché que les œuvres générées par une IA ne peuvent pas être protégées par le droit d'auteur.
  - Chine, 27 novembre 2023 : la Beijing Internet Court a reconnu qu'une image générée uniquement par IA pouvait être protégée, en estimant que l'investissement intellectuel de l'auteur du prompt était suffisant.

### IA « sûres » quant aux données d'entraînement

| Outil | Données d'entraînement |
|---|---|
| Adobe Firefly | Exclusivement Adobe Stock, contenus libres de droits et [[Domaine public\|domaine public]] ; Adobe promet une utilisation « commercialement sûre » |
| [[IA générative\|Generative AI]] by Getty Images / iStock | Modèle Nvidia Edify nourri par la photothèque Getty |
| Shutterstock + DALL·E 3 | L'outil Design Assistant s'appuie sur les clichés Shutterstock et offre un « bouclier juridique » à la demande |
| Bria.ai | Start-up israélo-new-yorkaise ; un milliard d'images intégralement sous licence, auprès d'une vingtaine de partenaires (dont Getty) |
| Public Diffusion | Projet open source, uniquement domaine public et CC0 ; encore en bêta |
| Tongyi Wanxiang / Wan 2.1 (Alibaba Cloud) | Corpus mixtes sous licence (Alibaba Stock, domaine public) ; accords sectoriels (e-commerce, automobile) |

Le cours ne contient pas d'exercice.

## Erreurs du cours

- Le prompt JSON de [[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]] écrit `« technical_specs": {` ; il faut `"technical_specs": {` : tel quel, l'exemple n'est pas un JSON valide (guillemet rétabli dans le bloc de cette fiche). Le texte du JSON décrit aussi « bikini », « her », « A old man » et « tank top », alors que l'image générée montre un homme jeune en t-shirt.
