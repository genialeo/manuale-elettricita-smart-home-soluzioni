// spegnimento_automatico.js – Spegne il relè 0 dopo un tempo fisso
// dall'accensione, come un relè temporizzato (sezione B.4.5).
// Ogni nuova accensione fa ripartire il conteggio; uno spegnimento
// manuale annulla il timer.

let DURATA_MS = 60 * 60 * 1000;   // 1 ora
let timer = null;

function annullaTimer() {
  if (timer !== null) {
    Timer.clear(timer);
    timer = null;
  }
}

Shelly.addStatusHandler(function (st) {
  if (st.component !== "switch:0" || st.delta.output === undefined) {
    return;
  }
  annullaTimer();
  if (st.delta.output === true) {
    timer = Timer.set(DURATA_MS, false, function () {
      timer = null;
      Shelly.call("Switch.Set", { id: 0, on: false });
      print("Carico spento per fine tempo");
    });
  }
});

print("Spegnimento automatico attivo:", DURATA_MS / 60000, "min");
