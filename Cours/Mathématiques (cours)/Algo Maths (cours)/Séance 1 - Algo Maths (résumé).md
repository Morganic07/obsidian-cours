---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]] (séance du 21/09/23), dans [[Algo Maths (index)]]. En cas d'écart, le cours fait foi. Pas d'image dans cette note : les dessins n'en restent que par leur texte.

## Idée générale

Premier cours d'algorithmique : notions de base, puis des problèmes qui introduisent la [[Récurrence]] et la [[Récursivité]].

## Repères et notions de base

- **Ada Lovelace** (1815-1852) a écrit le premier programme.
- **[[Algorithme]]** : production automatique d'un résultat à partir d'une entrée. Existe depuis 4000 ans ; le mot vient du nom francisé d'Al-Khwarizmi (le cours note « -800 »).
- **Machine** : fait des calculs et produit un résultat. Existe depuis 100 ans.
- **[[Bit]]** = *Binary Digit*, chiffre binaire.
- Dans un ordinateur, l'élément important est le **[[Transistor]]**, qui fonctionne grâce à la mécanique quantique.

## Interprétation géométrique des nombres premiers (les billes)

Un [[Nombre premier]] se reconnaît en rangeant des billes :

- si l'on peut former un rectangle avec $X$ billes, $X$ n'est pas premier ;
- si la seule manière de les placer est une ligne, $X$ est premier.

Exemples : 15 billes forment un rectangle $3 \times 5$ ; 7 billes ne forment qu'une ligne.

## Somme des $n$ premiers entiers

[[Somme des premiers entiers]], par un dessin : deux escaliers de $1 + 2 + \dots + n$ s'emboîtent en un rectangle $n \times (n+1)$. Texte du dessin : « n+1 ; n ; 2S = n(n+1) ; S = n(n+1) ». D'où

$$2S = n(n+1) \quad\Longrightarrow\quad S = \frac{n(n+1)}{2}.$$

(La division par 2 manque dans le texte du dessin.)

## Langages et nombres flottants

- Si un problème est résoluble dans un langage de programmation, il l'est dans tous : les langages résolvent les mêmes problèmes.
- En programmation, un [[Nombre à virgule flottante|float]] n'est pas un nombre réel. Exemple du cours : $0.1 + 0.3 \ne 0.4$ (voir « Points à vérifier »).

## Fractales

Une [[Fractale]] est un motif autosimilaire défini par récurrence (texte du dessin : « $u_0$ ; $u_1$ ; $u_2$ ; $u_n$ », étapes successives de construction).

- Propriété : les fractales ont un périmètre infini.
- Exemple : le flocon de Koch.

## Les tours de Hanoï

[[Tours de Hanoï]]. Problème : écrire un algorithme qui calcule le nombre minimal de coups pour déplacer $n$ disques.

### Raisonnement

1. Il faut retirer tous les disques posés sur le grand disque $D$, puis déplacer $D$ sur le pilier final.
2. On réitère le même procédé, $D$ étant désormais le deuxième plus grand disque.
3. Le problème fait donc appel à la récursivité.

### Algorithme

```text
def coup.min() :
    Pour n = 0 → ne rien faire
    Pour n ≥ 1 :
        Déplacer n-1 disques du pilier 1 au pilier 2
        Déplacer le grand disque du 1 au 3
        Déplacer n-1 disques de 2 à 3
```

### Nombre de coups

Formule donnée par l'enseignant : $\text{coup.min}(n) = 2 \times \text{coup.min}(n-1) + 1$, soit la suite définie par récurrence $u_{n+1} = 2u_n + 1$. Texte du dessin : $f(0) = 0$ ; $f(n+1) = 2f(n) + 1$.

Forme générale : $u_n = 2^n - 1$.

### Démonstration par récurrence de $P(n) : f(n) = 2^n - 1$

- **Initialisation** : $f(0) = 2^0 - 1 = 0$.
- **Hérédité** : supposons $P(k)$ vraie. Alors
$$f(k+1) = 2f(k) + 1 = 2(2^k - 1) + 1 = 2 \cdot 2^k - 2 + 1 = 2^{k+1} - 1.$$
- **Conclusion** : si $P(k)$ est vraie, $P(k+1)$ l'est ; or $P(0)$ est vraie, donc la propriété est vraie pour tout entier (le cours écrit « $\ge 1$ », voir « Points à vérifier »).

## Le problème des crayons

[[Problème des crayons]]. Fausse démonstration par récurrence de $P_n$ : « dans un ensemble de $n$ crayons, tous les crayons sont de la même couleur ».

- **Initialisation** : pour $n = 1$, un ensemble d'un crayon n'a qu'une couleur.
- **Hérédité** : on suppose $P_k$ vraie. Dans un ensemble de $k+1$ crayons, l'hypothèse s'applique aux crayons 1 à $k$ et aux crayons 2 à $k+1$. Ces deux sous-ensembles partagent la couleur des crayons « du milieu », donc tous les $k+1$ crayons sont de même couleur.

Commentaire de l'étudiant : cela semble absurde, « mais en fait ça devient vrai pour $n \ge 3$, il faut qu'il y ait des crayons du milieu pour que ça marche », puis « J'avoue j'ai pas capté ». L'erreur est expliquée dans « Points à vérifier ».

## Le carré magique $3 \times 3$

[[Carré magique]] : grille $3 \times 3$ remplie avec les nombres de 1 à 9, où chaque ligne, chaque colonne et chaque diagonale a la même somme.

1. **Somme des entiers du carré** : $\dfrac{n(n+1)}{2} = \dfrac{9 \times 10}{2} = 45$.
2. **Somme selon une direction** : on divise la somme totale par 3, soit $15$.
3. **Valeur de la case centrale** : raisonnement du cours (dessin en vert, non conservé) : « si on vire ce qui est en vert, il ne reste que le carré du milieu, qui vaut $45 - 30 = 15$ ; or on compte 3 fois la case du milieu, donc $15/3 = 5$ ». La case centrale vaut **5**.
4. **Nombre de manières d'obtenir 15** avec trois nombres distincts de 1 à 9 : 8 manières.

| | |
|---|---|
| 1+5+9 | 2+6+7 |
| 1+6+8 | 3+4+8 |
| 2+4+9 | 3+5+7 |
| 2+5+8 | 4+5+6 |

5. **Combien y a-t-il de solutions ?** Réponse notée : « Bah 8 ig ».

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Problème des crayons** : l'erreur est dans l'hérédité, qui échoue de $k = 1$ à $k = 2$ : deux groupes d'un crayon n'ont pas de crayon commun. L'étudiant dit « vrai pour $n \ge 3 $ » : à relire, le résultat est faux pour tout $n \ge 2$ (complément). Le passage s'arrête sur un aveu d'incompréhension.
2. **$0.1 + 0.3 \ne 0.4$** : en Python, `0.1 + 0.3 == 0.4` vaut `True` (vérifié). L'exemple classique est $0.1 + 0.2 \ne 0.3$. Le principe (flottants approchés) reste juste (complément).
3. **« Matrice $3 \times 3$ avec les 10 nombres »** : il y en a 9, de 1 à 9, ce que confirme la somme 45.
4. **Récurrence sur Hanoï** : la conclusion dit « vraie pour tout entier $\ge 1$ » alors que l'initialisation est en 0 ; et « $2^{k+1} - 1$ » s'écrit « 2^k+1 - 1 ».
5. **Nombre de solutions du carré magique** : le cours répond 8, qui est aussi le nombre de triplets. Il s'agit de coïncidence : il existe un seul carré à rotations et symétries près, soit 8 grilles (complément, non démontré ici).
6. **Algorithme `coup.min`** : écrit « Pour n=0 → ne rien faire » ; correct, mais la formule donnée par l'enseignant n'est démontrée que plus bas.
7. **Case centrale** : le raisonnement par la zone verte n'est pas reconstituable sans le dessin ; tel qu'il est écrit (« le carré du milieu vaut 45 - 30 »), il est elliptique. Un raisonnement complet : la ligne du milieu, la colonne du milieu et les deux diagonales passent toutes par le centre ; leur somme vaut $4 \times 15 = 60 = 45 + 3c$, d'où $c = 5$ (complément).
8. **Somme des entiers (dessin)** : le texte du dessin écrit « S = n(n+1) » sans la division par 2 ; la formule juste est $S = n(n+1)/2$.
