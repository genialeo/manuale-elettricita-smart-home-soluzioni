// eventi.js – Mostra in console gli eventi di tutti i componenti e le
// variazioni di stato del relè 0 (sezione B.4.4).
// - addEventHandler riceve gli eventi (pressione di un pulsante, toggle, ...):
//   i pulsanti arrivano dal componente input:0, il relè da switch:0
// - addStatusHandler riceve le variazioni di stato (campo delta)

let RELE = "switch:0";

Shelly.addEventHandler(function (ev) {
  if (ev.info && ev.info.event) {
    print("Evento:", ev.component, ev.info.event);
  }
});

Shelly.addStatusHandler(function (st) {
  // st.delta contiene solo i campi cambiati
  if (st.component === RELE && st.delta.output !== undefined) {
    print("Relè", st.delta.output ? "ACCESO" : "SPENTO",
      "(origine:", st.delta.source, ")");
  }
});

print("Monitoraggio avviato");
