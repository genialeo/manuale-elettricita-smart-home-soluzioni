"""rpc_http.py – Chiamate RPC a uno Shelly Gen2+ via HTTP con Python (sezione B.2.3).

Requisiti: Python 3.9+, pacchetto requests (pip install requests).
Uso:  python rpc_http.py <IP> [password]
La password serve solo se sull'accesso locale è attiva l'autenticazione
(utente sempre «admin», metodo digest SHA-256, supportato da requests).
"""
import sys

import requests
from requests.auth import HTTPDigestAuth


def rpc(ip, metodo, parametri=None, password=None):
    """Invia un comando RPC con POST /rpc/<Metodo> e restituisce il risultato."""
    auth = HTTPDigestAuth("admin", password) if password else None
    r = requests.post(f"http://{ip}/rpc/{metodo}", json=parametri or {},
                      auth=auth, timeout=5)
    r.raise_for_status()          # errore se il codice HTTP non è 2xx
    return r.json()


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python rpc_http.py <IP> [password]")
    ip = sys.argv[1]
    pw = sys.argv[2] if len(sys.argv) > 2 else None

    info = rpc(ip, "Shelly.GetDeviceInfo", password=pw)
    print("Modello:", info.get("model"), "- firmware:", info.get("ver"))

    print("Prima:", rpc(ip, "Switch.GetStatus", {"id": 0}, pw).get("output"))
    rpc(ip, "Switch.Toggle", {"id": 0}, pw)          # inverte lo stato
    stato = rpc(ip, "Switch.GetStatus", {"id": 0}, pw)
    print("Dopo:", stato.get("output"), "- potenza:", stato.get("apower"), "W")


if __name__ == "__main__":
    main()
