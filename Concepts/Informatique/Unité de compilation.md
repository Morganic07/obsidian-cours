---
type: concept
tags: [year4]
aliases: [translation unit, unité de traduction]
matieres: [C／C++]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : une unité de compilation (*translation unit*, « unité de traduction » dans la norme) est ce que le [[Compilateur|compilateur]] traite en une fois : un [[Fichier source|fichier source]] `.cpp` après le passage du [[Préprocesseur|préprocesseur]], c'est-à-dire avec le texte de tous les en-têtes qu'il inclut, directement ou non. Chacune donne un [[Fichier objet|fichier objet]].

Le compilateur ne voit rien au-delà de l'unité en cours : pour utiliser une fonction définie ailleurs, il lui faut sa déclaration ([[Fichier d'en-tête]]), et seule l'[[Édition de liens|édition de liens]] vérifie qu'elle est définie quelque part. Une [[Garde d'inclusion|garde d'inclusion]] n'agit qu'à l'intérieur d'une unité ; la [[Règle de la définition unique|règle de la définition unique]] s'applique, elle, à tout le programme.

## Dans le cours

Pas nommée : [[5 - Compilation séparée]] dit que « chaque `.cpp` est compilé séparément des autres » ; le terme apparaît dans ses compléments.

Voir aussi : [[Compilation séparée]].

Résumés : [[5 - Compilation séparée]]
