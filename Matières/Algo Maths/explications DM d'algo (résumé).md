---
type: source
tags: [year1]
sources: ["[[explications DM d'algo]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[explications DM d'algo]], dans [[Algo Maths (matière)]]. Note pédagogique d'un étudiant, partagée avec la promotion, autour d'un devoir sur le [[Problème du sac à dos]]. Pas d'image dans la note.

**Statut de la source** : l'auteur indique en préambule que la majorité du code provient de ChatGPT, qu'il ne détient « pas la vérité absolue », que le code peut être inexact, et demande de faire preuve d'esprit critique. Tout ce qui suit est donc une explication d'étudiant sur du code en grande partie généré, pas un corrigé de l'enseignant.

## Idée générale

Le problème : $n$ objets, chacun avec une valeur $v$ et un poids $w$, et un sac de capacité $P$. On cherche quels objets prendre (en entier, sans fractionner) pour maximiser la valeur totale sans dépasser $P$. Une configuration est une liste de $n$ bits : 1 si l'objet est pris, 0 sinon.

Plan de la note : lecture du fichier d'objets, puis plusieurs stratégies de résolution : exhaustive (binaire, binaire optimisée, code de Gray), gloutonne (par valeur, par poids, par densité), stochastique. La programmation dynamique est annoncée mais non rédigée.

## 1. Lecture du fichier : `lecture_fichier`

Format du fichier : la première ligne contient le nombre d'objets et la capacité $P$ du sac ; chaque ligne suivante contient la valeur puis le poids d'un objet.

```python
from dataclasses import dataclass

@dataclass
class Objet:
    num: int   # numéro de l'objet
    v: int     # valeur
    w: int     # poids

def lecture_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:          # ouverture en lecture
        lignes = f.readlines()                  # liste des lignes
    NbObjets, P = map(int, lignes[0].split())   # 1re ligne : nb d'objets, capacité
    objets = []
    for i, ligne in enumerate(lignes[1:], start=1):   # à partir de la 2e ligne
        valeur, poids = map(int, ligne.split())
        objets.append(Objet(i, valeur, poids))
    return NbObjets, P, objets

# Exemple d'utilisation
nom_fichier = 'exemple.txt'
NbObjets, P, objets = lecture_fichier(nom_fichier)
print(NbObjets, P, objets)
```

Explications de la note :

- `dataclasses` permet de créer des classes de données en Python ([[Dataclass (Python)]]) : chaque `Objet` contient son numéro, sa valeur et son poids.
- `split()` coupe la ligne en morceaux ; `map(int, …)` convertit chaque morceau en entier.
- La [[Boucle (programmation)|boucle `for`]] avec `enumerate(lignes[1:], start=1)` parcourt les lignes à partir de la deuxième et numérote les objets à partir de 1.
- Chaque objet est créé (`Objet(i, valeur, poids)`) puis ajouté à la liste `objets`.
- La fonction renvoie le nombre d'objets, la capacité maximale du sac et la liste des objets.

**Test conseillé** (à adapter au fichier utilisé) :

```python
nom_fichier = 'ks_4_0.txt'
NbObjets, P, objets = lecture_fichier(nom_fichier)
print(lecture_fichier(nom_fichier))
```

Méthode générale de la note : tester chaque fonction codée avec `print(nom_fonction('nom_fichier.txt'))` et comparer au résultat attendu.

## 2. Énumération exhaustive

### Nombre de configurations

Question du devoir : « Quel est le nombre total de configurations possibles pour un ensemble de $n$ objets (sans tenir compte du débordement du sac) ? »

Chaque objet est pris ou non, indépendamment des autres : il y a $2^n$ configurations. Ce n'est **pas** $n!$, qui compte les façons d'ordonner $n$ objets (permutations), pas les choix d'inclusion/exclusion.

Principe de la [[Recherche exhaustive]] : chaque configuration est représentée par un [[Numération binaire|nombre binaire]] de $n$ chiffres, où chaque [[Bit|bit]] dit si l'objet est inclus (1) ou non (0). On parcourt les nombres de $0$ à $2^n - 1$.

### 2.1 `exhaustif_binaire`

```python
def exhaustif_binaire(nom_fichier):
    NbObjets, P, objets = lecture_fichier(nom_fichier)
    meilleure_valeur = 0          # meilleure valeur totale trouvée
    meilleure_config = []         # configuration correspondante
    for i in range(2**NbObjets):  # toutes les configurations
        configuration = [int(x) for x in format(i, f'0{NbObjets}b')]
        valeur_totale = sum(objets[j].v for j in range(NbObjets) if configuration[j] == 1)
        poids_total = sum(objets[j].w for j in range(NbObjets) if configuration[j] == 1)
        if poids_total <= P and valeur_totale > meilleure_valeur:
            meilleure_valeur = valeur_totale
            meilleure_config = configuration
    return meilleure_config
```

- `format(i, f'0{NbObjets}b')` convertit $i$ en chaîne binaire de longueur `NbObjets`, complétée par des zéros à gauche ; la compréhension de liste la transforme en liste de 0 et de 1.
- On calcule la valeur et le poids de la configuration ; si le poids ne dépasse pas $P$ et que la valeur bat la meilleure, on met à jour.

### 2.2 `exhaustif_binaire_optimise`

```python
def exhaustif_binaire_optimise(nom_fichier):
    NbObjets, P, objets = lecture_fichier(nom_fichier)
    meilleure_valeur = 0
    meilleure_config = []
    for i in range(2**NbObjets):
        configuration = [int(x) for x in format(i, f'0{NbObjets}b')]
        valeur_totale = 0
        poids_total = 0
        for j in range(NbObjets):
            if configuration[j] == 1:
                valeur_totale += objets[j].v
                poids_total += objets[j].w
                if poids_total > P:
                    break          # inutile de continuer : le sac déborde
        if poids_total <= P and valeur_totale > meilleure_valeur:
            meilleure_valeur = valeur_totale
            meilleure_config = configuration
    return meilleure_config
```

Seule différence : valeur et poids sont calculés par incrément, et le `break` interrompt le calcul dès que le poids dépasse la capacité. `exhaustif_binaire`, lui, calcule toujours la valeur et le poids complets, même pour une configuration qui déborde.

### 2.3 Code de Gray : `code_gray` et `exhaustif_gray`

**Définition** : le [[Code de Gray]] est une séquence de nombres binaires dans laquelle deux valeurs successives diffèrent d'un seul bit.

```python
def code_gray(n):
    result = [0]                       # au départ : seulement 0
    for i in range(n):                 # n itérations, n = nombre de bits
        result += [x + (1 << i) for x in reversed(result)]
    return result                      # les 2^n codes de Gray sur n bits
```

À chaque tour, on reprend les codes déjà obtenus **à l'envers** et on leur ajoute le bit $i$ (`1 << i` vaut $2^i$) : les nouveaux éléments diffèrent des anciens d'exactement un bit. Par exemple, pour $n = 2$ : `[0]` → `[0, 1]` → `[0, 1, 3, 2]`, soit 00, 01, 11, 10 (exemple ajouté, vérifiable en exécutant la fonction).

`exhaustif_gray` cherche la meilleure configuration en parcourant les codes de Gray au lieu des entiers dans l'ordre :

```python
def exhaustif_gray(nom_fichier):
    NbObjets, P, objets = lecture_fichier(nom_fichier)
    meilleure_valeur = 0
    meilleure_config = []
    codes = code_gray(NbObjets)        # le bloc encadré écrit gray_code(...)
    for code in codes:
        configuration = [int(x) for x in format(code, f'0{NbObjets}b')]
        valeur_totale = sum(objets[j].v for j in range(NbObjets) if configuration[j] == 1)
        poids_total = sum(objets[j].w for j in range(NbObjets) if configuration[j] == 1)
        if poids_total <= P and valeur_totale > meilleure_valeur:
            meilleure_valeur = valeur_totale
            meilleure_config = configuration
    return meilleure_config
```

`code_gray` doit être écrite avant `exhaustif_gray`, qui en a besoin.

## 3. Algorithmes gloutons

**Définition** (selon la note) : un [[Algorithme glouton]] prend la meilleure décision possible au moment donné, sans se préoccuper des conséquences futures, et répète ce choix jusqu'à obtenir une solution complète. Il repose sur la propriété : « une solution optimale au problème global contient des solutions optimales aux sous-problèmes ». En résumé de l'auteur : le problème est découpé en sous-problèmes, chacun reçoit une sous-solution optimale, et la solution finale est leur combinaison.

**Attention** : un algorithme glouton généré par ChatGPT peut considérer des fractions d'objets. Ici, un objet est pris en entier ou pas du tout.

Les trois versions ont le même squelette ; seule la ligne de tri change.

```python
def glouton_valeur(nom_fichier):
    NbObjets, P, objets = lecture_fichier(nom_fichier)
    objets = sorted(objets, key=lambda x: x.v, reverse=True)   # ligne de tri
    valeur_totale = 0
    poids_total = 0
    configuration = [0] * NbObjets        # aucun objet pris au départ
    for objet in objets:
        if poids_total + objet.w <= P:    # l'objet tient encore dans le sac
            configuration[objet.num - 1] = 1
            valeur_totale += objet.v
            poids_total += objet.w
    return configuration
```

| Fonction | Ligne de tri | Ordre | Objets pris en premier |
|---|---|---|---|
| `glouton_valeur` | `sorted(objets, key=lambda x: x.v, reverse=True)` | valeur décroissante | les plus précieux |
| `glouton_poids` | `sorted(objets, key=lambda x: x.w)` | poids croissant | les plus légers |
| `glouton_densite` | `sorted(objets, key=lambda x: x.v/x.w, reverse=True)` | densité $v/w$ décroissante | la meilleure valeur « au kilo » |

- `sorted(…, key=…)` choisit le critère de tri ; par défaut l'ordre est croissant, `reverse=True` le rend décroissant.
- `configuration[objet.num - 1] = 1` : les objets sont numérotés à partir de 1, la liste à partir de 0.

**Limites** : aucun de ces algorithmes n'est optimal pour le sac à dos. `glouton_poids` ignore la valeur et peut remplir le sac d'objets de faible valeur ; `glouton_valeur` ignore le poids. `glouton_densite` combine les deux critères, sans garantie d'optimalité non plus.

## 4. Algorithme stochastique : `remplissage_aleatoire`

**Définition** : un [[Algorithme stochastique]] intègre du hasard ou des probabilités dans son processus de décision. Les algorithmes précédents étaient déterministes.

- Intérêt : il explore des combinaisons variées et peut échapper aux solutions locales sous-optimales où un glouton se coince.
- Limites : le résultat n'est probablement pas le meilleur, et il peut changer d'une exécution à l'autre.

Règle : pour chaque objet, on calcule le taux de remplissage qu'aurait le sac avec lui,
$$\text{taux} = \frac{\text{poids}_{\text{courant}} + w}{P}, \qquad p_{\text{inclusion}} = 1 - \text{taux}.$$
Plus le sac est plein, plus la probabilité d'inclure l'objet est faible. On tire un nombre au hasard dans $[0 ; 1[$ ; l'objet est pris si ce nombre est inférieur à $p_{\text{inclusion}}$ et si le sac ne déborde pas.

```python
import random    # indispensable pour le hasard

def remplissage_aleatoire(nom_fichier):
    NbObjets, P, objets = lecture_fichier(nom_fichier)
    valeur_totale = 0
    poids_total = 0
    configuration = [0] * NbObjets

    for objet in objets:
        # Inverse du taux de remplissage
        taux_remplissage = (poids_total + objet.w) / P
        prob_inclusion = 1 - taux_remplissage

        # Décision stochastique
        if random.random() < prob_inclusion and poids_total + objet.w <= P:
            configuration[objet.num - 1] = 1
            valeur_totale += objet.v
            poids_total += objet.w

    return configuration
```

## 5. Programmation dynamique

Section vide : « Je fais plus tard, mais normalement tout est expliqué dans la vidéo ». Voir [[Programmation dynamique]] pour la notion.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Première ligne du fichier** : le commentaire dit « le nombre d'objet et la valeur de chaque objet », alors que le code lit le nombre d'objets et la capacité $P$.
2. **Bloc de code de `glouton_valeur`** (encadré) : `sorted(..., key=lambda x: x.v)` sans `reverse=True`, donc tri croissant. La version commentée, plus bas, ajoute `reverse=True` et c'est elle qui correspond au texte.
3. **Bloc de code `exhaustif_gray`** (encadré) : appelle `gray_code(...)`, alors que la fonction définie s'appelle `code_gray` ; la version commentée utilise le bon nom. Dans les deux, la configuration est recalculée entièrement pour chaque code : l'intérêt du code de Gray (ne changer qu'un objet à chaque pas) n'est pas exploité (complément).
4. **Nom du fichier de test** : `ks_0_4` dans la consigne, `ks_4_0.txt` dans le code. Alerte de nom sans importance.
5. **`remplissage_aleatoire`** : la probabilité $1 - \frac{\ldots}{P}$ peut être négative pour un objet trop lourd, ce qui l'exclut (complément, sans conséquence sur le résultat).
6. **Programmation dynamique** : section annoncée et vide.
7. **Code généré** : l'auteur déclare que la majorité du code vient de ChatGPT et qu'il peut être inexact ; à relire avant de s'en servir.
8. **Propriété des gloutons** : la « sous-structure optimale » citée ne suffit pas à rendre un glouton optimal (il faut aussi la propriété du choix glouton), et la note dit elle-même plus loin que ces gloutons ne sont pas optimaux pour le sac à dos (complément). Le résumé « l'algo glouton divise le problème en sous-problèmes » rapproche le glouton de « diviser pour régner » : formulation de l'étudiant, à prendre avec recul.
9. **Commentaire de `glouton_valeur`** : il dit d'abord « trier par ordre décroissant », puis « ici par VALEUR croissante », avant d'expliquer `reverse=True` : formulation confuse, le résultat est bien un tri par valeur décroissante.
