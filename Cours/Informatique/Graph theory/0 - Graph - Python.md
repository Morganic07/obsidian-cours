---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Notes de TP en Python, sans image : dictionnaires, représentation d'un graphe (matrice d'adjacence ou dictionnaire de voisins), fonctions de test sur les chaînes et les graphes, puis algorithme de Kruskal avec Union-Find. Les définitions viennent de [[1 - Undirected graph]] et [[2 - tree]]. L'indentation du code, perdue dans la note, est reconstituée ici ; les erreurs du code de la note sont corrigées dans les blocs (marque ✎).

## Dictionnaires Python

Voir [[Dictionnaire (Python)]]. Dans `{"nom": "Michel", "age": 33}`, `"nom"` est une **clé**, `"Michel"` une **valeur**. [[Erreurs du cours#^e-0-graph-python|✎]]

```python
dic = {"nom": "Michel", "age": 33}

print(dic)            # {'nom': 'Michel', 'age': 33}
print(dic["nom"])     # Michel
print(dic["Michel"])  # erreur : "Michel" est une valeur, pas une clé

dic["numéro"] = ...   # ajoute une clé et sa valeur (numéro de téléphone dans la note)

for clé in dic.keys():          # toutes les clés : nom, age, numéro
    print(clé)

for clé, valeur in dic.items(): # clés et valeurs
    print(clé, ":", valeur)     # nom : Michel / age : 33 / numéro : ...
```

- On accède à une valeur **par sa clé**, pas l'inverse.
- `keys()` donne les clés, `items()` les couples (clé, valeur).
- L'erreur levée par `dic["Michel"]` est une `KeyError`. Pour l'éviter : tester d'abord `if "Michel" in dic:` (`in` cherche parmi les **clés**), ou écrire `dic.get("Michel", valeur_par_défaut)`, qui renvoie la valeur par défaut (`None` si on n'en donne pas) au lieu d'échouer. `values()` donne les valeurs seules. [[Complément hors du cours|ⓘ]]
- Un dictionnaire est une [[Table de hachage|table de hachage]] : l'accès, l'ajout et le test `in` par clé prennent en moyenne un temps constant, quelle que soit la taille. En contrepartie, une clé doit être **immuable** (entier, chaîne, tuple) : une liste ne peut pas servir de clé. Depuis Python 3.7, le dictionnaire garde l'ordre d'insertion des clés. [[Complément hors du cours|ⓘ]]

## Algorithmes

### 1. Afficher sommets et arêtes depuis une matrice d'adjacence

Représentation par [[Matrice d'adjacence|matrice d'adjacence]] (ici le triangle complet à 3 sommets) :

```python
graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

def showStruct(mat):
    nbNodes = len(mat)  # récupère le nombre de nœuds
    print("Number of nodes " + str(nbNodes))
    for i in range(nbNodes):
        print("v" + str(i), end=" ")
    print("")
    print("List of edges: ")
    for i in range(nbNodes):
        for j in range(nbNodes):
            if mat[i][j] == 1 and i < j:  # arête existante, sans doublon (v1--v2 / v2--v1) ni boucle (v0--v0)
                print("v" + str(i) + "-- v" + str(j) + " ")

showStruct(graph)
```

Le test porte sur la case `mat[i][j]` (l'arête existe-t-elle ?) et sur les indices (`i < j`), comme `node < neighbor` dans la version à dictionnaire. [[Erreurs du cours#^e-0-graph-python|✎]]

### 2. Afficher sommets et arêtes depuis un dictionnaire

Représentation par dictionnaire : **chaque clé est un sommet, sa valeur est la liste de ses voisins**. [[Erreurs du cours#^e-0-graph-python|✎]]

C'est la **[[Liste d'adjacence|liste d'adjacence]]**. Comparaison avec la matrice, pour $n$ sommets et $m$ arêtes : [[Complément hors du cours|ⓘ]]

| | Matrice d'adjacence | Dictionnaire de voisins |
|---|---|---|
| Mémoire | $n^2$ cases | proportionnelle à $n + m$ |
| « $v_1$ et $v_2$ sont-ils voisins ? » | `mat[v1][v2]`, temps constant | `v2 in dic[v1]`, parcourt les voisins de `v1` |
| Lister les voisins de $v$ | parcourir toute la ligne ($n$ cases) | `dic[v]` directement |
| Adapté à | graphes denses | graphes creux (réseaux routiers, sociaux) |

Chaque arête apparaît **deux fois** dans le dictionnaire (`1` dans `dic[0]` et `0` dans `dic[1]`) : il faut tenir les deux listes à jour quand on ajoute une arête. Remplacer les listes par des ensembles (`{0: {1, 2}, …}`) rend le test `v2 in dic[v1]` presque instantané. [[Complément hors du cours|ⓘ]]

```python
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

def showStruct(dic):
    print("Nodes :")
    for node in dic.keys():  # liste des clés = liste des nœuds
        print("v" + str(node), end=" ")
    print("")
    print("Edges :")
    for node in dic.keys():           # double boucle sur les listes de voisins
        for neighbor in dic[node]:
            if (node < neighbor):     # n'affiche chaque arête qu'une fois, et pas les boucles
                print("v" + str(node) + "--- v" + str(neighbor))

showStruct(graph)
```

### 3. Vérifier qu'une liste de nœuds est une chaîne

Voir [[Chaîne (graphe)]]. On vérifie que chaque sommet suivant est **voisin** du précédent.

```python
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
nodes_user_choice = [0, 1, 2]  # la séquence 0 -> 1 -> 2 est-elle une chaîne ?

def isChain(dic, nodes):
    for i in range(len(nodes) - 1):  # on s'arrête à len(nodes)-1 car on lit nodes[i+1]
        v1 = nodes[i]       # sommet de départ de l'étape courante
        v2 = nodes[i + 1]   # sommet d'arrivée de l'étape courante
        if v2 not in dic[v1]:  # v2 n'est pas voisin de v1 : pas une chaîne
            return False
    return True  # toute la liste parcourue sans problème : c'est une chaîne

print(isChain(graph, nodes_user_choice))  # True
```

Cas limites : une liste d'un seul sommet, ou vide, renvoie `True` sans entrer dans la boucle (`range(0)` est vide) ; une liste d'un seul sommet correspond bien à la chaîne de longueur 0 du cours. Un sommet absent du graphe fait lever une `KeyError` sur `dic[v1]`. [[Complément hors du cours|ⓘ]]

### 4. Autres fonctions d'entraînement

**Voisinage** (deux versions, dictionnaire et matrice, sous deux noms distincts) : [[Erreurs du cours#^e-0-graph-python|✎]]

```python
def estVoisinDic(v1, v2, dic):
    return v2 in dic[v1]

def estVoisinMat(v1, v2, mat):
    return mat[v1][v2] == 1
```

Python ne connaît pas la surcharge de fonctions : deux définitions sous le même nom `estVoisin`, la seconde **remplacerait** la première. `estChaine` ci-dessous appellerait alors la version matrice avec un dictionnaire ; `dic[v1][v2]` lirait l'élément d'indice `v2` de la liste des voisins (ou lèverait une `IndexError`), ce qui ne teste pas l'adjacence. [[Complément hors du cours|ⓘ]]

**Chaîne, chaîne élémentaire, chaîne simple** (une chaîne simple est d'abord une chaîne : `isSimpleChain` commence par appeler `estChaine`) : [[Erreurs du cours#^e-0-graph-python|✎]]

```python
def estChaine(dic, list_nodes):
    for i in range(len(list_nodes) - 1):
        if estVoisinDic(list_nodes[i], list_nodes[i + 1], dic) == False:
            return False
    return True

def estChaineElementaire(dic, list_nodes):
    if not estChaine(dic, list_nodes):
        return False
    return len(list_nodes) == len(set(list_nodes))  # tous les sommets distincts

def isSimpleChain(dic, list_nodes):
    if not estChaine(dic, list_nodes):
        return False
    lg = len(list_nodes)
    aretes = []
    for i in range(lg - 1):
        v1 = list_nodes[i]
        v2 = list_nodes[i + 1]
        if (v1, v2) in aretes or (v2, v1) in aretes:  # arête déjà utilisée
            return False
        aretes.append((v1, v2))
    return True
```

- Chaîne **élémentaire** : sommets deux à deux distincts, testé en comparant la longueur de la liste à celle de l'ensemble (`set`).
- Chaîne **simple** : arêtes deux à deux distinctes, dans un sens ou dans l'autre.
- Sans l'appel initial à `estChaine`, `isSimpleChain` ne vérifierait que la répétition des arêtes, pas que la suite est une chaîne : `[0, 5, 9]` passerait même sans arête 0–5. Elle suppose aussi le graphe simple : avec deux arêtes parallèles entre les mêmes sommets, une liste de sommets ne dit pas laquelle est empruntée. [[Complément hors du cours|ⓘ]]

**Graphe complet** (voir [[Graphe complet]]) : chaque sommet a $n - 1$ voisins (un nœud ne peut pas être voisin de lui-même).

```python
def isGraphFull(dic):
    n = len(dic)
    for node in dic:  # pour chaque nœud, le nombre de voisins doit valoir n-1
        if len(dic[node]) != n - 1:
            return False
    return True

def isGraphFull2(dic):
    n = len(dic)
    for i in dic.keys():
        if not len(dic[i]) == n - 1:
            return False
    return True

def infoGraphFull(dic):
    if not isGraphFull(dic):
        return "Le graphe n'est pas complet"
    else:
        n = len(dic)
        print("nombre de noeuds", n)
        print("degré : ", n - 1)
        nbAretes = n * (n - 1) / 2
        print("nombre d'arêtes : ", nbAretes)
```

En Python 3, `/` renvoie toujours un nombre à virgule : pour $n = 3$, le programme affiche `3.0`. La division entière `//` donne `3` ; elle est exacte ici, car $n(n-1)$ est un produit de deux entiers consécutifs, donc pair. Le test par les degrés suppose le graphe simple : une boucle ou un voisin écrit deux fois fausserait le compte de `len(dic[node])`. [[Complément hors du cours|ⓘ]]

**Degré** (on suppose le graphe simple ; voir [[Degré d'un sommet]]) :

```python
def degre(dic, v):
    return len(dic[v])
```

D'après le [[Lemme des poignées de main|lemme des poignées de main]], la somme des degrés vaut deux fois le nombre d'arêtes, d'où le nombre d'arêtes d'un graphe simple : `sum(len(voisins) for voisins in dic.values()) // 2`. [[Complément hors du cours|ⓘ]]

**Graphe biparti** (voir [[Graphe biparti]]) : [[Parcours en largeur|parcours en largeur]] qui colorie chaque sommet de 0 ou 1 ; chaque voisin reçoit la couleur opposée ; deux voisins de même couleur → pas biparti. La boucle externe traite chaque composante connexe.

```python
def isGraphBipartite(dic):
    tables = {}
    for sommet_depart in dic:
        if sommet_depart not in tables:
            tables[sommet_depart] = 0
            a_traiter = [sommet_depart]
            while len(a_traiter) > 0:
                sommet_actuel = a_traiter.pop(0)
                for voisin in dic[sommet_actuel]:
                    if voisin not in tables:
                        tables[voisin] = 1 - tables[sommet_actuel]
                        a_traiter.append(voisin)
                    elif tables[voisin] == tables[sommet_actuel]:
                        return False
    return True
```

(Le placement exact de `a_traiter` et du `while` sous le `if` est reconstitué : c'est la seule lecture qui fait fonctionner l'algorithme.)

`a_traiter` joue le rôle d'une **file** ([[Pile et file]]) : on retire au début (`pop(0)`), on ajoute à la fin (`append`). Mais `pop(0)` décale tous les éléments de la liste ; `collections.deque` et sa méthode `popleft()` font la même chose en temps constant. Avec elle, le test entier coûte $O(n + m)$ : chaque sommet entre une fois dans la file et chaque liste de voisins est lue une fois. [[Complément hors du cours|ⓘ]]

Le `elif` repère une arête entre deux sommets de même couleur, ce qui révèle un cycle de longueur impaire : c'est la caractérisation du cours (biparti si et seulement si tout cycle est pair). [[Complément hors du cours|ⓘ]]

## Algorithme de Kruskal

Voir [[Algorithme de Kruskal]], [[Union-Find]] et [[Arbre couvrant minimal]]. Le graphe est une **liste d'arêtes** `[u, v, w]` (sommet 1, sommet 2, poids).

### 1. Ajouter une arête

```python
def add_edge(graph, u, v, w):  # u et v : les sommets ; w : le poids
    graph.append([u, v, w])    # on agrandit la liste d'un élément [ville_A, ville_B, prix]
```

### 2. Trouver le représentant d'un groupe (récursif)

```python
def find_parent(parent, i):
    # Condition d'arrêt (point fixe) : i est la racine de sa composante connexe
    # si et seulement si parent[i] == i.
    if parent[i] == i:
        return i
    # Sinon, parent[i] est son ascendant direct : on remonte dans l'arborescence.
    return find_parent(parent, parent[i])
```

Voir [[Point fixe]] et [[Récursivité]].

Le tableau `parent` code une [[Forêt (graphe)|forêt]] : chaque groupe de sommets déjà reliés est un arbre, dont la racine sert de **représentant**. Deux sommets sont dans le même groupe si et seulement si `find_parent` leur renvoie la même racine. [[Complément hors du cours|ⓘ]]

Amélioration classique, la **compression de chemin** : en remontant, on rattache directement chaque sommet visité à la racine, ce qui raccourcit les recherches suivantes. Il suffit de remplacer la dernière ligne par `parent[i] = find_parent(parent, parent[i])` puis `return parent[i]`. Combinée à l'union par rang, elle rend chaque opération quasi constante en coût amorti (le coût croît comme l'inverse de la fonction d'Ackermann, qui ne dépasse pas 4 pour toute taille réaliste). [[Complément hors du cours|ⓘ]]

### 3. Fusionner deux groupes (union par rang)

```python
def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)
    # Pour éviter les chaînes trop longues, on compare la hauteur (rank) des groupes.
    if rank[xroot] < rank[yroot]:     # groupe de Y plus profond : X sous Y
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:   # groupe de X plus profond : Y sous X
        parent[yroot] = xroot
    else:                             # même hauteur : Y sous X, et X gagne un niveau
        parent[yroot] = xroot
        rank[xroot] += 1
```

Ce que garantit l'union par rang : un arbre de rang $r$ contient au moins $2^r$ sommets (le rang n'augmente que quand on fusionne deux arbres de même rang, ce qui double au moins la taille). La hauteur reste donc au plus $\log_2 n$, et `find_parent` fait au plus $\log_2 n$ appels récursifs : environ 20 pour un million de sommets, loin de la limite de récursion de Python (1000 appels par défaut). [[Complément hors du cours|ⓘ]]

### 4. Kruskal

```python
def kruskal(graph, V):
    result = []  # routes retenues
    i = 0        # indice dans la liste triée des routes
    e = 0        # nombre d'arêtes déjà acceptées
    # Étape 1 : tri glouton par coût (élément d'indice 2)
    graph = sorted(graph, key=lambda item: item[2])
    # Étape 2 : chaque ville est son propre parent ; hauteur 0
    parent = [i for i in range(V)]   # par exemple [0, 1, 2, 3] pour 4 villes
    rank = [0] * V
    # Étape 3 : il faut exactement V - 1 arêtes pour relier V sommets sans cycle
    while e < V - 1:
        u, v, w = graph[i]   # prochaine route la moins chère
        i = i + 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)
        # Test anti-cycle : racines différentes, les villes ne sont pas encore reliées
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    return result  # le réseau optimal
```

Déroulé : trier les arêtes ; initialiser `parent` et `rank` ; tant qu'on n'a pas $V - 1$ arêtes, prendre la moins chère ; si ses extrémités ont des racines différentes, la garder et fusionner les groupes, sinon la rejeter (elle créerait un cycle).

Points implicites du code : les sommets doivent être numérotés de `0` à `V - 1`, puisqu'ils servent d'indices dans `parent` et `rank` (des villes nommées se traduisent d'abord en numéros, par exemple avec un dictionnaire). Le `i` de la compréhension `[i for i in range(V)]` est local à celle-ci en Python 3 : il ne modifie pas le compteur `i = 0` défini juste avant. `sorted` renvoie une nouvelle liste triée sans toucher à la liste d'origine (contrairement à `graph.sort()`). [[Complément hors du cours|ⓘ]]

Coût : le tri, en $O(m \log m)$ pour $m$ arêtes, domine ; les appels à `find_parent` et `union` sont en $O(\log V)$ grâce à l'union par rang. On retrouve la complexité $O(\text{card}\,E \cdot \log \text{card}\,V)$ du [[2 - tree|chapitre 2]]. [[Complément hors du cours|ⓘ]]
