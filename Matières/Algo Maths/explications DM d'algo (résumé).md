---
type: source
tags: [year1]
sources: ["[[explications DM d'algo]]"]
maj: 2026-11-05
---

Résumé de [[explications DM d'algo]], dans [[Algo Maths (matière)]]. Note pédagogique de l'étudiant autour d'un devoir sur le [[Problème du sac à dos]]. L'auteur prévient lui-même que son code peut contenir des erreurs. Pas d'image dans la note.

## Idée générale

Lecture d'un fichier d'objets, puis plusieurs stratégies de résolution : exhaustive, gloutonne, stochastique. La programmation dynamique est annoncée mais non rédigée.

## Contenu, dans l'ordre de la note

- **`lecture_fichier`** : classe `Objet` (`num`, `v` valeur, `w` poids) en `dataclass`. La première ligne du fichier donne le nombre d'objets et la capacité $P$, chaque ligne suivante donne valeur et poids. La fonction renvoie `NbObjets, P, objets`.
- **Énumération exhaustive** : chaque objet est pris ou non, donc $2^n$ configurations. Ce n'est pas $n!$, qui compte des permutations.
- **`exhaustif_binaire`** : parcourt $i$ de 0 à $2^n - 1$, convertit en binaire sur $n$ bits (un bit à 1 prend l'objet), garde la meilleure valeur de poids total $\le P$.
- **`exhaustif_binaire_optimise`** : même principe, mais calcule valeur et poids par incrément et fait un `break` dès que le poids dépasse $P$.
- **Code de Gray** : deux valeurs successives diffèrent d'un seul bit. `code_gray(n)` part de `[0]` et, à chaque tour, ajoute les éléments déjà présents parcourus à l'envers avec le bit $i$ mis à 1. `exhaustif_gray` parcourt ces codes.
- **[[Algorithme glouton]]** : décision localement optimale, répétée. Trois versions, qui ne diffèrent que par la clé de tri : `glouton_valeur` (valeur décroissante), `glouton_poids` (poids croissant), `glouton_densite` (rapport valeur/poids décroissant). L'auteur précise qu'aucune n'est optimale et que l'objet ne peut pas être fractionné.
- **Algorithme stochastique `remplissage_aleatoire`** : pour chaque objet, probabilité d'inclusion $1 - \frac{\text{poids}_{\text{courant}} + w}{P}$, objet pris si un tirage est inférieur et si le sac ne déborde pas. Le résultat varie d'une exécution à l'autre et n'est pas garanti optimal.
- **Programmation dynamique** : « Je fais plus tard ».

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Première ligne du fichier** : le commentaire dit « le nombre d'objet et la valeur de chaque objet », alors que le code lit le nombre d'objets et la capacité $P$.
2. **Bloc de code de `glouton_valeur`** (encadré) : `sorted(..., key=lambda x: x.v)` sans `reverse=True`, donc tri croissant. La version commentée, plus bas, ajoute `reverse=True` et c'est elle qui correspond au texte.
3. **Bloc de code `exhaustif_gray`** (encadré) : appelle `gray_code(...)`, alors que la fonction définie s'appelle `code_gray` ; la version commentée utilise le bon nom. Dans les deux, la configuration est recalculée entièrement pour chaque code : l'intérêt du code de Gray (ne changer qu'un objet à chaque pas) n'est pas exploité (complément).
4. **Nom du fichier de test** : `ks_0_4` dans la consigne, `ks_4_0.txt` dans le code. Alerte de nom sans importance.
5. **`remplissage_aleatoire`** : la probabilité $1 - \frac{\ldots}{P}$ peut être négative pour un objet trop lourd, ce qui l'exclut (complément, sans conséquence sur le résultat).
6. **Programmation dynamique** : section annoncée et vide.
