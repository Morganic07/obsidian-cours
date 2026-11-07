---
type: concept
tags: [year2]
aliases: [secure boot]
sources: ["[[OS - chp 2 (résumé)|OS - chp 2]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : le démarrage sécurisé (*Secure Boot*) est une fonction de l'[[BIOS et UEFI|UEFI]] qui n'autorise à s'exécuter au démarrage que des programmes signés numériquement par une clé reconnue par le micrologiciel : [[Chargeur de démarrage|chargeur de démarrage]], pilotes UEFI, puis noyau. Il empêche ainsi un logiciel malveillant (*bootkit*) de s'insérer dans la chaîne de démarrage avant le système d'exploitation. Les distributions Linux courantes le prennent en charge via un petit chargeur signé (*shim*).

## Dans le cours

Nommé dans le chp 2 sans définition : le tableau BIOS contre UEFI indique des options de démarrage sécurisé limitées pour le BIOS et étendues pour l'UEFI (« more secure boot »).

Notion parente : [[BIOS et UEFI]].

Résumés : [[OS - chp 2 (résumé)]]
