---
type: concept
tags: [year1]
aliases: [relation de divisibilité, divisibility]
matieres: [Outil Maths]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]"]
maj: 2026-11-08
---

$a$ divise $b$, noté $a \mid b$, s'il existe $k \in \mathbb{N}^*$ tel que $b = ak$.

Sur $\mathbb{N}^*$, c'est une relation d'ordre non totale (le PDF donne les trois preuves). La partie $\{2; 3\}$ n'a ni maximum ni minimum. Étendue à $\mathbb{N}$ (avec $k$ entier quelconque), la divisibilité a 0 pour maximum et 1 pour minimum. [[Erreurs du cours#^e-divisibilite|✎]]

## Compléments (complément, hors du cours)

Ajoutés dans [[3 - pdf]].

- **Antisymétrie sur $\mathbb{N}^*$** : si $x \mid y$ et $y \mid x$, on a $y = kx$ et $x = k'y$, donc $x = kk'x$, d'où $kk' = 1$ ; comme $k, k' \in \mathbb{N}^*$, $k = k' = 1$ et $x = y$.
- **Sur $\mathbb{Z}$**, la divisibilité n'est pas antisymétrique : $2 \mid -2$ et $-2 \mid 2$, mais $2 \ne -2$. Ce n'est donc pas une relation d'ordre sur $\mathbb{Z}$.
- **Bornes** : pour l'ordre de divisibilité, $\inf\{a, b\} = \mathrm{PGCD}(a, b)$ et $\sup\{a, b\} = \mathrm{PPCM}(a, b)$. Exemple : $\{2, 3\}$, sans maximum ni minimum, a pour borne inférieure $1$ et pour borne supérieure $6$.
- **Le cas de 0** : avec la définition usuelle ($b = ak$ pour un entier $k$ quelconque), tout entier divise $0$ ($0 = a \times 0$), d'où $0$ maximum de $\mathbb{N}$ pour la divisibilité. Avec $k \in \mathbb{N}^*$, comme dans le cours, $0$ n'est divisible par aucun entier non nul.
- Un ordre de divisibilité fini (par exemple les diviseurs de 12) se représente par un [[Diagramme de Hasse]].

Notion parente : [[Relation d'ordre]]. Voir aussi : [[Congruence modulo n]].

Résumés : [[3 - pdf]]
