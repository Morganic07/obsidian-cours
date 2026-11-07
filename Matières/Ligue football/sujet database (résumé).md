---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF sujet database ([[Raw/Year 3/ligue football/for me/sujet database.pdf|sujet database.pdf]]) (2 pages, version 1.1 du 13 mai 2026), sujet de la SAÉ « Relational Database », ID3 semestre 2, 2025-2026, dans [[Ligue football (matière)]]. Le projet réalisé est résumé dans [[Rapport du projet Ligue Football (résumé)]].

## Préambule

Projet de type **SAÉ** (« Situation d'Apprentissage et d'Évaluation ») de l'UE « Relational Database », à réaliser au choix seul, en binôme ou en trinôme. Note de bas de page du sujet : la pédagogie par projet était déjà omniprésente dans la formation, mais le formalisme SAÉ lui donne un cadre pluridisciplinaire, en limitant le nombre de projets par semestre.

Le projet comprend :

- un serveur de bases de données utilisant le SGBDR [[PostgreSQL]] ([[Système de gestion de base de données]]) ;
- une application en Java, Python ou C, connectée au serveur par **ODBC ou JDBC** selon les cas ([[ODBC et JDBC]]).

Le contexte est libre, mais il doit respecter tous les attendus.

## Attendus

- SGBDR Postgres.
- Types de données variés : valeurs numériques, chaînes de caractères, booléen, BLOB, énumération… ([[Types de données SQL]]).
- Volumétrie indicative : **40 à 50 attributs**.
- Au minimum **10 tables**, au maximum **15**.
- Associations **1-N** (*one to many* / *many to one*) et **N-N** (*many to many*), ainsi que l'**héritage** ([[Type d'association]], [[Héritage en base de données]]).
- **8 à 10 requêtes `SELECT`** représentatives, dont des requêtes imbriquées ([[Sous-requête]]), une ou plusieurs requêtes d'agrégats ([[Fonction d'agrégation]]) et une requête avec `GROUP BY`.
- L'application doit montrer au moins **2 situations** : 1) une **modification** du contenu de la base (`INSERT`, `DELETE` ou `UPDATE`) ; 2) une **extraction** de données (`SELECT`) techniquement représentative.

## Livrables

- **Un rapport de projet de niveau professionnel**, permettant une éventuelle continuité ou maintenance du projet, aux formats odt et pdf, contenant :
  - la description détaillée du contexte ;
  - les principaux choix techniques (surtout s'ils diffèrent des recommandations initiales) ;
  - le [[Dictionnaire de données|dictionnaire de données]] ;
  - le schéma MCD (schéma E/A, [[Modèle entité-association]]) ;
  - le schéma MLD (schéma relationnel, [[Schéma relationnel]]) ;
  - un extrait représentatif du jeu de données ;
  - le texte (en français) des 8 à 10 requêtes DML, suivi du code SQL de chacune et de la capture d'écran du résultat.
- Le script SQL de création de la base (DDL + tous les `INSERT` du jeu de données initial).
- Le script SQL des requêtes `SELECT` (DML), en un unique fichier.
- Les codes de l'application.
- Un fichier `readme.md` « pour s'y retrouver dans l'ensemble des codes » ([[Fichier README]]).
- Une vidéo de démonstration de **3 minutes maximum** du projet avec ses tests.

## Calendrier indicatif (dates prévisionnelles)

| Étape | Contenu |
|---|---|
| Étape 1 | composition définitive de l'équipe ; description du contexte (½ page à 1 page) ; modélisation complète (dictionnaire de données, MCD, MLD) ; planning prévisionnel en [[Diagramme de Gantt]] ; schéma d'architecture contextualisé |
| Étape 2 | partie DDL (code SQL en annexe du rapport) ; jeu de données de test présenté en tableau + code `INSERT INTO` en annexe |
| Étape 3 | partie DML ; connexions à la base depuis l'application |
| Finalisation | tests d'intégration ; livrables au plus tard le **dimanche 7 juin 2026 à 23 h 59** (date provisoire) : rapport définitif, codes, vidéo |
| Présentation | **vendredi 12 juin 2026** (date provisoire) : soutenance de 5 min maximum avec 5 à 6 diapositives, suivie d'environ 5 min de questions |

## Notions mobilisées

[[Modèle entité-association]], [[Schéma relationnel]], [[Clé primaire et clé étrangère]], [[Langage SQL]], [[Algèbre relationnelle]] (complément : fondement des requêtes).
