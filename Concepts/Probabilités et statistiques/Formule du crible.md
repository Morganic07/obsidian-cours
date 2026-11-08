---
type: concept
tags: [year2]
aliases: [formule de Poincaré, inclusion-exclusion, principe d'inclusion-exclusion, inclusion-exclusion principle, formule d'inclusion-exclusion]
sources: ["[[Raw/Year 2/Probability/Chp 1 : Sample space,events, proba.docx|Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : formule qui donne la probabilité d'une réunion d'événements qui se chevauchent, en corrigeant les intersections comptées plusieurs fois. Elle généralise la propriété donnée par le cours :

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Trois événements** :

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

**$n$ événements** :

$$P\Bigl(\bigcup_{i=1}^{n} A_i\Bigr) = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \le i_1 < \dots < i_k \le n} P(A_{i_1} \cap \dots \cap A_{i_k})$$

On ajoute les intersections d'un nombre impair d'événements et on retranche celles d'un nombre pair. Si les événements sont deux à deux [[Événements incompatibles|incompatibles]], toutes les intersections sont vides et l'on retrouve l'additivité.

**En dénombrement**, la même formule vaut pour les cardinaux : $|A \cup B| = |A| + |B| - |A \cap B|$. C'est le principe additif quand les cas se chevauchent.

**Exemple** : on tire une carte parmi 52 ; probabilité d'avoir un cœur ou une figure (valet, dame, roi) :

$$P = \frac{13}{52} + \frac{12}{52} - \frac{3}{52} = \frac{22}{52} = \frac{11}{26}$$

(les trois figures de cœur sont comptées deux fois).

## Dans le cours

Le cours ne la nomme pas : il donne seulement le cas de deux événements. Elle apparaît dans les compléments de [[1 - Sample space,events, proba]] et de [[3 - Combinatorics]] (principe additif).

Voir aussi : [[Espace probabilisé]], [[Événement (probabilités)]], [[Événements incompatibles]], [[Dénombrement]]

Résumés : [[1 - Sample space,events, proba]], [[3 - Combinatorics]]
