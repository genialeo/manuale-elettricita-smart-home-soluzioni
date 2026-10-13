"""ewelink_cloud.py – eWeLink Cloud API v2: elenco dispositivi e comando
on/off (Appendice B, sezione B.7.1: nel libro solo un cenno).

Requisiti: Python 3.9+, pacchetto requests.

Credenziali (da variabili d'ambiente, mai scritte nel codice):
  EWELINK_APPID, EWELINK_SECRET  dell'applicazione creata su dev.ewelink.cc
  EWELINK_TOKEN                  access token dell'utente (validità tipica 30 giorni)
  EWELINK_REGION                 eu (Europa), us, as, cn

Il token si ottiene con il flusso OAuth 2.0 previsto per le app degli
sviluppatori: login dell'utente sulla pagina di autorizzazione eWeLink,
redirect con un «code», scambio del code con il token. La libreria Node.js
ewelink-api-next (indicata dal supporto eWeLink) contiene un esempio completo.

Uso:  python ewelink_cloud.py                  elenca i dispositivi
      python ewelink_cloud.py <ID> on|off      comanda un dispositivo monocanale
"""
import base64
import hashlib
import hmac
import json
import os
import sys

import requests

APPID = os.environ.get("EWELINK_APPID", "<APPID>")
SECRET = os.environ.get("EWELINK_SECRET", "<APP_SECRET>")
TOKEN = os.environ.get("EWELINK_TOKEN", "<TOKEN>")
REGIONE = os.environ.get("EWELINK_REGION", "eu")
BASE = (f"https://{REGIONE}-apia.coolkit.cc" if REGIONE != "cn"
        else "https://cn-apia.coolkit.cn")


def firma(corpo_testo):
    """Firma «Sign»: HMAC-SHA256 del corpo esatto, chiave = app secret, in base64.
    Serve solo per le chiamate prima del login (per esempio lo scambio del token)."""
    digest = hmac.new(SECRET.encode(), corpo_testo.encode(), hashlib.sha256).digest()
    return base64.b64encode(digest).decode()


def intestazioni():
    return {"X-CK-Appid": APPID, "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"}


def elenco():
    r = requests.get(f"{BASE}/v2/device/thing", headers=intestazioni(),
                     params={"num": 0}, timeout=10)
    dati = r.json()
    if dati.get("error"):
        raise RuntimeError(f"Errore {dati['error']}: {dati.get('msg')}")
    for cosa in dati["data"]["thingList"]:
        if cosa["itemType"] in (1, 2):          # 1 = proprio, 2 = condiviso
            d = cosa["itemData"]
            print(d["deviceid"], d["name"], "online" if d.get("online") else "offline")


def comanda(ident, stato):
    corpo = {"type": 1, "id": ident, "params": {"switch": stato}}
    r = requests.post(f"{BASE}/v2/device/thing/status", headers=intestazioni(),
                      data=json.dumps(corpo), timeout=10)
    dati = r.json()
    print("Esito:", "ok" if dati.get("error") == 0 else dati)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        comanda(sys.argv[1], sys.argv[2])
    else:
        elenco()
