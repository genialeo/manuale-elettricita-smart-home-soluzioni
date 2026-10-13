# Capitolo 4 – Dimensionare e posare le condutture

*Soluzioni complete del capitolo 4 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 4.9. Le portate sono quelle della tabella 4.2 (metodo B1, 30 °C), i fattori di correzione quelli delle tabelle 4.3 e 4.4. Le cadute di tensione si calcolano con \(\rho = 0{,}0213\,\Omega\cdot\mathrm{mm^2/m}\) e i valori di \(k\) della tabella 4.5.

## Esercizio 4.1 – Il circuito dello scaldabagno

Si calcola la corrente di impiego e si verificano le due condizioni della sezione 4.3.1.

Dati: \(P = 1200\,\mathrm{W}\); \(\cos\varphi = 1\); cavo da 2,5 mm² in PVC, da solo nel tubo, 30 °C, quindi \(I_z = 24\,\mathrm{A}\); \(I_n = 16\,\mathrm{A}\).

\[ I_B = \frac{1200}{230} = 5{,}22\,\mathrm{A} \]

Prima condizione: \(5{,}22 \le 16 \le 24\,\mathrm{A}\), rispettata.

Seconda condizione, con \(I_f = 1{,}45 \cdot I_n\) per un magnetotermico per uso domestico (sezione 4.3.2):

\[ I_f = 1{,}45 \cdot 16 = 23{,}2\,\mathrm{A} \le 1{,}45 \cdot 24 = 34{,}8\,\mathrm{A} \]

Anche la seconda condizione è rispettata, come accade sempre con questi interruttori quando \(I_n \le I_z\). Sarebbe accettabile anche un interruttore da 10 A, che lascia comunque un margine ampio sulla corrente di impiego.

## Esercizio 4.2 – Tre circuiti in un sottotetto caldo

Si applicano i fattori \(k_1\) per 40 °C e \(k_2\) per 3 circuiti.

Dati: \(k_2 = 0{,}70\); \(k_1 = 0{,}87\) per il PVC e \(0{,}91\) per l'EPR; \(I_0 = 24\,\mathrm{A}\) per il PVC e \(31\,\mathrm{A}\) per l'EPR.

Cavi in PVC:

\[ I_z = 24 \cdot 0{,}87 \cdot 0{,}70 = 14{,}6\,\mathrm{A} \]

Cavi in EPR:

\[ I_z = 31 \cdot 0{,}91 \cdot 0{,}70 = 19{,}7\,\mathrm{A} \]

Con il PVC la corrente nominale più alta ammessa è 13 A: 16 A supererebbe la portata. Con l'EPR si può arrivare a 16 A, mentre 20 A resta escluso. In pratica, in un ambiente caldo e con più circuiti raggruppati conviene un cavo con isolamento a 90 °C oppure una sezione maggiore.

## Esercizio 4.3 – La linea prese della cucina

Si calcola la caduta di tensione con le due sezioni e la si somma a quella del montante.

Dati: \(I = 16\,\mathrm{A}\); \(L = 25\,\mathrm{m}\); \(k = 28{,}40\,\mathrm{mV/(A \cdot m)}\) per 1,5 mm² e \(17{,}04\,\mathrm{mV/(A \cdot m)}\) per 2,5 mm²; caduta del montante 1 %.

Con 1,5 mm²:

\[ \Delta V = \frac{28{,}40 \cdot 16 \cdot 25}{1000} = 11{,}36\,\mathrm{V} \qquad \frac{11{,}36}{230} \cdot 100 = 4{,}94\,\% \]

La sola linea supera il 4 %; con il montante si arriva al 5,94 %.

Con 2,5 mm²:

\[ \Delta V = \frac{17{,}04 \cdot 16 \cdot 25}{1000} = 6{,}82\,\mathrm{V} \qquad \frac{6{,}82}{230} \cdot 100 = 2{,}96\,\% \]

Con il montante il totale è 3,96 %, appena sotto il 4 % raccomandato. Il calcolo assume 16 A per tutta la lunghezza della linea, e questo è prudente. Si basa però sulla sezione nominale: con la resistenza reale delle corde di classe 5 (sezione 4.4.3) il totale può superare di poco il 4 %. Con un margine così ridotto conviene quindi passare a 4 mm².

Seconda domanda. Con un secondo circuito nel tubo \(k_2 = 0{,}80\), e per 1,5 mm²:

\[ I_z = 17{,}5 \cdot 0{,}80 = 14{,}0\,\mathrm{A} < 16\,\mathrm{A} \]

La condizione \(I_n \le I_z\) non è rispettata: 1,5 mm² protetti a 16 A sono ammessi solo con portata piena, senza altri circuiti nel tubo. Per le prese la buona pratica è 2,5 mm².

## Esercizio 4.4 – La linea di una pompa di calore trifase

Si usa la formula trifase della sezione 4.4.2, nella quale il \(\sqrt{3}\) si è già semplificato.

Dati: \(P = 6000\,\mathrm{W}\); \(L = 40\,\mathrm{m}\); \(V = 400\,\mathrm{V}\); \(\Delta V = 0{,}02 \cdot 400 = 8\,\mathrm{V}\); \(\cos\varphi = 0{,}9\).

\[ S = \frac{\rho \cdot L \cdot P}{\Delta V \cdot V} = \frac{0{,}0213 \cdot 40 \cdot 6000}{8 \cdot 400} = 1{,}60\,\mathrm{mm^2} \]

La sezione commerciale immediatamente superiore è 2,5 mm². Con la formula errata, con \(\sqrt{3}\) al numeratore, si sarebbe ottenuto \(1{,}60 \cdot 1{,}732 = 2{,}77\,\mathrm{mm^2}\), e quindi 4 mm² senza motivo.

Controllo con la corrente di linea:

\[ I = \frac{P}{\sqrt{3} \cdot V \cdot \cos\varphi} = \frac{6000}{1{,}732 \cdot 400 \cdot 0{,}9} = 9{,}62\,\mathrm{A} \]

\[ \Delta V = \frac{\sqrt{3} \cdot \rho \cdot L \cdot I \cdot \cos\varphi}{S} = \frac{1{,}732 \cdot 0{,}0213 \cdot 40 \cdot 9{,}62 \cdot 0{,}9}{2{,}5} = 5{,}11\,\mathrm{V} \]

\[ \frac{5{,}11}{400} \cdot 100 = 1{,}28\,\% \]

La caduta resta sotto il 2 %. Con tre conduttori caricati la portata del 2,5 mm² in tubo è 21 A. La condizione \(I_B \le I_n \le I_z\) è quindi rispettata con un interruttore da 10 A o da 16 A, quadripolare se la linea porta il neutro, tripolare se non lo porta.

## Esercizio 4.5 – Tenuta al cortocircuito di un cavo da 1,5 mm²

Si confronta l'energia lasciata passare dall'interruttore con quella sopportata dal cavo.

Dati: \(K = 115\) (rame, PVC); \(S = 1{,}5\,\mathrm{mm^2}\); \(I^2 t = 15\,000\,\mathrm{A^2 \cdot s}\); \(I = 2000\,\mathrm{A}\).

\[ K^2 S^2 = 115^2 \cdot 1{,}5^2 = 29\,756\,\mathrm{A^2 \cdot s} \]

Poiché \(15\,000 \le 29\,756\,\mathrm{A^2 \cdot s}\), la condizione è rispettata.

Durata massima di un cortocircuito da 2000 A:

\[ t = \left( \frac{K \cdot S}{I} \right)^2 = \left( \frac{115 \cdot 1{,}5}{2000} \right)^2 = 0{,}0074\,\mathrm{s} = 7{,}4\,\mathrm{ms} \]

Un cavo da 1,5 mm² sopporta 2000 A per meno di un centesimo di secondo. Per questo le piccole sezioni si proteggono solo con dispositivi che limitano l'energia, come i magnetotermici modulari, e la verifica si fa sulla curva del costruttore.

## Esercizio 4.6 – Cavi da 1,5 mm² nei corrugati

Il cerchio circoscritto può essere al massimo \(D_i / f\), con \(f = 1{,}5\) oppure 1,3; diviso per il diametro del cavo, 3,4 mm, dà il numero di diametri disponibili. Si confronta con i rapporti del cerchio circoscritto: 2,41 per 4 cavi, 2,70 per 5, 3,00 per 6 e 7, 3,30 per 8, 3,61 per 9, 3,92 per 11, 4,03 per 12.

Tubo Ø20, diametro interno 13,6 mm:

- con \(f = 1{,}5\): \(13{,}6 / 1{,}5 = 9{,}07\,\mathrm{mm}\), cioè 2,67 diametri; entrano 4 cavi, perché 5 richiederebbero 2,70;
- con \(f = 1{,}3\): \(13{,}6 / 1{,}3 = 10{,}46\,\mathrm{mm}\), cioè 3,08 diametri; entrano 7 cavi, perché 8 richiederebbero 3,30.

Tubo Ø25, diametro interno 17,7 mm:

- con \(f = 1{,}5\): \(17{,}7 / 1{,}5 = 11{,}8\,\mathrm{mm}\), cioè 3,47 diametri; entrano 8 cavi, perché 9 richiederebbero 3,61;
- con \(f = 1{,}3\): \(17{,}7 / 1{,}3 = 13{,}62\,\mathrm{mm}\), cioè 4,005 diametri; entrano 11 cavi, perché 12 richiederebbero 4,03.

La regola delle abitazioni riduce di circa un terzo il numero di cavi ammessi. Un tubo Ø20 accoglie un circuito luci da 1,5 mm² con fase, neutro, conduttore di protezione e un ritorno di lampada, ma non due circuiti completi.
