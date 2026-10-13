# Capitolo 12 – Progettare la casa connessa

*Soluzioni complete del capitolo 12 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 12.10. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 12.1 – Autonomia dell'UPS

La potenza assorbita dagli apparati è la somma delle singole potenze:

\[ P = 6 + 10 + 8 + 4 = 28\,\mathrm{W} \]

L'energia utilizzabile della batteria, tenendo conto del rendimento e della frazione utilizzabile, vale:

\[ E = V_b \cdot C \cdot \eta \cdot k = 12 \cdot 9 \cdot 0{,}85 \cdot 0{,}8 = 73{,}4\,\mathrm{Wh} \]

L'autonomia è il rapporto tra energia utilizzabile e potenza:

\[ t = \frac{73{,}4}{28} = 2{,}62\,\mathrm{h} \]

cioè circa 2 ore e 37 minuti. Con la telecamera la potenza sale a 34 W:

\[ t = \frac{73{,}4}{34} = 2{,}16\,\mathrm{h} \]

cioè circa 2 ore e 10 minuti. In pratica, una telecamera in più riduce l'autonomia di circa mezz'ora; il valore reale va confrontato con le curve di autonomia del costruttore e cala con l'invecchiamento della batteria.

## Esercizio 12.2 – Distacco dei carichi

La potenza disponibile del contratto è:

\[ P_{disp} = 1{,}1 \cdot 4{,}5 = 4{,}95\,\mathrm{kW} \]

Alle 20:00 la potenza totale richiesta è:

\[ P = 0{,}4 + 2{,}4 + 2{,}0 + 2{,}0 + 1{,}2 = 8{,}0\,\mathrm{kW} \]

È molto oltre la potenza disponibile, e senza intervento il contatore staccherebbe in pochi minuti (sezione 2.3.3). L'automazione sospende prima lo scaldacqua:

\[ P = 8{,}0 - 1{,}2 = 6{,}8\,\mathrm{kW} > 4{,}95\,\mathrm{kW} \]

Il valore è ancora troppo alto, quindi sospende anche la lavatrice:

\[ P = 6{,}8 - 2{,}0 = 4{,}8\,\mathrm{kW} \le 4{,}95\,\mathrm{kW} \]

Devono essere sospesi entrambi i carichi. Restano accesi carichi di base, piano a induzione e forno; lavatrice e scaldacqua ripartono, uno alla volta, quando il forno o l'induzione si spengono.

## Esercizio 12.3 – Gestione dinamica della wallbox

La potenza disponibile è \(P_{disp} = 1{,}1 \cdot 4{,}5 = 4{,}95\,\mathrm{kW}\). La potenza assegnata alla ricarica si ricava da \(P_{wb} = P_{disp} - P_{casa} - P_{ris}\).

Con gli altri apparecchi a 1,0 kW:

\[ P_{wb} = 4{,}95 - 1{,}0 - 0{,}2 = 3{,}75\,\mathrm{kW} \qquad I = \frac{3750}{230} = 16{,}3\,\mathrm{A} \]

La wallbox carica a 16 A, cioè circa 3,7 kW: la corrente è sopra il minimo di 6 A e sotto il massimo di 32 A.

Con gli altri apparecchi a 3,9 kW:

\[ P_{wb} = 4{,}95 - 3{,}9 - 0{,}2 = 0{,}85\,\mathrm{kW} \qquad I = \frac{850}{230} = 3{,}7\,\mathrm{A} < 6\,\mathrm{A} \]

La corrente è inferiore al minimo ammesso: la ricarica si sospende e riprende quando i consumi della casa scendono. In pratica, con questo contratto la wallbox da 32 A non raggiunge mai la sua potenza massima di 7,4 kW.

## Esercizio 12.4 – Autoconsumo e autosufficienza

Senza accumulo:

\[ T_{auto} = \frac{1450}{4200} = 34{,}5\,\% \qquad T_{suff} = \frac{1450}{3800} = 38{,}2\,\% \]

L'energia immessa in rete è la produzione non autoconsumata:

\[ E_{imm} = 4200 - 1450 = 2750\,\mathrm{kWh} \]

Con l'accumulo:

\[ T_{auto} = \frac{2650}{4200} = 63{,}1\,\% \qquad T_{suff} = \frac{2650}{3800} = 69{,}7\,\% \]

\[ E_{imm} = 4200 - 2650 = 1550\,\mathrm{kWh} \]

L'accumulo sposta 1200 kWh all'anno dall'immissione all'autoconsumo. L'energia prelevata dalla rete scende di conseguenza da \(3800 - 1450 = 2350\,\mathrm{kWh}\) a \(3800 - 2650 = 1150\,\mathrm{kWh}\). Le perdite di carica e scarica della batteria sono trascurate.

## Esercizio 12.5 – Suddivisione della rete

Nella rete principale vanno il portatile, i due telefoni e il NAS, che contengono dati personali.

Nella rete IoT vanno i dieci relè smart, la telecamera e i sensori Thread. La telecamera può avere una rete propria, se il router lo permette.

Matter e Thread trovano i dispositivi con messaggi mDNS e multicast IPv6, che di norma non attraversano i confini tra reti separate (sezione 12.4.2). Senza configurazioni particolari devono quindi stare nella stessa rete:

- l'hub Home Assistant, che fa da controller;
- l'altoparlante che fa da Border Router Thread;
- i dispositivi Matter Wi-Fi, se presenti.

I telefoni usati per la messa in servizio dei dispositivi Matter devono raggiungere la stessa rete, per esempio collegandosi temporaneamente alla rete IoT. In alternativa il router deve inoltrare i messaggi mDNS e il traffico IPv6 tra le due reti. Il firewall consente alla rete principale di raggiungere l'hub e impedisce alla rete IoT di aprire connessioni verso la rete principale.

## Esercizio 12.6 – Telecamere e privacy

Caso a). La telecamera nel giardino orientata verso la porta riprende spazi di esclusiva pertinenza del proprietario. Rientra nell'esenzione per le attività domestiche del GDPR, purché l'inquadratura non comprenda la strada o le proprietà dei vicini. Il cartello non è obbligatorio, ma è utile; eventuali collaboratori domestici vanno informati.

Caso b). Il pianerottolo è una parte comune del condominio. Le FAQ del Garante escludono che un privato possa riprendere le aree comuni, come scale e pianerottoli: l'installazione non è ammessa così com'è. Si può limitare l'inquadratura alla sola porta, senza riprendere il pianerottolo, oppure chiedere all'assemblea un impianto condominiale (art. 1122-ter del Codice civile), con cartelli e conservazione limitata.

Caso c). Il videocitofono che riprende marciapiede e strada inquadra aree di pubblico passaggio, ed esce dall'esenzione domestica, come stabilito dalla Corte di giustizia UE nella causa C-212/13. Va riorientato o configurato con zone oscurate, in modo che riprenda solo l'ingresso della propria proprietà.
