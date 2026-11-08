---
type: concept
tags: [year1]
aliases: [codes de Gray, Gray code, code binaire réfléchi]
sources: ["[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]"]
maj: 2026-11-08
---

**Définition** (d'après le DM, [[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]) : « Le code de Gray est une séquence de nombres binaires (1 et 0) dans laquelle deux valeurs successives diffèrent par un seul bit. »

Autrement dit, le code de Gray sur $n$ bits range les $2^n$ mots binaires de $n$ bits dans un ordre tel que l'on passe de l'un au suivant en changeant **un seul** [[Bit]]. En [[Numération binaire|binaire classique]], au contraire, plusieurs bits peuvent changer d'un coup : de 3 (`011`) à 4 (`100`), les trois bits changent.

## Exemple sur 3 bits

| Rang $k$ | $k$ en binaire | Code de Gray | Bit qui change |
|---|---|---|---|
| 0 | `000` | `000` | — |
| 1 | `001` | `001` | bit 0 |
| 2 | `010` | `011` | bit 1 |
| 3 | `011` | `010` | bit 0 |
| 4 | `100` | `110` | bit 2 |
| 5 | `101` | `111` | bit 0 |
| 6 | `110` | `101` | bit 1 |
| 7 | `111` | `100` | bit 0 |

En décimal, la suite est 0, 1, 3, 2, 6, 7, 5, 4 : chaque nombre de 0 à 7 y apparaît une fois et une seule. La suite est aussi cyclique : de `100` on revient à `000` en changeant un seul bit.

## Construction par réflexion (celle du DM)

On part de la liste `[0]` (le code sur 0 bit). Pour passer de $i$ bits à $i+1$ bits :
1. on garde la liste telle quelle ;
2. on lui ajoute la même liste **parcourue à l'envers** (le « miroir »), en mettant à 1 le bit $i$ de chacun de ces éléments.

Sur l'exemple : `[0]` → `[0, 1]` → `[0, 1, 3, 2]` → `[0, 1, 3, 2, 6, 7, 5, 4]`.

La propriété « un seul bit change » se conserve : dans chaque moitié, elle est vraie par construction ; à la jonction des deux moitiés, le dernier élément de la première moitié et le premier de la seconde sont le même mot, au bit $i$ près.

Code du DM :

```python
def code_gray(n):
    result = [0]                      # la liste ne contient que l'élément nul
    for i in range(n):                # une itération par bit
        result += [x + (1 << i) for x in reversed(result)]   # miroir, avec le bit i mis à 1
    return result                     # les 2**n codes de Gray sur n bits
```

`1 << i` vaut $2^i$ : ajouter `1 << i` à un nombre qui a son bit $i$ à 0 met ce bit à 1.

## Usage dans le DM : parcourir toutes les configurations du sac à dos

Dans le [[Problème du sac à dos]], une configuration dit pour chaque objet s'il est dans le sac (bit 1) ou non (bit 0). Avec $n$ objets, il y a $2^n$ configurations, et la [[Recherche exhaustive]] les examine toutes. `exhaustif_gray` les parcourt dans l'ordre du code de Gray, en appelant la fonction `code_gray` définie plus haut : [[Erreurs du cours#^e-code-de-gray|✎]]

```python
def exhaustif_gray(nom_fichier):
    NbObjets, P, objets = lecture_fichier(nom_fichier)
    meilleure_valeur = 0
    meilleure_config = []
    codes = code_gray(NbObjets)
    for code in codes:
        configuration = [int(x) for x in format(code, f'0{NbObjets}b')]
        valeur_totale = sum(objets[j].v for j in range(NbObjets) if configuration[j] == 1)
        poids_total = sum(objets[j].w for j in range(NbObjets) if configuration[j] == 1)
        if poids_total <= P and valeur_totale > meilleure_valeur:
            meilleure_valeur = valeur_totale
            meilleure_config = configuration
    return meilleure_config
```

- `format(code, f'0{NbObjets}b')` écrit le code en binaire sur `NbObjets` chiffres ; la liste `configuration` en tire un 0 ou un 1 par objet.
- Une configuration est retenue si elle respecte la capacité $P$ du sac et si sa valeur dépasse la meilleure trouvée jusque-là.

## Pourquoi un code de Gray ici (complément, hors du cours)

L'intérêt est de passer d'une configuration à la suivante en **ajoutant ou en retirant un seul objet**. On peut alors mettre à jour le poids et la valeur totaux en une opération, au lieu de les recalculer :
- si le bit qui change passe à 1, on ajoute le poids et la valeur de cet objet ;
- s'il passe à 0, on les retire.

Le parcours coûte alors $O(2^n)$ opérations au lieu de $O(n \cdot 2^n)$ quand on refait les deux sommes à chaque configuration. Le bit qui change à l'étape $k$ (pour $k \ge 1$) est le bit de poids le plus faible égal à 1 dans $k$ : bit 0 aux étapes impaires, bit 1 aux étapes 2, 6, 10…, comme dans le tableau ci-dessus.

Autres repères, hors du cours :
- le code de Gray de rang $k$ se calcule directement par $g(k) = k \oplus (k \gg 1)$ (ou exclusif entre $k$ et $k$ décalé d'un bit vers la droite) : en Python, `k ^ (k >> 1)` redonne la suite 0, 1, 3, 2, 6, 7, 5, 4 ;
- ce code porte le nom de Frank Gray (Bell Labs, brevet de 1953). On l'emploie quand une lecture prise pendant un changement de valeur ne doit jamais tomber sur un nombre aberrant : capteurs de position rotatifs, tableaux de Karnaugh.

Notion parente : [[Numération binaire]]. Voir aussi : [[Recherche exhaustive]], [[Problème du sac à dos]].

Résumés (rapprochement, complément hors du cours) : [[0 - Algo Maths]]
