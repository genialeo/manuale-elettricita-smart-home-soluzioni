// distacco_carichi.js – Gestione dei carichi per non superare la potenza
// disponibile del contatore (sezione B.4.9).
// Gira sul misuratore di energia montato a valle del contatore:
// - monofase (Shelly Pro EM, EM Gen3): componente em1:0, campo act_power
// - trifase (Shelly Pro 3EM): impostare METODO "EM.GetStatus" e CAMPO "total_act_power"
// I carichi sono comandati da Shelly Gen2+ (componente switch:0).
// Ogni 10 s: se la potenza supera la soglia stacca UN carico (il meno
// importante ancora acceso); se scende sotto il rientro ne riattacca uno.
//
// Lo script NON è un dispositivo di protezione: interruttori automatici e
// differenziali del quadro restano indispensabili (capitolo 6).

let METODO = "EM1.GetStatus";   // oppure "EM.GetStatus"
let CAMPO = "act_power";        // oppure "total_act_power"
let SOGLIA_W = 3300;            // contratto da 3 kW: potenza disponibile 3,3 kW
let RIENTRO_W = 2300;           // si riattacca solo con almeno 1 kW di margine
let PERIODO_MS = 10000;

// In ordine di importanza crescente: il primo è il primo a essere staccato.
// Se i dispositivi sono protetti da password: "http://admin:<PASSWORD>@<IP>"
let CARICHI = [
  { nome: "asciugatrice", base: "http://<IP_ASCIUGATRICE>", staccato: false },
  { nome: "lavastoviglie", base: "http://<IP_LAVASTOVIGLIE>", staccato: false },
  { nome: "lavatrice", base: "http://<IP_LAVATRICE>", staccato: false }
];

let occupato = false;   // evita di sovrapporre due interventi

function comanda(carico, acceso) {
  occupato = true;
  let url = carico.base + "/rpc/Switch.Set?id=0&on=" + (acceso ? "true" : "false");
  Shelly.call("HTTP.GET", { url: url, timeout: 5 }, function (r, codice, msg) {
    occupato = false;
    if (codice === 0 && r.code === 200) {
      carico.staccato = !acceso;
      print(acceso ? "Riattaccato:" : "Staccato:", carico.nome);
    } else {
      print("Errore su", carico.nome + ":", msg);
    }
  });
}

function primoAcceso() {
  // primo carico non ancora staccato da questo script
  for (let i = 0; i < CARICHI.length; i++) {
    if (!CARICHI[i].staccato) {
      return CARICHI[i];
    }
  }
  return null;
}

function ultimoStaccato() {
  // si riattacca per primo il carico più importante tra quelli staccati
  for (let i = CARICHI.length - 1; i >= 0; i--) {
    if (CARICHI[i].staccato) {
      return CARICHI[i];
    }
  }
  return null;
}

function controlla() {
  if (occupato) {
    return;
  }
  Shelly.call(METODO, { id: 0 }, function (stato, codice) {
    if (codice !== 0 || !stato) {
      print("Lettura della potenza non riuscita");
      return;
    }
    let p = stato[CAMPO];
    print("Potenza prelevata:", p, "W");
    if (p > SOGLIA_W) {
      let c = primoAcceso();
      if (c !== null) {
        comanda(c, false);
      }
    } else if (p < RIENTRO_W) {
      let c2 = ultimoStaccato();
      if (c2 !== null) {
        comanda(c2, true);
      }
    }
  });
}

Timer.set(PERIODO_MS, true, controlla);
print("Gestione carichi avviata, soglia", SOGLIA_W, "W");
