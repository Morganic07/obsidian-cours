---
type: concept
tags: [year2]
aliases: [symbolic link, liens symboliques]
sources: ["[[5 - OS (résumé)|OS - chp 5]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : un lien symbolique (*symbolic link*, *symlink*) est un fichier spécial qui contient le chemin d'un autre fichier ou répertoire ; l'ouvrir revient à ouvrir sa cible. On le crée avec `ln -s cible nom_du_lien`, et `ls -l` l'affiche avec un `l` en tête des permissions et une flèche vers la cible. Il se distingue du lien physique (*hard link*), qui est un second nom pour le même fichier (même inode), et c'est le nombre de ces liens physiques, non des liens symboliques, que compte la 2e colonne de `ls -l` (voir « À vérifier ») ; si la cible d'un lien symbolique est supprimée, le lien reste mais devient cassé.

## Dans le cours

Nommé dans le chapitre 5 sans définition : le cours dit seulement que la 2e colonne de `ls -l` montre « le nombre de liens symboliques pointant vers le fichier ».

Notion parente : [[Système de fichiers]]. Voir aussi : [[Commande ls]].

## À vérifier

- Erreur du cours relevée par le résumé : la 2e colonne de `ls -l` compte les liens physiques (hard links), pas les liens symboliques.

Résumés : [[5 - OS (résumé)]]
