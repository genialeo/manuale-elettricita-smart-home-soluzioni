# Esempi dell'Appendice B – Programmare i dispositivi

Questa cartella contiene il codice completo degli esempi dell'Appendice B del libro *Manuale di Elettricità e Smart Home*. Nel libro compaiono solo gli estratti più importanti, di al massimo 15 righe; qui ci sono i file interi, commentati in italiano e pronti da provare.

Gli esempi sono stati controllati sulla documentazione ufficiale dei produttori a ottobre 2026. Firmware e servizi cloud cambiano: in caso di differenze vale la documentazione citata in fondo.

## Prima di cominciare

- Nessun file contiene credenziali. I valori tra parentesi angolari (`<IP>`, `<TOKEN>`, `<AUTH_KEY>`, `<PASSWORD>`…) vanno sostituiti con i propri, preferibilmente tramite variabili d'ambiente come indicato in testa a ogni file.
- Chiavi, token e password non vanno mai pubblicati, nemmeno in parte (attenzione a schermate, forum e repository pubblici).
- I dispositivi si provano sulla rete di casa. Non si espongono su Internet aprendo porte sul router: per l'accesso da fuori si usano il cloud del produttore o una VPN (capitolo 12).
- Gli script agiscono su carichi reali: le prove si fanno prima con una lampada, non con pompe, motori o elettrodomestici.

Requisiti generali: Python 3.9 o successivo (`pip install -r requirements.txt`), Node.js 22 o successivo per i file `.js` da eseguire sul computer, `curl` e, per MQTT, i client di Mosquitto (`mosquitto_pub`, `mosquitto_sub`).

## Contenuto

### `shelly/` – dispositivi Shelly Gen2, Gen3, Gen4

| File | Cosa fa | Sezione |
|:--|:--|:--|
| `rpc_http.sh` | Chiamate RPC con `curl`: GET, POST a `/rpc/<Metodo>`, POST a `/rpc` | B.2.3 |
| `rpc_http.py` | Le stesse chiamate in Python, con password (digest) | B.2.3, B.2.5 |
| `rpc_websocket.py` | Canale WebSocket con notifiche e autenticazione | B.2.4 |
| `carica_script.py` | Carica e avvia uno script tramite RPC | B.4.2 |
| `cloud_v2.sh`, `cloud_v2.py` | Shelly Cloud Control API v2 | B.6 |

### `shelly/script/` – script da eseguire **sul dispositivo**

Si incollano nell'editor della pagina *Scripts* dell'interfaccia web, oppure si caricano con `carica_script.py`. Non si eseguono con Node.js: usano oggetti (`Shelly`, `Timer`, `Virtual`) che esistono solo sul dispositivo.

| File | Cosa fa | Sezione |
|:--|:--|:--|
| `stato_rele.js` | Legge stato, potenza, tensione e corrente del relè | B.4.3 |
| `eventi.js` | Mostra eventi e variazioni di stato | B.4.4 |
| `spegnimento_automatico.js` | Spegne il carico dopo un tempo fisso | B.4.5 |
| `notifica_webhook.js` | Chiama un webhook all'accensione | B.4.6 |
| `kvs_soglia.js` | Salva e rilegge un parametro nella memoria permanente | B.4.7 |
| `luci_in_sequenza.js` | Accende in sequenza luci di altre stanze | B.4.8 |
| `distacco_carichi.js` | Stacca e riattacca carichi in base alla potenza prelevata | B.4.9 |
| `irrigazione_manuale.js` | Pulsante virtuale per avviare l'irrigazione | B.5.3 |

### `mqtt/`

| File | Cosa fa | Sezione |
|:--|:--|:--|
| `configura_shelly_mqtt.sh` | Collega uno Shelly a un broker MQTT | B.3.3 |
| `comandi_mosquitto.sh` | Ascolto dei topic e comandi RPC con Mosquitto | B.3.4 |
| `ascolta_shelly.py` | Client MQTT in Python (paho-mqtt 2) | B.3.4 |

### `sonoff/`

| File | Cosa fa | Sezione |
|:--|:--|:--|
| `diy_scoperta.py` | Trova i Sonoff in modalità DIY con mDNS | B.7.2 |
| `diy_comandi.py` | Legge lo stato e comanda un Sonoff in modalità DIY | B.7.2 |
| `ewelink_cloud.py` | eWeLink Cloud API v2: firma, elenco dispositivi e comandi (nel libro solo un cenno) | B.7.1 |

### `tuya/`

| File | Cosa fa | Sezione |
|:--|:--|:--|
| `firma_tuya.py` | API cloud Tuya senza SDK, con il calcolo della firma | B.8.2, B.8.3 |
| `controllo_sdk.py` | Le stesse operazioni con l'SDK `tuya-connector-python` | B.8.2 |
| `locale_tinytuya.py` | Controllo locale con TinyTuya | B.8.4 |
| `locale_tuyapi.js` | Controllo locale con TuyAPI (Node.js) | B.8.4 |

## Come sono stati controllati

- Python: `python -m py_compile` su tutti i file.
- JavaScript: `node --check` su tutti i file; gli script Shelly sono stati provati anche in un ambiente simulato che riproduce `Shelly.call`, `Timer` e `Virtual` (non su un dispositivo reale: la prima prova si fa con una lampada).
- La funzione di firma di `ewelink_cloud.py` e quella di `firma_tuya.py` riproducono gli esempi numerici della documentazione ufficiale eWeLink e Tuya.
- Shell: `sh -n` su tutti i file.

## Documentazione ufficiale

- Shelly, API Gen2+ e script: https://shelly-api-docs.shelly.cloud/gen2/
- Shelly Cloud Control API: https://shelly-api-docs.shelly.cloud/cloud-control-api/
- Sonoff, protocollo DIY: https://help.sonoff.tech/docs/DIY-MODE-API-PROTOCOL
- eWeLink Cloud API v2: https://coolkit-technologies.github.io/eWeLink-API/ e https://dev.ewelink.cc
- Tuya Developer Platform: https://developer.tuya.com
- TinyTuya: https://github.com/jasonacox/tinytuya
- TuyAPI: https://github.com/codetheweb/tuyapi
