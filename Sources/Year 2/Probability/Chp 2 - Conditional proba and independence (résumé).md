---
type: source
sources: ["[[Chp 2 - Conditional proba and independence]]"]
maj: 2026-11-05
---

Résumé de [[Chp 2 - Conditional proba and independence]], dans [[Year 2 - Probability]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Mesurer un événement une fois qu'on sait qu'un autre a eu lieu, puis en déduire trois outils : la règle de multiplication, les probabilités totales et le théorème de Bayes. Le chapitre finit sur l'indépendance.

## Contenu, dans l'ordre du cours

- **[[Probabilité conditionnelle]]** : pour $P(B) > 0$, $P(A|B) = P(A \cap B)/P(B)$. Conditionner sur $B$ revient à prendre $B$ comme nouvel espace d'échantillonnage : de $A$ il reste $A \cap B$.
- **Règle de multiplication** : $P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$. Elle sert pour les expériences en plusieurs étapes : $P(A_1 \cap A_2 \cap A_3) = P(A_3|A_1 \cap A_2)\,P(A_2|A_1)\,P(A_1)$.
- **Probabilités totales** : des événements $A_1, \dots, A_n$ sont exhaustifs si leur union est $S$. S'ils sont de plus mutuellement exclusifs, $P(B) = \sum_i P(B|A_i)P(A_i)$ pour tout événement $B$.
- **Théorème de Bayes** : avec les mêmes $A_i$ et $P(A_i) > 0$, $P(B) > 0$, $P(A_j|B) = P(B|A_j)P(A_j) / \sum_i P(B|A_i)P(A_i)$.
- **Indépendance** : $A$ et $B$ sont indépendants si $P(A|B) = P(A)$, ce qui équivaut à $P(A \cap B) = P(A)P(B)$ et entraîne $P(B|A) = P(B)$. Alors $(A^c, B)$, $(A, B^c)$ et $(A^c, B^c)$ sont aussi indépendants. Le cours démontre les trois cas à la main, en réutilisant $P(A^c \cap B) = P(B) - P(A \cap B)$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Définition de la probabilité conditionnelle** : la transcription lit « P(A) is the probability of A given B ». Il faudrait $P(A|B)$. Image non ouverte, à vérifier. Ce n'est qu'une coquille probable.
2. **Bornes dans Bayes** : l'énoncé parle de $A_1, \dots, A_n$, mais la formule somme jusqu'à $k$ et fait varier $j$ jusqu'à $k$. Cette alerte de la transcription est fondée sur le texte lu : $n$ et $k$ désignent la même chose (complément).
3. **Démonstration du cas $(A, B^c)$** : elle utilise $P(A \cap B^c) = P(A) - P(A \cap B)$ sans la justifier à part, comme pour le premier cas. Le cours ne l'écrit pas ici. Le résultat est juste.
4. **Indépendance et événements incompatibles** : le cours ne dit pas que deux événements disjoints de probabilité non nulle ne sont jamais indépendants. Le wiki ne l'affirme donc pas non plus.
