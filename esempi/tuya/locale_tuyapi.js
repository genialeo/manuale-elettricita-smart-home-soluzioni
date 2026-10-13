// locale_tuyapi.js – Controllo locale di un dispositivo Tuya Wi-Fi con
// TuyAPI per Node.js (sezione B.8.4).
// Requisiti: Node.js 22+, npm install tuyapi
// ID, IP, local key e versione si ricavano come per TinyTuya.
// Uso: node locale_tuyapi.js <ID> <IP> <LOCAL_KEY> <VERSIONE> [on|off]

const TuyAPI = require('tuyapi');

const [id, ip, key, version, comando] = process.argv.slice(2);
if (!version) {
  console.error('Uso: node locale_tuyapi.js <ID> <IP> <LOCAL_KEY> <VERSIONE> [on|off]');
  process.exit(1);
}

const presa = new TuyAPI({ id, ip, key, version });

presa.on('connected', () => console.log('Connesso'));
presa.on('disconnected', () => console.log('Disconnesso'));
presa.on('error', (err) => console.error('Errore:', err.message));
presa.on('data', (dati) => console.log('Data point:', JSON.stringify(dati.dps)));

async function main() {
  await presa.find();          // verifica che il dispositivo risponda
  await presa.connect();
  if (comando) {
    await presa.set({ dps: 1, set: comando === 'on' });   // dps 1 = uscita
  }
  setTimeout(() => presa.disconnect(), 3000);
}

main().catch((err) => {
  console.error('Errore:', err.message);
  presa.disconnect();
});
