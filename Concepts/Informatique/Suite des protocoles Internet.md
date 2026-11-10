---
type: concept
tags: [year4]
aliases: [TCP/IP, protocoles TCP/IP, Internet protocol suite, Transmission Control Protocol, Internet Protocol]
sources: ["[[Raw/Year 4/histoire du design et interactions /chp2 cours.pdf|chp2 cours.pdf]]"]
maj: 2026-11-10
---

**Définition** (d'après [[2 - Histoire du design]]) : protocoles communs, notamment TCP/IP, qui permettent à des réseaux différents de communiquer selon les mêmes règles ; une « langue commune » qui permet aux machines d'échanger des données. Leur adoption par [[ARPANET]] en **1983** est un jalon dans la formation d'[[Internet]] comme « réseau de réseaux ».

Complément (hors du cours) : TCP/IP est décrit par Vinton Cerf et Robert Kahn en 1974 (« A Protocol for Packet Network Intercommunication »), puis normalisé en 1981 (RFC 791 pour IP, RFC 793 pour TCP) ; ARPANET bascule le 1er janvier 1983. La suite est organisée en quatre couches : accès au réseau (par exemple [[Ethernet]]), **IP** (*Internet Protocol*) qui adresse et achemine les paquets d'un réseau à l'autre sans garantie ([[Routage IP]]), **TCP** (*Transmission Control Protocol*) qui assure une livraison fiable et ordonnée entre deux programmes (ou UDP, sans garantie), et les applications (HTTP, SMTP pour le courriel, [[DNS]]). Ce modèle en quatre couches, issu de la pratique, a supplanté le [[Modèle OSI]] en sept couches défini par l'ISO. Les règles sont publiées par l'[[IETF]]. [[Complément hors du cours|ⓘ]]

## Dans le cours

[[2 - Histoire du design]] : section « ARPANET : connecter des ordinateurs », tableau des trois inventions et fiche de lecture (« Internet n'est encore guère plus que la connexion physique des ordinateurs, l'adoption de protocoles communs, notamment TCP/IP »).

Voir aussi : [[Commutation de paquets]], [[Modèle OSI]], [[Routage IP]], [[HTTP]], [[World Wide Web]].

[[1 - Histoire du design]] : sommaire (1984-1993 : … → TCP/IP → …) et résumé du support du chapitre 2.

Résumés : [[2 - Histoire du design]] · [[1 - Histoire du design]]
