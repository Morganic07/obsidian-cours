---
type: source
sources: ["[[Cours 5 - Hypothesis Testing]]"]
maj: 2026-11-05
---

Résumé de [[Cours 5 - Hypothesis Testing]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Un test d'hypothèse décide, à partir d'un échantillon, si une affirmation sur un paramètre est crédible. Le cours donne le principe, les erreurs possibles, la procédure en six étapes et la façon de poser $H_0$ et $H_1$.

## Contenu, dans l'ordre du cours

- **Quand tester** : si une affirmation est faite sur un paramètre, on fait un test. Si aucune affirmation n'est faite et qu'on veut estimer un paramètre, on construit un intervalle de confiance.
- **Principe** : on compare l'hypothèse à la statistique de l'échantillon. L'écart est-il dû au hasard ou significatif ? S'il est significatif, on rejette l'hypothèse, sinon on ne peut pas la rejeter.
- **Hypothèses** : $H_0$ (nulle) contient la valeur testée et sert de référence. $H_1$ (alternative) n'est « acceptée » que si l'on prouve que $H_0$ est fausse.
- **On n'accepte jamais $H_0$** : faute de preuve on ne la rejette pas, comme un accusé « non coupable » faute de preuves.
- **Deux erreurs** :

| Décision | $H_0$ vraie | $H_0$ fausse |
|---|---|---|
| Ne pas rejeter $H_0$ | correct | erreur $\beta$ (type II) |
| Rejeter $H_0$ | erreur $\alpha$ (type I) | correct |

- **Compromis** : diminuer $\alpha$ fait augmenter $\beta$, et inversement. Même logique que l'intervalle de confiance : plus de confiance impose un intervalle plus large.
- **Procédure** : 1. formuler $H_0$ et $H_1$ ; 2. fixer le seuil $\alpha$ (0,05 ou 0,01), probabilité de rejeter $H_0$ alors qu'elle est vraie ; 3. choisir la statistique de test (loi $Z$, ou $t$ pour les petits échantillons) ; 4. établir la valeur critique, en dessinant la courbe ; 5. calculer la valeur de la statistique sur l'échantillon ; 6. décider.
- **Test bilatéral ou unilatéral** : en bilatéral, $\alpha$ est partagé entre les deux queues. En unilatéral, $\alpha$ est dans une seule queue. La zone de rejet correspond toujours à $H_1$. « Exactement 1 mg d'aspirine » donne un test bilatéral. « Au moins 100 raisins » donne un test unilatéral.
- **Placer l'affirmation** : une entreprise qui veut prouver sa propre affirmation la met dans $H_1$ (le coût d'une erreur est élevé). Un contrôleur ou un concurrent qui la conteste la met dans $H_0$.
- **Outils** : la statistique de test est calculée sur l'échantillon. La p-value est la probabilité d'obtenir les résultats observés, ou plus extrêmes, si $H_0$ est vraie.

| Test | Statistique |
|---|---|
| z-test | z |
| t-test | t |
| ANOVA | [[Statistique F\|F]] |
| Test du χ² | χ² |

- **Probabilité et vraisemblance** : la probabilité va des paramètres vers les données (le paramètre est fixe), la vraisemblance va des données vers les paramètres (les données sont fixes). Dans un test, la p-value sert à juger la vraisemblance de $H_0$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les deux images (arbre de décision et tableau des erreurs) n'ont pas été ouvertes.

1. **Symboles manquants** : la note écrit « $H_1$ : $\mu = 12{,}7$ » et, pour le bilatéral, « $\mu = \#$ ou $\mu \ne \#$ ». Le texte converti a perdu les signes : il faut lire $H_1 : \mu \ne 12{,}7$, et $\mu > \#$ ou $\mu < \#$ (complément).
2. **Exemple unilatéral des raisins** : seule une moyenne d'échantillon inférieure à 100 pose problème, donc $H_1 : \mu < 100$ et la zone de rejet est à gauche. Le cours ne l'écrit pas ainsi (complément).
