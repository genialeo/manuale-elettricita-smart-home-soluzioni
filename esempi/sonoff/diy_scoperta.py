"""diy_scoperta.py – Trova i dispositivi Sonoff in modalità DIY sulla rete
locale tramite mDNS (sezione B.7.2).

Requisiti: Python 3.9+, pacchetto zeroconf (pip install zeroconf).
Uso:  python diy_scoperta.py
"""
import time

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

SERVIZIO = "_ewelink._tcp.local."


class Ascoltatore(ServiceListener):
    def __init__(self):
        self.trovati = {}

    def add_service(self, zc, tipo, nome):
        info = zc.get_service_info(tipo, nome)
        if not info:
            return
        # il nome è del tipo eWeLink_<ID>._ewelink._tcp.local.
        ident = nome.split(".")[0].replace("eWeLink_", "")
        indirizzi = info.parsed_addresses()
        self.trovati[ident] = (indirizzi[0] if indirizzi else "?", info.port)
        print(f"Trovato {ident} su {self.trovati[ident][0]}:{info.port}")

    def update_service(self, zc, tipo, nome):
        pass                         # cambio di stato: qui non interessa

    def remove_service(self, zc, tipo, nome):
        pass


zc = Zeroconf()
ascoltatore = Ascoltatore()
ServiceBrowser(zc, SERVIZIO, ascoltatore)
time.sleep(5)                        # tempo per raccogliere le risposte
zc.close()
print("Dispositivi trovati:", ascoltatore.trovati or "nessuno")
