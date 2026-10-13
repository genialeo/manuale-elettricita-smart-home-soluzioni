# Capitolo 9 – Domotica e smart home: concetti e protocolli

*Soluzioni complete del capitolo 9 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 9.9. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 9.1 – Le funzioni domotiche del Livello 3

Si confrontano i sistemi previsti con l'elenco delle funzioni della norma degli impianti (sezione 9.2.4).

- L'antintrusione con sensori sulle finestre è la funzione «antintrusione».
- Il relè di controllo dei carichi è la funzione «controllo carichi».
- I cronotermostati smart in ogni stanza sono la funzione «termoregolazione multizona».
- Il rilevatore di allagamento è la funzione «antiallagamento».
- Le tapparelle motorizzate con pulsanti tradizionali non sono una funzione domotica: il motore è comandato direttamente, senza automazioni né scenari.

Le funzioni presenti sono quattro, quindi il requisito numerico del Livello 3 è soddisfatto. Non basta però a classificare l'impianto: le funzioni devono essere integrate tra loro e interoperabili, progettate come sistema e dichiarate nel progetto. L'impianto deve inoltre rispettare tutte le altre dotazioni del Livello 3 (sezione 7.2). L'app dei cronotermostati permette anche il comando a distanza, ma il controllo da remoto non conta come funzione aggiuntiva.

## Esercizio 9.2 – Router intermedi in una rete Zigbee

Il numero minimo di collegamenti è la distanza divisa per la portata, arrotondata per eccesso; i router intermedi sono uno in meno dei collegamenti.

Dati: \(r = 10\,\mathrm{m}\); \(d_1 = 45\,\mathrm{m}\) (capanno); \(d_2 = 18\,\mathrm{m}\) (cantina).

Capanno:

\[ n_1 = \left\lceil \frac{45}{10} \right\rceil = \lceil 4{,}5 \rceil = 5 \quad \Rightarrow \quad 5 - 1 = 4 \text{ router} \]

Cantina:

\[ n_2 = \left\lceil \frac{18}{10} \right\rceil = \lceil 1{,}8 \rceil = 2 \quad \Rightarrow \quad 2 - 1 = 1 \text{ router} \]

Servono 4 router verso il capanno e 1 verso la cantina, alimentati da rete. Se il percorso esterno non offre punti alimentati, conviene una rete sub-GHz, come Z-Wave o Z-Wave Long Range, oppure un secondo coordinatore collegato in rete.

## Esercizio 9.3 – Durata della batteria: Zigbee e Wi-Fi

La corrente media è la media pesata delle correnti nei due stati, sul periodo di un minuto; la durata è la capacità divisa per la corrente media.

\[ I_m = \frac{I_{tx} \cdot t_{tx} + I_{rip} \cdot (T - t_{tx})}{T} \qquad t_{vita} = \frac{C}{I_m} \]

dove \(I_{tx}\) e \(t_{tx}\) sono corrente e durata della trasmissione, \(I_{rip}\) la corrente a riposo, \(T = 60\,\mathrm{s}\) il periodo e \(C\) la capacità della batteria.

Sensore Zigbee. Dati: \(I_{tx} = 20\,\mathrm{mA}\); \(t_{tx} = 4\,\mathrm{ms}\); \(I_{rip} = 2\,\mu\mathrm{A}\); \(C = 220\,\mathrm{mAh}\).

\[ I_m = \frac{20\,000\,\mu\mathrm{A} \cdot 0{,}004 + 2\,\mu\mathrm{A} \cdot 59{,}996}{60} = \frac{80 + 120}{60} = 3{,}33\,\mu\mathrm{A} \]

\[ t_{vita} = \frac{220\,\mathrm{mAh}}{0{,}00333\,\mathrm{mA}} = 66\,000\,\mathrm{h} \approx 7{,}5 \text{ anni} \]

Sensore Wi-Fi. Dati: \(I_{tx} = 120\,\mathrm{mA}\); \(t_{tx} = 1{,}5\,\mathrm{s}\); \(I_{rip} = 5\,\mu\mathrm{A}\); \(C = 5000\,\mathrm{mAh}\).

\[ I_m = \frac{120 \cdot 1{,}5 + 0{,}005 \cdot 58{,}5}{60} = \frac{180 + 0{,}29}{60} = 3{,}00\,\mathrm{mA} \]

\[ t_{vita} = \frac{5000\,\mathrm{mAh}}{3{,}00\,\mathrm{mA}} = 1664\,\mathrm{h} \approx 69 \text{ giorni} \]

Il sensore Wi-Fi consuma circa 900 volte di più, quasi tutto durante la connessione alla rete, e con una batteria oltre venti volte più grande dura poco più di due mesi. La durata teorica del sensore Zigbee è in realtà limitata dall'autoscarica della pila e dalle trasmissioni aggiuntive: nella pratica si ottengono di solito alcuni anni.

## Esercizio 9.4 – Bilancio di corrente di una linea KNX

Si calcola la corrente disponibile lasciando la riserva del 20 % e la si divide per l'assorbimento di un dispositivo.

Dati: \(I_{alim} = 640\,\mathrm{mA}\); riserva 20 %; \(I_{disp} = 10\,\mathrm{mA}\); massimo 64 dispositivi per linea.

\[ I_{utile} = 640 \cdot (1 - 0{,}20) = 512\,\mathrm{mA} \]

\[ N = \frac{512}{10} = 51{,}2 \quad \Rightarrow \quad N = 51 \text{ dispositivi} \]

Il numero si arrotonda per difetto. Prevale il limite di corrente: 51 dispositivi, meno dei 64 ammessi dalla linea. Per collegarne di più serve un alimentatore più grande, se la linea lo consente, oppure una seconda linea con il proprio alimentatore.

## Esercizio 9.5 – Topic e caratteri jolly in MQTT

Il carattere `+` sostituisce un solo livello del topic; il carattere `#` sostituisce tutti i livelli successivi.

- L'app, iscritta a `casa/+/temperatura`, riceve `casa/cucina/temperatura` e `casa/camera/temperatura`, ma non l'umidità.
- Il registratore, iscritto a `casa/#`, riceve tutti e tre i messaggi.
- Il termostato, iscritto a `casa/camera/+`, riceve solo `casa/camera/temperatura`, l'unico topic della camera.

Se in futuro un sensore pubblicasse su `casa/camera/umidita`, il termostato riceverebbe anche quel messaggio senza modificare l'iscrizione.

## Esercizio 9.6 – Carico minimo di un dimmer senza neutro

Il numero minimo di lampade è il carico minimo diviso per la potenza di una lampada, arrotondato per eccesso; il massimo è il carico massimo diviso per la stessa potenza, arrotondato per difetto.

Dati: carico ammesso 5-100 W; \(P_L = 4\,\mathrm{W}\).

\[ N_{min} = \left\lceil \frac{5}{4} \right\rceil = \lceil 1{,}25 \rceil = 2 \qquad N_{max} = \left\lfloor \frac{100}{4} \right\rfloor = 25 \]

Si possono comandare da 2 a 25 lampade da 4 W. Con una sola lampada il carico è di 4 W, sotto il minimo di 5 W. L'elettronica del dimmer, che si alimenta attraverso la lampada, può non funzionare correttamente: la lampada può sfarfallare o restare debolmente accesa quando è spenta. In questi casi si aggiunge una lampada oppure il compensatore di carico indicato dal produttore, o si sceglie la versione con neutro.
