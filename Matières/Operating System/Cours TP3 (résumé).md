---
type: source
tags: [year2]
sources: ["[[Cours TP3]]"]
maj: 2026-11-05
---

Résumé de [[Cours TP3]], dans [[Operating System (matière)]]. Images lues par transcription seulement.

## Contenu, dans l'ordre du cours

- **Adresse IP** : étiquette numérique qui identifie un appareil et indique sa position. `ip address` ou `ifconfig`. Annotations de l'étudiant : `eth0` première interface Ethernet, `lo` boucle locale, `inet` IPv4, `netmask`, `broadcast`, `inet6` IPv6, `RX` / `TX` paquets reçus et envoyés, les drapeaux donnent l'état de l'interface. `wlan0` : Wi-Fi.
- **Résolution de noms** : le DNS convertit un nom en adresse ; `/etc/hosts` est une table locale, prise en compte immédiatement.
- **`ping`** : teste la connectivité ; le nom de la machine, `127.0.0.1` et un site répondent, une IP aléatoire non.
- **Configuration manuelle** : fichiers YAML dans `/etc/netplan` (sensibles à l'indentation) ; à défaut `/etc/network/interfaces`.
- **Sauvegarde** : scripts Bash en boucle infinie : ajouter la date toutes les 2 s dans `date.txt`, copier toutes les 15 s ; même principe avec `free -h` toutes les 5 s dans `memory.txt` et copie toutes les 20 s. Voir [[Script Bash]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`echo "$Backup Successful!"`** : le `$` devant « Backup » est probablement une faute, la variable n'existe pas et le mot disparaîtrait de l'affichage (complément ; alerte de la transcription confirmée).
2. **Script `time.sh` et de sauvegarde** : le `done` final de la boucle est absent des extraits recopiés (la note s'arrête avant). Le script de copie utilise des chemins `/home/user/...` génériques (complément).
3. **Dernière ligne de la définition de l'IP** : la transcription la dit coupée, le mot manquant est « communication » ; fausse alerte.
4. **Mélange des interfaces** : `ifconfig` demande le paquet `net-tools`, ce qui n'est pas dit dans la note (complément).
