#!/bin/sh
# rpc_http.sh – Chiamate RPC a uno Shelly Gen2+ via HTTP (sezione B.2.3).
# Uso:   SHELLY=<IP> sh rpc_http.sh
# Con password sull'accesso locale: SHELLY=<IP> PASS=<PASSWORD> sh rpc_http.sh
set -e
: "${SHELLY:?Impostare SHELLY con l'indirizzo IP del dispositivo}"

# Opzioni di autenticazione (digest SHA-256, utente sempre «admin»)
if [ -n "$PASS" ]; then AUTH="--anyauth -u admin:$PASS"; else AUTH=""; fi

echo "1) Informazioni sul dispositivo"
curl -s $AUTH "http://$SHELLY/rpc/Shelly.GetDeviceInfo"; echo

echo "2) GET con parametri nell'indirizzo: accende il relè 0"
curl -s $AUTH "http://$SHELLY/rpc/Switch.Set?id=0&on=true"; echo

echo "3) POST a /rpc/<Metodo> con i soli parametri JSON: legge lo stato"
curl -s $AUTH -X POST -H "Content-Type: application/json" \
  -d '{"id":0}' "http://$SHELLY/rpc/Switch.GetStatus"; echo

echo "4) POST a /rpc con il frame completo: spegne il relè 0"
curl -s $AUTH -X POST -H "Content-Type: application/json" \
  -d '{"id":1,"src":"pc","method":"Switch.Set","params":{"id":0,"on":false}}' \
  "http://$SHELLY/rpc"; echo

echo "5) Accensione temporizzata: acceso per 10 s, poi torna spento"
curl -s $AUTH "http://$SHELLY/rpc/Switch.Set?id=0&on=true&toggle_after=10"; echo
