"""ascolta_shelly.py – Client MQTT in Python per uno Shelly Gen2+ (sezione B.3.4).

Si iscrive ai topic del dispositivo, stampa stato e potenza del relè 0 e,
se richiesto, invia un comando RPC (Switch.Toggle) attendendone la risposta.

Requisiti: Python 3.9+, paho-mqtt 2.x (pip install "paho-mqtt>=2").
Configurazione da variabili d'ambiente:
  MQTT_BROKER, MQTT_PORT (1883, oppure 8883 con TLS), MQTT_USER, MQTT_PASS,
  SHELLY_ID (prefisso dei topic, per esempio shelly1pmminig3-aabbccddeeff)
Uso:  python ascolta_shelly.py [toggle]
"""
import json
import os
import sys

import paho.mqtt.client as mqtt

BROKER = os.environ.get("MQTT_BROKER", "<IP_BROKER>")
PORTA = int(os.environ.get("MQTT_PORT", "1883"))
UTENTE = os.environ.get("MQTT_USER", "<UTENTE>")
PASSWORD = os.environ.get("MQTT_PASS", "<PASSWORD>")
SHELLY = os.environ.get("SHELLY_ID", "<ID_DISPOSITIVO>")
SRC = "pc-py"                        # le risposte RPC arrivano su pc-py/rpc


def connesso(client, userdata, flags, codice, proprieta):
    if codice.is_failure:
        print("Connessione rifiutata:", codice)
        return
    client.subscribe(f"{SHELLY}/#")
    client.subscribe(f"{SRC}/rpc")
    if "toggle" in sys.argv:
        richiesta = {"id": 1, "src": SRC, "method": "Switch.Toggle", "params": {"id": 0}}
        client.publish(f"{SHELLY}/rpc", json.dumps(richiesta))


def messaggio(client, userdata, msg):
    testo = msg.payload.decode(errors="replace")
    if msg.topic == f"{SHELLY}/status/switch:0":
        stato = json.loads(testo)
        print("Relè 0:", "acceso" if stato.get("output") else "spento",
              "- potenza:", stato.get("apower"), "W")
    elif msg.topic == f"{SRC}/rpc":
        print("Risposta RPC:", testo)
    else:
        print(msg.topic, testo[:120])


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=SRC)
client.username_pw_set(UTENTE, PASSWORD)
if PORTA == 8883:
    client.tls_set()                 # TLS con le autorità di certificazione di sistema
client.on_connect = connesso
client.on_message = messaggio
client.connect(BROKER, PORTA)
client.loop_forever()
