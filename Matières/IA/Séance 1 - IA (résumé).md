---
type: source
tags:
  - year3
sources:
  - "[[Cours/Year 3/IA/Cours 1|Cours 1 (IA)]]"
maj: 2026-11-05
---

Résumé de [[Cours/Year 3/IA/Cours 1|Cours 1 (IA)]], dans [[IA (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Premier cours d'IA, d'orientation pratique : culture générale, façon d'écrire des prompts, grandes familles d'IA, outils, consommation d'énergie, positionnement politique des modèles, et droit d'auteur sur les contenus générés. Beaucoup de chiffres et de noms de produits datent de 2025 et vieillissent vite.

## Contenu, dans l'ordre du cours

- **Culture générale** (notes de l'étudiant) : le terme « intelligence artificielle » est proposé à la conférence de Dartmouth en 1956 (Minsky, McCarthy, Shannon, entre autres). Le cours affirme que les IA reposent sur des TPU et non des CPU ou GPU. Pour l'image, une IA répartit un nombre fixe de « tokens » : un portrait les concentre sur un visage, 50 visages les dispersent et chacun perd en qualité. Le cours dit aussi que le domaine est dominé par la Chine.
- **Types de prompt** : un prompt de texte détaillé (style de photo, éclairage, objectif, résolution) ; un prompt avec image de référence (planche de style, dans Gemini) ; un prompt sous **fichier JSON**, que les IA comprennent mieux et qu'une IA peut aussi rédiger. L'exemple JSON décrit éclairage, arrière-plan, composition, profil de couleur, spécifications techniques, sujet, éléments artistiques et paramètres de génération (dont un `negative_prompt`).
- **Histoire et familles d'IA** (schéma du cours, voir [[Approche symbolique et connexionniste]]) : précurseurs 1943 à 1956 (neurone de McCulloch-Pitts 1943, [[Cybernétique]] de Wiener 1948, test de Turing 1950, perceptron 1958) ; approche symbolique 1950 à 1970 (Logic Theorist 1955, Eliza 1966, systèmes experts, Deep Blue 1997) ; approche connexionniste dès 1980 (apprentissage supervisé, non supervisé, par renforcement avec AlphaGo Zero 2017 ; apprentissage profond avec réseaux convolutifs, récurrents, transformers 2017 dont BERT et GPT, modèles de diffusion 2020 dont Stable Diffusion et Midjourney) ; hybride dès 2000 (systèmes multimodaux, neuro-symbolique).
- **IA d'image** : Midjourney est très « créatif » mais peu contrôlable ; Nano Banana, ChatGPT et SeeDream sont moins créatifs mais beaucoup plus contrôlables.
- **Propriétaire ou ouvert** : le cours classe OpenAI, Midjourney et Anthropic en propriétaire ; DeepSeek, Mistral, Google (Gemini) et Hugging Face en « open source ».
- **Outils** (listes de sites) : images (Midjourney, Gemini, Vizcom, Krea, Seedream, Quiver), animation (Seed, Kling, Hailuo, Gemini video), texte (ChatGPT, Gemini, Claude, Perplexity, DeepSeek), 3D (Tripo, Meshy), son (Suno, Udio, ElevenLabs, Artlist), divers (Hugging Face, Pinokio, NotebookLM, Weavy, Ollama). Conseils d'usage : Meta AI pour des images façon Midjourney, NotebookLM pour une très grande masse de contenus, Gemini pour des images très contrôlables, Vizcom pour les designers, Hugging Face pour tester des modèles ouverts.
- **IA à usage malveillant** : liste de noms (DarkBERT, Dark GPT, FraudGPT, Wolf GPT, outils de deepfake, etc.) présentée comme « les IA maléfiques ».
- **Énergie, entraînement** : DeepSeek-V3 environ 1,95 GWh (450 foyers français par an), Mistral Large 2 environ 4,5 GWh, Llama 3 70B environ 6,4 GWh, Claude 3.5 environ 35 GWh, GPT-4 50 à 60 GWh, GPT-5 80 à 100 GWh (20 000 foyers).
- **Énergie, inférence** : recherche Google sans IA 0,1 à 0,3 Wh, DeepSeek-V3 0,15 Wh par texte, Nano Banana 2 0,24 Wh par image, Nano Banana Pro 0,8 Wh, FLUX 2.0 1,8 Wh, GPT-5 en réflexion approfondie 15 à 20 Wh. Comparaisons : une heure de jeu PC vaut 450 Wh (soit 1 865 images Nano Banana 2), une heure sur PS5 ou Netflix 210 Wh, une heure de route en Tesla à 130 km/h 23 400 Wh (97 500 images). Deux articles : Microsoft relance un réacteur de Three Mile Island (plus de 800 MW, jusqu'en 2054) et Google commande 6 à 7 mini-réacteurs (SMR) pour ses centres de données.
- **Politique des IA** : boussole politique 2025. Autoritaire de gauche : Qwen-Max et ERNIE Bot 4. Libertaire de gauche, près du centre : Claude 4, Mistral Large 2, ChatGPT, Gemini 2.5, Llama 3.1. Libertaire de droite : Perplexity près du centre, Grok 3 très loin. Le cours explique que l'orientation dépend du corpus d'entraînement et du recadrage des chercheurs, et qu'on la mesure en posant de 5 000 à 100 000 questions puis en analysant mots, tournures et idées. Biais décrits : les Californiens (OpenAI, Anthropic, Google) refusent les questions « sensibles » par peur juridique ; les Européens (Mistral) sont moins moralisateurs ; les Asiatiques (Qwen, DeepSeek) ont un alignement culturel et politique propre mais excellent en mathématiques et en code.
- **Copyright** (diapositives d'une avocate invitée, voir [[Droit d'auteur et IA]]) : une création faite seulement par prompts textuels ne peut pas être protégée ; les retouches (vary region, remix de Midjourney) peuvent démontrer un contrôle humain ; des éléments de référence intégrés dans l'output peuvent être protégés si l'on détient leurs droits. Le droit d'auteur protège des formes, pas des idées. Affaire Thaler contre Perlmutter (2023) : œuvres d'IA non protégées aux États-Unis. Chine, tribunal de Pékin, 27 novembre 2023 : image générée par IA protégée. Conseils : identifier les contenus protégeables, conserver des preuves du contrôle du processus créatif.
- **IA « sûres » sur les données d'entraînement** : Adobe Firefly, Generative AI by Getty Images et iStock, Shutterstock avec DALL·E 3, Bria.ai, Public Diffusion (domaine public et CC0), Tongyi Wanxiang / Wan 2.1 d'Alibaba.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes : transcriptions reprises.

1. **« Les IA sont basées sur des TPU »** : affirmation générale de l'étudiant. Les modèles d'IA s'entraînent et s'exécutent sur des GPU, des TPU et d'autres accélérateurs ; TPU est le matériel de Google (complément). **À corriger avant un examen.**
2. **Tokens d'image** : l'image décrite (50 tokens répartis sur les visages) est une explication imagée, pas une règle ; le cours ne donne pas de source.
3. **« Google » dans les logiciels « open source »** : Gemini est un produit propriétaire, seuls certains modèles de Google (Gemma) sont ouverts. La liste classe aussi Hugging Face (plateforme) parmi les éditeurs (complément).
4. **Chiffres énergétiques** : les consommations de GPT-4, GPT-5 et Claude 3.5 sont des estimations, aucune n'est publiée par les éditeurs ; le cours ne donne pas de source.
5. **JSON de l'exemple** : la transcription note des incohérences (« bikini », « her », « A old man » dans le texte, alors que l'image montre un homme jeune en t-shirt) et un guillemet « mal placé avant `technical_specs`. L'exemple n'est donc pas un JSON valide tel quel (complément). La liste `elements` est coupée sur la deuxième version de l'image.
6. **Tableau « Californiens, Européens, Asiatiques »** : opinions générales sans méthode ni source.
7. **Signature de l'avocate** sur les diapositives de copyright : orthographe incertaine selon les images (alerte de la transcription). Le nom de cette personne n'est pas repris dans le wiki.
8. **Positionnement politique** : placement de la boussole lu d'après la transcription, sans valeur numérique.
9. **Phrases coupées** : la note ne présente aucune phrase s'arrêtant net.
