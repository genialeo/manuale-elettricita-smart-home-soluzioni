"""rpc_websocket.py – Canale WebSocket di uno Shelly Gen2+ (sezione B.2.4).

Apre ws://<IP>/rpc, invia un comando e poi resta in ascolto delle notifiche
(NotifyStatus, NotifyEvent) che il dispositivo invia spontaneamente.
Gestisce anche l'autenticazione digest se sull'accesso locale c'è una password.

Requisiti: Python 3.9+, pacchetto websockets 11 o successivo
(pip install websockets).
Uso:  python rpc_websocket.py <IP> [password]
"""
import hashlib
import json
import random
import sys

from websockets.sync.client import connect

SRC = "pc"             # nome del client: le risposte arrivano a questo «indirizzo»


def sha256(testo):
    return hashlib.sha256(testo.encode()).hexdigest()


def oggetto_auth(sfida, password):
    """Calcola l'oggetto auth a partire dalla sfida contenuta nell'errore 401."""
    realm, nonce = sfida["realm"], sfida["nonce"]
    nc = "00000001"     # contatore a 8 cifre esadecimali: 1 per un nonce nuovo
    cnonce = random.randint(1, 2**31)
    ha1 = sha256(f"admin:{realm}:{password}")
    ha2 = sha256("dummy_method:dummy_uri")  # valori fissi previsti da Shelly
    risposta = sha256(f"{ha1}:{nonce}:{nc}:{cnonce}:auth:{ha2}")
    return {"realm": realm, "username": "admin", "nonce": nonce, "cnonce": cnonce,
            "nc": nc, "response": risposta, "algorithm": "SHA-256"}


def chiama(ws, ident, metodo, parametri, password):
    """Invia una richiesta e attende la risposta con lo stesso id."""
    frame = {"id": ident, "src": SRC, "method": metodo, "params": parametri}
    ws.send(json.dumps(frame))
    while True:
        msg = json.loads(ws.recv())
        if msg.get("id") != ident:
            continue                      # notifica arrivata nel frattempo
        err = msg.get("error")
        if err and err.get("code") == 401 and password:
            frame["auth"] = oggetto_auth(json.loads(err["message"]), password)
            ws.send(json.dumps(frame))    # stesso comando, ora autenticato
            continue
        return msg


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python rpc_websocket.py <IP> [password]")
    ip = sys.argv[1]
    pw = sys.argv[2] if len(sys.argv) > 2 else None
    with connect(f"ws://{ip}/rpc") as ws:
        print(chiama(ws, 1, "Switch.Toggle", {"id": 0}, pw))
        print("In ascolto delle notifiche (Ctrl+C per uscire)...")
        for testo in ws:
            msg = json.loads(testo)
            if msg.get("method") in ("NotifyStatus", "NotifyEvent"):
                print(msg["method"], json.dumps(msg["params"]))


if __name__ == "__main__":
    main()
