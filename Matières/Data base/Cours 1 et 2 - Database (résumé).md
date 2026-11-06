---
type: source
tags: [year3]
sources: ["[[Cours 1 et 2 - Database]]"]
maj: 2026-11-05
---

Résumé de [[Cours 1 et 2 - Database]], dans [[Data base (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Concevoir une base de données relationnelle : lister les données, les modéliser en entités et associations, puis en tirer les tables.

## Contenu, dans l'ordre du cours

- **Types de données SQL** : texte (`VARCHAR(n)`, `CHAR(n)` pour une longueur fixe, `TEXT`, `ENUM`), nombres (`INT`, `DECIMAL(p,s)` exact, donc à préférer pour l'argent, `FLOAT`), dates (`DATE`, `DATETIME` ou `TIMESTAMP`), `BOOLEAN`, `BLOB`. Une colonne est `NULL` (peut être vide) ou `NOT NULL` (obligatoire).
- **[[Clé primaire et clé étrangère]]** : la clé primaire identifie un enregistrement sans ambiguïté, éventuellement sur plusieurs attributs. La clé étrangère référence la clé primaire d'une autre table.
- **Méthode MERISE en 3 étapes** : dictionnaire de données (nom, type, null ou non, caractéristiques, valeur par défaut), puis schéma entités/associations ([[Modèle entité-association]]), puis schéma relationnel ([[Schéma relationnel]]). Exemple : `ETUDIANT(numero, nom, date_naissance)` et `FORMATION(code, intitule)`, associés par `EST_INSCRIT`.
- **Cardinalités** : « 1,1 : minimum 1 et maximum 1 formation par étudiant », « 0,N : une formation a de 0 à N étudiants ».
- **Passage au relationnel** : cas *one to one* (annoncé « un étudiant = une formation »), clé étrangère `#code formation` dans `étudiant`. Cas *many to many* : table de correspondance `est_inscrit(#code, #numéro)`, dont le couple est la clé primaire. Exemple du redoublement et de la bourse : `est_inscrit(#code, #numéro, année universitaire, boursier)`, avec trois attributs en clé primaire.
- **Règles** : 1-N : clé étrangère du côté « 1 » ; N-N : table de correspondance ; association avec attributs : table supplémentaire ; 1-1 : ne devrait pas apparaître dans un schéma de conception.
- **Héritage** : liaison « is-a » (`Client` avec `PersonnePhysique` et `PersonneMorale`), schéma relationnel `Client(numero)`, `PersonnePhysique(#numeroPP, nom, prenom)`, `PersonneMorale(#numeroPM)`. L'UML l'illustre avec `CompteBancaire`, `CompteCourant`, `CompteEpargne`.
- **Association réflexive** : une entité liée à elle-même (étudiant tuteur d'un autre : 0,1 d'un côté, 0,N de l'autre).
- **Entité faible** : elle n'est identifiée qu'avec l'identifiant d'une entité forte (enfants mineurs du personnel, cardinalité 1,1 côté enfant).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 8 (exemple de redoublement) a été ouverte ; les autres sont lues par leur transcription.

1. **« One to one » et le schéma qui l'accompagne** (complément). Le cours range sous « One to one » l'étude de cas « un étudiant a une formation », avec cardinalités 1,1 et 0,N. C'est une association many-to-one : plusieurs étudiants peuvent suivre la même formation. Le dessin de gauche (« me-to-one ») envoie $e_3$ et $e_4$ vers $f_3$, donc il n'est pas un one-to-one strict. L'alerte de la transcription est exacte. Le titre manuscrit est bien « me-to-one », probablement « one-to-one ».
2. **Exemple du redoublement** : image ouverte, la flèche du bas est bien « 24-23, non boursier ». Une année « 24-23 » est incohérente, on attend « 23-24 ». Le choix de cette année ne change pas la modélisation.
3. **Écriture manuscrite** : les fautes d'écriture manuscrite (« bousier », « format° », « primany ») sont des coquilles sans effet.
4. **Début de la note** : une zone surlignée « Rajouter tableau de variable » avec un tableau vide est un reste à compléter. Le contenu manque.
5. **Textes des encadrés** : plusieurs encadrés parlent à la deuxième personne (« Exemple de ton TD »). Leur ton diffère du reste de la note, on ne sait pas s'ils viennent du professeur.
6. **`DATETIME / TIMESTAMP`** sont présentés comme un seul type. Ils diffèrent selon le SGBD (complément).
