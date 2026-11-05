---
type: source
sources: ["[[Chapitre 2 ensembles]]"]
maj: 2026-11-05
---

Résumé de [[Chapitre 2 ensembles]], dans [[Year 1 - Outil Maths]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Vocabulaire et opérations sur les ensembles, relié aux connecteurs logiques de [[Chapitre 1 logique (résumé)]]. Voir [[Opérations sur les ensembles]].

## Contenu, dans l'ordre du cours

- **Définition par compréhension** $\{x \in E : P(x)\}$. Exemples : $2\mathbb{N}$, $2\mathbb{N}+1$, $\mathbb{Q} = \{p/q, p \in \mathbb{Z}, q \in \mathbb{N}^*\}$, $[a, b[$.
- **Appartenance et inclusion** : $0 \in \mathbb{N}$ et $\{0\} \subset \mathbb{N}$. $\mathbb{N}$ est une partie, ou un sous-ensemble, de $\mathbb{Z}$.
- **Égalité** : $E = F \iff (E \subset F \text{ et } F \subset E)$.
- **Ensemble des parties** $\mathcal{P}(E)$. Pour $E = \{1, 2, 3\}$ : 8 parties, de $\emptyset$ à $E$. L'exemple de la collection $\mathcal{A}$ des sous-ensembles de $\mathbb{N}$ ne contenant que des pairs : $A \subset \mathbb{N}$ mais $A \in \mathcal{A}$.
- **Opérations** : intersection, union, différence ($A \setminus B = A \cap \overline{B}$), complémentaire (notations $\overline{A}$, $\mathrm{C}_E(A)$, $A^c$). Diagrammes de Venn.
- **Familles** $(A_i)_{i \in I}$ : l'intersection est l'ensemble des $x$ dans tous les $A_i$, l'union celui des $x$ dans au moins un. Distributivité, y compris pour des familles.
- **Propriétés du complémentaire** : $\overline{\overline{A}} = A$, $A \cap \overline{A} = \emptyset$, $A \cup \overline{A} = E$, lois de De Morgan pour deux ensembles et pour les familles. Si $A \cap B = \emptyset$, ils sont disjoints.
- **Tableau logique et ensembles** : implication et inclusion, conjonction et intersection, disjonction et union, négation et complémentaire.
- **Partition** : parties non vides, d'union $E$, deux à deux disjointes. Annotation de l'étudiant : « en gros c pas possible que 2 ensembles aient le mm élément ».
- **Exemples de familles** : $\bigcup_n [1/n, 1] = ]0, 1]$, avec $n = \lfloor 1/x \rfloor + 1$ ; $\bigcap_n [0, 1 + 1/n[ = [0, 1]$.
- **Cardinal** : $|A \cup B| = |A| + |B| - |A \cap B|$, et $|A| + |B|$ si $A \cap B = \emptyset$.
- **Produit cartésien** : $n$-uplets, noté $E^n$ si les ensembles sont égaux.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **De Morgan, propriété 6** : image lue directement, elle écrit $\overline{A \cup B} = \overline{A} \cup \overline{B}$. La bonne formule est $\overline{A} \cap \overline{B}$ (complément). La propriété 8, sur les familles, est écrite correctement. **À corriger avant un examen.**
2. **« $N \in Z \in Q \in R$ »**, en tête de note : le signe d'appartenance est écrit à la place de l'inclusion $\subset$. Le cours distingue plus loin $0 \in \mathbb{N}$ et $\{0\} \subset \mathbb{N}$ (complément). **À corriger avant un examen.**
3. **Fausse alerte sur le cardinal** : la transcription signale que $|A \cup B| = |A| + |B|$ n'est vraie que pour des ensembles disjoints. Le cours place la condition $A \cap B = \emptyset$ juste après, dans une image séparée (« et si ... alors »).
4. **« $x B$ » et « $x A$ »** (différence, complémentaire) : alertes de lisibilité, symbole $\notin$ perdu. Le sens est certain d'après $A \setminus B = A \cap \overline{B}$. Images non ouvertes.
