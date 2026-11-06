---
type: source
sources: ["[[Chp1 - intro to data mining]]"]
maj: 2026-11-06
---

Résumé de [[Chp1 - intro to data mining]], dans [[Year 4 - data mining]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le data mining extrait des structures cachées, des corrélations non évidentes et des tendances exploitables de grandes masses de données, en combinant algorithmes, statistiques et intelligence artificielle. Le chapitre couvre la classification (k plus proches voisins, arbres de décision, validation), le regroupement (k-means, hiérarchique) et les combinaisons de modèles (bagging, boosting, forêts aléatoires).

## Contenu, dans l'ordre du cours

- **Tâches** : prédictives (classification, régression, séries temporelles, prédiction) ou descriptives (clustering, résumé, règles d'association, découverte de séquences).
- **Exemple de modèle, jeu météo** : 14 exemples avec Outlook, Temp., Humidity, Wind et une classe P ou N. L'arbre obtenu a pour racine Outlook : sunny mène à Humidity (strong donne N, normal donne P), overcast donne P, rainy mène à Wind (yes donne N, no donne P). Un arbre se lit comme un ensemble de règles « SI … ALORS CLASS = … ».
- **Classifieur** : fonction ou algorithme qui prend des caractéristiques et attribue une classe discrète. C'est lui qui produit les prédictions que l'on évalue ensuite avec la matrice de confusion (voir [[Validation d'un classifieur]]). Trois types : construction d'un modèle comme un arbre, estimation directe de la classe à partir d'exemples (k plus proches voisins), modèle paramétrable (réseaux de neurones, SVM).
- **k plus proches voisins** : on classe un point selon les classes de ses $k$ voisins. Sur la figure du cours, avec $k = 3$ il y a 1 point jaune et 2 violets, avec $k = 6$ 4 jaunes et 2 violets : le résultat dépend de $k$.
- **Validation** : la base est séparée en données d'entraînement (construction du modèle) et de test (précision). Si la précision est acceptable, on applique le modèle à des données inconnues. L'erreur $Er$ est la probabilité de mal prédire, le taux de réussite est $1 - Er$. L'erreur d'entraînement est mesurée sur la base d'entraînement.
- **Matrice de confusion** : TP et TN (vrais positifs et négatifs), FP et FN (faux positifs et négatifs). Précision positive $\dfrac{TP}{TP+FP}$ et négative $\dfrac{TN}{TN+FN}$. Rappel positif $\dfrac{TP}{TP+FN}$ et négatif $\dfrac{TN}{TN+FP}$. Exemple du filtre anti-spam sur 100 e-mails (20 spams, 80 légitimes) : 15 VP, 5 FN, 2 FP, 78 VN. Précision $15/17 \approx 88{,}2\,\%$, rappel $15/20 = 75\,\%$.
- **Validation croisée** : on coupe l'ensemble en $n$ parties disjointes de même taille, chaque valeur de la cible apparaissant dans chacune. Avec trois parties A, B, C, on entraîne sur A∪B et on teste sur C, et ainsi de suite. L'erreur globale est la moyenne $Er = \dfrac{Er_A + Er_B + Er_C}{3}$. Exemple du cours : 300 e-mails, erreurs 5 %, 9 %, 7 %, moyenne 7 %.
- **Travaux pratiques annoncés** : jeux Weather et IRIS, k plus proches voisins, arbres de décision, mesures (matrice de confusion, erreur, précision, rappel, F-score), logiciels Weka, R, Python.
- **Clustering et partitionnement** : étant donné des exemples sans étiquette, trouver une partition en $k$ groupes où les données d'un groupe sont semblables et celles de groupes différents ne le sont pas. Exemple : profils d'utilisateurs d'un site de commerce en ligne.
- **Centroïde et inertie** : le centroïde $g$ d'un ensemble est l'exemple moyen. L'inertie est $I = \frac{1}{N}\sum d^2(x_i, g)$, avec une distance euclidienne, de Manhattan ou de Hamming. Inertie intra-classes $I_W = \sum I_k$, inter-classes $I_B = \sum w_id^2(g_i, g)$ avec $w_i = |g_i|/N$, et $I = I_W + I_B$. But : des groupes denses et séparés, donc minimiser $I_W$. Voir [[K-moyennes]].
- **K-means** : choisir $K$ centroïdes au hasard, répéter l'affectation de chaque exemple au centroïde le plus proche et le recalcul des centroïdes, jusqu'à ce que $|I - I_W| < \epsilon$.
- **Classification hiérarchique** : approche ascendante, de $N$ groupes à un seul, qui donne un arbre (dendrogramme). Une coupe horizontale donne $K$ groupes. Critères de fusion : saut minimal, maximal, moyen (centroïdes) ou méthode de Ward (perte minimale de $I_W$, $S = \frac{w_iw_j}{w_i+w_j}d^2(g_i,g_j)$).
- **Arbres de décision** : voir [[Arbre de décision]]. Construction récursive : si tous les exemples ont la même classe, feuille ; sinon choisir un test, partitionner, recommencer sur chaque sous-ensemble.
- **ID3** : choix du test par gain d'information. Quantité d'information $\log_2(N/n)$, entropie $I = \sum p_i\log_2(1/p_i)$, gain $= I(E) - \sum W_lI(E_l)$. Exemple PlayTennis : gain(OUTLOOK) $= 0{,}246$, gain(TEMP.) $= 0{,}029$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$ bits, donc Outlook à la racine.
- **C4.5** : descendant d'ID3. Variables continues par discrétisation, normalisation du gain par $SplitInfo$ ($GainRatio = gain/SplitInfo$), regroupement de valeurs, valeurs manquantes (réparties avec probabilités), élagage.
- **CART** (Breiman, Friedman, Olshen, Stone, 1984) : arbres binaires, tous types de variables, critère de Gini $IG = 1 - \sum p_i^2$ (plus petit = nœud plus pur). On maximise $IG(\text{avant}) - [W_1IG(\text{fils}_1) + W_2IG(\text{fils}_2)]$. La courbe de Gini pour 20 individus et 2 classes est une parabole de maximum 0,5.
- **Combinaison de modèles** : voir [[Méthodes d'ensemble]]. On transforme les sorties de plusieurs modèles en une prédiction par vote (pondéré ou non).
- **Bagging** (bootstrap aggregating) : $k$ échantillons tirés avec remise, un modèle par échantillon, vote majoritaire (moyenne en numérique), pour réduire l'instabilité. Les ensembles ne sont pas disjoints.
- **Boosting** (AdaBoost.M1) : exemples pondérés, modèles construits l'un après l'autre. On arrête si l'erreur vaut 0 ou dépasse 0,5. Les exemples bien classés voient leur poids multiplié par $e_t/(1-e_t)$, puis les poids sont normalisés : les exemples difficiles gagnent du poids. Vote pondéré : chaque modèle ajoute $-\log\frac{e_t}{1-e_t}$ à sa classe prédite.
- **Forêt aléatoire** : $K$ arbres sur des échantillons tirés avec remise, avec à chaque nœud un tirage de $q$ variables parmi $p$. Vote ou moyenne.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes ; les tableaux météo, les comptes par attribut et les exemples numériques ont été recomptés.

1. **Gini de l'exemple windy** : le calcul du fils « false » écrit $\frac{2}{8}$ puis $\frac{6}{8}$ alors que l'arbre donne 6 oui et 2 non. L'ordre n'a pas d'incidence sur $1 - \sum p_i^2$ : fausse alerte de la transcription. Les comptes (6 oui et 2 non pour windy faux, 3 et 3 pour windy vrai) correspondent bien au tableau de 14 exemples.
2. **Arbre du jeu météo** : recomptage du tableau, sunny 2 oui et 3 non, overcast 4 oui, rainy 3 oui et 2 non. Conforme aux figures. La valeur « normale » de la ligne 10 est une coquille.
3. **Termes d'erreur du filtre anti-spam** : le texte classe les faux positifs en erreur de type I et les faux négatifs en erreur de type II. Cela suppose que « positif » est le rejet de $H_0$ (« spam ») ; un autre choix de $H_0$ échange les types (complément).
4. **Étiquettes « PNG »** dans l'exemple de validation croisée : artefacts de l'interface, pas du contenu.
5. **K-means, algorithme** : l'indice de boucle écrit $k$ et $K$ indifféremment, et $I_W$ ou $I_w$ ; l'ordre « $I \leftarrow I_W$ » puis « calculer $I_W$ » est inversé dans l'image (complément). Le critère d'arrêt ne tient que si $I$ est mis à jour après le calcul de $I_W$.
6. **Entropie, indice de somme** : $m$ puis $k$ pour le nombre de sous-ensembles. Coquille sans conséquence.
7. **Poids du boosting** : les poids initiaux valent $1/N$ (somme 1), mais on normalise ensuite « pour que la somme soit $N$ ». L'autre diapositive dit « pour que la somme reste la même ». Les deux ne sont cohérentes que si la somme initiale est $N$ (poids initiaux de 1) : le cours ne tranche pas (complément).
8. **Figure « Combinaison de plusieurs modèles »** : les échantillons y sont étiquetés « Test Sample » alors que ce sont des échantillons d'apprentissage (déduit du schéma).
9. **Fragments coupés** (diapositives masquées par une barre de navigation, mots coupés) : sans conséquence sur le contenu.
