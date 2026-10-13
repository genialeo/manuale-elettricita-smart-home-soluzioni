// kvs_soglia.js – Salva e rilegge un parametro nella memoria permanente
// KVS (Key-Value Store) del dispositivo (sezione B.4.7).
// Il valore resta memorizzato anche dopo un riavvio o una mancanza di rete.
// Limiti del KVS (documentazione Shelly): 50 chiavi, chiave fino a 42
// caratteri, valore fino a 253 caratteri.

let CHIAVE = "soglia_w";
let soglia = 3000;   // valore di partenza se la chiave non esiste

function letto(risposta, codice) {
  if (codice === 0 && risposta) {
    soglia = risposta.value;
    print("Soglia letta dalla memoria:", soglia, "W");
  } else {
    // chiave assente: la si crea con il valore di partenza
    Shelly.call("KVS.Set", { key: CHIAVE, value: soglia });
    print("Soglia salvata per la prima volta:", soglia, "W");
  }
}

Shelly.call("KVS.Get", { key: CHIAVE }, letto);
