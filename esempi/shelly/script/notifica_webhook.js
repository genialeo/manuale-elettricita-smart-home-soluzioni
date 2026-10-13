// notifica_webhook.js – Quando il relè 0 si accende, chiama un indirizzo
// HTTP (webhook) di un altro servizio (sezione B.4.6).
// Sostituire <URL_WEBHOOK> con l'indirizzo del servizio che riceve la notifica,
// per esempio un webhook di Home Assistant: http://<IP_HA>:8123/api/webhook/<ID>

let URL_WEBHOOK = "<URL_WEBHOOK>";

function esito(risposta, codice, messaggio) {
  if (codice === 0 && risposta.code === 200) {
    print("Notifica inviata");
  } else {
    print("Errore nell'invio:", codice, messaggio);
  }
}

Shelly.addStatusHandler(function (st) {
  if (st.component === "switch:0" && st.delta.output === true) {
    Shelly.call("HTTP.POST", {
      url: URL_WEBHOOK,
      body: JSON.stringify({ dispositivo: "corridoio", stato: "acceso" }),
      timeout: 5
    }, esito);
  }
});
