---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]"]
maj: 2026-11-07
complet: true
---

Résumé du PDF ARBRE AVL ([[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]) (5 pages, diapositives « 9 - Arbres AVL » datées du 26/11/2014, quatre par page, pseudo-code), dans [[Cours/Informatique/Algo/_index|Algo]]. Le texte est en deux colonnes et l'extraction mélange parfois l'ordre : le fond a été recoupé avec le sujet [[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2]] et avec les pages rendues.

## Idée générale

Fiche de cours sur l'[[Arbre AVL]] : définition, facteur d'équilibrage, rotations, insertion et suppression, avec les algorithmes en pseudo-code. Plan : arbre AVL ; facteur d'équilibrage et rotation ; implémentation.

## 1. Définition

> **Définition.**
> - Un arbre AVL est un [[Arbre binaire|arbre binaire]] éventuellement vide tel que la différence de hauteur entre le sous-arbre gauche et le sous-arbre droit d'un nœud diffère d'au plus 1.
> - Les arbres gauche et droit d'un sommet sont des arbres AVL.

Le nom vient des auteurs G.M. Adelson-Velsky et E.M. Landis (1982 selon la diapositive).

> **Propriété.** Si $n$ est le nombre de nœuds d'un arbre AVL, alors sa hauteur est $\log_2(n)$ (vrai en ordre de grandeur seulement, voir « Erreurs du cours »).

![[ARBRE AVL - p1a.jpg]]
*Figure : diapositive de définition, avec trois exemples d'arbres AVL.*

## 2. Facteur d'équilibrage et rotation

Chaque nœud contient un entier, le **facteur d'équilibrage**, qui permet de déterminer s'il faut rééquilibrer l'arbre.

> **Définition.** Soit $s$ un sommet de sous-arbre gauche $G_s$ et droit $D_s$. Le facteur d'équilibrage de $s$ est
> $$eq(s) = h(D_s) - h(G_s)$$
> avec $h(\text{NIL}) = 0$ et, si $A$ est un arbre, $h(A) = \text{hauteur}(A) + 1$.

- Dans un AVL, le facteur d'un nœud vaut $0$, $1$ ou $-1$.
- Lors d'une insertion ou d'une suppression, l'arbre peut se **déséquilibrer** (valeur $2$ ou $-2$) : on utilise alors des rotations.

### Rotations

> **Définition.** Une rotation droite autour du sommet $y$ d'un [[Arbre binaire de recherche|arbre binaire de recherche]] consiste à faire descendre $y$ et à faire remonter son fils gauche $x$ sans invalider l'ordre des éléments. L'opération inverse s'appelle rotation gauche autour du sommet $x$.

![[ARBRE AVL - p1b.jpg]]
*Figure : rotation droite ($y$ racine, $x$ fils gauche de sous-arbres $\alpha$, $\beta$, $\gamma$ à droite de $y$) vers $x$ racine avec $\alpha$ et $y$ (sous-arbres $\beta$, $\gamma$) ; rotation gauche en sens inverse.*

### Facteurs après rotation

Dans la rotation, seuls les facteurs de $X$ et $Y$ sont modifiés. On note $eq'(X)$ et $eq'(Y)$ les facteurs après rotation.

> **Propriété.** Après une rotation droite autour de $Y$ :
> $$eq'(X) = eq(X) + 1 + \max(eq'(Y), 0) \qquad eq'(Y) = eq(Y) + 1 - \min(eq(X), 0)$$

> **Propriété.** Après une rotation gauche autour de $X$ :
> $$eq'(X) = eq(X) - 1 - \max(eq(Y), 0) \qquad eq'(Y) = eq(Y) - 1 + \min(eq'(X), 0)$$

## 3. Insertion

Les opérations d'insertion et de suppression sont celles d'un ABR, auxquelles on ajoute la gestion du facteur d'équilibrage.

L'insertion aboutit à la création d'une feuille $f$. On considère le **premier ancêtre $y$ de cette feuille qui viole la condition AVL** : $eq(y) = -2$ ou $eq(y) = 2$, deux cas symétriques. Supposons $eq(y) = -2$ et soit $x$ le fils gauche de $y$. Deux cas :

- **$eq(x) = -1$ ou $0$** : on effectue une rotation droite (autour de $y$).

![[ARBRE AVL - p2a.jpg]]
*Figure : insertion, rotation droite illustrée sur le cas $eq(x) = 0$ : $y$ (−2) et $x$ (0) ; après la rotation, $x$ a un facteur 1 et $y$ un facteur −1.*

- **$eq(x) = 1$** : $x$ a un sous-arbre droit de racine $z$, qui a deux sous-arbres. On effectue une **rotation gauche autour de $x$**, puis une **rotation droite autour de $y$**.

![[ARBRE AVL - p2b.jpg]]
*Figure : insertion, cas $eq(x) = 1$ : détail du sous-arbre de racine $z$, rotation gauche autour de $x$ ($z$ remonte, facteur −1), puis rotation droite autour de $y$ ; $z$ devient racine de facteur 0.*

## 4. Suppression

- La suppression aboutit à la suppression d'une **feuille**.
- On considère le premier ancêtre $y$ de cette feuille qui viole la condition AVL : $eq(y) = -2$ ou $eq(y) = 2$, deux cas symétriques.
- Supposons $eq(y) = -2$. Soit $x$ le fils gauche de $y$ et $t$ le fils droit de $y$. La feuille a été supprimée dans le sous-arbre de racine $t$. Trois cas :
  - **$eq(x) = -1$** : rotation droite ;
  - **$eq(x) = 0$** : rotation droite aussi ;
  - **$eq(x) = 1$** : $x$ a un sous-arbre droit de racine $z$, qui a deux sous-arbres ; rotation gauche autour de $x$ puis rotation droite autour de $y$.

![[ARBRE AVL - p2c.jpg]]
*Figure : suppression, cas $eq(x) = -1$ : $y$ (−2), $x$ (−1), $t$ ; après la rotation droite, $x$ est racine de facteur 0.*

![[ARBRE AVL - p3a.jpg]]
*Figure : suppression, cas $eq(x) = 0$ : après la rotation droite, $x$ a un facteur 1 et $y$ un facteur −1 (la hauteur du sous-arbre ne change pas).*

![[ARBRE AVL - p3b.jpg]]
*Figure : suppression, cas $eq(x) = 1$ : $y$ (−2), $x$ (1), $z$ fils droit de $x$ avec deux sous-arbres.*

![[ARBRE AVL - p3c.jpg]]
*Figure : suppression, cas $eq(x) = 1$ suite : rotation gauche autour de $x$, puis rotation droite autour de $y$ ; $z$ devient racine de facteur 0, $x$ et $y$ à 0.*

Conséquences :

- Le nouveau sous-arbre a la même hauteur que le sous-arbre de départ si le facteur d'équilibrage de la racine est 0. Dans ce cas, **une seule opération d'équilibrage** suffit pour que l'arbre soit AVL.
- Dans les autres cas, il faut **recommencer la même opération en remontant** dans l'arbre.
- Le cas $eq(y) = 2$ s'obtient par symétrie.
- La diapositive renvoie à des « figures complètes » par un lien (non consulté).

## 5. Implémentation

L'intérêt du facteur d'équilibrage est que cette information nécessite **2 bits**. Néanmoins, les algorithmes de gestion de $eq$ sont délicats. Dans la suite, une cellule d'arbre AVL contient un champ supplémentaire, la **hauteur**.

```text
type celluleAVL = structure
        info: objet;
        hauteur: entier;
        gauche: sommet;
        droit: sommet;
        père: sommet;
     finstructure
sommetAVL = ^celluleAVL;
```

On accède à ce champ par deux primitives :

```text
fonction getHauteur(ref S: sommet): entier;
/* 1 pour une feuille ; 0 si NIL */
fonction setHauteur(ref S: sommet; val h: entier): entier;
/* 1 pour une feuille ; 0 si NIL */
```

### Rotations

Les fonctions implémentant les rotations sont « immédiates ».

```text
fonction rotationDroite(ref y: sommet): vide;
  var x, p: sommet;
  debut
    x = filsGauche(y);
    p = pere(y);
    si p != NIL alors
      si y = filsGauche(p) alors
        p^.gauche = x;
      sinon
        p^.droit = x;
      finsi
    finsi
    x^.pere = p;
    y^.pere = x;
    y^.gauche = x^.droit;
    x^.droit = y;
    setHauteur(y, max(getHauteur(filGauche(y)), getHauteur(filsDroit(y))) + 1);
    setHauteur(x, max(getHauteur(filGauche(x)), getHauteur(filsDroit(x))) + 1);
  fin
```

```text
fonction rotationGauche(ref x: sommet): vide;
  var y, p: sommet;
  début
    y = filsDroit(x);
    p = pere(x);
    si p != NIL alors
      si x = filsGauche(p) alors
        p^.gauche = y;
      sinon
        p^.droit = y;
      finsi
    finsi
    y^.pere = p;
    x^.pere = y;
    x^.droit = y^.gauche;
    y^.gauche = x;
    setHauteur(x, max(getHauteur(filGauche(x)), getHauteur(filsDroit(x))) + 1);
    setHauteur(y, max(getHauteur(filGauche(y)), getHauteur(filsDroit(y))) + 1);
  fin
```

L'ordre des deux `setHauteur` compte : on met d'abord à jour le nœud qui descend.

### Insertion

Les fonctions d'insertion et de suppression doivent prendre en compte le calcul du facteur d'équilibrage et le maintien de l'équilibre.

```text
fonction ajouter(ref x: sommet, val e: objet): vide;
  var s: sommet;
  début
    si e ≤ getValeur(x) alors
      s = filsGauche(x);
      si s == NIL alors
        ajouterFilsGauche(x, e);
        setHauteur(filsGauche(x), 1)
        equilibreAprèsInsertion(filsGauche(x))
      sinon
        ajouter(s, e);
      finsi
    sinon
      s = filsDroit(x);
      si s == NIL alors
        ajouterFilsDroit(x, e);
        setHauteur(filsDroit(x), 1);
        equilibreAprèsInsertion(filsDroit(x))
      sinon
        ajouter(s, e);
      finsi
    finsi
  fin
```

```text
fonction equilibreAprèsInsertion(ref x: sommet): vide;
  var eq: entier;
  var s, p: sommet;
  debut
    eq = 0;
    p = x;
    tantque pere(p) != NIL et eq != 2 et eq != 2 faire
      s = p;
      p = pere(s);
      setHauteur(p, max(getHauteur(filGauche(p)), getHauteur(filsDroit(p))) + 1);
      eq = getHauteur(filsDroit(p)) - getHauteur(filsGauche(p));
    fintantque
    si eq == 2 ou eq == -2 alors
      equilibreUnSommet(p, s);
    finsi
  fin
```

On remonte de la feuille insérée vers la racine en recalculant les hauteurs, jusqu'au premier nœud déséquilibré, qu'on rééquilibre une seule fois.

### Rééquilibrage d'un sommet

```text
fonction equilibreUnSommet(ref p, s: sommet): vide;
  début
    si s == filsGauche(p) alors
      si getEquilibre(p) == -2 alors
        si getEquilibre(s) < 1 alors
          rotationDroite(p);
        sinon
          rotationGauche(s);
          rotationDroite(p);
        finsi
      finsi
    sinon
      si getEquilibre(p) == 2 alors
        si getEquilibre(s) > -1 alors
          rotationGauche(p)
        sinon
          rotationDroite(s);
          rotationGauche(p);
        finsi
      finsi
    finsi
  fin
```

### Suppression

```text
fonction supprimer(ref x: sommet): booléen;
  var p, f, y: sommet;
  début
    si estFeuille(x) alors
      p = pere(x);
      si filsGauche(p) == x alors
        supprimerFilsGauche(p)
        setHauteur(p, getHauteur(filsDroit(p) + 1))
      sinon
        supprimerFilsDroit(p)
        setHauteur(p, getHauteur(filsGauche(p) + 1))
      finsi
      equilibreAprèsSuppression(p)
    sinon
      f = filsDroit(x);
      si f != NIL
        y = cherchePlusPetit(f);
      sinon
        f = filsGauche(x);
        y = cherchePlusGrand(f);
      finsi
      setValeur(x, getValeur(y));
      supprimer(y);
    finsi
  fin
```

Un nœud interne est remplacé par le plus petit de son sous-arbre droit (ou, à défaut, le plus grand de son sous-arbre gauche), puis on supprime ce dernier : on finit toujours par supprimer une feuille.

Dans le cas de la suppression, on remonte à partir de la feuille supprimée et on détecte de la même manière les nœuds déséquilibrés. **Plusieurs rotations peuvent être nécessaires** : un déséquilibre peut en entraîner un autre.

```text
fonction equilibreAprèsSuppression(ref x: sommet): vide;
  var eq: entier;
  var s, p: sommet;
  début
    eq = 1;
    p = x;
    p = pere(s);
    tantque p != NIL et eq != 0 faire
      s = p;
      p = pere(p);
      setHauteur(p, max(getHauteur(filGauche(p)), getHauteur(filsDroit(p))) + 1);
      eq = getHauteur(filsDroit(p)) - getHauteur(filsGauche(p));
      equilibreUnSommet(p, s);
    fintantque
  fin
```

## Liens

Même sujet que [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]] et [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]], et que le sujet [[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2]]. Voir aussi [[Hauteur d'un arbre]] et [[5 - ABR]] pour les opérations d'ABR.

## Erreurs du cours

Le pseudo-code ci-dessus est recopié tel quel ; les erreurs suivantes, relevées dans [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]], n'y sont pas corrigées.

- [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]], `equilibreAprèsInsertion` : écrit « tantque pere(p)!=NIL et eq!=2 et eq!=2 » ; il faut « eq!=2 et eq!=-2 », pour que la boucle s'arrête dans les deux cas de déséquilibre.
- [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]], `equilibreAprèsSuppression` : écrit `p=x;` puis `p=pere(s);`, alors que `s` n'a encore reçu aucune valeur ; il faut supprimer cette ligne (ou écrire `s=x`). La condition d'arrêt `eq!=0` est elle aussi discutable : un facteur nul après mise à jour ne garantit pas que la hauteur du sous-arbre est restée la même (complément).
- [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]], `supprimer` : écrit `setHauteur(p,getHauteur(filsDroit(p)+1))` (et de même avec `filsGauche`) ; il faut `setHauteur(p,getHauteur(filsDroit(p))+1)`. Le cas où la feuille supprimée est la racine (sans père) n'est pas traité. Coquille `filGauche` pour `filsGauche` dans plusieurs fonctions.
- [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]], propriété : écrit « Si n est le nombre de nœuds d'un arbre AVL alors sa hauteur est log2(n) » ; il faut « de l'ordre de $\log_2(n)$ » : la borne précise est $\log_2(1+n) \le 1+h \le 1{,}44\log_2(2+n)$ (voir [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]).
- [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]], insertion : écrit « soit eq(x)=-1 ou 0, on effectue une rotation droite », et illustre le cas $eq(x) = 0$ ; il faut « eq(x) = −1 » seulement : juste après une insertion, $eq(x) = 0$ ne peut pas se produire (ce cas ne survient qu'à la suppression). Même remarque que pour [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]], point 4 (complément).
