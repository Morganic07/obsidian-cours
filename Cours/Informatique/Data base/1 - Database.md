---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]], dans [[Cours/Informatique/Data base/_index|Data base]]. Les passages ajoutés finissent par ⓘ.

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
- **Pourquoi FLOAT arrondit** : `FLOAT` (et `DOUBLE`, sa version double précision) stocke le nombre en binaire, où beaucoup de décimaux simples n'ont pas d'écriture finie, comme $0{,}1$ ; on stocke donc une valeur approchée, et les erreurs s'accumulent dans les sommes. `DECIMAL` stocke les chiffres décimaux eux-mêmes : $0{,}10 + 0{,}20$ y vaut exactement $0{,}30$. [[Complément hors du cours|ⓘ]]
- **`NULL` n'est pas zéro** : c'est l'absence de valeur (inconnue ou sans objet), différente de `0` ou de la chaîne vide `''`. Toute comparaison avec `NULL` donne « inconnu » : on teste avec `IS NULL` / `IS NOT NULL`, jamais avec `= NULL`. [[Complément hors du cours|ⓘ]]

## 2. Clé primaire et clé étrangère

[[Clé primaire et clé étrangère]] :
- La **clé primaire** d'une relation permet d'identifier un enregistrement sans ambiguïté.
- Elle peut regrouper plusieurs attributs.
- Les attributs qui ne sont pas clé primaire peuvent apparaître plusieurs fois dans différentes tables.
- Une **clé étrangère** d'une relation est une référence vers la clé primaire d'une autre relation.
- En pratique, les relations sont appelées « tables » : une clé étrangère est un attribut (ou plusieurs) d'une table qui référence la clé primaire d'une autre table.
- Une clé primaire est **unique** (deux lignes ne la partagent pas), **non NULL** et **minimale** (on ne peut retirer aucun de ses attributs sans perdre l'unicité). Une table n'a qu'une clé primaire, mais peut avoir d'autres **clés candidates**, déclarées `UNIQUE` (un e-mail, un numéro de sécurité sociale). [[Complément hors du cours|ⓘ]]
- **Clé naturelle ou artificielle** : une clé naturelle est une donnée du monde réel (numéro d'étudiant, ISBN) ; une clé artificielle est un identifiant sans signification créé pour la base, souvent une [[Clé auto-incrémentée|clé auto-incrémentée]]. On préfère souvent la seconde, qui ne change jamais. [[Complément hors du cours|ⓘ]]
- **Intégrité référentielle** : le SGBD refuse une clé étrangère qui ne correspond à aucune clé primaire existante (elle peut seulement être `NULL` si la colonne l'autorise), et il faut dire ce qui se passe quand on supprime la ligne référencée : refus (par défaut), `ON DELETE CASCADE` (on supprime aussi les lignes qui la référencent) ou `ON DELETE SET NULL`. C'est une [[Contrainte d'intégrité|contrainte d'intégrité]]. [[Complément hors du cours|ⓘ]]

## 3. Méthode MERISE en trois étapes

1. **[[Dictionnaire de données]]** : lister les données non décomposables, leur type et leurs caractéristiques (obligatoire / optionnel, valeur par défaut, contraintes particulières).
2. **Schéma entités / associations** ([[Modèle entité-association|schéma E/A]], *E/R Entity / Relationship diagram*) : le **MCD**, modèle conceptuel de données.
3. **[[Schéma relationnel]]** : le **MLD**, modèle logique de données.

MERISE est une méthode française de conception des systèmes d'information, née à la fin des années 1970. Elle sépare le **quoi** (MCD, indépendant de toute technique) du **comment** (MLD, propre au modèle relationnel). Après le MLD vient le **MPD**, modèle physique de données : le script SQL (`CREATE TABLE`, types exacts, index) écrit pour un SGBD précis. [[Complément hors du cours|ⓘ]]

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

**Lire une cardinalité.** En MERISE, le couple (min, max) s'écrit **à côté de l'entité qu'il décrit** et répond à la question « une occurrence de cette entité participe à combien d'associations, au moins et au plus ? ». Le minimum vaut 0 (participation facultative) ou 1 (obligatoire), le maximum 1 ou N (plusieurs). Attention : en [[UML]], les multiplicités se lisent dans l'autre sens, écrites du côté opposé. On classe l'association d'après les deux maximums : ici 1 et N, soit une association « 1-N » ([[Type d'association]]). [[Complément hors du cours|ⓘ]]

## 5. MLD (relational diagram)

### Many to one

[[Type d'association|Many to one]] (chaque étudiant suit une seule formation, mais une formation accueille plusieurs étudiants : cardinalités 1,1 et 0,N) : la liste des tables pour chaque entité. On a 2 tables : [[Erreurs du cours#^e-1-database|✎]]
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

En SQL, la table de correspondance déclare une clé primaire composée et deux clés étrangères : [[Complément hors du cours|ⓘ]]
```sql
CREATE TABLE est_inscrit (
  code_formation CHAR(6) REFERENCES formation(code),
  numero_etudiant CHAR(8) REFERENCES etudiant(numero),
  PRIMARY KEY (code_formation, numero_etudiant)
);
```

![[Séances 1 et 2 - Database - image14.png]]
*Figure : correspondance « many to many » entre $e_1, \dots, e_n$ et $f_1, f_2, f_3$.*

### Exemple : redoublement et bourse

Énoncé : un étudiant redouble, et il est boursier ou non selon l'année.

![[Séances 1 et 2 - Database - image8.png]]
*Figure : $e_1 \to f_1$ « 22-23, boursier » ; $e_1 \to f_2$ l'année suivante, « non boursier ».* [[Erreurs du cours#^e-1-database|✎]]

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

**La normalisation.** Une fois les tables obtenues, on vérifie qu'elles ne stockent pas deux fois la même information, source d'incohérences (modifier une adresse à un endroit et pas à l'autre). On s'appuie sur les **dépendances fonctionnelles** : $A \to B$ quand une valeur de $A$ détermine une seule valeur de $B$ (le numéro d'étudiant détermine son nom). Les trois premières [[Normalisation (base de données)|formes normales]] : [[Complément hors du cours|ⓘ]]
- **1FN** : chaque attribut est atomique (une seule valeur par case, pas de liste « Java, SQL, Python ») ; c'est exactement l'exigence de données « non décomposables » du dictionnaire ; [[Complément hors du cours|ⓘ]]
- **2FN** : 1FN, et tout attribut non clé dépend de **toute** la clé primaire, pas d'une partie seulement. Dans `est_inscrit(#code formation, #n° étudiant, nom formation)`, `nom formation` ne dépend que de `code formation` : il doit rester dans `formation` ; [[Complément hors du cours|ⓘ]]
- **3FN** : 2FN, et aucun attribut non clé ne dépend d'un autre attribut non clé. Dans `étudiant(n° étudiant, code postal, ville)`, la ville dépend du code postal : on la met dans une table à part. [[Complément hors du cours|ⓘ]]

Un MLD tiré d'un MCD bien construit avec les règles ci-dessus est en général déjà en 3FN. [[Complément hors du cours|ⓘ]]

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

Ce passage (une table pour l'entité mère, une par sous-entité, reliées par la clé) est l'une des trois traductions classiques de l'héritage : [[Complément hors du cours|ⓘ]]
- **une table par entité** (celle du cours) : pas de colonne vide, mais une jointure pour reconstituer un client complet ; [[Complément hors du cours|ⓘ]]
- **une seule table** `Client(numero, type, nom, prenom, representant, …)` avec une colonne `type` qui dit la sous-entité : pas de jointure, mais beaucoup de `NULL` (une personne morale n'a pas de prénom) ; [[Complément hors du cours|ⓘ]]
- **une table par sous-entité seulement**, chacune recopiant les attributs de `Client` : pas de jointure, mais plus de table commune pour référencer « un client » quelconque. [[Complément hors du cours|ⓘ]]

## 8. Association réflexive

Une entité liée à **elle-même** : au lieu de relier deux entités différentes, le trait de l'association part d'une entité et y revient.
- **Exemple (TD)** : « Certains étudiants sont tuteurs, un étudiant peut au plus n'avoir qu'un tuteur. »
- **Modélisation** : l'entité ETUDIANT, avec une boucle nommée « Tutorer » ; cardinalité `0,1` d'un côté (un étudiant a 0 ou 1 tuteur), `0,N` de l'autre (un tuteur encadre plusieurs étudiants).
- **Passage au MLD** : c'est une association 1-N, donc on applique la règle habituelle, mais la clé étrangère pointe vers la **même table** : `ETUDIANT(numero, nom, …, #numero_tuteur)`, où `numero_tuteur` référence `numero` et peut être `NULL` (étudiant sans tuteur). Une association réflexive N-N donnerait une table de correspondance avec deux clés étrangères vers ETUDIANT, à nommer différemment. [[Complément hors du cours|ⓘ]]

## 9. Entité faible

Une entité est **faible** quand elle ne peut pas être identifiée de manière unique par ses propres attributs : elle a besoin de l'identifiant d'une entité **forte**. Son existence en dépend entièrement : si on supprime l'entité forte, l'entité faible n'a plus de sens.
- **Exemple (TD)** : les « enfants mineurs du personnel ». Un enfant « Léo » né le 10/05/2015 n'est pas forcément unique dans la base de l'université ; pour l'identifier, il faut dire « c'est le fils de l'employé n°452 ».
- **Modélisation** : ENFANT relié à PERSONNEL, cardinalité obligatoirement `1,1` côté enfant (un enfant appartient à un et un seul parent du personnel dans ce contexte).
- **Passage au MLD** : la clé primaire de l'entité faible combine la clé de l'entité forte et un attribut propre (son **identifiant partiel**) : `ENFANT(#numero_employe, prenom, date_naissance)`, avec (`#numero_employe`, `prenom`) pour clé. On déclare en général la clé étrangère avec `ON DELETE CASCADE` : supprimer l'employé supprime ses enfants, ce qui traduit la dépendance d'existence. [[Complément hors du cours|ⓘ]]
