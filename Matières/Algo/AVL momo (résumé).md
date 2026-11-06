---
type: source
tags: [year2]
sources: ["[[AVL momo]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[AVL momo]], dans [[Algo (matière)]]. Note étudiante de préparation d'un exposé sur les arbres AVL (voir [[qui dit quoi AVL (résumé)|qui dit quoi AVL]]), avec des extraits de l'amphi et le code [[Langage Python|Python]] des fonctions. En cas d'écart, le cours et ses images font foi.

## Idée générale

Un [[Arbre AVL]] est un [[Arbre binaire de recherche|arbre binaire de recherche]] équilibré : à chaque ajout ou suppression d'un nœud, l'arbre conserve un équilibre de hauteur. Pour chaque nœud, la différence de hauteur de ses deux sous-arbres est au maximum 1 (comprise entre $-1$ et $1$). Si l'arbre est équilibré, la hauteur est en $O(\log n)$, où $n$ est le nombre de nœuds.

## Hauteur et facteur d'équilibrage

- **Hauteur** ([[Hauteur d'un arbre]]) : $h = 1 + \max(h_{\text{gauche}}, h_{\text{droite}})$ ; si le sous-arbre est `None`, $h = -1$.
- **Facteur d'équilibrage** : différence de hauteur des sous-arbres.
  - « Aux US », on calcule $eq = h(\text{gauche}) - h(\text{droite})$ ;
  - ici, « comme la prof » : $eq = h(\text{droite}) - h(\text{gauche})$.
- Si $eq \in \{-1, 0, 1\}$ en chaque nœud, l'arbre est équilibré. Si $eq = 2$ ou $-2$, il y a déséquilibre et interviennent les rotations.

## Ajout et suppression

- **Ajout** : on fait comme pour un ABR, puis on calcule le facteur d'équilibrage, puis on fait une rotation si besoin.
- **Suppression** : même démarche (suppression d'ABR, calcul du facteur, rotation).
- Les rotations sont les mêmes pour un ajout ou une suppression, car elles dépendent du facteur d'équilibrage obtenu après l'opération.

## Propriété de hauteur (amphi)

> **Propriété.** Soit $A$ un arbre AVL ayant $n$ sommets et de hauteur $h$. Alors
> $$\log_2(1+n) \le 1 + h \le \alpha \log_2(2+n), \quad \text{avec } \alpha \le 1{,}44.$$
> Par exemple, si $n = 100000$, $17 \le h \le 25$.
> On a toujours $n \le 2^{h+1} - 1$, donc $\log_2(1+n) \le 1 + h$.

## Nombre de rotations

- Pour rééquilibrer un AVL après une **insertion**, une seule rotation ou double rotation suffit.
- Après une **suppression**, il faut jusqu'à $h$ rotations ou doubles rotations ($h$ : hauteur de l'arbre).

## Algorithme de rééquilibrage (amphi 9, diapo 15)

Soit $A$ un arbre, $G$ et $D$ ses sous-arbres gauche et droit, avec $|h(G) - h(D)| = 2$.

- Si $h(G) - h(D) = 2$ : on fait une **rotation droite**. Soient $g$ et $d$ les sous-arbres gauche et droit de $G$ ; si $h(g) < h(d)$, on fait d'abord une **rotation gauche de $G$**.
- Si $h(G) - h(D) = -2$ : opérations symétriques.

(Ici la convention est gauche moins droite.)

Vidéos citées : « Insertion dans un AVL » et « Suppression dans un AVL » (liens YouTube dans la note, non consultés).

## Rotations

> **Définition.** Une rotation droite autour du sommet $y$ d'un arbre binaire de recherche consiste à faire descendre $y$ et à faire remonter son fils gauche $x$ sans invalider l'ordre des éléments. L'opération inverse s'appelle rotation gauche autour du sommet $x$.

![[Cours/Year 2/Algo/DM/medias/AVL momo/image3.png]]
*Figure : rotation droite : $y$ (fils gauche $x$ de sous-arbres $\alpha$, $\beta$ ; sous-arbre droit $\gamma$) devient $x$ racine, avec $\alpha$ à gauche et $y$ à droite (sous-arbres $\beta$, $\gamma$) ; la rotation gauche fait l'inverse.*

## Cas à l'insertion (convention droite moins gauche)

Les opérations d'insertion et de suppression sont celles d'un ABR, auxquelles on ajoute la gestion du facteur d'équilibrage. L'insertion crée une feuille $f$. On considère le **premier ancêtre $y$ de cette feuille qui viole la condition AVL** : $eq(y) = -2$ ou $eq(y) = 2$, deux cas symétriques. Supposons $eq(y) = -2$ et soit $x$ le fils gauche de $y$.

### Cas 1 : $eq(x) = -1$ ou $0$ : rotation droite

![[Cours/Year 2/Algo/DM/medias/AVL momo/image4.png]]
*Figure : rotation droite autour de $y$ (−2) ; $x$ (0) remonte en racine avec le sous-arbre vert à gauche, $y$ passe à droite avec les sous-arbres rouge et jaune ; facteurs après rotation $x = 1$, $y = -1$.*

### Cas 2 : $eq(x) = 1$ : double rotation

$x$ a un sous-arbre droit de racine $z$, qui a deux sous-arbres. On effectue une **rotation gauche autour de $x$**, puis une **rotation droite autour de $y$**.

![[Cours/Year 2/Algo/DM/medias/AVL momo/image8.png]]
*Figure : double rotation : $y$ (−2), $x$ (1), $z$ fils droit de $x$ ; après la rotation gauche autour de $x$, $z$ devient fils gauche de $y$ ; après la rotation droite autour de $y$, $z$ (0) est racine avec $x$ à gauche et $y$ à droite.*

### Pseudo-code

```text
IF tree is right heavy
{
  IF tree's right subtree is left heavy
  {
     Perform Double Left rotation
  }
  ELSE
  {
     Perform Single Left rotation
  }
}
ELSE IF tree is left heavy
{
  IF tree's left subtree is right heavy
  {
     Perform Double Right rotation
  }
  ELSE
  {
     Perform Single Right rotation
  }
}
```

- *Double left* : rotation droite puis rotation gauche (right → left).
- *Double right* : rotation gauche puis rotation droite (left → right).

## Complexité des fonctions

![[Cours/Year 2/Algo/DM/medias/AVL momo/image7.png]]
*Figure : dépendances entre fonctions : `hauteur` → `fact_equilibrage` ; `fact_equilibrage`, `rotation_gauche` et `rotation_droite` → `equilibrer` ; `equilibrer` → `ajouter` et `supprimer` ; `trouver_min` → `supprimer`.*

Démarche : pour la [[Complexité algorithmique|complexité]] de `ajouter()` ou `supprimer()`, il faut celle de `hauteur()`, qui donne celle de `fact_equi()`, puis celle des rotations, pour calculer celle de `equilibrer()`.

### `hauteur` et `facteur_equilibrage` : $O(n)$ selon la note

```python
def hauteur(self):
    left_height = self.left.hauteur() if self.left else 0
    right_height = self.right.hauteur() if self.right else 0
    return 1 + max(left_height, right_height)

def facteur_equilibrage(self):
    return (self.right.hauteur() if self.right else 0) - (self.left.hauteur() if self.left else 0)
```

Justification (en anglais dans la note, d'allure générée) : `hauteur()` parcourt récursivement chaque nœud une fois, d'où $O(n)$ ; `facteur_equilibrage()` appelle deux fois `hauteur()`, donc $O(n)$ aussi.

### Rotations : $O(1)$

```python
def rotation_droit(self):
    new_root = self.left
    self.left = new_root.right
    new_root.right = self
    return new_root
```

Suite d'opérations en temps constant (affectations, mises à jour de références) : $O(1)$. Pareil pour `rotation_gauche()`.

### `rebalance` : $O(\log n)$ selon la note

```python
def rebalance(self):
    balance = self.facteur_equilibrage()

    if balance < -1:
        if self.left and self.left.facteur_equilibrage() > 0:
            self.left = self.left.rotation_gauche()   # rotation gauche-droite
        return self.rotation_droit()

    if balance > 1:
        if self.right and self.right.facteur_equilibrage() < 0:
            self.right = self.right.rotation_droit()  # rotation droite-gauche
        return self.rotation_gauche()

    return self
```

Justification de la note (en anglais, d'allure générée) : les rotations se font selon le facteur d'équilibrage des nœuds, donc $O(\log n)$. Voir point à vérifier 1.

La note s'arrête là : la complexité finale de `ajouter` et `supprimer` n'est pas écrite.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 1 (propriété de hauteur) a été ouverte ; les autres sont lues par leur transcription.

1. **Complexité de `rebalance`** (complément). **À corriger avant un examen.** La note annonce $O(\log n)$ avec une justification faible. Dans le code donné, `rebalance` appelle `facteur_equilibrage`, qui appelle `hauteur` deux fois, et `hauteur` parcourt tout le sous-arbre. `rebalance` est donc en $O(n)$ dans ce code. Elle n'est en $O(1)$ que si la hauteur est stockée dans chaque nœud. L'autre note de l'exposé, [[qui dit quoi AVL]], dit $O(1)$ : les deux notes se contredisent.
2. **Convention de hauteur** : la formule écrit $h = -1$ pour un sous-arbre vide, mais le code renvoie 0 pour un sous-arbre vide, donc 1 pour une feuille. La propriété $\log_2(1+n) \le 1 + h$ suppose qu'une feuille a $h = 0$.
3. **Exemple chiffré de la propriété** : image lue directement, « si $n = 100000$, $17 \le h \le 25$ ». Avec les formules écrites au-dessus, on trouve environ $16 \le h \le 22$ (complément). Les bornes de l'amphi ne suivent donc pas exactement ses formules.
4. **Facteurs après rotation** : la transcription juge incohérents $x = 1$ et $y = -1$ pour le cas $eq(x) = 0$. Fausse alerte (complément) : avec les sous-arbres de hauteurs $h+1$, $h+1$ et $h$, le calcul donne bien $x = 1$ et $y = -1$. Ce cas n'arrive qu'à la suppression.
5. **Étiquettes d'équilibre de la double rotation** : lues avec incertitude par la transcription, non vérifiées.
6. **Liens vidéo** (insertion et suppression) : non consultés.
7. **Deux conventions dans la même note** (complément) : l'algorithme de l'amphi (diapo 15) raisonne en $h(G) - h(D)$, les cas d'insertion et le code en droite moins gauche. Bien repérer la convention avant d'appliquer une règle de rotation.
