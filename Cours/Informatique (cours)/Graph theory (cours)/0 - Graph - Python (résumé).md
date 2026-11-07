---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]], dans [[Graph theory (index)]]. Notes de TP en Python, sans image : dictionnaires, représentation d'un graphe (matrice d'adjacence ou dictionnaire de voisins), fonctions de test sur les chaînes et les graphes, puis algorithme de Kruskal avec Union-Find. Les définitions viennent de [[1 - Undirected graph (résumé)]] et [[2 - tree (résumé)]]. L'indentation du code, perdue dans la note, est reconstituée ici ; le code est par ailleurs recopié tel quel, erreurs comprises (voir Points à vérifier).

## Dictionnaires Python

Voir [[Dictionnaire (Python)]]. Dans `{"nom": "Michel", "age": 33}`, `"nom"` est une **clé**, `"Michel"` une **valeur**.

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
            if (mat[i] < mat[j]):  # censé éliminer les doublons (v1--v2 / v2--v1) et les boucles (v0--v0)
                print("v" + str(i) + "-- v" + str(j) + " ")

showStruct(graph)
```

(le test `mat[i] < mat[j]` est faux : voir Points à vérifier, 1).

### 2. Afficher sommets et arêtes depuis un dictionnaire

Représentation par dictionnaire : **chaque clé est un sommet, sa valeur est la liste de ses voisins**.

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

### 4. Autres fonctions d'entraînement

**Voisinage** (deux versions, dictionnaire et matrice) :

```python
def estVoisin(v1, v2, dic):
    return v2 in dic[v1]

def estVoisin(v1, v2, mat):
    return mat[v1][v2] == 1
```

**Chaîne, chaîne élémentaire, chaîne simple :**

```python
def estChaine(dic, list_nodes):
    for i in range(len(list_nodes) - 1):
        if estVoisin(list_nodes[i], list_nodes[i + 1], dic) == False:
            return False
    return True

def estChaineElementaire(dic, list_nodes):
    if not estChaine(dic, list_nodes):
        return False
    return len(list_nodes) == len(set(list_nodes))  # tous les sommets distincts

def isSimpleChain(dic, list_nodes):
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

**Degré** (on suppose le graphe simple ; voir [[Degré d'un sommet]]) :

```python
def degre(dic, v):
    return len(dic[v])
```

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Affichage par matrice** : le test `if (mat[i] < mat[j])` compare deux lignes de la matrice (des listes), non des indices. Le commentaire annonce l'élimination des doublons et des boucles, ce que fait `node < neighbor` dans la version à dictionnaire. Pour la matrice, il faudrait tester `mat[i][j] == 1 and i < j` (complément).
2. **Version à dictionnaire** : le dernier `print` est écrit sans parenthèse fermante.
3. **`kruskal`** : la boucle lit `graph[i]` sans vérifier que `i` reste dans la liste. Sur un graphe non connexe, l'indice dépasse la taille de la liste (complément). Le cours suppose le graphe connexe (préconditions de Kruskal).
4. **`isGraphFull`** : suppose un graphe simple (commentaire de la note). Une boucle ou une arête multiple fausserait le test.
5. **Sorties** : les affichages de la note ne sont pas identiques à ceux du code (« Age » et « Numero » avec majuscules). Écart d'affichage sans importance.
6. Le code des autres fonctions n'a pas été exécuté ici, sauf lecture.
7. **Indentation reconstituée** : la note a perdu l'indentation du code ; celle de cette fiche est déduite de la logique (en particulier dans `isGraphBipartite` et `kruskal`). La note écrit aussi `For clé, valeur in ...` avec une majuscule, qui provoquerait une erreur en Python.
8. **Valeur du numéro** : la note ajoute à l'exemple un numéro de téléphone, non recopié ici ; écrit sans guillemets et commençant par 0, il provoquerait une erreur de syntaxe en Python 3 (complément).
9. **`infoGraphFull`** : `n * (n - 1) / 2` renvoie un flottant ; `//` donnerait un entier (complément).
