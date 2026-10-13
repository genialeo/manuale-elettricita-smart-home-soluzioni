"""firma_tuya.py – Chiamate alle API cloud Tuya senza SDK (sezione B.8.2).

Implementa la firma HMAC-SHA256 descritta nella documentazione Tuya:
  stringToSign = METODO \\n SHA256(corpo) \\n header_firmati \\n URL
  str  = client_id [+ access_token] + t + nonce + stringToSign
  sign = MAIUSCOLO( HMAC-SHA256(str, access_secret) )

Requisiti: Python 3.9+, pacchetto requests.
Credenziali da variabili d'ambiente: TUYA_ACCESS_ID, TUYA_ACCESS_SECRET.
Uso:  python firma_tuya.py <ID_DISPOSITIVO> [on|off]
"""
import hashlib
import hmac
import json
import os
import sys
import time
import uuid

import requests

ENDPOINT = "https://openapi.tuyaeu.com"          # data center Europa
ACCESS_ID = os.environ.get("TUYA_ACCESS_ID", "<ACCESS_ID>")
ACCESS_SECRET = os.environ.get("TUYA_ACCESS_SECRET", "<ACCESS_SECRET>")


def calcola_firma(metodo, url, corpo, t, nonce, token="", header_firmati=""):
    """Restituisce la firma per una richiesta (url = percorso + query ordinata)."""
    hash_corpo = hashlib.sha256(corpo.encode()).hexdigest()
    da_firmare = "\n".join([metodo, hash_corpo, header_firmati, url])
    testo = ACCESS_ID + token + t + nonce + da_firmare
    return hmac.new(ACCESS_SECRET.encode(), testo.encode(),
                    hashlib.sha256).hexdigest().upper()


def richiesta(metodo, percorso, corpo=None, token=""):
    testo = json.dumps(corpo) if corpo is not None else ""
    t = str(int(time.time() * 1000))                 # millisecondi, 13 cifre
    nonce = uuid.uuid4().hex
    intest = {"client_id": ACCESS_ID, "t": t, "nonce": nonce,
              "sign_method": "HMAC-SHA256",
              "sign": calcola_firma(metodo, percorso, testo, t, nonce, token)}
    if token:
        intest["access_token"] = token
    if corpo is not None:
        intest["Content-Type"] = "application/json"
    r = requests.request(metodo, ENDPOINT + percorso, headers=intest,
                         data=testo or None, timeout=10)
    dati = r.json()
    if not dati.get("success"):
        raise RuntimeError(f"Errore {dati.get('code')}: {dati.get('msg')}")
    return dati["result"]


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python firma_tuya.py <ID_DISPOSITIVO> [on|off]")
    ident = sys.argv[1]
    # 1) token: vale circa 2 ore (expire_time in secondi)
    tok = richiesta("GET", "/v1.0/token?grant_type=1")
    at = tok["access_token"]
    print("Token ottenuto, scade tra", tok["expire_time"], "s")
    # 2) funzioni disponibili e stato
    print(richiesta("GET", f"/v1.0/iot-03/devices/{ident}/functions", token=at))
    print(richiesta("GET", f"/v1.0/iot-03/devices/{ident}/status", token=at))
    # 3) comando (switch_1 per prese e interruttori, switch_led per lampadine)
    if len(sys.argv) > 2:
        comandi = {"commands": [{"code": "switch_1", "value": sys.argv[2] == "on"}]}
        richiesta("POST", f"/v1.0/iot-03/devices/{ident}/commands", comandi, at)
        print("Comando inviato")


if __name__ == "__main__":
    main()
