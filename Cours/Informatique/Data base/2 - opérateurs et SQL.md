---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]], dans [[Cours/Informatique/Data base/_index|Data base]]. Les passages ajoutés finissent par ⓘ.

## Idée générale

Les opérateurs de l'[[Algèbre relationnelle]] (sur une relation, entre deux relations, sur des relations de même schéma), puis le [[Langage SQL]] (DDL, DML, droits) et l'architecture d'un SGBD.

**Vocabulaire.**
- relation = table ; attributs = colonnes de la table (ex. relation `Etudiant`, attributs `id_etudiant`, `nom`, `age`) ;
- [[Système de gestion de base de données|SGBD]] : système de gestion de base de données ;
- SGBDR : SGBD relationnel, un type de SGBD.
- tuple = ligne (enregistrement) ; le nombre de colonnes est le **degré** de la relation, le nombre de lignes sa **cardinalité**. [[Complément hors du cours|ⓘ]]

Le modèle relationnel et son algèbre ont été proposés par Edgar F. Codd, chercheur chez IBM, en 1970. Une relation y est un **ensemble** de tuples : pas de doublon, pas d'ordre des lignes. Chaque opérateur prend une ou deux relations et rend une relation, ce qui permet de les enchaîner. [[Complément hors du cours|ⓘ]]

Exemples de SGBDR : [[PostgreSQL]], MySQL / MariaDB, SQLite, Oracle Database, Microsoft SQL Server. À côté existent les bases **NoSQL** (documents, clé-valeur, graphes), qui abandonnent le modèle en tables pour d'autres besoins. [[Complément hors du cours|ⓘ]]

## 1. Opérateurs sur une relation

### Projection $\pi_A(R)$

Choisir uniquement les **colonnes** qui intéressent : $\pi_A(R)$ est la projection de la relation $R$ sur l'attribut $A$ (une ou plusieurs colonnes).

![[Séance 3 - opérateurs et SQL - image31.png]]
*Figure : la projection garde certaines colonnes de la table (surlignées).*

**Exemple.** Table `Etudiant(ID, Nom, Age)`, on ne veut que les noms : $\pi_{Nom}(Etudiant)$ donne une table d'une seule colonne contenant tous les noms.

En algèbre, la projection supprime les doublons (deux étudiants « Martin » ne donnent qu'une ligne). Son équivalent SQL, `SELECT Nom FROM Etudiant`, les garde : il faut écrire `SELECT DISTINCT Nom FROM Etudiant`. [[Complément hors du cours|ⓘ]]

### Restriction $\sigma_F(R)$

Choisir uniquement les **lignes** (enregistrements) qui satisfont la condition $F$ ; on retient un ou plusieurs enregistrements.

![[Séance 3 - opérateurs et SQL - image3.png]]
*Figure : la restriction garde certaines lignes de la table (surlignées).*

**Exemple.** Les étudiants de plus de 20 ans : $\sigma_{Age>20}(Etudiant)$ donne toutes les colonnes, mais seulement pour ces étudiants.

La restriction s'appelle aussi **sélection** (d'où le $\sigma$) et correspond au `WHERE` de SQL, alors que le mot-clé `SELECT` correspond à la projection. La condition $F$ peut combiner des comparaisons avec et ($\wedge$), ou ($\vee$), non ($\neg$). On compose les opérateurs : les noms des plus de 20 ans s'écrivent $\pi_{Nom}(\sigma_{Age>20}(Etudiant))$, soit `SELECT Nom FROM Etudiant WHERE Age > 20`. [[Complément hors du cours|ⓘ]]

### Renommage $\rho_{A \to B}$

Renomme, le temps de l'opération, l'attribut « A » en « B ». Indispensable quand deux attributs de même nom (appartenant à des relations différentes) sont présents dans l'opération.

En SQL, le renommage s'écrit avec `AS` : `SELECT nom AS nom_etudiant FROM Etudiant`. `AS` renomme aussi une table (`FROM Etudiant AS e`), ce qui sert pour joindre une table avec elle-même, par exemple un étudiant et son tuteur. [[Complément hors du cours|ⓘ]]

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

En général, $R \times S$ a pour degré la somme des degrés et pour cardinalité le produit $|R| \times |S|$ : sur deux tables de 1 000 lignes, un million de lignes. En SQL : `SELECT * FROM R CROSS JOIN S`, ou `FROM R, S` sans condition. Oublier la condition de jointure produit ce résultat par accident. [[Complément hors du cours|ⓘ]]

### Jointure naturelle $R \bowtie S$

Elle s'appuie sur les clés étrangères (ici l'attribut C de la première relation), ou plus exactement sur des **noms de champs identiques**. C'est l'opérateur le plus utilisé : il lie deux tables via un point commun, souvent une [[Clé primaire et clé étrangère|clé étrangère]] (ex. associer un `Etudiant` à sa `Classe` par `Id_Classe`).

**Note importante :** une jointure peut être vue comme un produit cartésien suivi d'une restriction sur le champ commun.

Pour $R(A, B, C)$ et $S(C, D)$, cela s'écrit $R \bowtie S = \pi_{A,B,R.C,D}(\sigma_{R.C = S.C}(R \times S))$ : la projection finale ne garde qu'une colonne C. Quand la condition est quelconque (pas forcément une égalité de champs de même nom), on parle de **θ-jointure** ($R \bowtie_{\theta} S$). [[Complément hors du cours|ⓘ]]

En SQL, on écrit le plus souvent la condition explicitement : `SELECT * FROM R JOIN S ON R.C = S.C` (jointure **interne**, `INNER JOIN`). `NATURAL JOIN` existe mais joint sur **toutes** les colonnes de même nom, ce qui peut surprendre si deux tables ont par hasard une colonne `nom` commune. Pour garder les lignes sans correspondance (comme la salle S3 plus bas), on utilise une [[Jointure externe|jointure externe]] (`LEFT JOIN`). [[Complément hors du cours|ⓘ]]

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

En SQL : [[Complément hors du cours|ⓘ]]
```sql
SELECT p.film, s.nom_salle, s.capacite
FROM PROGRAMME p JOIN SALLE s ON p.id_salle = s.id_salle ;
```

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

La division n'est pas un opérateur de base : pour $R(A, B)$ et $S(B)$, elle se déduit des autres par $R \div S = \pi_A(R) \setminus \pi_A\big((\pi_A(R) \times S) \setminus R\big)$. Lecture : $\pi_A(R) \times S$ liste tous les couples (employé, certification requise) qu'il faudrait avoir ; en retirant $R$, il reste ceux qui manquent ; on retire enfin les employés à qui il manque quelque chose. [[Complément hors du cours|ⓘ]]

SQL n'a pas d'opérateur de division. La façon la plus lisible de l'écrire compte les certifications requises de chaque employé : [[Complément hors du cours|ⓘ]]
```sql
SELECT Employe
FROM EMPLOYE_CERTIF
WHERE Certif IN (SELECT Certif FROM REQUIS)
GROUP BY Employe
HAVING COUNT(DISTINCT Certif) = (SELECT COUNT(*) FROM REQUIS) ;
```
Elle repose sur une [[Sous-requête|sous-requête]] et une [[Fonction d'agrégation|fonction d'agrégation]] ; l'autre écriture classique utilise deux `NOT EXISTS` imbriqués (« il n'existe pas de certification requise que l'employé n'ait pas »). [[Complément hors du cours|ⓘ]]

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

En SQL, ces opérateurs s'écrivent entre deux `SELECT` : `UNION`, `INTERSECT` et `EXCEPT` (`MINUS` sous Oracle). `UNION` supprime les doublons ; `UNION ALL` les garde et va plus vite. La différence n'est pas commutative ($R \setminus S \neq S \setminus R$ en général), contrairement à l'union et à l'intersection. L'intersection se déduit de la différence : $R \cap S = R \setminus (R \setminus S)$. [[Complément hors du cours|ⓘ]]

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

SQL est né chez IBM au milieu des années 1970 (sous le nom SEQUEL), puis a été normalisé par l'ANSI en 1986 et l'ISO en 1987 ; la norme a été révisée de nombreuses fois depuis. Chaque SGBD en implémente une partie, plus ses propres extensions, d'où les variantes. C'est un langage **déclaratif** : on décrit le résultat voulu, et le SGBD choisit lui-même comment le calculer (ordre des opérations, index), grâce à son optimiseur de requêtes. [[Complément hors du cours|ⓘ]]

### Requêtes de structure : DDL (*Data Definition Language*)

`CREATE`, `ALTER`, `DROP`, `DESCRIBE` : uniquement lors de la conception ou de la modification du **modèle**. [[Erreurs du cours#^e-2-operateurs-et-sql|✎]]

```sql
CREATE TABLE etudiant (numero INTEGER PRIMARY KEY, nom VARCHAR(30) NOT NULL, ...) ;
ALTER TABLE etudiant ADD COLUMN date_naissance DATE NOT NULL ;
DROP TABLE etudiant ;
DESCRIBE etudiant ;
```
NB : la syntaxe peut (beaucoup) varier d'un SGBDR à l'autre, en particulier pour `DESCRIBE`.

`DESCRIBE` est la commande de MySQL et d'Oracle (dans son outil en ligne de commande) ; sous [[PostgreSQL]], on tape `\d etudiant` dans le client `psql`, et sous SQLite `PRAGMA table_info(etudiant);`. [[Complément hors du cours|ⓘ]]

À ne pas confondre : `DROP TABLE` supprime la table elle-même (structure et données) ; `DELETE FROM etudiant` (DML) vide ses lignes en gardant la structure ; `TRUNCATE TABLE etudiant` la vide aussi, plus vite, sans condition possible. [[Complément hors du cours|ⓘ]]

Les [[Contrainte d'intégrité|contraintes]] se déclarent dans le `CREATE TABLE` : `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT valeur`, `CHECK (age >= 0)`, et `FOREIGN KEY (code) REFERENCES formation(code)` pour une clé étrangère. C'est la traduction directe du dictionnaire de données (voir [[1 - Database]]). [[Complément hors du cours|ⓘ]]

### Requêtes DML (*Data Manipulation Language*)

`INSERT INTO ... ;`, `UPDATE ... SET ... ;`, `DELETE FROM ... ;`, `SELECT ... FROM ... [WHERE ...] ;`. Ce sont les plus courantes, en particulier `SELECT`.

```sql
INSERT INTO etudiant (numero, nom, prenom) VALUES (2201234, 'MARTIN', 'Luc') ;
UPDATE etudiant SET prenom='Jean' WHERE numero=2201234 ;
DELETE FROM etudiant WHERE numero=2201234 ;
SELECT * FROM etudiant ;
SELECT nom, prenom FROM etudiant WHERE numero > 2200001 ;
```

Attention : un `UPDATE` ou un `DELETE` **sans** `WHERE` s'applique à toutes les lignes de la table. [[Complément hors du cours|ⓘ]]

La forme complète d'un `SELECT`, dans l'ordre d'écriture : [[Complément hors du cours|ⓘ]]
```sql
SELECT colonnes          -- projection (et calculs, fonctions d'agrégation)
FROM tables / jointures  -- produit cartésien ou jointure
WHERE condition          -- restriction des lignes
GROUP BY colonnes        -- regroupement
HAVING condition         -- restriction des groupes
ORDER BY colonnes [ASC | DESC] ;  -- tri du résultat
```
Le SGBD l'évalue dans un autre ordre : `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, puis `ORDER BY`. C'est pourquoi on ne peut pas filtrer sur un `COUNT(*)` dans le `WHERE` (les groupes n'existent pas encore) : il faut `HAVING`, voir [[Fonction d'agrégation]]. [[Complément hors du cours|ⓘ]]

**Transactions.** Plusieurs requêtes DML peuvent former une [[Transaction (base de données)|transaction]], exécutée en entier ou pas du tout : `BEGIN` (ou `START TRANSACTION`), les requêtes, puis `COMMIT` pour valider ou `ROLLBACK` pour tout annuler. Exemple type : un virement débite un compte et en crédite un autre, jamais l'un sans l'autre. Un SGBDR garantit les propriétés **ACID** : atomicité (tout ou rien), cohérence (les contraintes restent vraies), isolation (les transactions simultanées ne se voient pas à moitié), durabilité (ce qui est validé survit à une panne). [[Complément hors du cours|ⓘ]]

### Gestion des droits

Les privilèges des utilisateurs sur les éléments de la base : [[Gestion des droits SQL|GRANT]] et `REVOKE` (on donne un droit `TO` un utilisateur, on le retire `FROM` lui ; sous MySQL, `dbname.*` désigne toute la base, alors qu'un nom seul désigne une table de la base courante), généralement réservés aux administrateurs. [[Erreurs du cours#^e-2-operateurs-et-sql|✎]]

```sql
GRANT ALL PRIVILEGES ON dbname.* TO user IDENTIFIED BY password ;
REVOKE UPDATE ON dbname.tablename FROM user ;
```
NB : la syntaxe peut **beaucoup** différer d'un SGBDR à l'autre.

Ces commandes forment la troisième famille de SQL, le **DCL** (*Data Control Language*) ; `COMMIT` et `ROLLBACK` sont parfois rangés à part, dans le **TCL** (*Transaction Control Language*). La forme `GRANT … IDENTIFIED BY` du cours, qui crée l'utilisateur au passage, est propre aux anciennes versions de MySQL ; aujourd'hui on crée d'abord l'utilisateur (`CREATE USER`) puis on lui donne ses droits. Bonne pratique : n'accorder à chaque utilisateur que les droits dont il a besoin (principe du moindre privilège), par exemple `GRANT SELECT ON base.etudiant TO lecteur ;`. [[Complément hors du cours|ⓘ]]

## 6. Architecture

- **Client – serveur : 2 *tiers*** (*tier* = niveau), en mode console ou en mode graphique.

![[Séance 3 - opérateurs et SQL - image21.png]]
*Figure : un client en mode console relié directement au SGBD.*

![[Séance 3 - opérateurs et SQL - image29.png]]
*Figure : un client en mode graphique relié directement au SGBD.*

- **Architecture Web 3 *tiers*** : navigateur web → serveur web → SGBD.
- Chaque niveau a son rôle : la **présentation** (l'interface, dans le navigateur), la **logique métier** (le programme du serveur web, en PHP, Python, Java…, qui construit les requêtes SQL) et les **données** (le SGBD). Le navigateur ne parle jamais directement à la base : seul le serveur web y a accès, ce qui protège la base. [[Complément hors du cours|ⓘ]]
- Danger propre à cette architecture : l'[[Injection SQL|injection SQL]]. Si le serveur colle tel quel dans sa requête ce que l'utilisateur a tapé, une saisie comme `' OR '1'='1` change le sens de la requête (connexion sans mot de passe, lecture ou suppression de données). La parade est la **requête préparée** (paramétrée), où les valeurs sont transmises à part et jamais interprétées comme du SQL. [[Complément hors du cours|ⓘ]]

![[Séance 3 - opérateurs et SQL - image30.png]]
*Figure : navigateur web, serveur web et base de données en trois niveaux.*

- Les architectures 2 ou 3 *tiers* peuvent être exécutées en local (sans réseau).
- Elles peuvent être considérées au niveau applicatif : 3 *tiers* est la solution classique du Web, mais 4 *tiers* et plus sont possibles avec un [[Architecture n-tiers|serveur d'application]].
- L'administration des SGBD peut se faire en 2 ou 3 *tiers*, mais jamais en 1 *tier*.
