"""controllo_sdk.py – API cloud Tuya con l'SDK ufficiale tuya-connector-python
(Appendice B, sezione B.8.2: nel libro solo un cenno).

Requisiti: Python 3.9+, pip install tuya-connector-python
(versione 0.1.2: l'SDK non riceve aggiornamenti dal 2021 ma funziona; in
alternativa firma_tuya.py fa le stesse chiamate senza SDK).
Credenziali da variabili d'ambiente: TUYA_ACCESS_ID, TUYA_ACCESS_SECRET.
Uso:  python controllo_sdk.py <ID_DISPOSITIVO> [on|off]
"""
import os
import sys

from tuya_connector import TuyaOpenAPI

ENDPOINT = "https://openapi.tuyaeu.com"          # data center Europa
ACCESS_ID = os.environ.get("TUYA_ACCESS_ID", "<ACCESS_ID>")
ACCESS_SECRET = os.environ.get("TUYA_ACCESS_SECRET", "<ACCESS_SECRET>")

if len(sys.argv) < 2:
    sys.exit("Uso: python controllo_sdk.py <ID_DISPOSITIVO> [on|off]")
ident = sys.argv[1]

api = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_SECRET)
api.connect()                                    # ottiene e rinnova il token

# Prima le funzioni: dicono quali codici (data point) accetta il dispositivo
print(api.get(f"/v1.0/iot-03/devices/{ident}/functions"))
print(api.get(f"/v1.0/iot-03/devices/{ident}/status"))

if len(sys.argv) > 2:
    comandi = {"commands": [{"code": "switch_1", "value": sys.argv[2] == "on"}]}
    print(api.post(f"/v1.0/iot-03/devices/{ident}/commands", comandi))
