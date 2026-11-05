---
type: source
sources: ["[[chp2 - piles listes file]]"]
maj: 2026-11-05
---

Résumé de [[chp2 - piles listes file]], dans [[Year 2 - Algo]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Trois structures de données qui rangent des éléments dans un certain ordre : la liste, la pile et la file.

## Contenu, dans l'ordre du cours

- **Tableau comparatif pile / file** : la pile suit l'ordre LIFO (empiler, dépiler) et n'a qu'un pointeur, vers le haut. La file suit l'ordre FIFO (enfiler, défiler) et a deux pointeurs, la tête et la fin. Voir [[Pile et file]].
- **Liste** : éléments de même nature, chacun avec un rang, qu'on peut ajouter ou supprimer n'importe où. La tête est le dernier élément ajouté, la queue est le reste. Voir [[Liste chaînée]] : chaque chaînon contient un élément et un pointeur vers le suivant, les éléments ne sont pas contigus en mémoire. Opérations : `vide()`, `estVide(L)`, `ajouteEnTete(x,L)`, `supprEnTete(L)`, `compte(L)`, `cons(x,L)`.
- **Pile** : le pointeur `top` désigne le dernier élément. Méthodes : `estVide()`, `empiler`, `depiler`, `lireSommet`, `taille`. En Python, une liste fait office de pile avec `append` et `pop`.
- **File** : le pointeur avant désigne l'élément inséré en premier et encore présent, le pointeur arrière le dernier inséré. Méthodes : `enfiler`, `defiler`, `estVide`, `longeur` (écrit ainsi dans le cours).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images lues par leur transcription, aucune ouverte.

1. **Tableau pile / file** : la colonne File dit que les objets sont « insérés et retirés aux 2 extrémités ». C'est imprécis : une file insère à une extrémité et retire à l'autre, comme le montre l'illustration enfiler/défiler (complément).
2. **Coquilles signalées par les transcriptions** : « le tète » et `longeur()` sont recopiés tels quels, probablement pour « tête » et `longueur()`.
3. **Aucune implémentation de la file** n'est donnée, ni pour la pile hors de la liste Python.
