---
type: source
tags:
  - year3
sources:
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]], dans [[Cours/Informatique/IA/_index|IA]]. Les diapositives à texte (listes, tableaux, articles) sont recopiées ; les images d'exemples, le schéma des familles d'IA et la boussole politique sont intégrés.

## Idée générale

Premier cours d'IA, d'orientation pratique : culture générale, façon d'écrire des prompts, grandes familles d'IA, outils, consommation d'énergie, positionnement politique des modèles, et droit d'auteur sur les contenus générés. Beaucoup de chiffres et de noms de produits datent de 2025 et vieillissent vite.

## Éléments de culture générale

Notes de l'étudiant :
- Le terme « [[Intelligence artificielle|intelligence artificielle]] » est proposé à la **[[Conférence de Dartmouth|conférence de Dartmouth]]** en 1956, qui réunit notamment Marvin Minsky, John McCarthy et Claude Shannon.
- Le projet de l'atelier, rédigé en 1955 par John McCarthy, Marvin Minsky, Nathaniel Rochester et Claude Shannon, part de l'hypothèse que tout aspect de l'apprentissage ou de l'intelligence peut, en principe, être décrit assez précisément pour qu'une machine le simule. L'atelier se tient à l'été 1956 au Dartmouth College (New Hampshire) et marque la naissance de l'IA comme discipline. [[Complément hors du cours|ⓘ]]
- Les IA tournent sur des processeurs spécialisés dans le calcul parallèle : surtout des GPU, et des **[[TPU]]** chez Google. [[Erreurs du cours#^e-1-ia|✎]]
- **CPU, GPU, TPU.** Le **CPU** (processeur central) a quelques cœurs puissants et polyvalents, qui enchaînent des tâches variées. Le **[[Processeur graphique|GPU]]** (processeur graphique), conçu pour l'affichage, a des milliers de cœurs simples qui font la même opération en parallèle : c'est exactement ce que demandent les multiplications de matrices des [[Réseau de neurones|réseaux de neurones]]. Le **TPU** (*Tensor Processing Unit*) est un circuit spécialisé conçu par Google, annoncé en 2016, encore plus optimisé pour ces calculs. En pratique, la plupart des modèles sont entraînés et servis sur des GPU (Nvidia surtout) ; les TPU servent surtout aux modèles de Google, comme Gemini. [[Complément hors du cours|ⓘ]]
- **[[Token (IA)|Tokens]] par image** : à chaque requête de génération d'image, l'IA répartit son nombre de tokens. Exemple : pour un portrait, les 50 tokens se concentrent sur la femme ; pour une image de 50 visages, les 50 tokens se répartissent sur les 50 visages, et chaque visage perd en qualité.
- **Ce qu'est un token.** C'est l'unité de base que traite un modèle. En texte, un token est un mot ou un fragment de mot (en anglais, environ quatre caractères en moyenne, selon OpenAI) ; en image, selon le modèle, c'est un petit carré de l'image (*patch*) ou un code d'un vocabulaire visuel. Le nombre de tokens qu'un modèle peut prendre en compte d'un coup s'appelle sa **fenêtre de contexte**, et les services payants facturent au token. Le chiffre de 50 tokens du cours est une image : une image en compte bien plus, selon sa résolution, mais l'idée tient, car la quantité de détail disponible est limitée et se partage entre les éléments représentés. [[Complément hors du cours|ⓘ]]
- **[[Hallucination (IA)|Hallucination]].** Un [[Grand modèle de langage|grand modèle de langage]] produit la suite de texte la plus probable, pas la plus vraie : il peut affirmer avec aplomb des faits, des citations ou des références qui n'existent pas. D'où la règle de vérifier ce qu'il avance, et l'intérêt des outils qui renvoient à leurs sources (Perplexity) ou qui répondent à partir de documents fournis (NotebookLM). [[Complément hors du cours|ⓘ]]
- Le domaine de l'IA serait dominé par la Chine, qui ferait aussi revenir ses chercheurs pour travailler pour elle (affirmation de la note).
- Le rapport *AI Index* 2025 de l'université Stanford nuance : en 2024, les institutions américaines ont produit 40 modèles d'IA jugés marquants, contre 15 pour la Chine et 3 pour l'Europe, mais la Chine publie le plus d'articles et dépose le plus de brevets en IA, et l'écart de performance entre meilleurs modèles américains et chinois s'est fortement réduit. [[Complément hors du cours|ⓘ]]

## Types de prompt

Un prompt efficace, pour le texte comme pour l'image, précise en général : le **rôle** ou le point de vue attendu, le **contexte**, la **tâche**, les **contraintes** et le **format** de la réponse. Donner un ou plusieurs exemples du résultat voulu s'appelle le *few-shot prompting* (sans exemple : *zero-shot*). Un prompt se travaille par itérations : on corrige d'après le résultat obtenu plutôt que d'espérer tout réussir du premier coup. [[Complément hors du cours|ⓘ]]

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

Le **[[JSON]]** (*JavaScript Object Notation*) est un format texte de données structurées : des paires `"clé": valeur` entre accolades, des listes entre crochets, des chaînes entre guillemets doubles, des objets imbriqués les uns dans les autres. Pour un prompt, son intérêt est d'obliger à remplir chaque rubrique (lumière, cadrage, couleurs…) et de servir de gabarit réutilisable : on change une seule valeur pour obtenir une variante. Le modèle le reçoit comme du texte ; le gain tient surtout à la précision et à l'exhaustivité de la description. Une seule faute de syntaxe (un guillemet manquant, une virgule en trop) rend le JSON invalide, ce qui gêne surtout quand un programme doit le lire. [[Complément hors du cours|ⓘ]]

![[Séance 1 - IA - image13.png]]
*Figure : le prompt JSON et l'image obtenue — un homme en t-shirt blanc et jean, appuyé à la rambarde d'un yacht, mer bleue et île rocheuse au loin.*

Structure du prompt de l'exemple (recopié d'après la transcription ; le texte mêle « A old man », un débardeur (*tank top*) et des détails féminins (« her », un bikini), alors que l'image montre un homme jeune en t-shirt) : [[Erreurs du cours#^e-1-ia|✎]]

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

Le prompt négatif est surtout propre aux [[Modèle de diffusion|modèles de diffusion]] (Stable Diffusion et ses dérivés) : à chaque étape de génération, l'image est poussée vers ce que décrit le prompt et éloignée de ce que décrit le prompt négatif. Les assistants conversationnels n'ont souvent pas de champ dédié : on y écrit simplement « sans texte, sans filigrane… » dans le prompt. [[Complément hors du cours|ⓘ]]

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

Ce que recouvrent les familles du schéma : [[Complément hors du cours|ⓘ]]
- **Symbolique** : des humains codent des règles et des connaissances (« si… alors… ») que la machine applique par raisonnement logique. Les décisions sont explicables, mais chaque cas doit être prévu à la main. [[Deep Blue]] (IBM), qui bat le champion du monde Garry Kasparov en 1997, calcule des millions de coups par seconde sans rien apprendre. [[Complément hors du cours|ⓘ]]
- **Connexionniste** : le système règle lui-même ses paramètres à partir d'exemples, avec des réseaux de neurones artificiels. Il traite bien l'image, le son et la langue, mais reste une « boîte noire » difficile à expliquer. [[Complément hors du cours|ⓘ]]
- **Supervisé, non supervisé, par renforcement** : en apprentissage supervisé, les exemples portent la bonne réponse (une photo et son étiquette « chat ») et le modèle apprend à la prédire ; en non supervisé, les données n'ont pas d'étiquette et le modèle y cherche des structures (groupes, régularités) ; par renforcement, un agent apprend par essais et erreurs en recevant des récompenses. AlphaGo (DeepMind) bat en 2016 le joueur de go Lee Sedol ; AlphaGo Zero apprend sans aucune partie humaine, en jouant contre lui-même. [[Complément hors du cours|ⓘ]]
- **[[Hiver de l'IA|Hivers de l'IA]]** : le schéma ne montre pas les deux périodes de désillusion et de chute des financements qui séparent ses étapes, vers 1974-1980 (après le rapport Lighthill de 1973 au Royaume-Uni, très critique) et vers 1987-1993 (effondrement du marché des systèmes experts, trop coûteux à maintenir). [[Complément hors du cours|ⓘ]]
- **Le tournant de 2012** : le réseau convolutif AlexNet remporte le concours de reconnaissance d'images ImageNet avec une avance nette. Trois ingrédients expliquent l'essor de l'apprentissage profond qui suit : de très grands jeux de données, la puissance de calcul des GPU et de meilleurs algorithmes d'entraînement. [[Complément hors du cours|ⓘ]]
- **Transformers** : architecture présentée par Google en 2017 dans l'article « *Attention Is All You Need* ». Son mécanisme d'**attention** permet à chaque token de pondérer l'importance de tous les autres tokens du texte, et le calcul se parallélise bien sur GPU. **GPT** (*Generative Pre-trained Transformer*, OpenAI, 2018) apprend à prédire le token suivant et sert à générer du texte ; **BERT** (Google, 2018) lit la phrase dans les deux sens et sert plutôt à la comprendre (classement, recherche). [[Complément hors du cours|ⓘ]]
- **Grands modèles de langage (LLM)** : des transformers à des milliards de paramètres, pré-entraînés sur d'immenses corpus de texte à prédire le token suivant, puis ajustés pour suivre des instructions et dialoguer. ChatGPT, lancé par OpenAI le 30 novembre 2022, a fait connaître ces modèles au grand public. [[Complément hors du cours|ⓘ]]
- **Modèles de diffusion** : à l'entraînement, on ajoute progressivement du bruit à des images et le réseau apprend à inverser chaque étape ; pour générer, il part d'un bruit pur qu'il débruite pas à pas, guidé par le prompt. Stable Diffusion (2022) travaille sur une version compressée de l'image (espace latent), ce qui le rend utilisable sur une carte graphique grand public. [[Complément hors du cours|ⓘ]]
- **Multimodal** : un modèle multimodal reçoit ou produit plusieurs types de données (texte, image, son, vidéo) ; c'est ce qui permet le prompt avec image de référence vu plus haut. [[Complément hors du cours|ⓘ]]

### IA d'image : Midjourney contre les autres

| Midjourney | Nano Banana, ChatGPT, SeeDream |
|---|---|
| Très « créatif », mais très peu de contrôle | Moins « créatif », mais beaucoup de contrôle |

« Nano Banana » est le surnom du modèle d'image de Gemini (Google, 2025). Intégrés à un assistant conversationnel, ces modèles permettent de corriger une image par instructions successives (« garde le visage, change la veste ») et de tenir compte d'images fournies, d'où le contrôle du tableau. [[Complément hors du cours|ⓘ]]

### IA propriétaires et open source

[[Modèle d'IA propriétaire ou ouvert|Logiciels propriétaires contre open source]], selon la diapositive :

| *Close* (propriétaire) | *Open source* |
|---|---|
| OpenAI — https://openai.com/ | DeepSeek — https://www.deepseek.com/ |
| Midjourney — https://www.midjourney.com/ | Mistral — https://mistral.ai/fr/ |
| Anthropic — https://claude.ai/ | Hugging Face (plateforme qui héberge des modèles ouverts) — https://huggingface.co/ [[Erreurs du cours#^e-1-ia\|✎]] |
| Google (Gemini) — https://gemini.google.com/ [[Erreurs du cours#^e-1-ia\|✎]] | |

Les mots demandent à être précisés : [[Complément hors du cours|ⓘ]]
- **Open source** au sens strict : le modèle, son code et de quoi le reproduire (données ou description détaillée des données d'entraînement) sont publiés sous une licence qui permet de l'utiliser, l'étudier, le modifier et le redistribuer ; l'Open Source Initiative a publié en 2024 une définition de l'IA open source (OSAID 1.0). [[Complément hors du cours|ⓘ]]
- **Poids ouverts** (*open weights*) : la plupart des modèles dits « open source » (DeepSeek, Llama, une partie des modèles Mistral) publient seulement leurs **poids**, les paramètres appris, que l'on peut télécharger et faire tourner chez soi, mais pas leurs données d'entraînement, et parfois sous une licence restrictive. [[Complément hors du cours|ⓘ]]
- **Gemini** est un modèle propriétaire de Google, utilisable seulement en ligne ; les modèles à poids ouverts de Google forment la famille **Gemma**. **Hugging Face** n'est pas un modèle mais une plateforme qui héberge des centaines de milliers de modèles et de jeux de données ouverts. [[Complément hors du cours|ⓘ]]
- Intérêt d'un modèle ouvert : l'exécuter en local, sans que les données quittent la machine, l'adapter à un besoin (*fine-tuning*), ne pas dépendre d'un fournisseur ; limite : il faut une machine puissante, la mémoire de la carte graphique surtout. [[Complément hors du cours|ⓘ]]

### Outils IA

| Usage | Outils (liens du cours) |
|---|---|
| Images | https://www.midjourney.com/app/ ; https://gemini.google.com/app ; https://www.vizcom.ai/ ; https://www.krea.ai/home ; Seedream ; https://quiver.ai/ |
| Animation | https://seed.bytedance.com/ ; https://klingai.com/global/ ; https://hailuoai.video/ ; https://gemini.google/overview/video-generation |
| Texte | https://chat.openai.com/ ; https://gemini.google.com/app ; https://claude.ai ; https://www.perplexity.ai/ ; https://www.deepseek.com/ |
| 3D | https://www.tripo3d.ai/ ; https://www.meshy.ai/ |
| Son | https://suno.com/ ; https://www.udio.com/ ; https://elevenlabs.io/ ; https://artlist.io/voice-over |
| Divers | https://huggingface.co/ ; https://pinokio.computer/ ; https://notebooklm.google.com/ ; https://www.weavy.ai/ ; https://ollama.com/ |

Dans la ligne « Divers », Ollama et Pinokio servent à installer et faire tourner des modèles ouverts sur son propre ordinateur. Dans la ligne « Texte », Perplexity se distingue des autres : c'est un moteur de recherche conversationnel qui cite ses sources. [[Complément hors du cours|ⓘ]]

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

Ces outils servent surtout à trois usages : les **[[Deepfake|deepfakes]]** (hypertrucages : remplacer un visage ou imiter une voix), pour la désinformation, les montages sexuels sans consentement ou l'arnaque au faux dirigeant ; la rédaction automatique d'**hameçonnage** (*phishing*) et de code malveillant ; la génération de contenus interdits par les services grand public. Contourner les garde-fous d'un modèle grand public par un prompt astucieux s'appelle un ***jailbreak***. [[Complément hors du cours|ⓘ]]

En France, la loi du 21 mai 2024 visant à sécuriser et réguler l'espace numérique (loi SREN) punit la diffusion sans consentement d'un montage produit par traitement algorithmique représentant l'image ou les paroles d'une personne, s'il n'apparaît pas à l'évidence qu'il s'agit d'un montage, et plus lourdement les hypertrucages à caractère sexuel (articles 226-8 et 226-8-1 du Code pénal). [[Complément hors du cours|ⓘ]]

Dans l'Union européenne, le **[[Règlement européen sur l'IA|règlement européen sur l'IA]]** (*AI Act*, règlement (UE) 2024/1689) classe les systèmes par niveau de risque : risque inacceptable (interdits, comme la notation sociale des citoyens), haut risque (obligations fortes : recrutement, éducation, santé…), risque limité (obligations de transparence) et risque minimal. Il impose notamment de signaler qu'un contenu est un deepfake et d'indiquer à l'utilisateur qu'il parle à une IA. Il est entré en vigueur le 1er août 2024, avec une application échelonnée : interdictions depuis le 2 février 2025, obligations des modèles d'IA à usage général depuis le 2 août 2025 ; un règlement modificatif (« omnibus numérique » sur l'IA, proposé par la Commission en novembre 2025 et adopté en 2026) a reporté les obligations des systèmes à haut risque à décembre 2027, voire août 2028 pour ceux intégrés à des produits réglementés. [[Complément hors du cours|ⓘ]]

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

Pour lire le tableau : 1 GWh = 1 000 MWh = 1 million de kWh = 1 milliard de Wh. Les équivalences du cours comptent environ 4,3 à 4,6 MWh d'électricité par foyer et par an (1,95 GWh ÷ 450 ≈ 4,3 MWh). Ces chiffres sont des estimations : les entreprises publient rarement la consommation de leurs entraînements. [[Complément hors du cours|ⓘ]]

### Consommation d'énergie pour l'inférence

Voir [[Entraînement et inférence]].

L'**entraînement** est le coût, unique, de la fabrication du modèle ; l'**inférence** est le coût de chaque utilisation. Une requête consomme peu, mais elles se comptent par milliards : sur la durée de vie d'un modèle très utilisé, l'inférence cumulée peut dépasser l'entraînement. Les modèles qui « réfléchissent » longtemps (comme GPT-5 en *Deep Thinking*) génèrent beaucoup plus de tokens, d'où leur consommation par texte bien plus élevée. [[Complément hors du cours|ⓘ]]

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

À l'échelle mondiale, selon le rapport *Energy and AI* de l'Agence internationale de l'énergie (AIE, 2025), les centres de données ont consommé environ 415 TWh d'électricité en 2024, soit environ 1,5 % de la consommation mondiale, et pourraient atteindre environ 945 TWh en 2030, l'IA étant le premier moteur de cette hausse. [[Complément hors du cours|ⓘ]]

L'énergie n'est qu'une partie de l'impact : l'empreinte carbone dépend du mix électrique du pays où tournent les serveurs (faible avec une électricité nucléaire ou renouvelable, forte avec du charbon), les centres de données consomment de l'eau pour se refroidir, et la fabrication des puces et des serveurs pèse aussi (métaux, énergie de fabrication). [[Complément hors du cours|ⓘ]]

### Le nucléaire pour les centres de données (articles cités)

- **Microsoft relance la centrale nucléaire de Three Mile Island** : en relançant l'un des deux réacteurs du site, Microsoft mise sur plus de 800 MW d'électricité, jusqu'en 2054, pour alimenter ses data centers.
- **Google commande des mini-réacteurs nucléaires** : six à sept [[Petit réacteur modulaire|petits réacteurs modulaires]] (SMR) pour ses data centers et bureaux américains ; à long terme, ces réacteurs de nouvelle génération devraient coûter moins cher que les centrales traditionnelles.
- Three Mile Island (Pennsylvanie) est connu pour l'accident de 1979 sur son réacteur 2 (fusion partielle du cœur), le plus grave de l'histoire du nucléaire civil américain. C'est l'autre réacteur, le 1, arrêté en 2019 pour raisons économiques, que l'exploitant Constellation relance pour Microsoft. [[Complément hors du cours|ⓘ]]
- Un petit réacteur modulaire a une puissance d'au plus 300 MW électriques environ (définition de l'Agence internationale de l'énergie atomique), contre environ 900 à 1 650 MW pour un réacteur du parc français ; ses modules sont fabriqués en usine puis assemblés sur site. Le contrat de Google, annoncé en octobre 2024, est passé avec l'entreprise Kairos Power. [[Complément hors du cours|ⓘ]]
- Pourquoi le nucléaire : un centre de données consomme jour et nuit, il lui faut une électricité **pilotable** (disponible à la demande, contrairement au solaire et à l'éolien) et bas carbone, pour tenir les engagements climatiques de ces entreprises. [[Complément hors du cours|ⓘ]]

## Politique des IA

![[Séance 1 - IA - image22.png]]
*Figure : [[Biais politique des IA|positionnement politique des IA]] en 2025, sur une boussole politique (axe vertical autoritaire / libertaire, axe horizontal gauche / droite économique).*

| Quadrant | IA placées |
|---|---|
| Autoritaire de gauche | Qwen-Max (Alibaba), ERNIE Bot 4 (Baidu) |
| Libertaire de gauche (près du centre) | Claude 4, Mistral Large 2, ChatGPT (o1/o3), Gemini 2.5, Llama 3.1 |
| Libertaire de droite | Perplexity (près du centre), Grok 3 (loin, vers le coin) |
| Autoritaire de droite | — |

La boussole politique (*Political Compass*, test en ligne lancé en 2001) croise deux axes au lieu du seul clivage gauche-droite : l'économie (intervention de l'État contre marché libre) et les libertés (autorité contre liberté individuelle). Appliquée aux IA, la mesure reste fragile : une même IA répond différemment selon la formulation, la langue et la version du modèle. [[Complément hors du cours|ⓘ]]

**Comment mesurer l'orientation d'une IA** (note) : l'orientation dépend du corpus d'entraînement et de la manière dont les chercheurs recadrent l'IA pendant l'entraînement. On lui pose beaucoup de questions (entre 5 000 et 100 000), puis on détermine son spectre politique d'après les mots employés, les tournures de phrase et les idées proposées.

Le « recadrage » dont parle la note s'appelle l'**alignement**. Après le pré-entraînement sur le corpus, on ajuste le modèle avec des exemples de bonnes réponses rédigés par des humains, puis par **[[Apprentissage par renforcement à partir de retours humains|apprentissage par renforcement à partir de retours humains]]** (RLHF) : des annotateurs comparent plusieurs réponses, un modèle de récompense apprend leurs préférences, et le modèle est entraîné à produire les réponses préférées. Les consignes données aux annotateurs et le **prompt système** (instructions cachées ajoutées par l'éditeur avant chaque conversation) pèsent donc sur les positions de l'IA, autant que le corpus. [[Complément hors du cours|ⓘ]]

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
  - La décision *Thaler v. Perlmutter* a été confirmée en appel en mars 2025 par la cour d'appel fédérale du district de Columbia : le droit d'auteur américain exige un auteur humain. [[Complément hors du cours|ⓘ]]
  - États-Unis, bande dessinée *Zarya of the Dawn* (février 2023) : le Copyright Office protège le texte de l'autrice ainsi que le choix et l'agencement des images, mais pas les images elles-mêmes, produites avec Midjourney. C'est la logique des diapositives : seule la part de contrôle humain est protégée. [[Complément hors du cours|ⓘ]]
- **En droit français**, l'auteur d'une œuvre de l'esprit en a la propriété « du seul fait de sa création » (article L111-1 du Code de la propriété intellectuelle), sans dépôt ni formalité. Les juges exigent que l'œuvre soit **originale**, c'est-à-dire qu'elle porte l'empreinte de la personnalité de son auteur, ce qui suppose un auteur humain. Le droit d'auteur réunit un **droit moral** (paternité, respect de l'œuvre : perpétuel) et des **droits patrimoniaux** (reproduction, représentation : jusqu'à 70 ans après la mort de l'auteur, article L123-1), après quoi l'œuvre entre dans le [[Domaine public|domaine public]]. [[Complément hors du cours|ⓘ]]
- **Les données d'entraînement** posent l'autre question : a-t-on le droit d'entraîner une IA sur des œuvres protégées ? Dans l'Union européenne, la directive (UE) 2019/790 autorise la **fouille de textes et de données** (*text and data mining*) sur des contenus accessibles légalement, sauf si l'ayant droit s'y est opposé de façon appropriée (*opt-out*, par exemple par une mention lisible par machine). Le règlement européen sur l'IA oblige en outre les fournisseurs de modèles d'IA à usage général à respecter ces oppositions et à publier un résumé du contenu utilisé pour l'entraînement. [[Complément hors du cours|ⓘ]]

### IA « sûres » quant aux données d'entraînement

| Outil | Données d'entraînement |
|---|---|
| Adobe Firefly | Exclusivement Adobe Stock, contenus libres de droits et [[Domaine public\|domaine public]] ; Adobe promet une utilisation « commercialement sûre » |
| [[IA générative\|Generative AI]] by Getty Images / iStock | Modèle Nvidia Edify nourri par la photothèque Getty |
| Shutterstock + DALL·E 3 | L'outil Design Assistant s'appuie sur les clichés Shutterstock et offre un « bouclier juridique » à la demande |
| Bria.ai | Start-up israélo-new-yorkaise ; un milliard d'images intégralement sous licence, auprès d'une vingtaine de partenaires (dont Getty) |
| Public Diffusion | Projet open source, uniquement domaine public et CC0 ; encore en bêta |
| Tongyi Wanxiang / Wan 2.1 (Alibaba Cloud) | Corpus mixtes sous licence (Alibaba Stock, domaine public) ; accords sectoriels (e-commerce, automobile) |

**CC0** est l'outil de [[Creative Commons]] par lequel un auteur renonce à tous ses droits sur une œuvre, dans la mesure où la loi le permet : l'œuvre se réutilise alors librement, comme si elle était dans le domaine public. Une IA entraînée seulement sur ces contenus, ou sur des contenus sous licence, limite le risque qu'une image générée reproduise une œuvre protégée. [[Complément hors du cours|ⓘ]]

Le cours ne contient pas d'exercice.
