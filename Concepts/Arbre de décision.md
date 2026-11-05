---
type: concept
aliases: [decision tree, decision trees, arbres de décision, ID3, C4.5, CART, indice de Gini, Gini index, gain d'information, information gain]
matieres: [data mining]
sources: ["[[Chp1 - intro to data mining]]"]
maj: 2026-11-05
---

Modèle de classification où chaque nœud teste un attribut, chaque branche une valeur du test et chaque feuille une classe. Il se lit comme un ensemble de règles « SI … ALORS CLASS = … ».

**Construction** : si tous les exemples ont la même classe, on crée une feuille ; sinon on choisit un test, on partitionne les exemples et on recommence sur chaque sous-ensemble sans ce test.

**ID3** choisit le test de plus grand **gain d'information** : $gain(T) = I(E) - \sum_l W_lI(E_l^T)$, où $I = \sum p_i\log_2\dfrac{1}{p_i}$ est l'entropie et $W_l$ la proportion d'exemples du sous-ensemble $l$. Exemple du jeu météo (14 exemples) : gain(Outlook) 0,246 bit, gain(Humidity) 0,151, gain(Wind) 0,048, gain(Temp.) 0,029, donc Outlook à la racine.

**C4.5**, descendant d'ID3 : attributs continus par discrétisation, gain normalisé $\dfrac{gain}{SplitInfo}$, valeurs manquantes traitées par probabilités, élagage.

**CART** (1984) : arbres binaires, tous types de variables, critère de Gini $1 - \sum p_i^2$ (plus il est petit, plus le nœud est pur). On maximise la baisse de Gini pondérée entre le nœud et ses deux fils.

Les arbres servent de base aux [[Méthodes d'ensemble]]. Évaluation : [[Validation d'un classifieur]].

Résumé : [[Chp1 - intro to data mining (résumé)]]
