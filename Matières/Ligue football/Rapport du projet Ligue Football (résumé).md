---
type: source
tags: [year3]
sources: [".raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf"]
maj: 2026-11-06
complet: true
---

Résumé du rapport PDF Ligue Football - Projet DATABASE ID3-B (`.raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf`) (30 pages, 23 mai 2026, ID3-B), dans [[Ligue football (matière)]]. C'est le rapport demandé par [[sujet database (résumé)]]. La couverture porte les noms des auteurs : ils ne sont pas repris ici. Le MCD (page 9) et le schéma d'architecture (page 11), images dans le PDF, sont repris ci-dessous en figure, ainsi que les captures des résultats des requêtes. Le fichier [[readme|readme]] décrit le reste du rendu, résumé dans [[readme (résumé)]].

## Sommaire du rapport

1. Description du projet (p. 2)
2. Dictionnaire de données (p. 4)
3. MCD (p. 9)
4. MLD (p. 10)
5. Schéma d'architecture contextualisé (p. 11)
6. Code SQL (p. 12) : DDL (p. 12), insertion DML (p. 17), requêtes DML (p. 25)

## 1. Description du projet

Objectif : concevoir et implémenter une base de données relationnelle pour gérer **toute une ligue de football**, sur l'ensemble du cycle de vie d'une compétition : les **acteurs** (joueurs, arbitres), les **structures** (équipes, saisons, journées), les **événements** (matchs, reports) et les **aspects financiers** (sponsors). Situations à prendre en compte :

- **A.** Les acteurs sont des **personnes** : nom, prénom, date de naissance, e-mail, photo, nationalité. Joueurs et arbitres **héritent** d'une entité commune `Personne`, avec un **héritage exclusif total** : une personne n'est que d'un seul type à la fois ([[Héritage en base de données]]).
- **B.** Un **joueur** est rattaché à une **unique** équipe, a un numéro de maillot, un poste (gardien, défenseur, milieu, attaquant), un pied fort (gauche, droit, les deux) et peut être capitaine.
- **C.** Un **arbitre** a un grade (régional, national, international, FIFA) et un nombre d'années d'expérience ; il peut arbitrer plusieurs matchs.
- **D.** Une **équipe** a un nom, une ville, une date de création, éventuellement un entraîneur et un logo, et un stade de référence. Elle est composée de plusieurs joueurs et joue des matchs à domicile ou à l'extérieur.
- **E.** La compétition est organisée en **saisons** (année de début, année de fin, statut en cours ou terminée), découpées en **journées** numérotées avec une date limite.
- **F.** Un **match** oppose deux équipes (domicile et extérieur), est arbitré par un arbitre, a une date, un lieu et un statut (planifié, en cours, terminé, reporté). Les scores ne sont renseignés qu'une fois le match joué.
- **G.** Pour chaque match, on enregistre les **statistiques individuelles** de chaque joueur : buts, passes décisives, cartons jaunes et rouges, minutes jouées. Un joueur joue plusieurs matchs et un match implique plusieurs joueurs : **association N-N**.
- **H.** Des **sponsors** (nom, secteur d'activité, logo) financent des équipes, chaque sponsor pouvant financer plusieurs équipes et inversement. Le sponsoring varie selon la saison, avec un montant : **association ternaire** Équipe–Sponsor–Saison, qui porte la propriété `montant` ([[Association ternaire]]).
- **I.** Un match peut être **reporté**. Chaque report garde l'historique : date initiale, nouvelle date (si déjà reprogrammé), motif, date de la décision.

Toute autre hypothèse est à préciser et justifier dans le rapport.

## 2. Dictionnaire de données

Voir [[Dictionnaire de données]] et [[Types de données SQL]]. Pour chaque attribut : nom, type, domaine, nullabilité, contrainte, exemple.

**1. Personne**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_personne | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 1 |
| nom | VARCHAR(50) | alphanumérique | NOT NULL | | Mbappé |
| prenom | VARCHAR(50) | alphanumérique | NOT NULL | | Kylian |
| date_naissance | DATE | date valide | NOT NULL | | 1998-12-20 |
| email | VARCHAR(100) | format e-mail | NOT NULL | UNIQUE | kylian@email.com |
| photo | BLOB | image | NULL | | mbappe.jpg |
| nationalite | VARCHAR(50) | alphanumérique | NOT NULL | | Française |

**2. Equipe**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_equipe | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 3 |
| nom | VARCHAR(100) | alphanumérique | NOT NULL | UNIQUE | PSG |
| ville | VARCHAR(100) | alphanumérique | NOT NULL | | Paris |
| date_creation | DATE | date valide | NOT NULL | | 1970-08-12 |
| logo | BLOB | image | NULL | | psg.png |
| stade | VARCHAR(100) | alphanumérique | NOT NULL | | Stade de France |
| entraineur | VARCHAR(100) | alphanumérique | NULL | | Pep Guardiola |

**3. Joueur**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_joueur | INT | entier ≥ 1 | NOT NULL | PK | 1 |
| poste | ENUM | Gardien, Défenseur, Milieu, Attaquant | NOT NULL | | Attaquant |
| numero_maillot | INT | entier ≥ 0 | NOT NULL | CHECK BETWEEN 0 AND 99 | 7 |
| pied_fort | ENUM | Gauche, Droit, Les deux | NOT NULL | | Droit |
| est_capitaine | BOOL | TRUE / FALSE | NOT NULL | DEFAULT FALSE | TRUE |

**4. Arbitre**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_arbitre | INT | entier ≥ 1 | NOT NULL | PK | 5 |
| grade | ENUM | Régional, National, International, FIFA | NOT NULL | | FIFA |
| annees_experience | INT | entier ≥ 0 | NOT NULL | CHECK ≥ 0 | 12 |

**5. Saison**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_saison | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 1 |
| annee_debut | YEAR | année valide | NOT NULL | | 2025 |
| annee_fin | YEAR | année valide | NOT NULL | CHECK > annee_debut | 2026 |
| statut | ENUM | En cours, Terminée | NOT NULL | DEFAULT 'En cours' | En cours |

**6. Journee**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_journee | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 4 |
| numero_journee | INT | entier ≥ 1 | NOT NULL | UNIQUE | 12 |
| date_limite | DATE | date valide | NOT NULL | | 2025-11-20 |

**7. Match**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_match | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 15 |
| date_match | DATETIME | date et heure valides | NOT NULL | | 2025-11-15 20:45:00 |
| lieu | VARCHAR(100) | alphanumérique | NOT NULL | | Parc des Princes |
| statut | ENUM | Planifié, En cours, Terminé, Reporté | NOT NULL | DEFAULT 'Planifié' | Terminé |
| score_dom | INT | entier ≥ 0 | NULL | CHECK >= 0 | 2 |
| score_ext | INT | entier ≥ 0 | NULL | CHECK >= 0 | 1 |

**8. Statistique_joueur_match**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_match | INT | entier ≥ 1 | NOT NULL | PK | 15 |
| id_joueur | INT | entier ≥ 1 | NOT NULL | PK | 1 |
| buts | INT | entier ≥ 0 | NOT NULL | DEFAULT 0 | 2 |
| passes_decisives | INT | entier ≥ 0 | NOT NULL | DEFAULT 0 | 1 |
| cartons_jaunes | INT | entier ≥ 0 | NOT NULL | DEFAULT 0 | 0 |
| cartons_rouges | INT | entier ≥ 0 | NOT NULL | DEFAULT 0 | 0 |
| minutes_jouees | INT | 0 à 120 | NOT NULL | CHECK BETWEEN 0 AND 120 | 90 |

**9. Sponsor**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_sponsor | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 2 |
| nom | VARCHAR(100) | alphanumérique | NOT NULL | UNIQUE | Nike |
| secteur_activite | VARCHAR(100) | alphanumérique | NOT NULL | | Sport |
| logo | BLOB | image | NOT NULL | | nike.png |

**10. Sponsor_equipe_saison**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_sponsor | INT | entier ≥ 1 | NOT NULL | PK | 2 |
| id_equipe | INT | entier ≥ 1 | NOT NULL | PK | 3 |
| id_saison | INT | entier ≥ 1 | NOT NULL | PK | 1 |
| montant | DECIMAL(12,2) | valeur ≥ 0 | NOT NULL | CHECK >= 0 | 15000000.00 |

**11. Report_match**

| Nom | Type | Domaine | Null | Contrainte | Exemple |
|---|---|---|---|---|---|
| id_report | INT | entier ≥ 1 | NOT NULL | PK, AUTO_INCREMENT | 8 |
| date_initiale | DATETIME | date valide | NOT NULL | | 2025-11-10 20:45:00 |
| nouvelle_date | DATETIME | date valide | NULL | CHECK > date_initiale | 2025-11-18 20:45:00 |
| date_decision | DATE | date valide | NOT NULL | CHECK < nouvelle_date | 2025-11-08 |
| motif | TEXT | alphanumérique | NOT NULL | | Intempéries |

## 3. MCD

Voir [[Modèle entité-association]] et [[Type d'association]].

![[Rapport Ligue Football - p10.jpg]]

*Figure : le MCD de la ligue, avec la spécialisation `is_a` de PERSONNE en JOUEUR et ARBITRE, les associations et leurs cardinalités, et la légende.*

Lecture du MCD :

- **PERSONNE** (0;1) — `is_a` — **ARBITRE** (1;1) et **JOUEUR** (1;1) : spécialisation (héritage).
- **EQUIPE** (1;N) — `CONTRAT` — (1;1) **JOUEUR** : un joueur a une seule équipe.
- **JOUEUR** (0;N) — **STATISTIQUE_JOUEUR_MATCH** (entité associative) — (1;N) **MATCH**.
- **EQUIPE** (0;N) — `EQUIPE_DOM` / `EQUIPE_EXT` — (1;1) **MATCH**.
- **ARBITRE** (0;N) — `EST_ARBITRE_PAR` — (1;1) **MATCH**.
- **SAISON** (0;N) — `CONTIENT` — (1;1) **JOURNEE** ; **JOURNEE** (0;N) — `CONTIENT` — (1;1) **MATCH**.
- **MATCH** (0;N) — `EST_REPORTE` — (1;1) **REPORT_MATCH**.
- **SPONSOR_EQUIPE_SAISON** (entité associative ternaire) : SPONSOR (1;N), EQUIPE (1;N), SAISON (1;N).

Légende : entité (nom en en-tête), association (verbe, rectangle arrondi), identifiant souligné (clé primaire), `id (FK)` clé étrangère, cercle `is_a` spécialisation (héritage), cardinalité `0,N` (min, max), entité associative (arrondie).

## 4. MLD

Voir [[Schéma relationnel]] et [[Clé primaire et clé étrangère]] ; le `#` marque une clé étrangère.

1. PERSONNE(**id_personne**, nom, prenom, date_naissance, email, photo, nationalite)
2. EQUIPE(**id_equipe**, nom, ville, date_creation, logo, stade, entraineur)
3. JOUEUR(**#id_joueur**, poste, pied_fort, numero_maillot, est_capitaine, #id_equipe)
4. ARBITRE(**#id_arbitre**, grade, annees_experience)
5. SAISON(**id_saison**, annee_debut, annee_fin, statut)
6. JOURNEE(**id_journee**, #id_saison, numero_journee, date_limite)
7. MATCH(**id_match**, date_match, lieu, statut, score_dom, score_ext, #id_arbitre, #id_equipe_dom, #id_equipe_ext, #id_journee)
8. STATISTIQUE_JOUEUR_MATCH(**#id_match, #id_joueur**, buts, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees)
9. SPONSOR(**id_sponsor**, nom, secteur_activite, logo)
10. SPONSOR_EQUIPE_SAISON(**#id_sponsor, #id_equipe, #id_saison**, montant)
11. REPORT_MATCH(**id_report**, #id_match, date_initiale, nouvelle_date, date_decision, motif)

L'héritage est traduit par des clés `id_joueur` et `id_arbitre` qui sont à la fois clé primaire et clé étrangère vers `PERSONNE`. Les associations N-N et ternaire deviennent des tables à clé composée.

## 5. Schéma d'architecture contextualisé

![[Rapport Ligue Football - p12.jpg]]

*Figure : architecture en trois couches — poste client (application Python en ligne de commande), couche de connexion (psycopg), serveur de base de données PostgreSQL hébergé chez Alwaysdata.*

- **Poste client** : l'utilisateur (administrateur de la ligue) fait de la saisie et de la consultation sur le terminal, via l'**application Python (CLI)** et ses 7 fonctions : classement des meilleurs buteurs (SELECT), liste des capitaines (SELECT), historique des matchs d'une saison (SELECT), changer le capitaine d'une équipe (UPDATE), ajouter un joueur (INSERT INTO), supprimer un joueur (DELETE), afficher tous les joueurs (SELECT).
- **Couche connexion** : requêtes SQL transmises par **psycopg**, port 5432, protocole TCP/IP ([[ODBC et JDBC]], [[Numéro de port]]).
- **Serveur de base de données** : accès au cloud, hébergeur Alwaysdata, SGBDR [[PostgreSQL]], base contenant les 11 tables ([[Modèle client-serveur]], [[Système de gestion de base de données]]).

## 6. Code SQL

### 6.2 DDL (création des tables)

Voir [[Langage SQL]], [[Contrainte d'intégrité]], [[Clé auto-incrémentée]]. Code tel qu'imprimé dans le rapport (espaces internes simplifiés), y compris ses erreurs de syntaxe (voir Points à vérifier).

```sql
CREATE TABLE PERSONNE (
    id_personne SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    photo VARCHAR(255) NULL,
    nationalite VARCHAR(50) NOT NULL
);

CREATE TABLE EQUIPE (
    id_equipe SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL UNIQUE,
    ville VARCHAR(100) NOT NULL,
    date_creation DATE NOT NULL,
    logo VARCHAR(255) NULL,
    stade VARCHAR(100) NOT NULL,
    entraineur VARCHAR(100) NULL
);

CREATE TABLE JOUEUR (
    id_joueur INT PRIMARY KEY,
    poste VARCHAR(20) NOT NULL CHECK (poste IN (" Gardien ", " Défenseur ", " Milieu ", " Attaquant ")),
    numero_maillot INT NOT NULL CHECK (numero_maillot BETWEEN 0 AND 99),
    pied_fort VARCHAR(20) NOT NULL CHECK (pied_fort IN ("' Gauche ", " Droit ", " Les deux ")),
    id_equipe INT NOT NULL,
    est_capitaine BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_joueur_personne FOREIGN KEY (id_joueur) REFERENCES PERSONNE (id_personne)
);

CREATE TABLE ARBITRE (
    id_arbitre INT PRIMARY KEY,
    grade VARCHAR(20) NOT NULL CHECK (grade IN (" Régional ", " National ", " International ", " FIFA ")),
    annees_experience INT NOT NULL DEFAULT 0 CHECK (annees_experience >= 0),
    CONSTRAINT fk__arbitre_personne FOREIGN KEY (id_arbitre) REFERENCES PERSONNE (id_personne),
);

CREATE TABLE SAISON (
    id_saison SERIAL PRIMARY KEY,
    annee_debut INT NOT NULL CHECK (annee_debut >= 1863),
    annee_fin INT NOT NULL,
    statut VARCHAR(20) NOT NULL DEFAULT " En cours " CHECK (statut IN (" En cours ", " Terminé ")),
    CONSTRAINT check_date CHECK (annee_fin > annee_debut));

CREATE TABLE JOURNEE (
    id_journee SERIAL PRIMARY KEY,
    id_saison INT NOT NULL,
    numero_journee INT NOT NULL,
    date_limite DATE NOT NULL,
    CONSTRAINT fk_journee_saison FOREIGN KEY (id_saison) REFERENCES SAISON (id_saison),
    CONSTRAINT unique_journee_saison UNIQUE (id_saison, numero_journee)
);

CREATE TABLE MATCH (
    id_match SERIAL PRIMARY KEY,
    id_journee INT NOT NULL,
    id_arbitre INT NOT NULL,
    id_equipe_dom INT NOT NULL,
    id_equipe_ext INT NOT NULL,
    date_match TIMESTAMP NOT NULL,
    lieu VARCHAR(100) NOT NULL,
    statut VARCHAR(20) NOT NULL DEFAULT " Planifié " CHECK (statut IN (" Planifié ", " Terminé ", " Reporté ")),
    score_dom INT CHECK (score_dom >= 0),
    score_ext INT CHECK (score_ext >= 0),
    CONSTRAINT fk_match_journee FOREIGN KEY (id_journee) REFERENCES JOURNEE (id_journee),
    CONSTRAINT fk_match_arbitre FOREIGN KEY (id_arbitre) REFERENCES ARBITRE (id_arbitre),
    CONSTRAINT fk_match_equipe_dom FOREIGN KEY (id_equipe_dom) REFERENCES EQUIPE (id_equipe),
    CONSTRAINT fk_match_equipe_ext FOREIGN KEY (id_equipe_ext) REFERENCES EQUIPE (id_equipe)
    CONSTRAINT check_equipes_diff CHECK (id_equipe_dom != id_equipe_ext)
);

CREATE TABLE STATISTIQUE_JOUEUR_MATCH (
    id_match INT NOT NULL,
    id_joueur INT NOT NULL,
    buts INT NOT NULL DEFAULT 0 CHECK (buts >= 0),
    passes_decisives INT NOT NULL DEFAULT 0 CHECK (passes_decisives >= 0),
    cartons_jaunes INT NOT NULL DEFAULT 0 CHECK (cartons_jaunes >= 0),
    cartons_rouges INT NOT NULL DEFAULT 0 CHECK (cartons_rouges >= 0),
    minutes_jouees INT NOT NULL CHECK (minutes_jouees BETWEEN 0 AND 120),
    PRIMARY KEY (id_match, id_joueur),
    CONSTRAINT fk_stat_match FOREIGN KEY (id_match) REFERENCES MATCH (id_match),
    CONSTRAINT fk_stat_joueur FOREIGN KEY (id_joueur) REFERENCES JOUEUR (id_joueur)
);

CREATE TABLE SPONSOR (
    id_sponsor SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL UNIQUE,
    secteur_activite VARCHAR(50) NOT NULL,
    logo VARCHAR(255) NOT NULL,
);

CREATE TABLE SPONSOR_EQUIPE_SAISON (
    id_sponsor INT NOT NULL,
    id_equipe INT NOT NULL,
    id_saison INT NOT NULL,
    montant DECIMAL(15, 2) NOT NULL CHECK (montant >= 0),
    PRIMARY KEY (id_sponsor, id_equipe, id_saison),
    CONSTRAINT fk_sponsor_equipe_saison_sponsor FOREIGN KEY (id_sponsor) REFERENCES SPONSOR (id_sponsor),
    CONSTRAINT fk_sponsor_equipe_saison_equipe FOREIGN KEY (id_equipe) REFERENCES EQUIPE (id_equipe),
    CONSTRAINT fk_sponsor_equipe_saison_saison FOREIGN KEY (id_saison) REFERENCES SAISON (id_saison),
);

CREATE TABLE REPORT_MATCH (
    id_report SERIAL PRIMARY KEY,
    id_match INT NOT NULL,
    date_initiale TIMESTAMP NOT NULL,
    nouvelle_date TIMESTAMP CHECK (nouvelle_date > date_initiale),
    date_decision DATE NOT NULL CHECK (date_decision < nouvelle_date),
    motif TEXT NOT NULL,
    CONSTRAINT fk_report_match FOREIGN KEY (id_match) REFERENCES MATCH (id_match),
);
```

Choix notables : `SERIAL` pour les clés générées ; `id_joueur` et `id_arbitre` en `INT` non générés, car ils reprennent `id_personne` (héritage) ; images stockées sous forme de **chemins** `VARCHAR(255)` et non de `BLOB` ; `annee_debut >= 1863` ; clé composée dans les tables d'association ; `UNIQUE (id_saison, numero_journee)` ; `CHECK (id_equipe_dom != id_equipe_ext)`.

### 6.3 Insertion DML (jeu de données)

Le rapport donne pour chaque table un tableau puis le `INSERT INTO` correspondant. Les personnes du jeu de données sont des joueurs et arbitres réels de Ligue 1, avec des e-mails fictifs.

**Personne** (13 lignes : id 1 à 9 joueurs, 10 à 13 arbitres)

```sql
INSERT INTO PERSONNE (nom, prenom, date_naissance, email, photo, nationalite) VALUES
('Mbappé', 'Kylian', '1998-12-20', 'k.mbappe@email.com', 'mbappe.jpg', 'Française'),
('Marquinhos', 'Marcos', '1994-05-14', 'm.marqui@email.com', 'marqui.jpg', 'Brésilienne'),
('Barcola', 'Bradley', '2002-09-02', 'b.barcola@email.com', 'barcola.jpg', 'Française'),
('Balerdi', 'Leonardo', '1999-01-26', 'l.balerdi@email.com', 'balerdi.jpg', 'Argentine'),
('Højbjerg', 'Pierre', '1995-08-05', 'p.hojbjerg@email.com', 'hojbjerg.jpg', 'Danoise'),
('Wahi', 'Elye', '2003-01-02', 'e.wahi@email.com', 'wahi.jpg', 'Française'),
('Lacazette', 'Alexandre', '1991-05-28', 'a.laca@email.com', 'laca.jpg', 'Française'),
('Cherki', 'Rayan', '2003-08-17', 'r.cherki@email.com', 'cherki.jpg', 'Française'),
('Tolisso', 'Corentin', '1994-08-03', 'c.tolisso@email.com', 'tolisso.jpg', 'Française'),
('Turpin', 'Clément', '1982-05-16', 'c.turpin@email.com', 'turpin.jpg', 'Française'),
('Frappart', 'Stéphanie', '1983-12-14', 's.frappart@email.com', 'frappart.jpg', 'Française'),
('Brisard', 'Jérôme', '1986-03-24', 'j.brisard@email.com', 'brisard.jpg', 'Française'),
('Batta', 'Florent', '1980-06-12', 'f.batta@email.com', 'batta.jpg', 'Française');
```

**Equipe**

| id | nom | ville | création | logo | stade | entraîneur |
|---|---|---|---|---|---|---|
| 1 | Paris Saint-Germain | Paris | 1970-08-12 | psg.png | Parc des Princes | Luis Enrique |
| 2 | Olympique de Marseille | Marseille | 1899-08-31 | om.png | Orange Vélodrome | Roberto De Zerbi |
| 3 | Olympique Lyonnais | Lyon | 1950-08-03 | ol.png | Groupama Stadium | Pierre Sage |

```sql
INSERT INTO EQUIPE (nom, ville, date_creation, logo, stade, entraineur) VALUES
('Paris Saint-Germain', 'Paris', '1970-08-12', 'psg.png', 'Parc des Princes', 'Luis Enrique'),
('Olympique de Marseille', 'Marseille', '1899-08-31', 'om.png', 'Orange Vélodrome', 'Roberto De Zerbi'),
('Olympique Lyonnais', 'Lyon', '1950-08-03', 'ol.png', 'Groupama Stadium', 'Pierre Sage');
```

**Joueur**

```sql
INSERT INTO JOUEUR (id_joueur, poste, numero_maillot, pied_fort, id_equipe, est_capitaine) VALUES
(1, 'Attaquant', 7, 'Droit', 1, FALSE),
(2, 'Défenseur', 5, 'Droit', 1, TRUE),
(3, 'Attaquant', 29, 'Gauche', 1, FALSE),
(4, 'Défenseur', 5, 'Droit', 2, TRUE),
(5, 'Milieu', 23, 'Droit', 2, FALSE),
(6, 'Attaquant', 9, 'Droit', 2, FALSE),
(7, 'Attaquant', 10, 'Droit', 3, TRUE),
(8, 'Milieu', 18, 'Gauche', 3, FALSE),
(9, 'Milieu', 24, 'Droit', 3, FALSE);
```

Joueurs 1 à 3 au PSG, 4 à 6 à l'OM, 7 à 9 à l'OL ; un capitaine par équipe (2, 4, 7).

**Arbitre**

```sql
INSERT INTO ARBITRE (id_arbitre, grade, annees_experience) VALUES
(10, 'FIFA', 12), (11, 'International', 8), (12, 'National', 5), (13, 'Régional', 3);
```

**Saison** et **Journée**

```sql
INSERT INTO SAISON (annee_debut, annee_fin, statut) VALUES
(2024, 2025, 'Terminé'),
(2025, 2026, 'En cours');

INSERT INTO JOURNEE (id_saison, numero_journee, date_limite) VALUES
(1, 1, '2024-09-15'), (1, 2, '2024-09-22'), (2, 1, '2025-09-15'), (2, 2, '2025-09-22');
```

**Match**

| id | journée | arbitre | domicile | extérieur | date | lieu | statut | score |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 (S1-J1) | 10 | PSG | OM | 2024-09-14 | Parc des Princes | Terminé | 3-1 |
| 2 | 2 (S1-J2) | 11 | OL | PSG | 2024-09-21 | Groupama Stadium | Terminé | 0-2 |
| 3 | 3 (S2-J1) | 12 | OM | OL | 2025-09-14 | Orange Vélodrome | Terminé | 2-1 |
| 4 | 4 (S2-J2) | 13 | PSG | OM | 2025-09-21 | Parc des Princes | Reporté | 0-0 |

```sql
INSERT INTO MATCH (id_journee, id_arbitre, id_equipe_dom, id_equipe_ext, date_match, lieu, statut, score_dom, score_ext) VALUES
(1, 10, 1, 2, '2024-09-14 21:00:00', 'Parc des Princes', 'Terminé', 3, 1),
(2, 11, 3, 1, '2024-09-21 21:00:00', 'Groupama Stadium', 'Terminé', 0, 2),
(3, 12, 2, 3, '2025-09-14 21:00:00', 'Orange Vélodrome', 'Terminé', 2, 1),
(4, 13, 1, 2, '2025-09-21 21:00:00', 'Parc des Princes', 'Reporté', 0, 0);
```

**Statistique_joueur_match**

| match | joueur | buts | passes | jaunes | rouges | minutes |
|---|---|---|---|---|---|---|
| 1 | 1 (Mbappé) | 2 | 0 | 0 | 0 | 90 |
| 1 | 3 (Barcola) | 1 | 1 | 0 | 0 | 75 |
| 1 | 6 (Wahi) | 1 | 0 | 1 | 0 | 90 |
| 2 | 1 (Mbappé) | 1 | 1 | 0 | 0 | 90 |
| 2 | 2 (Marquinhos) | 1 | 0 | 0 | 0 | 90 |
| 3 | 5 (Højbjerg) | 1 | 0 | 0 | 0 | 90 |
| 3 | 8 (Cherki) | 0 | 1 | 0 | 0 | 60 |
| 3 | 7 (Lacazette) | 1 | 0 | 0 | 0 | 90 |

```sql
INSERT INTO STATISTIQUE_JOUEUR_MATCH (id_match, id_joueur, buts, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees) VALUES
(1, 1, 2, 0, 0, 0, 90), (1, 3, 1, 1, 0, 0, 75), (1, 6, 1, 0, 1, 0, 90), (2, 1, 1, 1, 0, 0, 90),
(2, 2, 1, 0, 0, 0, 90), (3, 5, 1, 0, 0, 0, 90), (3, 8, 0, 1, 0, 0, 60), (3, 7, 1, 0, 0, 0, 90);
```

**Sponsor** et **Sponsor_equipe_saison**

```sql
INSERT INTO SPONSOR (nom, secteur_activite, logo) VALUES
('Nike', 'Sportswear', 'nike.png'),
('Emirates', 'Compagnie Aérienne', 'emirates.png'),
('Adidas', 'Sportswear', 'adidas.png');

INSERT INTO SPONSOR_EQUIPE_SAISON (id_sponsor, id_equipe, id_saison, montant) VALUES
(1, 1, 1, 10000000.00), (2, 2, 1, 8000000.00), (3, 3, 1, 6000000.00),
(1, 2, 2, 9500000.00), (2, 3, 2, 7000000.00), (3, 1, 2, 11000000.00);
```

Saison 1 : Nike → PSG, Emirates → OM, Adidas → OL ; saison 2 : Nike → OM, Emirates → OL, Adidas → PSG.

**Report_match**

```sql
INSERT INTO REPORT_MATCH (id_match, date_initiale, nouvelle_date, date_decision, motif) VALUES
(4, '2025-09-21 21:00:00', '2025-10-05 17:00:00', '2025-09-19', 'Fortes intempéries');
```

### 6.4 Requêtes DML

Neuf requêtes ([[Langage SQL]], [[Algèbre relationnelle]]), chacune suivie de la capture de son résultat dans le rapport.

**1. Liste des joueurs et de leur équipe** (jointures)

```sql
SELECT PERSONNE.nom, PERSONNE.prenom, EQUIPE.nom AS nom_equipe
FROM JOUEUR
JOIN PERSONNE ON JOUEUR.id_joueur = PERSONNE.id_personne
JOIN EQUIPE ON JOUEUR.id_equipe = EQUIPE.id_equipe;
```

![[Rapport Ligue Football - requete 1.png]]

*Figure : résultat — les 9 joueurs avec leur équipe (9 lignes).*

**2. Classement des meilleurs buteurs** (somme des buts sur toutes les saisons ; [[Fonction d'agrégation]], `GROUP BY`)

```sql
SELECT PERSONNE.nom, PERSONNE.prenom, SUM(STATISTIQUE_JOUEUR_MATCH.buts) AS total_buts
FROM STATISTIQUE_JOUEUR_MATCH
JOIN PERSONNE ON STATISTIQUE_JOUEUR_MATCH.id_joueur = PERSONNE.id_personne
GROUP BY PERSONNE.id_personne, PERSONNE.nom, PERSONNE.prenom
ORDER BY total_buts DESC;
```

![[Rapport Ligue Football - requete 2.png]]

*Figure : résultat — Mbappé 3 buts, cinq joueurs à 1, Cherki 0 (7 lignes).*

**3. Classement des équipes par matchs gagnés** (sur toutes les saisons ; [[Expression CASE]], [[Jointure externe]])

```sql
SELECT EQUIPE.nom,
  SUM(CASE
        WHEN MATCH.id_equipe_dom = EQUIPE.id_equipe AND MATCH.score_dom > MATCH.score_ext THEN 1
        WHEN MATCH.id_equipe_ext = EQUIPE.id_equipe AND MATCH.score_ext > MATCH.score_dom THEN 1
        ELSE 0
      END) AS total_matchs_gagnes
FROM EQUIPE
LEFT JOIN MATCH ON EQUIPE.id_equipe = MATCH.id_equipe_dom OR EQUIPE.id_equipe = MATCH.id_equipe_ext
GROUP BY EQUIPE.nom
ORDER BY total_matchs_gagnes DESC;
```

![[Rapport Ligue Football - requete 3.png]]

*Figure : résultat — PSG 2, OM 1, OL 0 (3 lignes).*

**4. Moyenne des buts par match de chaque joueur** (sur toutes les saisons ; `AVG`, `ROUND`)

```sql
SELECT PERSONNE.nom, PERSONNE.prenom,
       ROUND(AVG(STATISTIQUE_JOUEUR_MATCH.buts), 1) AS moyenne_buts_par_match
FROM STATISTIQUE_JOUEUR_MATCH
JOIN PERSONNE ON STATISTIQUE_JOUEUR_MATCH.id_joueur = PERSONNE.id_personne
GROUP BY PERSONNE.nom, PERSONNE.prenom
ORDER BY moyenne_buts_par_match DESC;
```

![[Rapport Ligue Football - requete 4.png]]

*Figure : résultat — Mbappé 1,5, les autres buteurs 1,0, Cherki 0,0 (7 lignes).*

**5. Historique des matchs d'une saison** (jointures multiples avec alias de la table EQUIPE)

```sql
SELECT JOURNEE.numero_journee,
       EQUIPE_DOMICILE.nom AS equipe_domicile,
       EQUIPE_EXTERIEURE.nom AS equipe_exterieure,
       MATCH.score_dom,
       MATCH.score_ext
FROM MATCH
JOIN JOURNEE ON MATCH.id_journee = JOURNEE.id_journee
JOIN EQUIPE AS EQUIPE_DOMICILE ON MATCH.id_equipe_dom = EQUIPE_DOMICILE.id_equipe
JOIN EQUIPE AS EQUIPE_EXTERIEURE ON MATCH.id_equipe_ext = EQUIPE_EXTERIEURE.id_equipe
WHERE JOURNEE.id_saison = 1
ORDER BY JOURNEE.numero_journee, MATCH.date_match;
```

![[Rapport Ligue Football - requete 5.png]]

*Figure : résultat — journée 1 PSG 3-1 OM, journée 2 OL 0-2 PSG (2 lignes).*

**6. Matchs reportés avec le motif**

```sql
SELECT REPORT_MATCH.id_match,
       EQUIPE_DOMICILE.nom AS equipe_domicile,
       EQUIPE_EXTERIEURE.nom AS equipe_exterieure,
       REPORT_MATCH.date_initiale,
       REPORT_MATCH.nouvelle_date,
       REPORT_MATCH.motif
FROM REPORT_MATCH
JOIN MATCH ON REPORT_MATCH.id_match = MATCH.id_match
JOIN EQUIPE AS EQUIPE_DOMICILE ON MATCH.id_equipe_dom = EQUIPE_DOMICILE.id_equipe
JOIN EQUIPE AS EQUIPE_EXTERIEURE ON MATCH.id_equipe_ext = EQUIPE_EXTERIEURE.id_equipe;
```

![[Rapport Ligue Football - requete 6.png]]

*Figure : résultat — match 4, PSG contre OM, reporté du 21/09/2025 au 05/10/2025 pour fortes intempéries (1 ligne).*

**7. Bilan offensif et disciplinaire par équipe** (sur toutes les saisons)

```sql
SELECT EQUIPE.nom,
       SUM(STATISTIQUE_JOUEUR_MATCH.buts) AS total_buts_marques,
       SUM(STATISTIQUE_JOUEUR_MATCH.passes_decisives) AS total_passes_decisives,
       SUM(STATISTIQUE_JOUEUR_MATCH.cartons_jaunes) AS total_cartons_jaunes,
       SUM(STATISTIQUE_JOUEUR_MATCH.cartons_rouges) AS total_cartons_rouges
FROM EQUIPE
JOIN JOUEUR ON EQUIPE.id_equipe = JOUEUR.id_equipe
JOIN STATISTIQUE_JOUEUR_MATCH ON JOUEUR.id_joueur = STATISTIQUE_JOUEUR_MATCH.id_joueur
GROUP BY EQUIPE.nom
ORDER BY total_buts_marques DESC;
```

![[Rapport Ligue Football - requete 7.png]]

*Figure : résultat — PSG 5 buts, OM 2, OL 1, avec passes et cartons (3 lignes).*

**8. Capitaines de chaque équipe**

```sql
SELECT EQUIPE.nom AS nom_equipe, PERSONNE.nom, PERSONNE.prenom, JOUEUR.poste
FROM JOUEUR
JOIN PERSONNE ON JOUEUR.id_joueur = PERSONNE.id_personne
JOIN EQUIPE ON JOUEUR.id_equipe = EQUIPE.id_equipe
WHERE JOUEUR.est_capitaine = TRUE;
```

![[Rapport Ligue Football - requete 8.png]]

*Figure : résultat — PSG Marquinhos (défenseur), OM Balerdi (défenseur), OL Lacazette (attaquant) (3 lignes).*

**9. Joueurs ayant marqué plus que la moyenne des buts du championnat** (`HAVING`, [[Sous-requête|sous-requêtes]] imbriquées)

```sql
SELECT PERSONNE.nom, PERSONNE.prenom, SUM(STATISTIQUE_JOUEUR_MATCH.buts) AS total_buts
FROM STATISTIQUE_JOUEUR_MATCH
JOIN PERSONNE ON STATISTIQUE_JOUEUR_MATCH.id_joueur = PERSONNE.id_personne
GROUP BY PERSONNE.id_personne, PERSONNE.nom, PERSONNE.prenom
HAVING SUM(STATISTIQUE_JOUEUR_MATCH.buts) > (
    SELECT AVG(total_saison)
    FROM (
        SELECT SUM(buts) AS total_saison
        FROM STATISTIQUE_JOUEUR_MATCH
        GROUP BY id_joueur
    ) AS sous_calcul
)
ORDER BY total_buts DESC;
```

![[Rapport Ligue Football - requete 9.png]]

*Figure : résultat — Mbappé, 3 buts (1 ligne).*

## Points à vérifier

1. **Dictionnaire et DDL ne coïncident pas** : le dictionnaire annonce des `ENUM`, `BLOB`, `YEAR` et une clé `AUTO_INCREMENT` (syntaxe MySQL), alors que le DDL PostgreSQL utilise `VARCHAR` avec `CHECK`, des chemins d'image et `SERIAL`. Le statut de saison est « Terminée » dans le dictionnaire et « Terminé » dans le DDL.
2. **Statut du match** : le contexte et le dictionnaire prévoient quatre statuts, dont « En cours » ; la contrainte `CHECK` du DDL n'en liste que trois (planifié, terminé, reporté).
3. **Erreurs de syntaxe du DDL** : guillemets doubles `" Gardien "` à la place d'apostrophes (en PostgreSQL, ils désignent des identifiants) avec des espaces intérieurs, virgules finales avant `)` dans `ARBITRE`, `SPONSOR` et `SPONSOR_EQUIPE_SAISON`, virgule manquante avant `CHECK` dans `MATCH`. Le DDL tel qu'imprimé ne s'exécute pas (complément : lecture du texte du rapport).
4. **Clé étrangère manquante** : dans le DDL de `JOUEUR`, `id_equipe` n'a pas de clé étrangère vers `EQUIPE`, alors que le MLD en note une (complément).
5. **Requête 9** : « plus de buts que la moyenne du championnat » compare le total d'un joueur à la moyenne des totaux des joueurs ayant au moins une ligne de statistiques.
6. **Numéro de journée** : le dictionnaire le déclare `UNIQUE` seul, ce qui interdit le même numéro dans deux saisons ; le DDL le rend unique par saison.
7. **Score du match 3 et statistiques** : le match OM–OL est noté 2-1, mais les statistiques n'attribuent qu'un but à un joueur de l'OM (Højbjerg). Le total de buts de l'OM dans la requête 7 (2, dont celui de Wahi au match 1) ne correspond donc pas aux scores (complément : recoupement des tables du rapport).
8. **Match reporté noté 0-0** : le contexte dit que les scores ne sont renseignés qu'une fois le match joué, mais le match 4, reporté, a `score_dom = 0` et `score_ext = 0` au lieu de `NULL`.
9. **`id_report = 2`** dans le tableau du jeu de données, alors que l'`INSERT` laisse `SERIAL` attribuer l'identifiant (qui vaudrait 1 sur une base neuve).
10. **MLD** : « id equipe » est écrit sans tiret bas dans la ligne EQUIPE ; dans le DDL, plusieurs références s'écrivent « id _equipe », « id _match » avec une espace (artefact probable de mise en page, à vérifier dans `base.sql`).
11. **Exemples du dictionnaire** : l'exemple d'équipe (« PSG », « Stade de France », « Pep Guardiola ») ne correspond pas au jeu de données (Parc des Princes, Luis Enrique) : simple illustration.
