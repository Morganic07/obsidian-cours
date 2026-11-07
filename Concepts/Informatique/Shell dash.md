---
type: concept
tags: [year2]
aliases: [dash, Debian Almquist shell]
matieres: [Operating System]
sources: ["[[5 - OS|OS - chp 5]]", "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : dash (*Debian Almquist shell*) est un shell léger, compatible avec la norme POSIX et dérivé du shell Almquist (ash), lui-même une réimplémentation du [[Bourne Shell (sh)]]. Plus petit et plus rapide que Bash, il n'en a pas les extensions (tableaux, `[[ … ]]`, etc.). Sous Debian et Ubuntu, `/bin/sh` pointe vers dash : les scripts lancés avec `sh` ou commençant par `#!/bin/sh` sont donc exécutés par dash, et non par Bash (voir [[Shell et Bash]]).

## Dans le cours

Nommé sans définition : dash est cité parmi les shells, et `/bin/dash` figure dans la sortie de `cat /etc/shells`.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Bourne Shell (sh)]].

Résumés : [[5 - OS]]
