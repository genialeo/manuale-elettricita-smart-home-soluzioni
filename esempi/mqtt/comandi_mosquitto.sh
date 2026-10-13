#!/bin/sh
# comandi_mosquitto.sh – Prove MQTT con i client a riga di comando di
# Mosquitto (sezione B.3.4). Installazione: pacchetto «mosquitto-clients».
# Uso:
#   BROKER=<IP_BROKER> MQTT_USER=<UTENTE> MQTT_PASS=<PASSWORD> \
#   SHELLY_ID=<ID_DISPOSITIVO> sh comandi_mosquitto.sh ascolta|comando|stato
#   SHELLY_ID è il prefisso dei topic, per esempio shelly1pmminig3-aabbccddeeff
set -e
: "${BROKER:?}" "${MQTT_USER:?}" "${MQTT_PASS:?}" "${SHELLY_ID:?}"
OPZ="-h $BROKER -p 1883 -u $MQTT_USER -P $MQTT_PASS"

case "$1" in
  ascolta)
    # tutti i messaggi del dispositivo: # è il carattere jolly multilivello
    mosquitto_sub $OPZ -v -t "$SHELLY_ID/#" ;;
  comando)
    # richiesta RPC: la risposta arriva sul topic <src>/rpc, cioè pc/rpc
    mosquitto_sub $OPZ -v -C 1 -t "pc/rpc" &
    sleep 1
    mosquitto_pub $OPZ -t "$SHELLY_ID/rpc" \
      -m '{"id":1,"src":"pc","method":"Switch.Toggle","params":{"id":0}}'
    wait ;;
  stato)
    # chiede allo Shelly di ripubblicare lo stato completo
    mosquitto_pub $OPZ -t "$SHELLY_ID/command" -m status_update ;;
  *)
    echo "Uso: sh comandi_mosquitto.sh ascolta|comando|stato" ;;
esac
