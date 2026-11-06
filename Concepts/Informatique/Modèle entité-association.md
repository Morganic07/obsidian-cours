---
type: concept
tags: [year3]
aliases: [MCD, schéma E/A, schéma entité-association, diagramme entité-association, ER diagram, modèle conceptuel de données, MERISE, cardinalités, entité faible, association réflexive]
matieres: [Data base, ligue football]
sources: ["[[Cours 1 et 2 - Database]]"]
maj: 2026-11-06
---

Le MCD (modèle conceptuel de données, ou schéma E/A) est la deuxième étape de la méthode MERISE, après le [[Dictionnaire de données|dictionnaire de données]] et avant le [[Schéma relationnel]]. Il montre :
- les **entités** (ETUDIANT, FORMATION) et leurs attributs avec leurs types ;
- les **clés primaires** (soulignées) ;
- les **associations** entre entités (EST_INSCRIT ; voir [[Type d'association]]) ;
- les **cardinalités**.

**Cardinalités** : `1,1` signifie au minimum 1 et au maximum 1 (un étudiant a une seule formation) ; `0,N` signifie de 0 à N (une formation a de 0 à N étudiants).

**Cas particuliers vus en cours**
- **Héritage** : liaison « is-a » ([[UML]]) (`Client` spécialisé en `PersonnePhysique` et `PersonneMorale`).
- **Association réflexive** : une entité liée à elle-même (un étudiant tuteur d'un autre : 0,1 d'un côté, 0,N de l'autre).
- **Entité faible** : identifiée seulement avec l'identifiant d'une entité forte (enfants mineurs du personnel, 1,1 côté enfant).

Le projet de la ligue de football applique l'[[Héritage en base de données]] et une [[Association ternaire|association ternaire]] ([[Rapport du projet Ligue Football (résumé)]], [[sujet database (résumé)]]).

Liens : [[Schéma relationnel]], [[Clé primaire et clé étrangère]], [[Héritage en base de données]]

Résumés : [[Cours 1 et 2 - Database (résumé)]], [[Rapport du projet Ligue Football (résumé)]], [[sujet database (résumé)]]
