---
type: concept
tags: [year3]
aliases: [GPU, carte graphique, Graphics Processing Unit, processeurs graphiques]
sources: ["[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le processeur graphique (GPU, *Graphics Processing Unit*) est un processeur conçu à l'origine pour calculer l'affichage (pixels, rendu 3D). Il compte des milliers de cœurs simples qui exécutent la même opération sur de nombreuses données en parallèle, à l'inverse du [[Processeur|CPU]], qui a peu de cœurs, puissants et polyvalents, optimisés pour enchaîner rapidement des tâches variées.

- **Intérêt pour l'IA** : ce parallélisme convient aux multiplications de matrices de l'[[Apprentissage profond|apprentissage profond]], où les mêmes opérations s'appliquent à des millions de poids. Les GPU ont rendu possible l'essor du deep learning à partir de 2012 : AlexNet, [[Réseau de neurones convolutif|réseau convolutif]] entraîné sur deux GPU, remporte cette année-là le concours de classement d'images ImageNet avec une large avance.
- **Marché** : Nvidia domine le marché des GPU pour l'IA, notamment grâce à sa plateforme de programmation CUDA.
- **Mémoire** : le GPU dispose de sa propre mémoire (VRAM). Sa taille limite celle des modèles qu'on peut faire tourner en local, car les paramètres du modèle doivent y tenir.
- **Puces plus spécialisées** : le [[TPU]] de Google pousse plus loin la spécialisation pour les calculs de tenseurs.

## Dans le cours

Le cours ne le définit pas. [[1 - IA]] ne le nomme que pour affirmer que les IA reposent sur des TPU « pas des CPU ou GPU » (affirmation corrigée dans [[TPU]]) ; la comparaison CPU, GPU, TPU figure dans les compléments de la fiche.

Voir aussi : [[TPU]], [[Processeur]], [[Apprentissage profond]], [[Réseau de neurones]], [[Consommation énergétique de l'IA]].

Résumés : [[1 - IA]]
