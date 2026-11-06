---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre 2 - Ensembles (PDF)]]"]
maj: 2026-11-06
---

Résumé du support du professeur [[raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre 2 - Ensembles (PDF)]] (26 diapositives, octobre 2023), dans [[Outil Maths (matière)]]. C'est la version du professeur du cours déjà résumé dans [[Chapitre 2 ensembles (résumé)]] ; notions : [[Opérations sur les ensembles]], [[Logique propositionnelle]].

## Contenu, dans l'ordre

- **Ensemble** : collection d'objets distincts. Appartenance $x \in E$, non-appartenance $x \notin E$. Ensembles usuels $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, et l'ensemble vide.
- **Définition par compréhension** $\{x \in E : P(x)\}$ : $2\mathbb{N}$, impairs, $\mathbb{Q}$, $[a, b[$.
- **Inclusion** $E \subset F \iff \forall x,\ (x \in E \Rightarrow x \in F)$. Mise en garde : $0 \in \mathbb{N}$ mais $\{0\} \subset \mathbb{N}$ ; $\mathbb{N} \subset \mathbb{Z}$ mais $\mathbb{N} \notin \mathbb{Z}$, sauf pour un ensemble d'ensembles.
- **Méthode** pour une inclusion : « Soit $x \in E$. Montrons que $x \in F$ ». Exemple : $\{x \in \mathbb{R} : \exists y \in \mathbb{R}_+, x \ge y\} \subset \mathbb{R}_+$.
- **Égalité** et **double inclusion** : $E = F \iff (E \subset F \text{ et } F \subset E)$, rédigée en deux étapes, ou par équivalences.
- **Ensemble des parties** $\mathcal{P}(E)$ : pour $\{1,2,3\}$, 8 parties. Le cours distingue $A \subset \mathbb{N}$ et $A \in \mathcal{A}$ pour la collection $\mathcal{A}$ des parties de $\mathbb{N}$ formées de pairs.
- **Intersection, union** de deux ensembles puis d'une famille $(A_i)_{i \in I}$ ($\forall i$ pour l'intersection, « au moins un » pour l'union).
- **Distributivité** de $\cap$ sur $\cup$ et réciproquement, y compris pour des familles.
- **Différence** $A \setminus B$ et **complémentaire** $\overline{A}$ (notations $\mathrm{C}_E(A)$, $A^c$).
- **Propriétés du complémentaire** : double complémentaire, $A \cap \overline{A} = \emptyset$, $A \cup \overline{A} = E$, $A \setminus B = A \cap \overline{B}$, lois de De Morgan (deux ensembles, familles). Ensembles **disjoints** si $A \cap B = \emptyset$.
- **Lien logique / ensembles** : implication et inclusion, conjonction et intersection, disjonction et union, négation et complémentaire.
- **Partition** : parties non vides, d'union $E$, deux à deux disjointes.
- **Cardinal** d'un ensemble fini : $|A \cup B| = |A| + |B|$ si $A \cap B = \emptyset$, sinon $|A| + |B| - |A \cap B|$.
- **Diagramme de Venn** : schéma des relations entre ensembles ; exemple avec trois ensembles $A$, $B$, $C$ dans $E$.
- **Produit cartésien** $E_1 \times \dots \times E_n$ : $n$-uplets, couple, triplet ; $E^n$ si tous les ensembles sont égaux. $(2,3) \neq (3,2)$ ; $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$.

## Points à vérifier

1. **De Morgan, propriété 6** (diapositive 18, image ouverte) : le support écrit $\overline{A \cup B} = \overline{A} \cup \overline{B}$. La bonne formule est $\overline{A} \cap \overline{B}$ (complément). Même erreur que dans [[Chapitre 2 ensembles (résumé)]]. La propriété 8, sur les familles, est correcte.
2. **Proposition d'égalité** (diapositive 9) : « $E \subset F$ et $F \subset F$ » est une coquille, il faut $F \subset E$ (complément).
