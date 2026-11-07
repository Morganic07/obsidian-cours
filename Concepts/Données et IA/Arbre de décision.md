---
type: concept
tags: [year4]
aliases: [decision tree, decision trees, arbres de décision]
matieres: [data mining]
sources: ["[[Chp1 - intro to data mining (résumé)|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-06
---

Modèle de classification ([[Classifieur]]) où chaque nœud teste un attribut, chaque branche (arête) une valeur du domaine de l'attribut et chaque feuille une valeur de classe. Il se lit comme un ensemble de règles « SI … ALORS CLASS = … ».

**Construction** : si tous les exemples ont la même classe, on crée une feuille ; sinon on choisit un test, on partitionne les exemples et on recommence sur chaque sous-ensemble sans ce test. La base d'entraînement doit couvrir le domaine, y compris les exemples inhabituels.

**[[Algorithme ID3]]** choisit le test de plus grand **[[Gain d'information]]** : $gain(T) = I(E) - \sum_l W_lI(E_l^T)$, où $I = \sum p_i\log_2\dfrac{1}{p_i}$ est l'[[Entropie (théorie de l'information)|entropie]] et $W_l$ la proportion d'exemples du sous-ensemble $l$. Exemple du jeu météo (14 exemples) : gain(Outlook) 0,246 bit, gain(Humidity) 0,151, gain(Wind) 0,048, gain(Temp.) 0,029, donc Outlook à la racine.

**[[Algorithme C4.5]]**, descendant d'ID3 : attributs continus par discrétisation, gain normalisé $\dfrac{gain}{SplitInfo}$, valeurs manquantes traitées par probabilités, [[Élagage|élagage]].

**[[Algorithme CART]]** (1984) : arbres binaires, tous types de variables, critère de Gini $1 - \sum p_i^2$ ([[Indice de Gini]] : plus il est petit, plus le nœud est pur). On maximise la baisse de Gini pondérée entre le nœud et ses deux fils.

Les arbres servent de base aux [[Méthodes d'ensemble]]. Évaluation : [[Validation d'un classifieur]].

**Le cours complet en PDF** détaille ces trois algorithmes : ID3 choisit la variable de plus grand gain d'information (entropie), C4.5 utilise le rapport de gain et gère les valeurs manquantes et l'élagage, CART utilise l'indice de Gini. Sur l'exemple PlayTennis, les gains valent 0,246 (outlook), 0,151 (humidity), 0,048 (wind) et 0,029 (temperature) : outlook est donc à la racine.

Notion parente : [[Classifieur]]. Voir aussi : [[Algorithme ID3]], [[Algorithme C4.5]], [[Algorithme CART]], [[Entropie (théorie de l'information)]], [[Élagage]].

## À vérifier

- La description de la classe P donnée par le cours, $(\text{overcast} \wedge \text{HUMI}=\text{normal}) \vee \text{overcast} \vee (\text{rainy} \wedge \text{WIND}=\text{no})$, oublie la branche sunny et HUMI = normal (relevé du résumé).

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
