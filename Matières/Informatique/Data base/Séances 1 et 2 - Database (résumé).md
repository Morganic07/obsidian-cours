---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]], dans [[Data base (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Concevoir une base de données relationnelle : lister les données (dictionnaire), les modéliser en entités et associations (MCD), puis en tirer les tables (MLD). La note mêle des diapositives du cours et des schémas manuscrits.

## 1. Les types de données SQL

Une zone surlignée en tête de note annonce un « tableau de variable » à rajouter, de mémoire avec les colonnes : nom variable, type, domaine, N / NN, particularité, et deux colonnes « ? » (tableau vide).

| Catégorie | Type [[Langage SQL\|SQL]] courant | Description | Exemple |
|---|---|---|---|
| Texte | [[Types de données SQL\|VARCHAR]](n) | Chaîne de longueur variable (max $n$) | Un nom, une adresse email |
| Texte | CHAR(n) | Chaîne qui a toujours la même longueur | Le sexe H/F ; un numéro de carte bancaire (16 chiffres) |
| Texte | TEXT | Long bloc de texte sans limite stricte | Un article de blog, un commentaire |
| Texte | ENUM | Valeur parmi des valeurs prédéfinies | « Petit », « Moyen », « Grand » |
| Nombre | INT / INTEGER | Entier positif ou négatif | Un âge, un nombre de vues |
| Nombre | DECIMAL(p,s) | [[Ensembles de nombres\|Décimal]] **précis** ($p$ = nombre total de chiffres, $s$ = chiffres après la virgule) | Un prix (19.99), des coordonnées GPS |
| Nombre | FLOAT | Virgule flottante, précision simple | |
| Date/Heure | DATE | Date seule (AAAA-MM-JJ) | Une date de naissance |
| Date/Heure | DATETIME / TIMESTAMP | Date et heure précises | Date de création d'un compte |
| Logique | BOOLEAN | Vrai ou faux (souvent 0 ou 1 en interne) | Abonnement actif (oui/non) |
| Binaire | BLOB | Données binaires brutes | Une image, un PDF |

- **Précision du DECIMAL** : pour de l'argent, ne jamais utiliser `FLOAT` ou `DOUBLE`, qui arrondissent « bizarrement » ; `DECIMAL` est exact.
- **NULL ou [[Valeur NULL|NOT NULL]]** : la colonne a-t-elle le droit d'être vide (`NULL`) ou est-elle obligatoire (`NOT NULL`) ?

## 2. Clé primaire et clé étrangère

[[Clé primaire et clé étrangère]] :
- La **clé primaire** d'une relation permet d'identifier un enregistrement sans ambiguïté.
- Elle peut regrouper plusieurs attributs.
- Les attributs qui ne sont pas clé primaire peuvent apparaître plusieurs fois dans différentes tables.
- Une **clé étrangère** d'une relation est une référence vers la clé primaire d'une autre relation.
- En pratique, les relations sont appelées « tables » : une clé étrangère est un attribut (ou plusieurs) d'une table qui référence la clé primaire d'une autre table.

## 3. Méthode MERISE en trois étapes

1. **[[Dictionnaire de données]]** : lister les données non décomposables, leur type et leurs caractéristiques (obligatoire / optionnel, valeur par défaut, contraintes particulières).
2. **Schéma entités / associations** ([[Modèle entité-association|schéma E/A]], *E/R Entity / Relationship diagram*) : le **MCD**, modèle conceptuel de données.
3. **[[Schéma relationnel]]** : le **MLD**, modèle logique de données.

### Étape 1 : le dictionnaire de données

Lister toutes les données à stocker et leurs particularités :

| Nom du champ | Type | Null / Non null | Autres caractéristiques | Valeur par défaut |
|---|---|---|---|---|
| NUMERO | CHAR(8) | NN | unique | |
| NOM | VARCHAR(30) | NN | | |
| … | | | | |

### Étape 2 : le schéma E/A (MCD)

Il représente les entités et les associations, les attributs et leurs types, les clés primaires et les cardinalités.

![[Séances 1 et 2 - Database - image4.png]]
*Figure : MCD — ETUDIANT (`numero CHAR(8)` souligné, `nom VARCHAR(30)`, `date_naissance DATE`) relié à FORMATION (`code CHAR(6)` souligné, `intitule VARCHAR(30)`) par l'association EST_INSCRIT, sans attribut ; cardinalités 1,1 côté ETUDIANT et 0,N côté FORMATION.*

### Étape 3 : le schéma relationnel (MLD)

La liste des tables avec leurs PK (*Primary Key*, soulignée) et FK (*Foreign Key*, préfixée par `#`) :
```
FORMATION ( code, intitule )
ETUDIANT ( numero, nom, date_naissance, #code )
```

![[Séances 1 et 2 - Database - image15.png]]
*Figure : la flèche part de `#code` dans ETUDIANT et pointe vers la clé primaire `code` de FORMATION : c'est la clé étrangère.*

## 4. MCD (ER diagram) : étude de cas

Énoncé : un étudiant peut avoir une formation.

![[Séances 1 et 2 - Database - image7.png]]
*Figure : schéma manuscrit — entités « étudiant » (`n° étudiant`, `nom`, …) et « formation » (`code format°`, `nom format°`, …), clés primaires annotées, association « est_inscrit » entre les deux.*

**Cardinalités :**
- ① 1,1 : l'étudiant a au minimum 1 formation et au maximum 1 formation ;
- ② 0,N : la formation a au minimum 0 étudiant et au maximum N étudiants.

## 5. MLD (relational diagram)

### « One to one »

[[Type d'association|One to one]] (annoncé « 1 étudiant = 1 formation ») : la liste des tables pour chaque entité. On a 2 tables :
```
formation( code formation, nom formation, ... )
étudiant( n° étudiant, ..., #code formation )
```
La clé étrangère (*foreign key*) est la clé primaire (*primary key*) d'une autre table.

![[Séances 1 et 2 - Database - image12.png]]
*Figure : la flèche rouge relie `code formation` (clé primaire de formation) à `#code formation` dans étudiant.*

![[Séances 1 et 2 - Database - image2.png]]
*Figure : à gauche (« me-to-one »), chaque $e_i$ va vers un seul $f_j$, mais $e_3$ et $e_4$ vont tous deux vers $f_3$ ; à droite (« many to many »), $e_1$ et $e_3$ vont chacun vers deux $f_j$.*

### Many to many

Many to many : un étudiant peut avoir plusieurs formations. On a 3 tables :
```
formation( code formation, nom formation, ... )
étudiant( n° étudiant, ... )            -- aucune clé étrangère
est_inscrit( #code formation, #n° étudiant )
```
Le couple (`#code formation`, `#n° étudiant`) devient la nouvelle clé primaire de `est_inscrit` : c'est une [[Table de correspondance|table de correspondance]].

![[Séances 1 et 2 - Database - image14.png]]
*Figure : correspondance « many to many » entre $e_1, \dots, e_n$ et $f_1, f_2, f_3$.*

### Exemple : redoublement et bourse

Énoncé : un étudiant redouble, et il est boursier ou non selon l'année.

![[Séances 1 et 2 - Database - image8.png]]
*Figure : $e_1 \to f_1$ « 22-23, boursier » ; $e_1 \to f_2$ « 24-23, non boursier ».*

On garde les mêmes tables `formation()` et `étudiant()`, et on rajoute deux paramètres à la table de correspondance :
```
est_inscrit( #code formation, #n° étudiant, année universitaire, boursier )
```
Les trois paramètres en rouge (`#code formation`, `#n° étudiant`, `année universitaire`) forment la nouvelle clé primaire.

![[Séances 1 et 2 - Database - image10.png]]
*Figure : schéma relationnel annoté — « on rajoute ces 2 paramètres », « les 3 paramètres en rouge sont la nouvelle primary key ».*

## 6. Règles de passage selon les cardinalités

- **Cardinalité 1-N (ou N-1)** : une clé étrangère doit apparaître du côté de la cardinalité « 1 ».
- **Cardinalité N-N (ou N-M)** : une table de correspondance doit être créée.
- **Association avec attribut(s) porté(s)** : une table supplémentaire doit être créée.
- **Cardinalité 1-1** : ne devrait pas apparaître dans un schéma de conception (on regroupe les entités, ou c'est une optimisation au moment de l'implémentation).

## 7. L'héritage

La liaison (association) « [[Héritage en base de données|is-a]] » : `Client` (`numero INT`) se spécialise en `PersonnePhysique` (`nom`, `prenom`) et `PersonneMorale` (`représentant`), avec cardinalité 0,1 côté `Client` et 1 côté sous-entité. Représentation [[UML]] (*Unified Modeling Language*) de la POO : `CompteBancaire` (`numero: INTEGER (PK)`) est la classe parente de `CompteCourant` (`decouvert: BOOLEAN`) et `CompteEpargne` (`TauxInteret: FLOAT`).

![[Séances 1 et 2 - Database - image13.png]]
*Figure : en haut, l'association is-a entre Client, PersonnePhysique et PersonneMorale ; en bas, le diagramme de classes UML des comptes bancaires.*

Schéma relationnel :
```
Client( numero, ... )
PersonnePhysique( #numeroPP, nom, prenom, ... )
PersonneMorale( #numeroPM, ... )
```
(`numeroPP` et `numeroPM` sont à la fois clé primaire, soulignée, et clé étrangère vers `Client`.)

## 8. Association réflexive

Une entité liée à **elle-même** : au lieu de relier deux entités différentes, le trait de l'association part d'une entité et y revient.
- **Exemple (TD)** : « Certains étudiants sont tuteurs, un étudiant peut au plus n'avoir qu'un tuteur. »
- **Modélisation** : l'entité ETUDIANT, avec une boucle nommée « Tutorer » ; cardinalité `0,1` d'un côté (un étudiant a 0 ou 1 tuteur), `0,N` de l'autre (un tuteur encadre plusieurs étudiants).

## 9. Entité faible

Une entité est **faible** quand elle ne peut pas être identifiée de manière unique par ses propres attributs : elle a besoin de l'identifiant d'une entité **forte**. Son existence en dépend entièrement : si on supprime l'entité forte, l'entité faible n'a plus de sens.
- **Exemple (TD)** : les « enfants mineurs du personnel ». Un enfant « Léo » né le 10/05/2015 n'est pas forcément unique dans la base de l'université ; pour l'identifier, il faut dire « c'est le fils de l'employé n°452 ».
- **Modélisation** : ENFANT relié à PERSONNEL, cardinalité obligatoirement `1,1` côté enfant (un enfant appartient à un et un seul parent du personnel dans ce contexte).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 8 (exemple de redoublement) a été ouverte ; les autres sont lues par leur transcription.

1. **« One to one » et le schéma qui l'accompagne** (complément). Le cours range sous « One to one » l'étude de cas « un étudiant a une formation », avec cardinalités 1,1 et 0,N. C'est une association many-to-one : plusieurs étudiants peuvent suivre la même formation. Le dessin de gauche (« me-to-one ») envoie $e_3$ et $e_4$ vers $f_3$, donc il n'est pas un one-to-one strict. L'alerte de la transcription est exacte. Le titre manuscrit est bien « me-to-one », probablement « one-to-one ».
2. **Exemple du redoublement** : image ouverte, la flèche du bas est bien « 24-23, non boursier ». Une année « 24-23 » est incohérente, on attend « 23-24 ». Le choix de cette année ne change pas la modélisation.
3. **Écriture manuscrite** : les fautes d'écriture manuscrite (« bousier », « format° », « primany ») sont des coquilles sans effet.
4. **Début de la note** : une zone surlignée « Rajouter tableau de variable » avec un tableau vide est un reste à compléter. Le contenu manque.
5. **Textes des encadrés** : plusieurs encadrés parlent à la deuxième personne (« Exemple de ton TD »). Leur ton diffère du reste de la note, on ne sait pas s'ils viennent du professeur.
6. **`DATETIME / TIMESTAMP`** sont présentés comme un seul type. Ils diffèrent selon le SGBD (complément).
7. **Transcriptions** (mentions « À vérifier » reprises) : dans les schémas « many to many », le dernier élément de gauche est écrit « $e_n$ » ou « $e_4$ », peu net ; une petite barre sous $f_3$ est sans doute un trait parasite ; « nv » se lit « nouvelle ».
