// luci_in_sequenza.js – Script per lo Shelly del corridoio (sezione B.4.8).
// Quando il relè 0 del corridoio si accende, accende in sequenza due luci
// comandate da dimmer Shelly Gen2+ (componente light) in altre stanze.
// Sostituire <IP_SOGGIORNO> e <IP_CAMERA> con gli indirizzi dei dimmer.
// Se i dimmer sono protetti da password: "http://admin:<PASSWORD>@<IP>".

let LUCI = [
  { nome: "soggiorno", base: "http://<IP_SOGGIORNO>", luce: 80, fade: 2, ritardo: 500 },
  { nome: "camera", base: "http://<IP_CAMERA>", luce: 50, fade: 1.5, ritardo: 1000 }
];

function accendi(l) {
  let url = l.base + "/rpc/Light.Set?id=0&on=true&brightness=" + l.luce +
    "&transition_duration=" + l.fade;
  Shelly.call("HTTP.GET", { url: url, timeout: 5 }, function (r, codice, msg) {
    if (codice !== 0) {
      print("Errore", l.nome + ":", msg);
    }
  });
}

Shelly.addStatusHandler(function (st) {
  if (st.component === "switch:0" && st.delta.output === true) {
    print("Corridoio acceso: avvio la sequenza");
    for (let i = 0; i < LUCI.length; i++) {
      // userdata (quarto argomento) passa a ogni timer la sua luce
      Timer.set(LUCI[i].ritardo, false, accendi, LUCI[i]);
    }
  }
});
