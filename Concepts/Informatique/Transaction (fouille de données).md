---
type: concept
tags: [year4]
aliases: [base de transactions, transactional database]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : en fouille de règles d'association, une transaction est un ensemble d'items, par exemple T1 [vin, fromage, viande] ou T2 [vin, fromage, chocolat]. L'ensemble des transactions $D$ forme l'ensemble d'apprentissage, dans lequel on cherche les [[Itemset fréquent|itemsets fréquents]] et les [[Règle d'association|règles d'association]].

## Compléments (complément, hors du cours)

- Exemple type : un ticket de caisse, qui liste les produits d'un même achat ([[Analyse du panier de la ménagère]]). La quantité achetée et le prix sont ignorés : seule compte la présence de l'item.
- À ne pas confondre avec une [[Transaction (base de données)|transaction de SGBD]], suite d'opérations exécutée de façon atomique (propriétés ACID).
- Deux représentations : horizontale (pour chaque transaction, sa liste d'items, celle d'[[Algorithme Apriori|Apriori]]) et verticale (pour chaque item, la liste des transactions qui le contiennent, celle d'Eclat).

Voir aussi : [[Support (règle d'association)]], [[Fouille de données]].

Résumés : [[2 - association rules]]
