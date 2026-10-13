# Capitolo 6 – Le protezioni

*Soluzioni complete del capitolo 6 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 6.11. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 6.1 – Magnetotermico per il circuito del forno

La corrente di impiego del forno, con \(\cos\varphi = 1\), è:

\[ I_B = \frac{P}{V} = \frac{2800}{230} = 12{,}2\,\mathrm{A} \]

La prima condizione chiede \(12{,}2\,\mathrm{A} \le I_n \le 24\,\mathrm{A}\). Il 10 A è escluso perché è minore della corrente di impiego; il 25 A è escluso perché supera la portata del cavo. Restano 16 A e 20 A: si sceglie il 16 A, che lascia margine al cavo ed è il valore più comune per questo tipo di circuito.

La seconda condizione, con \(I_f = 1{,}45 \cdot I_n\) per un interruttore conforme alla CEI EN 60898-1, è:

\[ I_f = 1{,}45 \cdot 16 = 23{,}2\,\mathrm{A} \le 1{,}45 \cdot I_z = 1{,}45 \cdot 24 = 34{,}8\,\mathrm{A} \]

Anche la seconda condizione è rispettata, come atteso, perché \(I_n \le I_z\).

Le correnti convenzionali dell'interruttore da 16 A sono:

\[ I_{nf} = 1{,}13 \cdot 16 = 18{,}1\,\mathrm{A} \qquad I_f = 1{,}45 \cdot 16 = 23{,}2\,\mathrm{A} \]

Fino a 18,1 A l'interruttore non interviene entro un'ora; a 23,2 A interviene entro un'ora.

## Esercizio 6.2 – Comportamento di un interruttore C16

Per ogni corrente si calcola il multiplo \(I/I_n\) con \(I_n = 16\,\mathrm{A}\) e lo si confronta con i punti della tabella 6.1.

15 A: \(15 / 16 = 0{,}94\,I_n\). È sotto 1,13 \(I_n\) (18,1 A): l'interruttore non interviene.

30 A: \(30 / 16 = 1{,}88\,I_n\). È oltre 1,45 \(I_n\) (23,2 A) e sotto la soglia magnetica: interviene lo sganciatore termico. La norma garantisce l'intervento entro un'ora; poiché la corrente è inferiore a 2,55 \(I_n\) (40,8 A), il tempo tipico è di decine di secondi o qualche minuto.

60 A: \(60 / 16 = 3{,}75\,I_n\). È sotto il limite inferiore della curva C (5 \(I_n\) = 80 A), quindi il magnetico non interviene. Interviene il termico; poiché la corrente supera 2,55 \(I_n\), il tempo è inferiore a 60 s, tipicamente qualche secondo.

120 A: \(120 / 16 = 7{,}5\,I_n\). È nella zona tra 5 e 10 \(I_n\) (80-160 A): l'intervento magnetico è possibile ma non garantito. Se il magnetico non interviene, interviene comunque il termico in qualche secondo.

400 A: \(400 / 16 = 25\,I_n\). È oltre 10 \(I_n\) (160 A): lo sganciatore magnetico interviene con certezza in meno di 0,1 s.

## Esercizio 6.3 – Potere di interruzione in una fornitura monofase

Il generale è subito a valle del contatore. Per una fornitura monofase la CEI 0-21 fissa una corrente di cortocircuito convenzionale di 6 kA al punto di consegna. Il potere di interruzione minimo è quindi 6 kA; un 4,5 kA non è adatto, un 10 kA va bene ma supera il minimo.

Nel quadro d'appartamento la corrente di cortocircuito calcolata è 2,8 kA. Basta un potere di interruzione di 4,5 kA:

\[ I_{cn} = 4{,}5\,\mathrm{kA} \ge I_{cc} = 2{,}8\,\mathrm{kA} \]

Per un interruttore con \(I_{cn} = 10\,\mathrm{kA}\) la CEI EN 60898-1 fissa \(I_{cs} = 0{,}75 \cdot I_{cn}\), con un minimo di 6 kA:

\[ I_{cs} = 0{,}75 \cdot 10\,000 = 7500\,\mathrm{A} = 7{,}5\,\mathrm{kA} \]

Fino a 7,5 kA l'interruttore resta pienamente funzionante dopo l'interruzione; tra 7,5 e 10 kA interrompe in sicurezza, ma può dover essere sostituito.

## Esercizio 6.4 – Coordinamento con la terra in un'azienda agricola

Per l'abitazione, con \(U_L = 50\,\mathrm{V}\):

\[ R_A \cdot I_{\Delta n} = 95 \cdot 0{,}03 = 2{,}85\,\mathrm{V} \le 50\,\mathrm{V} \]

La condizione è rispettata con ampio margine.

Per la stalla, con \(U_L = 25\,\mathrm{V}\) (CEI 64-8, sezione 705):

\[ R_A \cdot I_{\Delta n} = 95 \cdot 0{,}3 = 28{,}5\,\mathrm{V} > 25\,\mathrm{V} \]

La condizione non è rispettata. La resistenza di terra massima ammessa con il 300 mA è:

\[ R_A \le \frac{U_L}{I_{\Delta n}} = \frac{25}{0{,}3} = 83{,}3\,\Omega \]

Le soluzioni possibili sono due: migliorare l'impianto di terra fino a meno di 83 Ω, oppure proteggere la stalla con un differenziale di soglia più bassa. Con un 100 mA, per esempio, si ottiene \(95 \cdot 0{,}1 = 9{,}5\,\mathrm{V} \le 25\,\mathrm{V}\).

## Esercizio 6.5 – Selettività tra 300 mA e 30 mA

Dispersione di 90 mA. Per il 30 mA vale \(90 / 30 = 3\,I_{\Delta n}\): il dispositivo interviene, al più tardi entro 150 ms, perché la corrente supera 2 \(I_{\Delta n}\). Per il 300 mA vale \(90 / 300 = 0{,}3\,I_{\Delta n}\), meno di 0,5 \(I_{\Delta n}\): il generale non deve intervenire, sia di tipo generale sia di tipo S. In entrambi i casi interviene solo il 30 mA.

Dispersione di 600 mA. Per il 30 mA vale \(600 / 30 = 20\,I_{\Delta n}\): interviene entro 40 ms. Per il 300 mA vale \(600 / 300 = 2\,I_{\Delta n}\).

Con il generale di tipo generale la norma fissa solo il tempo massimo, 150 ms, e nessun tempo minimo. I tempi reali dei due dispositivi sono simili, di qualche decina di millisecondi, quindi possono intervenire entrambi: la selettività non è garantita.

Con il generale di tipo S, a 2 \(I_{\Delta n}\) il tempo minimo di non intervento è 60 ms. Il 30 mA apre entro 40 ms, prima che il tipo S possa intervenire, e il guasto è eliminato. Interviene solo il 30 mA: la selettività è garantita.

## Esercizio 6.6 – Lunghezza dei collegamenti di un SPD

Con 1 kV per metro di collegamento, la tensione all'apparecchio è circa \(U_p + \Delta U_{cavi}\).

\[ U_{0{,}35} \approx 1{,}3 + 0{,}35 = 1{,}65\,\mathrm{kV} \qquad U_{1{,}4} \approx 1{,}3 + 1{,}4 = 2{,}7\,\mathrm{kV} \]

Con 35 cm la tensione, 1,65 kV, è inferiore ai 2,5 kV della categoria II, quindi gli elettrodomestici sono protetti. Supera però gli 1,5 kV della categoria I.

Con 1,4 m la tensione, 2,7 kV, supera anche la tenuta della categoria II: il collegamento va rifatto, riportando la lunghezza totale entro 50 cm. In alternativa la CEI 64-8 ammette un SPD con \(U_p\) più basso o un secondo SPD vicino agli apparecchi (sezione 6.7.5).

Per un apparecchio di categoria I non basta l'SPD del quadro. Si aggiunge un SPD di tipo 3 vicino all'apparecchio, con un livello di protezione adeguato alla sua tenuta, come indicato dal costruttore. La stessa soluzione serve se l'apparecchio è lontano più di circa 10 m di cavo dal quadro.
