"""diy_comandi.py – Comandi locali a un Sonoff in modalità DIY (sezione B.7.2).

Vale per i modelli che supportano la modalità DIY (per esempio BASICR3,
RFR3, MINIR2, MINIR3, D1), non per la serie R4. Intervallo minimo tra due
richieste indicato da Sonoff: 200 ms.

Requisiti: Python 3.9+, pacchetto requests.
Uso:  python diy_comandi.py <IP> <ID_DISPOSITIVO> [on|off]
"""
import sys
import time

import requests

PORTA = 8081
ERRORI = {400: "JSON non valido", 401: "richiesta non cifrata (cifratura attiva)",
          404: "dispositivo inesistente", 422: "parametri non validi"}


def comando(ip, ident, percorso, dati):
    """POST http://<IP>:8081/zeroconf/<percorso> con il formato DIY."""
    corpo = {"deviceid": ident, "data": dati}
    r = requests.post(f"http://{ip}:{PORTA}/zeroconf/{percorso}", json=corpo, timeout=5)
    risposta = r.json()
    if risposta.get("error", 0) != 0:
        cod = risposta["error"]
        raise RuntimeError(f"Errore {cod}: {ERRORI.get(cod, 'sconosciuto')}")
    time.sleep(0.2)
    return risposta.get("data", {})


def main():
    if len(sys.argv) < 3:
        sys.exit("Uso: python diy_comandi.py <IP> <ID_DISPOSITIVO> [on|off]")
    ip, ident = sys.argv[1], sys.argv[2]
    info = comando(ip, ident, "info", {})
    print("Firmware:", info.get("fwVersion"), "- uscita:", info.get("switch"))
    if len(sys.argv) > 3:
        comando(ip, ident, "switch", {"switch": sys.argv[3]})
        print("Uscita portata a", sys.argv[3])
    # MINIR3: percorso "switches", con l'elenco dei canali,
    #   {"switches": [{"switch": "on", "outlet": 0}]}; anche «info»
    #   restituisce «switches» al posto di «switch»
    # Dimmer D1: percorso "dimmable", {"switch": "on", "brightness": 50}


if __name__ == "__main__":
    main()
