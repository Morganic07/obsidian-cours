---
type: source
tags:
  - year1
sources:
  - "[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]"
maj: 2026-11-05
---

Résumé de [[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]], dans [[Algo Maths (matière)]]. En cas d'écart, le cours fait foi. Pas d'image dans cette note.

## Idée générale

Premier cours d'algorithmique : notions de base, puis des problèmes qui introduisent la récurrence et la récursivité.

## Contenu, dans l'ordre du cours

- **Repères** : Ada Lovelace (1815-1852) a écrit le premier programme. Un algorithme produit automatiquement un résultat à partir d'une entrée, le mot vient du nom d'Al-Khwarizmi. Une machine fait des calculs. Un bit est un chiffre binaire.
- **Nombres premiers aux billes** : $X$ billes forment un rectangle si $X$ n'est pas premier, une seule ligne s'il l'est (15 billes : $3 \times 5$, 7 billes : ligne).
- **Somme des $n$ premiers entiers** : interprétation géométrique, $2S = n(n+1)$. Annotation du dessin : « n+1 ; n ; 2S = n(n+1) ; S = n(n+1) », la division par 2 manque à la fin.
- **Langages** : un problème résoluble dans un langage l'est dans tous. Un `float` n'est pas un réel : le cours note $0.1 + 0.3 \ne 0.4$.
- **Fractale** : motif autosimilaire défini par récurrence, de périmètre infini (flocon de Koch).
- **[[Tours de Hanoï]]** : pour déplacer le grand disque, il faut d'abord retirer les $n - 1$ disques au-dessus, puis les replacer. Algorithme récursif et nombre de coups $f(0) = 0$, $f(n+1) = 2f(n) + 1$, soit $f(n) = 2^n - 1$, démontré par [[Récurrence]].
- **Problème des crayons** : « dans $n$ crayons, tous ont la même couleur », « démontré » par récurrence. L'étudiant note que cela semble absurde, que cela devient vrai pour $n \ge 3$ et qu'il faut des crayons « du milieu », puis écrit « Javoue g pas capté ».
- **Carré magique $3 \times 3$** : somme totale $n(n+1)/2 = 45$, somme par ligne 15, case centrale 5 (raisonnement du dessin vert, non reconstituable). Huit façons d'obtenir 15 avec trois nombres distincts de 1 à 9 : 1+5+9, 1+6+8, 2+4+9, 2+5+8, 2+6+7, 3+4+8, 3+5+7, 4+5+6. Réponse à « combien de solutions ? » : « Bah 8 ig ».

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Problème des crayons** : l'erreur est dans l'hérédité, qui échoue de $k = 1$ à $k = 2$ : deux groupes d'un crayon n'ont pas de crayon commun. L'étudiant dit « vrai pour $n \ge 3 $ » : à relire, le résultat est faux pour tout $n \ge 2$ (complément). Le passage s'arrête sur un aveu d'incompréhension.
2. **$0.1 + 0.3 \ne 0.4$** : en Python, `0.1 + 0.3 == 0.4` vaut `True` (vérifié). L'exemple classique est $0.1 + 0.2 \ne 0.3$. Le principe (flottants approchés) reste juste (complément).
3. **« Matrice $3 \times 3$ avec les 10 nombres »** : il y en a 9, de 1 à 9, ce que confirme la somme 45.
4. **Récurrence sur Hanoï** : la conclusion dit « vraie pour tout entier $\ge 1$ » alors que l'initialisation est en 0 ; et « $2^{k+1} - 1$ » s'écrit « 2^k+1 - 1 ».
5. **Nombre de solutions du carré magique** : le cours répond 8, qui est aussi le nombre de triplets. Il s'agit de coïncidence : il existe un seul carré à rotations et symétries près, soit 8 grilles (complément, non démontré ici).
6. **Algorithme `coup.min`** : écrit « Pour n=0 → ne rien faire » ; correct, mais la formule donnée par l'enseignant n'est démontrée que plus bas.
