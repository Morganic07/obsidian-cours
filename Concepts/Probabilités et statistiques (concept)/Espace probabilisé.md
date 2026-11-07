---
type: concept
tags: [year2]
aliases: [sample space, espace d'échantillonnage, espace des événements, sigma-algèbre, sigma-algebra, tribu, axiomes de probabilité, événement impossible, événement nul, sample set, espace des issues, space of events]
matieres: [Probability]
sources: ["[[1 - Sample space,events, proba (résumé)|Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-06
---

Une [[Expérience aléatoire|expérience]] a une issue incertaine. L'espace d'échantillonnage $S$ (ou $\Omega$) est l'ensemble de ses issues possibles : exhaustif (aucune issue oubliée) et exclusif (aucun doublon). Un [[Événement (probabilités)|événement]] est un sous-ensemble de $S$ : simple (une issue) ou composé. Le complémentaire de $A$ est $A^C = S \setminus A$.

**Espace des événements** : famille stable par union, intersection et complémentaire ; formellement, stable par complémentaire et union dénombrable, qui contient $\Omega$ (une sigma-algèbre). Si $S$ est fini, c'est l'ensemble des parties $\mathcal{P}(S)$. $S$ est discret s'il est fini ou si ses éléments se rangent en suite, continu sinon.

**Probabilité** $P$ : $P(A) \ge 0$, $P(S) = 1$, additivité pour des événements disjoints (finie et dénombrable). On en déduit $P(A^c) = 1 - P(A)$, $P(\emptyset) = 0$ et $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. Si les issues sont équiprobables ([[Équiprobabilité]]), $P(A) = |A|/|S|$ (voir [[Dénombrement]]). Sinon, on pose un poids $p_i \ge 0$ par issue, avec $\sum p_i = 1$.

Un événement est nul si $P(A) = 0$ et impossible si $A = \emptyset$ : tout événement impossible est nul, pas l'inverse.

Liens : [[Probabilité conditionnelle]], [[Variable aléatoire]], [[Opérations sur les ensembles]] (ensemble des parties)

## À vérifier

- [[1 - Sample space,events, proba (résumé)|Chp 1 - Sample space,events, proba]] écrit « A is impossible if P(A) = ø », qui mélange $P(A) = 0$ (événement nul) et $A = \emptyset$ (événement impossible).

Résumé : [[1 - Sample space,events, proba (résumé)]]
