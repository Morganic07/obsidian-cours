---
type: source
sources: ["TP3 du dossier DM/TP3"]
maj: 2026-11-05
---

Résumé de la note TP3 du dossier `DM/TP3` de [[Year 2 - Operating System]] (la note porte le nom de l'étudiant, d'où l'absence de lien direct). Captures lues par transcription seulement.

## Ce qu'apprend le TP

Même contenu que [[Cours TP3]], en version rendue.
- Tâche 1 : lire son adresse (`ip address`, `hostname -I`), `/etc/hosts`, éditer le fichier et vérifier par `ping`. Pas de fichier netplan : la configuration se trouve dans `/etc/network/interfaces` (`iface eth0 inet dhcp`).
- Script `time.sh` : ajoute la date toutes les 2 s ; `backup.sh` la copie toutes les 15 s avec message de réussite. Lancés en arrière-plan avec `&`, arrêtés avec `kill`.
- Tâche 2 : même principe avec `free -h` toutes les 5 s dans `memory.txt`. Voir [[Script Bash]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Adresse `127.0.0.1.1`** : la transcription la signale ; probablement `127.0.1.1` (curseur sur le premier caractère). Image non rouverte.
2. **`ping penguin` après modification** : la sortie montre `127.0.1.1`, alors que le fichier modifié associe `penguin` à `127.0.0.1` ; la capture date peut-être d'avant la modification (complément).
3. **Doublons dans `date.txt`** : les horodatages se répètent deux fois par intervalle, ce qui indique que deux copies du script écrivaient en même temps (complément).
4. **Adresse affichée comme « interne »** : `127.0.0.1` est l'adresse de bouclage, pas une adresse locale du réseau.
