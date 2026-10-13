#!/bin/sh
# configura_shelly_mqtt.sh – Collega uno Shelly Gen2+ a un broker MQTT
# (sezione B.3.3).
# Uso:
#   SHELLY=<IP> BROKER=<IP_BROKER>:1883 MQTT_USER=<UTENTE> MQTT_PASS=<PASSWORD> \
#     sh configura_shelly_mqtt.sh
# Per un broker con TLS (porta 8883) aggiungere SSL_CA=ca.pem
# (certificato verificato con le autorità integrate nel dispositivo).
# Se l'accesso locale dello Shelly è protetto: aggiungere PASS=<PASSWORD_SHELLY>.
set -e
: "${SHELLY:?}" "${BROKER:?}" "${MQTT_USER:?}" "${MQTT_PASS:?}"
if [ -n "$PASS" ]; then AUTH="--anyauth -u admin:$PASS"; else AUTH=""; fi
if [ -n "$SSL_CA" ]; then CA="\"$SSL_CA\""; else CA="null"; fi

CONF="{\"enable\":true,\"server\":\"$BROKER\",\"user\":\"$MQTT_USER\",\
\"pass\":\"$MQTT_PASS\",\"ssl_ca\":$CA,\"rpc_ntf\":true,\"status_ntf\":true}"

echo "Invio della configurazione MQTT"
curl -s $AUTH -X POST -H "Content-Type: application/json" \
  -d "{\"id\":1,\"method\":\"Mqtt.SetConfig\",\"params\":{\"config\":$CONF}}" \
  "http://$SHELLY/rpc"; echo

echo "Riavvio (la nuova configurazione MQTT lo richiede)"
curl -s $AUTH "http://$SHELLY/rpc/Shelly.Reboot"; echo
sleep 20

echo "Verifica: «connected» deve valere true"
curl -s $AUTH "http://$SHELLY/rpc/Mqtt.GetStatus"; echo
