# Capitolo 8 – Realizzare, verificare, certificare

*Soluzioni complete del capitolo 8 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 8.11. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 8.1 – Resistenza di un picchetto e condizione di protezione

La stima rapida della resistenza di un picchetto (sezione 8.5.1) dà:

\[ R_A \approx \frac{\rho}{L} = \frac{150}{2} = 75\,\Omega \]

La formula completa di Dwight, con un diametro di 2 cm, darebbe circa 68 Ω: la stima è del 10 % più alta, quindi a favore della sicurezza.

Con il differenziale da 30 mA:

\[ R_A \cdot I_{\Delta n} = 75 \cdot 0{,}03 = 2{,}25\,\mathrm{V} \le 50\,\mathrm{V} \]

Con il differenziale da 300 mA:

\[ R_A \cdot I_{\Delta n} = 75 \cdot 0{,}3 = 22{,}5\,\mathrm{V} \le 50\,\mathrm{V} \]

La condizione è rispettata in entrambi i casi. Il valore stimato va comunque confermato con una misura a impianto finito.

## Esercizio 8.2 – Più differenziali sullo stesso impianto

La condizione va rispettata per ogni differenziale presente.

Per i differenziali da 30 mA:

\[ R_A \cdot I_{\Delta n} = 210 \cdot 0{,}03 = 6{,}3\,\mathrm{V} \le 50\,\mathrm{V} \]

La condizione è rispettata.

Per il differenziale generale da 300 mA:

\[ R_A \cdot I_{\Delta n} = 210 \cdot 0{,}3 = 63\,\mathrm{V} > 50\,\mathrm{V} \]

La condizione non è rispettata: con 300 mA la resistenza massima ammessa è \(50 / 0{,}3 = 167\,\Omega\).

Le soluzioni sono due. La prima è migliorare l'impianto di terra, per esempio aggiungendo picchetti o collegando le armature delle fondazioni, fino a scendere sotto 167 Ω. La seconda è scegliere per il generale una corrente differenziale più bassa: con un selettivo da 100 mA si ottiene \(210 \cdot 0{,}1 = 21\,\mathrm{V}\), che rispetta la condizione. La scelta spetta all'impresa e al progettista. In ogni caso 210 Ω è un valore alto per una terra domestica (sezione 8.5.4): migliorare il dispersore è la soluzione più robusta.

## Esercizio 8.3 – Sezioni minime dei conduttori di terra

I valori si ricavano dalla tabella 8.3.

Caso a). Il PE è nello stesso tubo della fase da 2,5 mm², che non supera 16 mm²: la sua sezione è uguale a quella della fase, cioè 2,5 mm².

Caso b). Il PE non fa parte di un cavo con la fase ed è protetto meccanicamente dalla canalina: la sezione minima è 2,5 mm².

Caso c). La fase del montante è da 10 mm², quindi fino a 16 mm²: il PE deve avere la stessa sezione, 10 mm².

Caso d). Il conduttore equipotenziale principale deve avere almeno 6 mm².

Caso e). Il conduttore di terra interrato in rame non protetto contro la corrosione deve avere almeno 25 mm².

## Esercizio 8.4 – Prova di isolamento

I valori minimi sono 1 MΩ per i circuiti fino a 500 V, provati a 500 V, e 0,5 MΩ per i circuiti SELV e PELV, provati a 250 V.

Circuito prese: 0,8 MΩ è inferiore a 1 MΩ. Il circuito non supera la prova.

Circuito luci: 45 MΩ è molto superiore a 1 MΩ. Il circuito supera la prova.

Circuito SELV: 0,6 MΩ è superiore a 0,5 MΩ. Il circuito supera la prova, anche se con poco margine.

Il valore basso del circuito prese può dipendere da un isolante danneggiato durante l'infilaggio, da umidità in una scatola appena murata o da un apparecchio rimasto collegato. Prima di cercare il guasto si controlla che nessun utilizzatore, SPD o dispositivo elettronico sia collegato al circuito. Poi si divide il circuito in tratti, aprendo le giunzioni nelle cassette, finché si trova il tratto difettoso.

## Esercizio 8.5 – Prova dei differenziali

Per un differenziale da 30 mA di tipo generale la corrente di intervento deve stare tra \(0{,}5 \cdot 30 = 15\,\mathrm{mA}\) e 30 mA. Con una corrente pari a 30 mA il tempo di intervento non deve superare 300 ms.

Primo differenziale. Interviene a 22 mA, compreso tra 15 e 30 mA, e con 30 mA apre in 28 ms, molto meno di 300 ms. Il risultato è regolare.

Secondo differenziale. Interviene a 9 mA, cioè meno di 15 mA. Il valore è anomalo: un differenziale integro non dovrebbe intervenire sotto metà della sua corrente nominale. La spiegazione più probabile è che nel circuito circoli già una corrente di dispersione verso terra, dovuta per esempio ad apparecchi elettronici collegati. Questa corrente si somma a quella dello strumento. Se, per esempio, circolano già 8 mA, con 9 mA di prova il differenziale vede \(8 + 9 = 17\,\mathrm{mA}\) e interviene regolarmente, ma lo strumento indica solo i 9 mA che ha aggiunto. Si ripete la prova con gli apparecchi scollegati. Se il valore resta sotto 15 mA, il differenziale è difettoso e va sostituito.

## Esercizio 8.6 – Impianto senza Dichiarazione di conformità

L'impianto è stato eseguito nel 1995, prima del 27 marzo 2008, data di entrata in vigore del DM 37/08. La Dichiarazione mancante può quindi essere sostituita da una Dichiarazione di rispondenza, rilasciata dopo un sopralluogo e gli accertamenti necessari.

L'appartamento ha 3 kW impegnati, non più di 6 kW, e 90 m², meno di 400 m². Non ricade quindi nei casi della sezione 7.1.1 che richiedono un professionista. La Dichiarazione di rispondenza può essere rilasciata da un professionista iscritto all'albo con almeno cinque anni di esperienza nel settore. In alternativa può rilasciarla chi ricopre da almeno cinque anni il ruolo di responsabile tecnico di un'impresa abilitata nel settore elettrico.
