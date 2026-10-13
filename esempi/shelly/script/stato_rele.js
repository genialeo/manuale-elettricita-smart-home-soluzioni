// stato_rele.js – Legge e stampa lo stato del relè 0 (sezione B.4.3).
// Dispositivi: Shelly Gen2, Gen3, Gen4 con componente switch e misura di potenza
// (per esempio 1PM Mini Gen3). Sui modelli senza misura alcuni campi mancano.

let stato = Shelly.getComponentStatus("switch:0");

if (stato) {
  print("Uscita accesa:", stato.output);
  print("Potenza attiva:", stato.apower, "W");
  print("Tensione:", stato.voltage, "V");
  print("Corrente:", stato.current, "A");
} else {
  print("Componente switch:0 non trovato");
}
