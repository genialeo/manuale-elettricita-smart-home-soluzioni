"""locale_tinytuya.py – Controllo locale di un dispositivo Tuya Wi-Fi con
TinyTuya, senza passare dal cloud (sezione B.8.4).

Requisiti: Python 3.9+, pip install tinytuya
Prima di usare lo script servono ID, indirizzo IP, local key e versione del
protocollo del dispositivo:
  python -m tinytuya scan      trova i dispositivi in rete (IP, ID, versione)
  python -m tinytuya wizard    ricava le local key dal proprio progetto cloud Tuya
Uso:  python locale_tinytuya.py <ID> <IP> <LOCAL_KEY> <VERSIONE> [on|off]
      per esempio versione 3.3, 3.4 o 3.5
"""
import sys

import tinytuya

if len(sys.argv) < 5:
    sys.exit("Uso: python locale_tinytuya.py <ID> <IP> <LOCAL_KEY> <VERSIONE> [on|off]")
ident, ip, chiave, versione = sys.argv[1:5]

presa = tinytuya.OutletDevice(dev_id=ident, address=ip, local_key=chiave,
                              version=float(versione))
stato = presa.status()
if "Error" in stato:
    sys.exit(f"Errore: {stato['Error']}")
print("Data point (dps):", stato.get("dps"))     # per una presa, «1» = uscita

if len(sys.argv) > 5:
    if sys.argv[5] == "on":
        presa.turn_on()
    else:
        presa.turn_off()
    print("Nuovo stato:", presa.status().get("dps"))
