---
type: concept
tags: [year4]
aliases: [Apriori, apriori-gen, Apriori algorithm]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : algorithme d'extraction des [[Itemset fréquent|itemsets fréquents]] d'une base de [[Transaction (fouille de données)|transactions]], première étape de la recherche des [[Règle d'association|règles d'association]]. Il repose sur la [[Propriété de fermeture descendante|propriété de fermeture descendante]] et fait une recherche en largeur ([[Parcours en largeur|breadth-first]]) : les candidats de longueur $k+1$ sont générés à partir des itemsets fréquents de longueur $k$.

**Déroulé** : calculer $L_1$ ; puis, tant que $L_{k-1}$ n'est pas vide, générer les candidats $C_k$ = `apriori-gen`($L_{k-1}$), compter le [[Support (règle d'association)|support]] de chaque candidat en lisant la base, garder dans $L_k$ ceux dont le support atteint `minSupp` ; renvoyer $\bigcup_k L_k$.

**apriori-gen** : une étape de jointure (deux itemsets de $L_{k-1}$ qui partagent leurs $k-2$ premiers items donnent un candidat de longueur $k$), puis une étape de suppression (un candidat dont un sous-ensemble de longueur $k-1$ n'est pas dans $L_{k-1}$ est retiré). Exemple du cours : $L_3 = \{123, 124, 134, 135, 234\}$ donne $C_4 = \{1234, 1345\}$ après jointure, $\{1234\}$ après suppression.

## Compléments (complément, hors du cours)

- Publié par Rakesh Agrawal et Ramakrishnan Srikant chez [[IBM]] (conférence VLDB, 1994), un an après l'article qui pose le problème des règles d'association (Agrawal, Imieliński et Swami, SIGMOD 1993).
- Coût : une lecture de la base par niveau, et un nombre de candidats qui peut exploser quand les itemsets fréquents sont longs ([[Explosion combinatoire]]). L'[[Algorithme FP-Growth]] et Eclat trouvent les mêmes itemsets sans génération de candidats ou avec moins de lectures.
- Implémentations courantes : `apriori()` du paquet `arules` en [[Langage R|R]], `mlxtend.frequent_patterns.apriori` en [[Langage Python|Python]], `Apriori` dans Weka.

Notion parente : [[Règle d'association]]. Voir aussi : [[Itemset fréquent]], [[Redondance des règles d'association]], [[Fouille de données]].

Résumés : [[2 - association rules]]
