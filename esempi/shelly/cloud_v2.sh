#!/bin/sh
# cloud_v2.sh – Shelly Cloud Control API, versione 2 (sezione B.6).
# Uso:  SERVER=<SERVER> AUTH_KEY=<AUTH_KEY> ID=<ID_DISPOSITIVO> sh cloud_v2.sh
#   SERVER: indirizzo indicato nell'app (Impostazioni utente > Chiave cloud
#           di autorizzazione), senza https://
#   ID:     identificativo del dispositivo, in minuscolo, senza due punti
# Limite: una richiesta al secondo. Non condividere mai la chiave.
set -e
: "${SERVER:?}" "${AUTH_KEY:?}" "${ID:?}"
BASE="https://$SERVER/v2/devices/api"

echo "1) Stato del dispositivo (solo la parte «status»)"
curl -s -X POST "$BASE/get?auth_key=$AUTH_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"ids\":[\"$ID\"],\"select\":[\"status\"]}"; echo
sleep 1

echo "2) Accende il relè 0"
curl -s -X POST "$BASE/set/switch?auth_key=$AUTH_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"id\":\"$ID\",\"channel\":0,\"on\":true}" -w "HTTP %{http_code}\n"
sleep 1

echo "3) Comando di gruppo: spegne il relè 0 (formato <ID>_<CANALE>)"
curl -s -X POST "$BASE/set/groups?auth_key=$AUTH_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"switch\":{\"ids\":[\"${ID}_0\"],\"command\":{\"on\":false}}}"; echo
