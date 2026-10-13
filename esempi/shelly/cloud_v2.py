"""cloud_v2.py – Shelly Cloud Control API v2 da Python (sezione B.6).

Requisiti: Python 3.9+, pacchetto requests.
Le credenziali si leggono da variabili d'ambiente, per non scriverle nel codice:
  SHELLY_SERVER   indirizzo del server dell'account (lo indica l'app)
  SHELLY_AUTH_KEY la chiave cloud di autorizzazione
Uso:  python cloud_v2.py <ID_DISPOSITIVO> [on|off]
"""
import os
import sys
import time

import requests

SERVER = os.environ.get("SHELLY_SERVER", "<SERVER>")
AUTH_KEY = os.environ.get("SHELLY_AUTH_KEY", "<AUTH_KEY>")
BASE = f"https://{SERVER}/v2/devices/api"


def chiama(percorso, corpo):
    """POST verso l'API v2; auth_key va nell'indirizzo (query string)."""
    r = requests.post(f"{BASE}/{percorso}", params={"auth_key": AUTH_KEY},
                      json=corpo, timeout=10)
    time.sleep(1)                 # rispetta il limite di 1 richiesta al secondo
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text}")
    return r.json() if r.text else None


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python cloud_v2.py <ID_DISPOSITIVO> [on|off]")
    ident = sys.argv[1].lower()
    for disp in chiama("get", {"ids": [ident], "select": ["status"]}):
        rele = disp.get("status", {}).get("switch:0", {})
        print(disp["id"], "online" if disp["online"] else "offline",
              "- relè 0 acceso:", rele.get("output"))
    if len(sys.argv) > 2:
        chiama("set/switch", {"id": ident, "channel": 0, "on": sys.argv[2] == "on"})
        print("Comando inviato")


if __name__ == "__main__":
    main()
