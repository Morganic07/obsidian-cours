---
type: concept
tags: [year3]
aliases: [JavaScript Object Notation, fichier JSON, prompt JSON]
sources: ["[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : JSON (*JavaScript Object Notation*) est un format texte d'échange de données structurées, lisible par un humain comme par un programme.

- un **objet** s'écrit entre accolades et contient des paires `"clé": valeur` séparées par des virgules ;
- une **liste** (tableau) s'écrit entre crochets : `[1, 2, 3]` ;
- les **chaînes** et les clés s'écrivent entre guillemets doubles ;
- les **valeurs** peuvent être des nombres, des chaînes, `true`, `false`, `null`, ou d'autres objets et listes imbriqués.

```json
{
  "sujet": "homme sur un yacht",
  "couleurs": ["#FFFFFF", "#1E90FF"],
  "negative_prompt": null
}
```

Une seule faute de syntaxe (guillemet manquant, virgule après le dernier élément, guillemets simples) rend le fichier invalide, et un programme refuse alors de le lire. JSON est très utilisé par les API web pour échanger des données et par les fichiers de configuration.

## Dans le cours

[[1 - IA]] présente le prompt d'image écrit en JSON : les IA le comprendraient mieux, et une IA peut aider à le rédiger. Les rubriques de l'exemple : `lighting`, `background`, composition, `color_profile`, spécifications techniques, éléments artistiques et `negative_prompt` (voir [[Prompt (IA)]]). Dans l'exemple du cours, la clé s'écrit `"technical_specs": {`, avec des guillemets doubles droits. [[Erreurs du cours#^e-json|✎]]

Voir aussi : [[Prompt (IA)]], [[YAML]], [[Fichier CSV]].

Résumés : [[1 - IA]]
