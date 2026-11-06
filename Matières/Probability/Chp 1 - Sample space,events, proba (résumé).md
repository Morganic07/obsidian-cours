---
type: source
tags: [year2]
sources: ["[[Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-05
---

Résumé de [[Chp 1 - Sample space,events, proba]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Poser le cadre de toute la probabilité : un espace d'issues, des événements qui en sont des sous-ensembles, et une fonction $P$ qui les mesure.

## Contenu, dans l'ordre du cours

- **Ensembles** : le cardinal $|S|$ est le nombre d'éléments, et $|\emptyset| = 0$. Un ensemble est fini ou infini, dénombrable ou non (comme $\mathbb{R}$), discret ou continu. Un ensemble n'a ni ordre ni répétition : $\{a,b,b,c,c\} = \{a,b,c\} = \{c,b,a\}$.
- **[[Espace probabilisé]]** : une expérience est une action à issue incertaine, répétable dans les mêmes conditions. L'espace d'échantillonnage $S$ liste toutes les issues. Il doit être exhaustif (aucune issue oubliée) et exclusif (aucun doublon).
- **Événements** : un événement est un sous-ensemble de $S$. Un événement simple a une seule issue ($A = \{6\}$), un événement composé en a plusieurs ($A = \{2,4,6\}$). Le complémentaire est $A^C = S \setminus A$. Le cours donne les diagrammes de Venn pour $\cap$, $\cup$, $A^c$ et des ensembles disjoints, puis les lois de De Morgan, $(A \cup B)^c = A^c \cap B^c$ et $(A \cap B)^c = A^c \cup B^c$, et leur version pour une famille $(A_i)$.
- **Espace des événements** : stable par union, intersection et complémentaire. Une telle famille est une sigma-algèbre : elle contient $\Omega$, elle est stable par complémentaire et par union dénombrable. Si $S$ est fini, c'est l'ensemble des parties $\mathcal{P}(S)$, qui contient toujours $\emptyset$.
- **Espaces discrets** : $S$ est discret s'il est fini ou si ses points se rangent en suite (dénombrable). Sinon il est continu.
- **Probabilité** : $P : $ espace des événements $\to \mathbb{R}$. Si les issues sont équiprobables, $P(A) = |A|/|S|$. Les axiomes sont : (i) $P(A) \ge 0$ ; (ii) additivité pour deux événements disjoints ; (ii\*) additivité dénombrable ; (iii) $P(S) = 1$.
- **Propriétés** : $P(A) = 1 - P(A^c)$, $P(\emptyset) = 0$, $P(A) \le 1$, $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, $P(A \cup B) \le P(A) + P(B)$, additivité et sous-additivité finies.
- **Construire une probabilité** : sur $S = \{\omega_1, \omega_2, \dots\}$, on donne à chaque issue un poids $p_i \ge 0$ avec $\sum p_i = 1$ (les poids n'ont pas à être égaux), puis $P(A) = \sum_{\omega_i \in A} p_i$.
- **Événements nul et impossible** : $A$ est nul si $P(A) = 0$ et impossible si $A = \emptyset$. Un événement impossible est nul, la réciproque est fausse.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Impossible** : la note écrit « A is impossible if P(A) = ø », ce qui mélange $P(A) = 0$ et $A = \emptyset$. La phrase suivante (« un événement impossible est nul, inverse pas toujours vrai ») n'a de sens que si impossible veut dire $A = \emptyset$ (complément).
2. **Tableau fini / dénombrable** : la transcription note « 5 éléments » pour $\{1,2,3\}$, qui en a 3. À vérifier sur l'image, non ouverte. La coquille ne touche pas le fond.
3. **Lois de De Morgan en famille** : les bornes des unions et intersections ne sont pas visibles dans la transcription. À vérifier sur l'image, non ouverte.
4. **Définition de $P$** : le cours donne (ii) et (ii\*) comme deux axiomes. L'additivité finie (ii) découle de (ii\*) avec $P(\emptyset) = 0$ (complément).
