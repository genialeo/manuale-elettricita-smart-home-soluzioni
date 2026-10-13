# Capitolo 10 – Relè e dispositivi smart

*Soluzioni complete del capitolo 10 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 10.11. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 10.1 – Scaldacqua comandato da un relè smart

Lo scaldacqua è un carico resistivo, quindi la corrente si ricava dalla potenza con \(\cos\varphi = 1\).

Dati: \(P = 2000\,\mathrm{W}\); \(V = 230\,\mathrm{V}\); relè da 16 A.

\[ I_B = \frac{P}{V} = \frac{2000}{230} = 8{,}70\,\mathrm{A} \]

\[ \frac{I_B}{I_n} = \frac{8{,}70}{16} = 0{,}54 = 54\,\% \]

Il relè lavora al 54 % della corrente nominale, sotto la soglia prudente dell'80 % della tabella 10.2: dal punto di vista della corrente è adatto. Lo scaldacqua però funziona tre ore ogni notte, e la corrente scalda per ore il relè nella scatola. Un contattore modulare in categoria AC-7a, per esempio da 20 o 25 A, non è obbligatorio ma è consigliato (sezione 10.2.2). Il relè smart comanda allora solo la bobina, e il carico passa su contatti costruiti per quell'uso, come nello schema della figura 10.2.

## Esercizio 10.2 – Spunto di quattro alimentatori LED

La corrente di regime si calcola con il fattore di potenza degli alimentatori, il picco sommando i picchi dei singoli alimentatori.

Dati: \(P = 4 \cdot 60 = 240\,\mathrm{W}\); \(V = 230\,\mathrm{V}\); fattore di potenza 0,9; picco per alimentatore 25 A; picco ammesso dal relè 80 A.

\[ I_B = \frac{240}{230 \cdot 0{,}9} = 1{,}16\,\mathrm{A} \]

\[ I_{picco} = 4 \cdot 25 = 100\,\mathrm{A} \]

A regime il relè porta poco più di 1 A, ma all'accensione il picco può arrivare a 100 A, oltre gli 80 A ammessi: il relè non è adatto. Si può dividere il carico su due relè, ciascuno con due alimentatori e un picco di 50 A. In alternativa il relè smart comanda un contattore, oppure si sceglie un dispositivo con una corrente di spunto ammessa più alta.

## Esercizio 10.3 – Potenza dissipata nella scatola

La potenza dissipata nel percorso interno si calcola con \(P = I^2 \cdot R\); a questa si somma l'autoconsumo dell'elettronica.

Dati: \(R = 6\,\mathrm{m}\Omega = 0{,}006\,\mathrm{}\Omega\); autoconsumo 0,8 W.

Con 12 A:

\[ P = 12^2 \cdot 0{,}006 = 0{,}864\,\mathrm{W} \qquad P_{tot} = 0{,}864 + 0{,}8 = 1{,}66\,\mathrm{W} \]

Con 6 A:

\[ P = 6^2 \cdot 0{,}006 = 0{,}216\,\mathrm{W} \qquad P_{tot} = 0{,}216 + 0{,}8 = 1{,}02\,\mathrm{W} \]

Dimezzando la corrente, la potenza dissipata nel percorso si riduce a un quarto, da 0,86 W a 0,22 W, perché dipende dal quadrato della corrente. L'autoconsumo resta invece costante.

## Esercizio 10.4 – Punto luce a tre comandi e impulso per un cancello

Il relè smart si installa nella scatola dell'ultimo deviatore, quella da cui parte il ritorno di lampada, dove arriva anche il neutro. Basta un solo relè: deviatori e invertitore restano come sono (sezione 10.4.3).

I collegamenti sono questi: fase e neutro ai morsetti L e N; il comune dell'ultimo deviatore, che prima andava alla lampada, all'ingresso SW; il morsetto O al ritorno di lampada. Con un relè a contatto pulito si aggiunge il ponticello tra L e I. L'ingresso va impostato in modalità commutazione (*edge* o *flip*), così ogni manovra di uno qualunque dei tre comandi cambia lo stato della luce.

Per il cancello si usa un relè a contatto pulito, con I e O collegati all'ingresso di comando della centralina. Si imposta lo spegnimento automatico a 1 s, così ogni comando chiude il contatto per un secondo. La cautela riguarda il circuito a 24 V. Senza una separazione di protezione dichiarata dal costruttore del relè, quel circuito non si può più considerare SELV (sezione 10.3.3). I suoi conduttori, se passano nella scatola con quelli a 230 V, devono essere isolati per la tensione più alta.

## Esercizio 10.5 – Una giornata senza Internet

Caso a). Il relè Shelly risponde all'interruttore a parete e, se è attivo il controllo locale, all'app in casa. La pianificazione è salvata nel dispositivo e continua a funzionare; manca solo il comando da fuori casa, che passa dal cloud.

Caso b). Il relè Tuya risponde al comando a parete, ma l'automazione di Smart Life è eseguita nel cloud e non funziona. Anche il comando dall'app, di norma, passa dal cloud; solo alcuni dispositivi accettano il controllo in rete locale.

Caso c). Il relè Matter è comandato dal controller sulla rete di casa e continua a funzionare, comprese le automazioni eseguite dal controller locale. Non funzionano i comandi da fuori casa e le funzioni che dipendono da servizi cloud.

## Esercizio 10.6 – Consumo di uno scaldacqua

L'energia è il prodotto della potenza per il tempo di funzionamento (sezione 1.3.2).

Dati: \(P = 1200\,\mathrm{W} = 1{,}2\,\mathrm{kW}\); 3 ore al giorno per 30 giorni; prezzo 0,30 euro per kWh.

\[ E = 1{,}2 \cdot 3 \cdot 30 = 108\,\mathrm{kWh} \qquad C = 108 \cdot 0{,}30 = 32{,}40\ \text{euro} \]

Con 2,5 ore al giorno:

\[ E' = 1{,}2 \cdot 2{,}5 \cdot 30 = 90\,\mathrm{kWh} \qquad C' = 90 \cdot 0{,}30 = 27{,}00\ \text{euro} \]

Il risparmio è di 18 kWh al mese, pari a 5,40 euro. La misura del relè permette di verificarlo sul consumo reale, che dipende anche dalla temperatura dell'acqua e dall'uso.
