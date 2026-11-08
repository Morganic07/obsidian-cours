---
type: concept
tags: [year3]
aliases: [forme normale, formes normales, 1FN, 2FN, 3FN, dépendance fonctionnelle, dépendances fonctionnelles, normal form, database normalization]
matieres: [Data base]
sources: ["[[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la normalisation est la démarche qui vérifie qu'un [[Schéma relationnel|schéma relationnel]] ne stocke pas deux fois la même information. Une redondance provoque des **anomalies de mise à jour** : modifier une donnée à un endroit et pas à l'autre rend la base incohérente, insérer un fait oblige à en saisir un autre, supprimer une ligne fait perdre une information qui n'y était qu'en passant.

**Dépendance fonctionnelle.** Dans une relation $R$, l'attribut (ou groupe d'attributs) $A$ détermine $B$, noté $A \to B$, quand une valeur de $A$ correspond toujours à une seule valeur de $B$ : deux lignes qui ont le même $A$ ont le même $B$. Exemple : numéro d'étudiant $\to$ nom. Une [[Clé primaire et clé étrangère|clé primaire]] détermine tous les autres attributs de sa table.

**Les trois premières formes normales**, chacune contenant la précédente :

- **1FN** (première forme normale) : chaque attribut est **atomique**, une seule valeur par case. Une colonne `competences = "Java, SQL, Python"` viole la 1FN ; on crée une table à part, une ligne par compétence.
- **2FN** : la relation est en 1FN, et tout attribut non clé dépend de **toute** la clé primaire, pas d'une partie seulement. La question ne se pose que pour une clé composée. Dans `est_inscrit(#code_formation, #numero_etudiant, nom_formation)`, `nom_formation` ne dépend que de `code_formation` : il est répété pour chaque inscrit et doit rester dans la table `formation`.
- **3FN** : la relation est en 2FN, et aucun attribut non clé ne dépend d'un autre attribut non clé (pas de dépendance **transitive**). Dans `etudiant(numero, code_postal, ville)`, on a $\text{numero} \to \text{code\_postal} \to \text{ville}$ : la ville se met dans une table `commune(code_postal, ville)`.

Normaliser revient à **décomposer** une table en plusieurs, reliées par des clés étrangères, sans perdre d'information : la jointure des tables obtenues redonne la table de départ.

Il existe des formes plus exigeantes (forme normale de Boyce-Codd, 4FN, 5FN), rarement utiles en pratique. À l'inverse, on **dénormalise** parfois volontairement (entrepôts de données, tables de statistiques) pour éviter des jointures coûteuses, en acceptant la redondance.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[1 - Database]], après le passage du MCD au MLD : un MLD tiré d'un [[Modèle entité-association|MCD]] bien construit avec les règles de passage est en général déjà en 3FN. L'exigence de données « non décomposables » du [[Dictionnaire de données|dictionnaire de données]] correspond à la 1FN.

Voir aussi : [[Schéma relationnel]], [[Clé primaire et clé étrangère]], [[Table de correspondance]], [[Modèle entité-association]], [[Dictionnaire de données]]

Résumés : [[1 - Database]]
