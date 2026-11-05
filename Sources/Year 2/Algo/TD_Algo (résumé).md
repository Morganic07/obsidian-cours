---
type: source
sources: ["[[TD_Algo]]"]
maj: 2026-11-05
---

Résumé de [[TD_Algo]], dans [[Year 2 - Algo]]. Note de TD très courte : du code Python sans énoncé.

## Contenu

Cinq questions de dessin de motifs avec le caractère `#`, la plupart mises en commentaire :

- Q1 : afficher `n` lignes de `n` caractères `#` (boucle `for _ in range(n)` et `n*"#"`).
- Q2 : variante avec `n` colonnes et `m` lignes.
- Q3 : motif en damier, seule question non commentée. Elle utilise `ceil` et `floor` du module `math` pour la moitié de `n`.
- Q4 : triangle de `#`, de 1 à `n` caractères par ligne.
- Q5 : début de motif à parcours imbriqué (`i`, `j`), non terminé.

## Points à vérifier dans le cours

L'énoncé n'étant pas donné, rien n'est vérifiable sur le résultat attendu.

1. **Q3** (complément) : le test `n//2 == 0` n'est vrai que pour `n` égal à 0 ou 1. Il voulait sans doute dire « `n` pair », soit `n % 2 == 0`.
2. **Q5** : `print((j-i+1)"#")` oublie l'opérateur `*` et ne s'exécute pas. Le code est de toute façon commenté.
3. **Mise en forme** : l'indentation est perdue à la conversion, le code ne se lit qu'avec effort.
