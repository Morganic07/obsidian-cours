---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du PDF ARBRE AVL ([[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]) (5 pages, diapositives « 9 - Arbres AVL » datées du 26/11/2014, quatre par page, pseudo-code), dans [[Cours/Informatique/Algo/_index|Algo]]. Le texte est en deux colonnes et l'extraction mélange parfois l'ordre : le fond a été recoupé avec le sujet [[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2]] et avec les pages rendues.

## Idée générale

Fiche de cours sur l'[[Arbre AVL]] : définition, facteur d'équilibrage, rotations, insertion et suppression, avec les algorithmes en pseudo-code. Plan : arbre AVL ; facteur d'équilibrage et rotation ; implémentation.

## 1. Définition

> **Définition.**
> - Un arbre AVL est un [[Arbre binaire|arbre binaire]] éventuellement vide tel que la différence de hauteur entre le sous-arbre gauche et le sous-arbre droit d'un nœud diffère d'au plus 1.
> - Les arbres gauche et droit d'un sommet sont des arbres AVL.

Le nom vient des auteurs G.M. Adelson-Velsky et E.M. Landis, qui l'ont publié en 1962 (« An algorithm for the organization of information », *Doklady Akademii Nauk SSSR*). [[Erreurs du cours#^e-6-avl|✎]]

> **Propriété.** Si $n$ est le nombre de nœuds d'un arbre AVL, alors sa hauteur $h$ est de l'ordre de $\log_2(n)$ : précisément, $\log_2(1+n) \le 1+h \le 1{,}44\log_2(2+n)$. [[Erreurs du cours#^e-6-avl|✎]]

L'AVL est un [[Arbre binaire de recherche|ABR]] (la définition ci-dessus ne le dit pas, mais les rotations et l'insertion le supposent) auquel on ajoute cette condition d'équilibre. Son but : éviter l'ABR dégénéré, de hauteur $n - 1$, que produit par exemple l'insertion de valeurs déjà triées (voir [[5 - ABR]]), et garantir que recherche, insertion et suppression restent en $O(\log n)$. [[Complément hors du cours|ⓘ]]

Pourquoi la hauteur reste logarithmique (hauteur d'une feuille = 0) : notons $N(h)$ le plus petit nombre de nœuds d'un AVL de hauteur $h$. Le plus « creux » des AVL de hauteur $h$ a une racine, un sous-arbre de hauteur $h - 1$ et l'autre de hauteur $h - 2$, eux-mêmes minimaux : [[Complément hors du cours|ⓘ]]
$$N(0) = 1, \quad N(1) = 2, \quad N(h) = 1 + N(h-1) + N(h-2)$$
On trouve $N(h) = F_{h+3} - 1$, où $F_k$ est la [[Suite de Fibonacci|suite de Fibonacci]] ($F_1 = F_2 = 1$) : 1, 2, 4, 7, 12, 20… Ces arbres minimaux sont appelés **arbres de Fibonacci**. Comme $F_k$ croît comme $\varphi^k$ avec $\varphi = \frac{1 + \sqrt 5}{2} \approx 1{,}618$, un AVL de $n$ nœuds vérifie $h \lesssim \log_\varphi n \approx 1{,}44 \log_2 n$ : au pire 44 % plus haut qu'un arbre parfait. C'est l'origine du coefficient 1,44 de la borne de la propriété. [[Complément hors du cours|ⓘ]]

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

Pourquoi l'ordre est préservé : avant comme après la rotation, toute clé de $\alpha$ est inférieure à $x$, $x$ est inférieur à toute clé de $\beta$, ces clés sont inférieures à $y$, et $y$ est inférieur à toute clé de $\gamma$. Le parcours infixe reste $\alpha, x, \beta, y, \gamma$ : l'arbre reste un ABR. Seul $\beta$ change de père (il passe de $x$ à $y$). Une rotation ne modifie qu'un nombre fixe de pointeurs : elle se fait en temps constant, $O(1)$. [[Complément hors du cours|ⓘ]]

### Facteurs après rotation

Dans la rotation, seuls les facteurs de $X$ et $Y$ sont modifiés. On note $eq'(X)$ et $eq'(Y)$ les facteurs après rotation.

> **Propriété.** Après une rotation droite autour de $Y$ :
> $$eq'(X) = eq(X) + 1 + \max(eq'(Y), 0) \qquad eq'(Y) = eq(Y) + 1 - \min(eq(X), 0)$$

> **Propriété.** Après une rotation gauche autour de $X$ :
> $$eq'(X) = eq(X) - 1 - \max(eq(Y), 0) \qquad eq'(Y) = eq(Y) - 1 + \min(eq'(X), 0)$$

## 3. Insertion

Les opérations d'insertion et de suppression sont celles d'un ABR, auxquelles on ajoute la gestion du facteur d'équilibrage.

L'insertion aboutit à la création d'une feuille $f$. On considère le **premier ancêtre $y$ de cette feuille qui viole la condition AVL** : $eq(y) = -2$ ou $eq(y) = 2$, deux cas symétriques. Supposons $eq(y) = -2$ et soit $x$ le fils gauche de $y$. Deux cas :

- **$eq(x) = -1$** : on effectue une rotation droite (autour de $y$). Juste après une insertion, $eq(x) = 0$ ne peut pas se produire : ce cas ne survient qu'à la suppression. [[Erreurs du cours#^e-6-avl|✎]]

![[ARBRE AVL - p2a.jpg]]
*Figure : rotation droite autour de $y$, dessinée avec $y$ (−2) et $x$ (0), configuration qui ne se rencontre qu'après une suppression ; après la rotation, $x$ a un facteur 1 et $y$ un facteur −1.* [[Erreurs du cours#^e-6-avl|✎]]

- **$eq(x) = 1$** : $x$ a un sous-arbre droit de racine $z$, qui a deux sous-arbres. On effectue une **rotation gauche autour de $x$**, puis une **rotation droite autour de $y$**.

![[ARBRE AVL - p2b.jpg]]
*Figure : insertion, cas $eq(x) = 1$ : détail du sous-arbre de racine $z$, rotation gauche autour de $x$ ($z$ remonte, facteur −1), puis rotation droite autour de $y$ ; $z$ devient racine de facteur 0.*

Les quatre cas, avec le nom qu'on leur donne souvent (selon le chemin qui mène de $y$ vers la partie trop haute) : [[Complément hors du cours|ⓘ]]

| $eq(y)$ | $eq(x)$, $x$ fils du côté trop haut | Cas | Rééquilibrage |
|---|---|---|---|
| $-2$ | $-1$ | gauche-gauche | rotation droite autour de $y$ |
| $-2$ | $+1$ | gauche-droite | rotation gauche autour de $x$, puis droite autour de $y$ (double rotation) |
| $+2$ | $+1$ | droite-droite | rotation gauche autour de $y$ |
| $+2$ | $-1$ | droite-gauche | rotation droite autour de $x$, puis gauche autour de $y$ (double rotation) |

Une seule rotation, simple ou double, suffit après une insertion : le sous-arbre rééquilibré retrouve exactement la hauteur qu'il avait **avant** l'insertion, donc les ancêtres de $y$ ne voient aucun changement. C'est pourquoi `equilibreAprèsInsertion` (section 5) s'arrête au premier nœud déséquilibré. [[Complément hors du cours|ⓘ]]

Exemple : on insère 10, 20, 30 dans un AVL vide. Après 30, la racine 10 a $eq = 2$ (sous-arbre droit 20 → 30 avec $h = 2$ au sens de la définition de $eq$, gauche vide avec $h = 0$) et son fils droit 20 a $eq = 1$ : cas droite-droite, rotation gauche autour de 10. On obtient 20 (10, 30), équilibré. Dans un ABR simple, ces trois insertions auraient donné une chaîne. Si l'on insère 10, 30, 20, le cas est droite-gauche : rotation droite autour de 30, puis gauche autour de 10, avec le même résultat. [[Complément hors du cours|ⓘ]]

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

Pourquoi la suppression peut demander plusieurs rotations : elle fait baisser la hauteur d'un sous-arbre, et une rotation de rééquilibrage peut elle-même faire baisser d'un niveau la hauteur du sous-arbre rééquilibré (tous les cas sauf $eq(x) = 0$). Le déséquilibre peut alors se reporter sur l'ancêtre suivant, jusqu'à la racine : au pire une rotation par niveau, soit $O(\log n)$ rotations, chacune en $O(1)$. [[Complément hors du cours|ⓘ]]

Bilan des coûts dans un AVL de $n$ nœuds : recherche, insertion et suppression en $O(\log n)$, puisque la hauteur est en $O(\log n)$ et que chaque opération descend puis remonte une branche ; au plus une rotation (simple ou double) par insertion, $O(\log n)$ rotations par suppression. À comparer à l'ABR non équilibré, en $O(n)$ dans le pire cas ([[5 - ABR]]). [[Complément hors du cours|ⓘ]]

## 5. Implémentation

L'intérêt du facteur d'équilibrage est que cette information nécessite **2 bits**. Néanmoins, les algorithmes de gestion de $eq$ sont délicats. Dans la suite, une cellule d'arbre AVL contient un champ supplémentaire, la **hauteur**.

Les 2 bits viennent de ce que le facteur ne prend que trois valeurs, $-1$, $0$ et $1$, et que 2 bits codent $2^2 = 4$ valeurs. Stocker la hauteur coûte un entier complet par nœud, mais simplifie le code : le facteur se recalcule à la demande comme $h(D_s) - h(G_s)$, et une hauteur se met à jour par $h = 1 + \max(h(G), h(D))$ sans formules de rotation à retenir. [[Complément hors du cours|ⓘ]]

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

Les fonctions implémentant les rotations sont « immédiates ». [[Erreurs du cours#^e-6-avl|✎]]

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
    setHauteur(y, max(getHauteur(filsGauche(y)), getHauteur(filsDroit(y))) + 1);
    setHauteur(x, max(getHauteur(filsGauche(x)), getHauteur(filsDroit(x))) + 1);
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
    setHauteur(x, max(getHauteur(filsGauche(x)), getHauteur(filsDroit(x))) + 1);
    setHauteur(y, max(getHauteur(filsGauche(y)), getHauteur(filsDroit(y))) + 1);
  fin
```

L'ordre des deux `setHauteur` compte : on met d'abord à jour le nœud qui descend.

### Insertion

Les fonctions d'insertion et de suppression doivent prendre en compte le calcul du facteur d'équilibrage et le maintien de l'équilibre. [[Erreurs du cours#^e-6-avl|✎]]

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
    tantque pere(p) != NIL et eq != 2 et eq != -2 faire
      s = p;
      p = pere(s);
      setHauteur(p, max(getHauteur(filsGauche(p)), getHauteur(filsDroit(p))) + 1);
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

### Suppression [[Erreurs du cours#^e-6-avl|✎]]

```text
fonction supprimer(ref x: sommet): booléen;
  var p, f, y: sommet;
  début
    si estFeuille(x) alors
      p = pere(x);
      si p == NIL alors
        x = NIL;   /* la feuille était la racine : l'arbre devient vide */
      sinon
        si filsGauche(p) == x alors
          supprimerFilsGauche(p)
          setHauteur(p, getHauteur(filsDroit(p)) + 1)
        sinon
          supprimerFilsDroit(p)
          setHauteur(p, getHauteur(filsGauche(p)) + 1)
        finsi
        equilibreAprèsSuppression(p)
      finsi
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

Dans le cas de la suppression, on remonte à partir de la feuille supprimée et on détecte de la même manière les nœuds déséquilibrés. **Plusieurs rotations peuvent être nécessaires** : un déséquilibre peut en entraîner un autre. On remonte donc jusqu'à la racine, et chaque nœud déséquilibré est rééquilibré du côté de son sous-arbre le plus haut. [[Erreurs du cours#^e-6-avl|✎]]

```text
fonction equilibreAprèsSuppression(ref x: sommet): vide;
  var eq: entier;
  var s, p: sommet;
  début
    p = x;
    tantque p != NIL faire
      setHauteur(p, max(getHauteur(filsGauche(p)), getHauteur(filsDroit(p))) + 1);
      eq = getHauteur(filsDroit(p)) - getHauteur(filsGauche(p));
      si eq == 2 alors
        equilibreUnSommet(p, filsDroit(p));
      sinon si eq == -2 alors
        equilibreUnSommet(p, filsGauche(p));
      finsi
      p = pere(p);
    fintantque
  fin
```

## Liens

L'AVL est le premier arbre de recherche équilibré publié. D'autres structures poursuivent le même but : l'**[[Arbre rouge-noir|arbre rouge-noir]]**, moins strictement équilibré (hauteur au plus $2\log_2(n+1)$), qui fait moins de rotations lors des mises à jour et sert par exemple à la classe `TreeMap` de Java ; le **[[B-arbre]]**, dont les nœuds contiennent de nombreuses clés, utilisé par les bases de données et les systèmes de fichiers pour limiter les accès disque. L'AVL, plus strictement équilibré, est un peu plus rapide en recherche. [[Complément hors du cours|ⓘ]]

Même sujet que [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]] et [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]], et que le sujet [[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2]]. Voir aussi [[Hauteur d'un arbre]] et [[5 - ABR]] pour les opérations d'ABR.
