// irrigazione_manuale.js – Pulsante virtuale «Avvio manuale irrigazione»
// (sezione B.5.3).
// Richiede un dispositivo con componenti virtuali (Gen3, Gen4, Pro).
// Prima di avviare lo script si crea il componente boolean:200, dall'interfaccia
// web (Components > Create new > Boolean) oppure con la chiamata:
//   curl "http://<IP>/rpc/Virtual.Add?type=\"boolean\"&id=200"
//
// Funzionamento: quando il componente passa a true si accende la pompa sul
// relè 0; dopo DURATA_MS la pompa si spegne e il componente torna a false.
// Riportando a false il componente prima del tempo, la pompa si spegne subito.

let DURATA_MS = 15000;          // 15 s per la prova; in uso reale, minuti
let comando = Virtual.getHandle("boolean:200");
let timer = null;

function ferma() {
  if (timer !== null) {
    Timer.clear(timer);
    timer = null;
  }
  Shelly.call("Switch.Set", { id: 0, on: false });
}

function fineTempo() {
  timer = null;
  ferma();
  comando.setValue(false);      // aggiorna anche l'interfaccia e l'app
  print("Irrigazione terminata");
}

if (comando === null) {
  print("Componente boolean:200 assente: crearlo prima di avviare lo script");
} else {
  comando.setConfig({ name: "Avvio manuale irrigazione" });
  comando.on("change", function (ev) {
    if (ev.value === true && timer === null) {
      Shelly.call("Switch.Set", { id: 0, on: true });
      timer = Timer.set(DURATA_MS, false, fineTempo);
      print("Irrigazione avviata da", ev.source);
    } else if (ev.value === false && timer !== null) {
      ferma();
      print("Irrigazione interrotta");
    }
  });
  print("In attesa del comando manuale");
}
