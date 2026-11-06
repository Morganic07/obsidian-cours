---
type: source
tags: [year3]
sources: ["[[raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B]]"]
maj: 2026-11-06
---

Résumé du rapport PDF [[raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B]] (30 pages, 23 mai 2026, ID3-B), dans [[Ligue football (matière)]]. C'est le rapport demandé par [[sujet database (résumé)]]. La couverture porte les noms des auteurs : ils ne sont pas repris ici. Le MCD (page 9) et le schéma d'architecture (page 11) sont des images dont le texte n'est pas extrait ; ils n'ont pas été ouverts. Le fichier [[Cours/Year 3/ligue football/readme|readme]] décrit le reste du rendu, résumé dans [[readme (résumé)]].

## Sommaire du rapport

Description du projet, dictionnaire de données, MCD, MLD, schéma d'architecture contextualisé, code SQL (DDL, insertions, requêtes).

## Contexte

Base relationnelle pour gérer une ligue de football : acteurs (joueurs, arbitres), structures (équipes, saisons, journées), événements (matchs, reports) et finances (sponsors). Hypothèses du contexte :

- joueurs et arbitres héritent d'une entité `Personne` (nom, prénom, date de naissance, e-mail, photo, nationalité), avec un héritage exclusif total : voir [[Héritage en base de données]] ;
- un joueur est rattaché à une équipe, avec numéro de maillot, poste (gardien, défenseur, milieu, attaquant), pied fort, capitaine ou non ; un arbitre a un grade (régional, national, international, FIFA) et des années d'expérience ;
- une équipe a nom, ville, date de création, stade, entraîneur éventuel et logo ;
- saisons découpées en journées numérotées avec une date limite ;
- un match oppose deux équipes, avec un arbitre, une date, un lieu, un statut (planifié, en cours, terminé, reporté) et des scores renseignés après le match ;
- statistiques individuelles par joueur et par match (buts, passes décisives, cartons, minutes), association N-N ;
- sponsors : association ternaire entre équipe, sponsor et saison, avec un montant ;
- reports de match avec date initiale, nouvelle date, motif et date de décision.

## Modèle

11 tables : `PERSONNE`, `EQUIPE`, `JOUEUR`, `ARBITRE`, `SAISON`, `JOURNEE`, `MATCH`, `STATISTIQUE_JOUEUR_MATCH`, `SPONSOR`, `SPONSOR_EQUIPE_SAISON`, `REPORT_MATCH`. Le dictionnaire de données donne pour chaque attribut type, domaine, nullabilité, contrainte et exemple (types `ENUM`, `BOOL`, `BLOB`, `DECIMAL`, `YEAR`). Le MLD note les clés étrangères avec `#`. Clés composées : `STATISTIQUE_JOUEUR_MATCH` (match, joueur) et `SPONSOR_EQUIPE_SAISON` (sponsor, équipe, saison). Voir [[Clé primaire et clé étrangère]], [[Schéma relationnel]], [[Modèle entité-association]].

## Code SQL

- **DDL** (PostgreSQL) : `SERIAL` pour les clés, contraintes `CHECK` (numéro de maillot entre 0 et 99, minutes entre 0 et 120, scores positifs, équipes à domicile et à l'extérieur différentes, `annee_fin > annee_debut`, `nouvelle_date > date_initiale`), `UNIQUE` sur l'e-mail, le nom d'équipe et le nom de sponsor, `UNIQUE (id_saison, numero_journee)`. Les images sont stockées sous forme de chemins `VARCHAR(255)`.
- **Insertions** : 13 personnes (9 joueurs, 4 arbitres), 3 équipes, et des jeux de données pour les autres tables, avec un tableau puis le code `INSERT INTO`.
- **Neuf requêtes** (voir [[Langage SQL]]) : joueurs et leur équipe (jointures) ; classement des buteurs (`SUM`, `GROUP BY`) ; équipes classées par victoires (`CASE`, `LEFT JOIN`) ; moyenne de buts par match (`AVG`, `ROUND`) ; historique d'une saison (jointures multiples avec alias d'équipes) ; matchs reportés avec motif ; bilan offensif et disciplinaire par équipe ; capitaines de chaque équipe ; joueurs au-dessus de la moyenne de buts (`HAVING` et sous-requêtes imbriquées).

## Points à vérifier

1. **Dictionnaire et DDL ne coïncident pas** : le dictionnaire annonce des `ENUM`, `BLOB`, `YEAR` et une clé `AUTO_INCREMENT` (syntaxe MySQL), alors que le DDL PostgreSQL utilise `VARCHAR` avec `CHECK`, des chemins d'image et `SERIAL`. Le statut de saison est « Terminée » dans le dictionnaire et « Terminé » dans le DDL.
2. **Statut du match** : le contexte et le dictionnaire prévoient quatre statuts, dont « En cours » ; la contrainte `CHECK` du DDL n'en liste que trois (planifié, terminé, reporté).
3. **Erreurs de syntaxe du DDL** : guillemets doubles `" Gardien "` à la place d'apostrophes (en PostgreSQL, ils désignent des identifiants) avec des espaces intérieurs, virgules finales avant `)` dans `ARBITRE`, `SPONSOR` et `SPONSOR_EQUIPE_SAISON`, virgule manquante avant `CHECK` dans `MATCH`. Le DDL tel qu'imprimé ne s'exécute pas (complément : lecture du texte du rapport).
4. **Clé étrangère manquante** : dans le DDL de `JOUEUR`, `id_equipe` n'a pas de clé étrangère vers `EQUIPE`, alors que le MLD en note une (complément).
5. **Requête 9** : « plus de buts que la moyenne du championnat » compare le total d'un joueur à la moyenne des totaux des joueurs ayant au moins une ligne de statistiques.
6. **Numéro de journée** : le dictionnaire le déclare `UNIQUE` seul, ce qui interdit le même numéro dans deux saisons ; le DDL le rend unique par saison.
