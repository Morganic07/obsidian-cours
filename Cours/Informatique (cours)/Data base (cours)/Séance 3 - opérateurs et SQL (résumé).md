---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]], dans [[Data base (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les opérateurs de l'[[Algèbre relationnelle]] (sur une relation, entre deux relations, sur des relations de même schéma), puis le [[Langage SQL]] (DDL, DML, droits) et l'architecture d'un SGBD.

**Vocabulaire.**
- relation = table ; attributs = colonnes de la table (ex. relation `Etudiant`, attributs `id_etudiant`, `nom`, `age`) ;
- [[Système de gestion de base de données|SGBD]] : système de gestion de base de données ;
- SGBDR : SGBD relationnel, un type de SGBD.

## 1. Opérateurs sur une relation

### Projection $\pi_A(R)$

Choisir uniquement les **colonnes** qui intéressent : $\pi_A(R)$ est la projection de la relation $R$ sur l'attribut $A$ (une ou plusieurs colonnes).

![[Séance 3 - opérateurs et SQL - image31.png]]
*Figure : la projection garde certaines colonnes de la table (surlignées).*

**Exemple.** Table `Etudiant(ID, Nom, Age)`, on ne veut que les noms : $\pi_{Nom}(Etudiant)$ donne une table d'une seule colonne contenant tous les noms.

### Restriction $\sigma_F(R)$

Choisir uniquement les **lignes** (enregistrements) qui satisfont la condition $F$ ; on retient un ou plusieurs enregistrements.

![[Séance 3 - opérateurs et SQL - image3.png]]
*Figure : la restriction garde certaines lignes de la table (surlignées).*

**Exemple.** Les étudiants de plus de 20 ans : $\sigma_{Age>20}(Etudiant)$ donne toutes les colonnes, mais seulement pour ces étudiants.

### Renommage $\rho_{A \to B}$

Renomme, le temps de l'opération, l'attribut « A » en « B ». Indispensable quand deux attributs de même nom (appartenant à des relations différentes) sont présents dans l'opération.

## 2. Opérateurs entre deux relations

### Produit cartésien $R \times S$

Multiplication des tuples : chaque ligne de $R$ est associée à chaque ligne de $S$.

| A | B | C |
|---|---|---|
| A1 | B1 | C1 |
| A2 | B1 | C2 |
| A3 | B2 | C2 |

| D | E |
|---|---|
| D1 | E1 |
| D2 | E2 |

$R \times S$ (5 colonnes, $3 \times 2 = 6$ lignes) :

| A | B | C | D | E |
|---|---|---|---|---|
| A1 | B1 | C1 | D1 | E1 |
| A1 | B1 | C1 | D2 | E2 |
| A2 | B1 | C2 | D1 | E1 |
| A2 | B1 | C2 | D2 | E2 |
| A3 | B2 | C2 | D1 | E1 |
| A3 | B2 | C2 | D2 | E2 |

### Jointure naturelle $R \bowtie S$

Elle s'appuie sur les clés étrangères (ici l'attribut C de la première relation), ou plus exactement sur des **noms de champs identiques**. C'est l'opérateur le plus utilisé : il lie deux tables via un point commun, souvent une [[Clé primaire et clé étrangère|clé étrangère]] (ex. associer un `Etudiant` à sa `Classe` par `Id_Classe`).

**Note importante :** une jointure peut être vue comme un produit cartésien suivi d'une restriction sur le champ commun.

$R(A, B, C)$ et $S(C, D)$ :

| A | B | C |
|---|---|---|
| A1 | B1 | C1 |
| A2 | B2 | C2 |
| A3 | B3 | C2 |

| C | D |
|---|---|
| C1 | D1 |
| C2 | D2 |
| C3 | D3 |

$R \bowtie S$ :

| A | B | C | D |
|---|---|---|---|
| A1 | B1 | C1 | D1 |
| A2 | B2 | C2 | D2 |
| A3 | B3 | C2 | D2 |

(La ligne C3 de $S$ n'a pas de correspondant dans $R$ : elle disparaît.)

**Exemple : `PROGRAMME` ⋈ `SALLE`.**

`PROGRAMME` (le film et son identifiant de salle) :

| film | id_salle |
|---|---|
| Inception | S1 |
| Batman | S2 |
| Avatar | S1 |

`SALLE` (le nom de la salle et sa capacité) :

| id_salle | nom_salle | capacite |
|---|---|---|
| S1 | Salle IMAX | 300 |
| S2 | Salle Prestige | 50 |
| S3 | Salle Junior | 100 |

Déroulement :
1. Première ligne de `PROGRAMME` : « Inception » est en S1.
2. On cherche S1 dans `SALLE` : « Salle IMAX ».
3. On crée une ligne qui fusionne tout.
4. S3 (« Salle Junior ») est ignorée : aucun film n'y est programmé.

### Division $R \div S$ (ou $R / S$)

- $R$ (**dividende**) contient des couples d'éléments (ex. des étudiants et les matières qu'ils étudient).
- $S$ (**diviseur**) contient une liste d'éléments de référence (ex. des matières précises).
- Le résultat contient uniquement les éléments de $R$ associés à **tous** les éléments de $S$ : c'est un sous-ensemble des éléments de $R$ en relation avec tous ceux de $S$.

Exemple abstrait : $R = \{(A,X), (A,Y), (A,Z), (B,X), (C,Y), (C,Z)\}$, $S = \{X, Y\}$, donc $R \div S = \{A\}$ ($B$ n'a pas $Y$, $C$ n'a pas $X$).

**Exemple : certifications.** $R$ = `EMPLOYE_CERTIF` (quel employé possède quelle certification) :

| Employé | Certif |
|---|---|
| Alice | Sécurité |
| Alice | Réseau |
| Bob | Sécurité |
| Charlie | Sécurité |
| Charlie | Réseau |
| Charlie | Cloud |

$S$ = `REQUIS` (certifications obligatoires pour un poste) : Sécurité, Réseau.

Résultat de $R \div S$, les employés qui ont **à la fois** Sécurité et Réseau :
- **Alice** a les deux : dans le résultat ;
- **Bob** n'a que Sécurité : éliminé ;
- **Charlie** a les deux (et plus) : dans le résultat.

## 3. Opérateurs sur des relations de même schéma

Pour l'union, l'intersection et la différence, les deux tables doivent être « compatibles », c'est-à-dire avoir exactement le **même schéma** (ça n'a pas de sens de fusionner une liste de noms et une liste de prix de voitures) :
1. le même nombre de colonnes ;
2. des colonnes de mêmes types de données (texte avec texte) ;
3. en général, des colonnes de mêmes noms.

| Opérateur | Symbole | Résultat |
|---|---|---|
| Union | $R \cup S$ | tous les tuples de $R$ et de $S$ |
| Intersection | $R \cap S$ | les tuples présents à la fois dans $R$ et dans $S$ |
| Différence | $R \setminus S$ (parfois $R - S$) | les tuples de $R$ absents de $S$ |

![[Séance 3 - opérateurs et SQL - image27.png]]
*Figure : union, les deux cercles entiers en rouge.*

![[Séance 3 - opérateurs et SQL - image18.png]]
*Figure : intersection, seule la zone commune en rouge.*

![[Séance 3 - opérateurs et SQL - image20.png]]
*Figure : différence $R \setminus S$, la partie de $R$ hors de $S$ en rouge.*

## 4. Récapitulatif

- **Sur une relation** : projection, restriction, renommage d'attribut.
- **Entre deux relations** : produit cartésien, jointure (naturelle) ⇒ PK / FK, (division).
- **Sur des relations de même schéma** : union, intersection, différence.

Tous les opérateurs ne sont pas forcément implémentés dans les SGBD (ex. la division). Certains se réalisent de façon dérivée : une jointure s'exprime comme un produit cartésien suivi d'une restriction.

## 5. Le langage SQL

SQL (*Structured Query Language*) : langage de haut niveau syntaxique, le langage des SGBDR, langage de requêtes. Il existe **des** langages SQL, selon les SGBD et leurs implémentations.

### Requêtes de structure : DDL (*Data Definition Language*)

`CREATE`, `ALTER`, `DROP`, `DESCRIBE` : uniquement lors de la conception ou de la modification du **modèle**.

```sql
CREATE TABLE etudiant (numero INTEGER PRIMARY KEY, nom VARCHAR(30) NOT NULL, ...) ;
ALTER TABLE etudiant ADD COLUMN date_naissance DATE NOT NULL) ;   -- tel quel dans le cours, parenthèse en trop
DROP TABLE etudiant ;
DESCRIBE etudiant ;
```
NB : la syntaxe peut (beaucoup) varier d'un SGBDR à l'autre, en particulier pour `DESCRIBE`.

### Requêtes DML (*Data Manipulation Language*)

`INSERT INTO ... ;`, `UPDATE ... SET ... ;`, `DELETE FROM ... ;`, `SELECT ... FROM ... [WHERE ...] ;`. Ce sont les plus courantes, en particulier `SELECT`.

```sql
INSERT INTO etudiant (numero, nom, prenom) VALUES (2201234, 'MARTIN', 'Luc') ;
UPDATE etudiant SET prenom='Jean' WHERE numero=2201234 ;
DELETE FROM etudiant WHERE numero=2201234 ;
SELECT * FROM etudiant ;
SELECT nom, prenom FROM etudiant WHERE numero > 2200001 ;
```

### Gestion des droits

Les privilèges des utilisateurs sur les éléments de la base : [[Gestion des droits SQL|GRANT]] et `REVOKE`, généralement réservés aux administrateurs.

```sql
GRANT ALL PRIVILEGES ON dbname TO user IDENTIFIED BY password ;
REVOKE UPDATE ON dbname.tablename TO user ;   -- tel quel dans le cours : il faut FROM, voir les points à vérifier
```
NB : la syntaxe peut **beaucoup** différer d'un SGBDR à l'autre.

## 6. Architecture

- **Client – serveur : 2 *tiers*** (*tier* = niveau), en mode console ou en mode graphique.

![[Séance 3 - opérateurs et SQL - image21.png]]
*Figure : un client en mode console relié directement au SGBD.*

![[Séance 3 - opérateurs et SQL - image29.png]]
*Figure : un client en mode graphique relié directement au SGBD.*

- **Architecture Web 3 *tiers*** : navigateur web → serveur web → SGBD.

![[Séance 3 - opérateurs et SQL - image30.png]]
*Figure : navigateur web, serveur web et base de données en trois niveaux.*

- Les architectures 2 ou 3 *tiers* peuvent être exécutées en local (sans réseau).
- Elles peuvent être considérées au niveau applicatif : 3 *tiers* est la solution classique du Web, mais 4 *tiers* et plus sont possibles avec un [[Architecture n-tiers|serveur d'application]].
- L'administration des SGBD peut se faire en 2 ou 3 *tiers*, mais jamais en 1 *tier*.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 19 (droits) a été ouverte ; les autres sont lues par leur transcription.

1. **`REVOKE UPDATE ON dbname.tablename TO user ;`** (complément). **À corriger avant un examen.** Image ouverte : le cours écrit bien `TO`. En SQL, on retire un droit avec `REVOKE ... FROM user`. `TO` appartient à `GRANT`. Même ligne : `dbname.tablename` désigne une table alors que le `GRANT` voisin vise une base (`dbname`).
2. **`GRANT ... IDENTIFIED BY password`** (complément) : cette forme est propre à certaines versions de MySQL. Le cours précise de toute façon que la syntaxe varie beaucoup.
3. **`ALTER TABLE ... DATE NOT NULL) ;`** : la parenthèse fermante est en trop. Alerte de la transcription confirmée par le texte.
4. **`DESCRIBE`** est rangé dans le DDL, mais c'est une commande propre à certains SGBD (le cours le signale : syntaxe variable).
5. **Fausses alertes** : « +1 » et « +2 » sont des badges d'interface, pas du cours.
6. **Images de la division** : l'image de la relation `R` semble coupée en bas, d'autres lignes pourraient manquer. Le résultat du cours reste cohérent avec les lignes visibles.
7. **Contenu absent** : pas de jointure SQL ni de `GROUP BY` dans cette note.
8. **Transcriptions** (mentions reprises) : les trois tableaux de la division abstraite n'ont pas d'en-tête sur l'image (noms $R$, $S$, $R \div S$ déduits du texte) ; dans le tableau des certifications, « Cloud » n'est pas en gras ; la ligne « (*tier* ↔ niveau) » est en partie coupée par le schéma.
