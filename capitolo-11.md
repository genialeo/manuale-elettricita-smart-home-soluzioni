# Capitolo 11 – Home Assistant

*Soluzioni complete del capitolo 11 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 11.11. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 11.1 – Energia di un ciclo di lavaggio

L'energia di ogni fase è la potenza per la durata, con il tempo in ore (sezione 1.3.2): 15 minuti sono 0,25 h, 60 minuti 1 h, 10 minuti 0,167 h.

\[ E = 2000 \cdot 0{,}25 + 150 \cdot 1 + 400 \cdot \frac{10}{60} = 500 + 150 + 66{,}7 = 716{,}7\,\mathrm{Wh} \]

Il ciclo consuma circa 0,72 kWh. Il costo è:

\[ C = 0{,}717 \cdot 0{,}25 = 0{,}18\,\text{euro} \]

La soglia dell'automazione deve stare sopra il consumo in attesa, 1,5 W, e sotto la potenza più bassa del ciclo, cioè quella delle pause tra le fasi, di qualche decina di watt. Un valore tra 3 e 10 W è ragionevole; 5 W, con un ritardo di qualche minuto, evita sia i falsi avvisi durante le pause sia il mancato avviso a fine ciclo.

## Esercizio 11.2 – Distacco dei carichi

La potenza prelevata è la somma delle potenze dei carichi accesi:

\[ P = 0{,}3 + 2{,}8 + 1{,}2 = 4{,}3\,\mathrm{kW} \]

Con fattore di potenza unitario la corrente è:

\[ I = \frac{P}{V} = \frac{4300}{230} = 18{,}7\,\mathrm{A} \]

La potenza supera i 4 kW della soglia superiore (tabella 2.2): senza intervento il contatore stacca entro circa 2 minuti. Interviene quindi il primo innesco dell'automazione, quello con soglia 4000 W, dopo 20 s di superamento continuo, e spegne lo scaldabagno. Resta:

\[ P' = 0{,}3 + 2{,}8 = 3{,}1\,\mathrm{kW} \qquad I' = \frac{3100}{230} = 13{,}5\,\mathrm{A} \]

Il valore di 3,1 kW è sotto 3,3 kW: il prelievo torna nella fascia ammessa senza limiti di tempo, e il secondo innesco, che richiede un'ora sopra 3,3 kW, non scatta.

## Esercizio 11.3 – Autoconsumo e autosufficienza

L'energia autoconsumata è la produzione meno l'energia immessa:

\[ E_{auto} = 18{,}5 - 9{,}3 = 9{,}2\,\mathrm{kWh} \]

Il consumo della casa è la somma di prelievo e autoconsumo:

\[ E_{cons} = 7{,}4 + 9{,}2 = 16{,}6\,\mathrm{kWh} \]

Il tasso di autosufficienza, con la formula della sezione 11.4.3, è:

\[ T_{suff} = \frac{9{,}2}{16{,}6} = 55{,}4\,\% \]

Il tasso di autoconsumo, cioè la quota della produzione consumata in casa, è:

\[ T_{auto} = \frac{9{,}2}{18{,}5} = 49{,}7\,\% \]

Il fotovoltaico copre più di metà dei consumi, ma circa metà della produzione finisce in rete: spostare i carichi programmabili nelle ore di sole aumenterebbe entrambi gli indici.

## Esercizio 11.4 – Consumo del frigorifero

La potenza media è la media pesata sui tempi di funzionamento:

\[ P_m = 120 \cdot 0{,}35 + 2 \cdot 0{,}65 = 42 + 1{,}3 = 43{,}3\,\mathrm{W} \]

L'energia giornaliera è la potenza media per 24 ore:

\[ E_g = 43{,}3 \cdot 24 = 1039\,\mathrm{Wh} = 1{,}04\,\mathrm{kWh} \]

L'energia annua è:

\[ E_a = 1{,}039 \cdot 365 = 379\,\mathrm{kWh} \]

Il frigorifero assorbe solo 120 W, ma restando sempre collegato consuma in un anno circa 380 kWh. È l'esempio tipico della differenza tra potenza ed energia vista nella sezione 1.3.

## Esercizio 11.5 – Spazio dei backup e regola 3-2-1

Lo spazio occupato è il numero di backup per la dimensione di ciascuno:

\[ S_{loc} = 7 \cdot 350 = 2450\,\mathrm{MB} = 2{,}45\,\mathrm{GB} \qquad S_{NAS} = 14 \cdot 350 = 4900\,\mathrm{MB} = 4{,}9\,\mathrm{GB} \]

Home Assistant Cloud conserva un solo backup, di 350 MB, ben sotto il limite di 5 GB.

Per la regola 3-2-1 servono tre copie, su due supporti diversi, di cui una fuori casa. Le copie sono la configurazione in uso, i backup sul NAS e quello in cloud. I backup locali stanno sullo stesso disco della configurazione: proteggono dagli errori di configurazione, ma non da un guasto del disco, e non contano come supporto diverso. I supporti diversi sono il disco dell'hub e quello del NAS, e la copia fuori casa è quella in cloud: il piano rispetta la regola.

La chiave di cifratura va conservata fuori da Home Assistant, per esempio stampata e in un gestore di password. Senza la chiave nessuno dei backup cifrati si può ripristinare.

## Esercizio 11.6 – Aggiornare un'automazione

Le chiavi superate sono `trigger` e `action` al singolare, `platform:` dentro l'innesco e `service:` dentro l'azione. Anche `entity_id` scritto direttamente sotto l'azione va spostato in `target`, e il parametro `color_temp`, in mired, è superato: oggi si usa `color_temp_kelvin`. Nel file `automations.yaml` l'elenco inizia direttamente con il trattino, senza la chiave `automation:`.

La temperatura di colore in kelvin si ottiene dividendo un milione per i mired:

\[ T = \frac{1\,000\,000}{250} = 4000\,\mathrm{K} \]

La versione aggiornata, con la condizione sullo stato del sole, è:

```yaml
- alias: "Luce ingresso"
  triggers:
    - trigger: state
      entity_id: person.anna
      to: "home"
  conditions:
    - condition: state           # solo se il sole è tramontato
      entity_id: sun.sun
      state: "below_horizon"
  actions:
    - action: light.turn_on
      target:
        entity_id: light.ingresso
      data:
        color_temp_kelvin: 4000  # bianco neutro
```

L'automazione ora accende la luce dell'ingresso quando Anna rientra, ma solo dopo il tramonto.
