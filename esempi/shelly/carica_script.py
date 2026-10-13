"""carica_script.py – Carica e avvia uno script su uno Shelly Gen2+ via RPC
(sezione B.4.2), senza passare dall'interfaccia web.

Requisiti: Python 3.9+, pacchetto requests.
Uso:  python carica_script.py <IP> <file.js> [password]

Passi: Script.Create (se non esiste uno script con lo stesso nome),
Script.Stop, Script.PutCode a blocchi, Script.SetConfig (avvio automatico
all'accensione), Script.Start.
"""
import os
import sys

import requests
from requests.auth import HTTPDigestAuth

BLOCCO = 1024          # caratteri per ogni chiamata Script.PutCode


def rpc(ip, metodo, parametri, auth):
    r = requests.post(f"http://{ip}/rpc/{metodo}", json=parametri, auth=auth, timeout=10)
    r.raise_for_status()
    return r.json()


def main():
    if len(sys.argv) < 3:
        sys.exit("Uso: python carica_script.py <IP> <file.js> [password]")
    ip, percorso = sys.argv[1], sys.argv[2]
    auth = HTTPDigestAuth("admin", sys.argv[3]) if len(sys.argv) > 3 else None
    nome = os.path.splitext(os.path.basename(percorso))[0]
    with open(percorso, encoding="utf-8") as f:
        codice = f.read()

    esistenti = rpc(ip, "Script.List", {}, auth)["scripts"]
    trovati = [s["id"] for s in esistenti if s["name"] == nome]
    if trovati:
        sid = trovati[0]
        rpc(ip, "Script.Stop", {"id": sid}, auth)
    else:
        sid = rpc(ip, "Script.Create", {"name": nome}, auth)["id"]

    for i in range(0, len(codice), BLOCCO):
        rpc(ip, "Script.PutCode",
            {"id": sid, "code": codice[i:i + BLOCCO], "append": i > 0}, auth)

    rpc(ip, "Script.SetConfig", {"id": sid, "config": {"enable": True}}, auth)
    rpc(ip, "Script.Start", {"id": sid}, auth)
    print(f"Script «{nome}» caricato (id {sid}) e avviato")


if __name__ == "__main__":
    main()
