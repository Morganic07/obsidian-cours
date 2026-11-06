#!/usr/bin/env bash
# Mise à jour depuis Drive (lecture seule) : récupère, compare, convertit, transcrit et
# prépare le lot que /maj-cours intègre au wiki. Rien n'est écrit dans le wiki.
# Options : --reprendre (sans contacter Drive), --clore (une fois le wiki à jour).
# Tout le travail, gardes comprises, est dans maj.py.
set -euo pipefail
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/maj.py" "$@"
