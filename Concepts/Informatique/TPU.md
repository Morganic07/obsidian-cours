---
type: concept
tags:
  - year3
aliases:
  - Tensor Processing Unit
matieres:
  - IA
sources:
  - "[[1 - IA|Cours 1]]"
  - "[[Raw/Year 3/IA/Cours 1.docx|Cours 1 (IA)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le TPU (*Tensor Processing Unit*) est un circuit intégré spécialisé (ASIC, *application-specific integrated circuit*) conçu par Google et annoncé en 2016. Il est optimisé pour les multiplications de matrices et de tenseurs qui dominent les calculs des [[Réseau de neurones|réseaux de neurones]].

Comparaison des trois types de puces :
- le [[Processeur|CPU]] a quelques cœurs puissants et polyvalents, qui enchaînent des tâches variées ;
- le [[Processeur graphique|GPU]] a des milliers de cœurs simples qui exécutent la même opération en parallèle ;
- le TPU est encore plus spécialisé : il ne sait faire efficacement que ces calculs d'algèbre linéaire, mais les fait avec moins d'énergie par opération.

En pratique, la plupart des modèles d'IA sont entraînés et servis sur des GPU (Nvidia surtout) ; les TPU servent surtout aux modèles de Google (Gemini) et sont accessibles aux autres via son offre de cloud.

## Dans le cours

Nommé dans [[1 - IA|Cours 1 (IA)]] sans définition : les IA tournent sur des processeurs spécialisés dans le calcul parallèle, surtout des GPU, et des TPU chez Google. [[Erreurs du cours#^e-tpu|✎]]

Voir aussi : [[Consommation énergétique de l'IA]], [[Processeur graphique]], [[Apprentissage profond]].

Résumés : [[1 - IA|Cours 1 (IA, résumé)]]
