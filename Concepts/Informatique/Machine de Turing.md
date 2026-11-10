---
type: concept
tags: [year1, year4]
aliases: [Turing machine, machines de Turing, Turing-complet, Turing-complete, Turing complétude, machine universelle, machine de Turing universelle, universal Turing machine]
sources: ["[[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]]", "[[Raw/Year 4/histoire du design et interactions /chp1 cours.pdf|chp1 cours.pdf]]"]
maj: 2026-11-10
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

En histoire du design (Year 4), [[1 - Histoire du design]] la décrit (d'après l'article de 1936, « On Computable Numbers ») comme une machine abstraite extrêmement simple, conçue pour donner une définition mathématique de « calculer » : un ruban théoriquement illimité divisé en cases, une tête de lecture et d'écriture, un ensemble limité de symboles et des règles indiquant quoi faire selon ce qui est lu ; la machine peut lire un symbole, l'effacer, en écrire un autre, déplacer la tête à droite ou à gauche et changer d'état. Idée fondamentale : un calcul complexe se décompose en une succession d'opérations élémentaires exécutées selon des règles (ENTRÉE → INSTRUCTIONS → OPÉRATIONS → RÉSULTAT). Le cours retient aussi, pour 1936, la **machine universelle** (une machine peut simuler d'autres machines grâce à leurs descriptions) et les **limites du calcul** (certains problèmes ne peuvent pas être résolus par un algorithme universel). La thèse de Church-Turing y est citée dans un extrait de livre ; elle date des travaux de 1936, son nom lui ayant été donné par Stephen Kleene en 1952.

La machine universelle est le modèle théorique de l'ordinateur à programme enregistré, où le programme est une donnée lue par la machine comme une autre ; l'architecture décrite par John von Neumann en 1945 en est la réalisation. [[Complément hors du cours|ⓘ]]

Voir aussi : [[Thèse de Church-Turing]], [[Problème indécidable|Problème de l'arrêt]], [[Calculabilité]], [[Entscheidungsproblem]], [[Architecture de von Neumann]], [[Algorithme]], [[Terminaison d'un algorithme]], [[Complexité algorithmique]], [[Classe de complexité]], [[Langage Python]], [[Test de Turing]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[1 - Histoire du design]]
