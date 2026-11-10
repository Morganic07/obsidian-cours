---
type: concept
tags: [year4]
aliases: [HyperText Transfer Protocol, HTTPS, requête HTTP]
sources: ["[[Raw/Year 4/histoire du design et interactions /chp2 cours.pdf|chp2 cours.pdf]]"]
maj: 2026-11-10
---

**Définition** (d'après [[2 - Histoire du design]]) : *HyperText Transfer Protocol*, protocole qui organise les requêtes entre un utilisateur (son [[Navigateur web|navigateur]]) et un serveur, selon le [[Modèle client-serveur|modèle client-serveur]], principe fondamental du Web. Exemples de méthodes : `GET` (récupérer des données), `POST` (envoyer des données), `DELETE` (supprimer des données). Chaîne : utilisateur → navigateur → requête HTTP → Internet → serveur → réponse → navigateur → page affichée.

Complément (hors du cours) : HTTP est un protocole de la couche application, transporté par TCP ([[Suite des protocoles Internet]]), sur le port 80 (443 pour HTTPS, la version chiffrée par TLS). Une requête indique une méthode et une ressource (`GET /index.html`) ; la réponse commence par un code d'état : `200` (succès), `301` (redirection), `404` (introuvable), `500` (erreur du serveur). La première version (1991) ne connaît que `GET` ; HTTP/1.0 (1996) et HTTP/1.1 (1997) ajoutent `POST`, `PUT`, `DELETE` et les en-têtes ; HTTP/2 (2015) et HTTP/3 (2022) accélèrent les échanges. HTTP est **sans état** : chaque requête est indépendante, d'où l'usage des cookies pour garder une session. [[Complément hors du cours|ⓘ]]

## Dans le cours

[[2 - Histoire du design]] : fiche de lecture, section 10.

Voir aussi : [[URL]], [[HTML]], [[World Wide Web]], [[Modèle client-serveur]], [[Numéro de port]].

[[1 - Histoire du design]] : sommaire (1984-1993 : … → HTTP/HTML/URL → Web) et résumé du support du chapitre 2.

Résumés : [[2 - Histoire du design]] · [[1 - Histoire du design]]
