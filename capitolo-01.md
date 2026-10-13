# Capitolo 1 – Le grandezze elettriche

*Soluzioni complete del capitolo 1 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 1.11. I risultati sono arrotondati alla seconda cifra decimale; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 1.1 – Corrente di una lavatrice

Con fattore di potenza pari a 1 la corrente si ricava dalla formula della potenza, \(P = V \cdot I\).

Dati: \(P = 2200\,\mathrm{W}\); \(V = 230\,\mathrm{V}\); \(\cos\varphi = 1\).

\[ I = \frac{P}{V} = \frac{2200}{230} = 9{,}57\,\mathrm{A} \]

La lavatrice assorbe circa 9,6 A. In un circuito prese protetto a 16 A resta un margine di circa 6 A per altri apparecchi.

## Esercizio 1.2 – Resistenza di un asciugacapelli

Si considera l'asciugacapelli come un carico resistivo e si usa la formula \(P = V^2/R\), ricavando la resistenza.

Dati: \(P = 1800\,\mathrm{W}\); \(V = 230\,\mathrm{V}\).

\[ R = \frac{V^2}{P} = \frac{230^2}{1800} = \frac{52\,900}{1800} = 29{,}39\,\Omega \]

Il valore vale a caldo, cioè con la resistenza alla temperatura di funzionamento. Misurata a freddo con il multimetro, la resistenza risulta un po' più bassa.

## Esercizio 1.3 – Costo mensile di un apparecchio

Si calcola l'energia consumata in 30 giorni e la si moltiplica per il prezzo del kWh.

Dati: \(P = 150\,\mathrm{W}\); 8 h al giorno per 30 giorni; prezzo 0,30 euro/kWh.

Ore di funzionamento in un mese: \(t = 8 \cdot 30 = 240\,\mathrm{h}\).

\[ E = P \cdot t = 150 \cdot 240 = 36\,000\,\mathrm{Wh} = 36\,\mathrm{kWh} \]

\[ \text{Costo} = 36\,\mathrm{kWh} \cdot 0{,}30\,\mathrm{euro/kWh} = 10{,}80\,\mathrm{euro} \]

Il calcolo comprende solo la quota energia; la bolletta reale comprende anche quote fisse, quota potenza e imposte.

## Esercizio 1.4 – Due apparecchi sulla stessa presa

I due apparecchi sono in parallelo: hanno la stessa tensione e le loro correnti si sommano. Si calcola la corrente di ciascuno con la formula della potenza, poi la corrente totale con la legge dei nodi e infine la resistenza equivalente con la legge di Ohm.

Dati: \(P_1 = 2000\,\mathrm{W}\); \(P_2 = 800\,\mathrm{W}\); \(V = 230\,\mathrm{V}\).

Correnti dei due apparecchi:

\[ I_1 = \frac{2000}{230} = 8{,}70\,\mathrm{A} \qquad I_2 = \frac{800}{230} = 3{,}48\,\mathrm{A} \]

Corrente totale nella presa, per la legge dei nodi:

\[ I = I_1 + I_2 = 8{,}70 + 3{,}48 = 12{,}17\,\mathrm{A} \]

Lo stesso risultato si ottiene dalla potenza totale: \(2800/230 = 12{,}17\,\mathrm{A}\).

Resistenza equivalente dei due apparecchi, vista dalla presa:

\[ R_{eq} = \frac{V}{I} = \frac{230}{12{,}17} = 18{,}89\,\Omega \]

Controllo con la formula del parallelo. Le resistenze dei due apparecchi sono \(R_1 = 230^2/2000 = 26{,}45\,\Omega\) e \(R_2 = 230^2/800 = 66{,}13\,\Omega\), quindi:

\[ R_{eq} = \frac{26{,}45 \cdot 66{,}13}{26{,}45 + 66{,}13} = 18{,}89\,\Omega \]

Come previsto, la resistenza equivalente è minore di quella di ciascun apparecchio.

## Esercizio 1.5 – Caduta di tensione su una linea da 2,5 mm²

In monofase la corrente percorre sia la fase sia il neutro, quindi la lunghezza del conduttore è il doppio della distanza.

Dati: \(I = 13\,\mathrm{A}\); \(L = 25\,\mathrm{m}\); \(S = 2{,}5\,\mathrm{mm^2}\); \(\rho = 0{,}0178\,\Omega\cdot\mathrm{mm^2/m}\) a 20 °C.

Resistenza della linea, andata e ritorno:

\[ R = \frac{2 \cdot \rho \cdot L}{S} = \frac{2 \cdot 0{,}0178 \cdot 25}{2{,}5} = 0{,}356\,\Omega \]

Caduta di tensione:

\[ \Delta V = I \cdot R = 13 \cdot 0{,}356 = 4{,}63\,\mathrm{V} \]

\[ \Delta V\,\% = \frac{4{,}63}{230} \cdot 100 = 2{,}01\,\% \]

La caduta è inferiore al 4 % raccomandato dalla norma degli impianti. A temperatura di esercizio, 70 °C, con \(\rho \approx 0{,}0213\,\Omega\cdot\mathrm{mm^2/m}\), la resistenza sale a 0,426 Ω e la caduta a 5,54 V, pari al 2,41 %: il valore resta comunque sotto il 4 %. Se la linea parte da un quadro già lontano dal contatore, la caduta va sommata a quella della linea a monte.

## Esercizio 1.6 – Le potenze di un motore monofase

Si calcolano nell'ordine la corrente di impiego, la potenza apparente e la potenza reattiva.

Dati: \(P = 2000\,\mathrm{W}\); \(V = 230\,\mathrm{V}\); \(\cos\varphi = 0{,}85\).

Corrente di impiego:

\[ I_B = \frac{P}{V \cdot \cos\varphi} = \frac{2000}{230 \cdot 0{,}85} = 10{,}23\,\mathrm{A} \]

Potenza apparente:

\[ S = \frac{P}{\cos\varphi} = \frac{2000}{0{,}85} = 2353\,\mathrm{VA} \]

Lo stesso valore si ottiene da \(S = V \cdot I_B = 230 \cdot 10{,}23 = 2353\,\mathrm{VA}\).

Potenza reattiva:

\[ Q = \sqrt{S^2 - P^2} = \sqrt{2353^2 - 2000^2} = 1239\,\mathrm{var} \]

In alternativa, \(Q = P \cdot \tan\varphi = 2000 \cdot 0{,}620 = 1239\,\mathrm{var}\). Con fattore di potenza unitario la stessa potenza attiva richiederebbe 8,70 A: il motore assorbe circa 1,5 A in più per lo scambio di energia reattiva.

## Esercizio 1.7 – Riduzione al circuito equivalente

Si riduce il circuito un passo alla volta, come nella sezione 1.4.2: prima il parallelo, poi la serie. Dalla corrente del generatore si ricavano infine le correnti dei due rami con il partitore di corrente.

Dati: \(V = 12\,\mathrm{V}\); \(R_1 = 4\,\Omega\); \(R_2 = 12\,\Omega\); \(R_3 = 6\,\Omega\).

Passo 1: \(R_2\) e \(R_3\) sono collegate tra gli stessi due punti, quindi sono in parallelo.

\[ R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} = \frac{12 \cdot 6}{12 + 6} = 4\,\Omega \]

Passo 2: restano in serie \(R_1\) e \(R_{23}\).

\[ R_{eq} = R_1 + R_{23} = 4 + 4 = 8\,\Omega \qquad I = \frac{V}{R_{eq}} = \frac{12}{8} = 1{,}5\,\mathrm{A} \]

Tensione ai capi del parallelo:

\[ V_{23} = R_{23} \cdot I = 4 \cdot 1{,}5 = 6\,\mathrm{V} \]

Correnti nei due rami, con il partitore di corrente:

\[ I_2 = \frac{R_3}{R_2 + R_3} \cdot I = \frac{6}{18} \cdot 1{,}5 = 0{,}5\,\mathrm{A} \qquad I_3 = \frac{R_2}{R_2 + R_3} \cdot I = \frac{12}{18} \cdot 1{,}5 = 1\,\mathrm{A} \]

Controllo con la legge di Ohm: \(6/12 = 0{,}5\,\mathrm{A}\) e \(6/6 = 1\,\mathrm{A}\). La somma, 1,5 A, è la corrente del generatore, come vuole la legge dei nodi. La corrente maggiore passa nella resistenza più piccola.
