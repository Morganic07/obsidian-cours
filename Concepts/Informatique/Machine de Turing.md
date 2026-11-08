---
type: concept
tags: [year1]
aliases: [Turing machine, machines de Turing, Turing-complet, Turing-complete, Turing complétude, thèse de Church-Turing, Church-Turing thesis, problème de l'arrêt, halting problem]
sources: ["[[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : modèle mathématique de calcul défini par Alan Turing en 1936 (article « On Computable Numbers, with an Application to the Entscheidungsproblem »). Une machine de Turing se compose :

- d'un **ruban** infini divisé en cases, chacune contenant un symbole d'un alphabet fini (dont un symbole « blanc ») ;
- d'une **tête de lecture-écriture** placée sur une case ;
- d'un ensemble fini d'**états**, dont un état initial et un ou plusieurs états d'arrêt ;
- d'une **table de transition** finie : selon l'état courant et le symbole lu, la machine écrit un symbole, déplace la tête d'une case à gauche ou à droite, et passe dans un nouvel état.

Formellement, la fonction de transition s'écrit $\delta : Q \times \Gamma \to Q \times \Gamma \times \{G, D\}$, où $Q$ est l'ensemble des états et $\Gamma$ l'alphabet du ruban. Le calcul s'arrête quand la machine atteint un état d'arrêt ; le contenu du ruban est alors le résultat.

**Thèse de Church-Turing** (années 1930, Alonzo Church et Alan Turing) : tout ce qui est calculable par un procédé mécanique effectif est calculable par une machine de Turing. C'est une thèse et non un théorème : la notion intuitive de « procédé mécanique » n'a pas de définition mathématique, mais tous les modèles de calcul proposés depuis (lambda-calcul, fonctions récursives, ordinateurs réels) se sont révélés équivalents.

**Turing-complétude** : un langage ou un système est *Turing-complet* s'il peut simuler n'importe quelle machine de Turing (à la limite près de la mémoire, finie dans un ordinateur réel). Python, C, Java et les autres langages généralistes le sont ; ils calculent donc exactement les mêmes fonctions et ne diffèrent que par la facilité d'écriture et l'efficacité.

**Limite : le problème de l'arrêt.** Turing a montré en 1936 qu'aucune machine de Turing (donc aucun programme) ne peut décider, pour tout programme $P$ et toute entrée $x$, si $P$ s'arrête sur $x$ : le problème est **indécidable**. Idée de la preuve, par l'absurde : si un tel décideur `arret(P, x)` existait, on construirait un programme `D(P)` qui boucle indéfiniment si `arret(P, P)` répond « s'arrête » et s'arrête sinon ; `D(D)` s'arrêterait si et seulement s'il ne s'arrête pas, contradiction. Conséquence pratique : aucun outil ne peut prouver automatiquement la [[Terminaison d'un algorithme|terminaison]] de tous les programmes ; on la démontre au cas par cas.

À ne pas confondre avec le [[Test de Turing]] (1950), qui porte sur l'imitation d'une conversation humaine par une machine, et non sur ce qui est calculable.

## Dans le cours

Le cours ne la nomme pas : Cours 1 (Algo Maths) affirme seulement que, si un problème est résoluble dans un langage de programmation, il l'est dans tous, les langages résolvant les mêmes problèmes. La machine de Turing et la Turing-complétude apparaissent dans les compléments de [[0 - Algo Maths]], qui donnent le nom et la raison de cette équivalence.

Voir aussi : [[Algorithme]], [[Terminaison d'un algorithme]], [[Complexité algorithmique]], [[Classe de complexité]], [[Langage Python]], [[Test de Turing]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]]
