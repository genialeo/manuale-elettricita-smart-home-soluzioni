# Capitolo 7 – Progettare l'impianto di casa

*Soluzioni complete del capitolo 7 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 7.11. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti. Le dotazioni minime sono quelle delle tabelle 7.1 e 7.2.

## Esercizio 7.1 – Dotazioni minime di Livello 1

Il soggiorno da 22 m² supera 20 m²: servono 6 punti presa, 2 punti luce e 1 presa TV.

La cucina separata è un locale cucina: servono 5 punti presa, di cui almeno 2 sul piano di lavoro, 1 punto luce e 1 presa TV.

La camera da 14 m² è nella fascia da 12 a 20 m². Gli altri locali di questa fascia richiedono 5 punti presa; per le camere da letto se ne ammette uno in meno, quindi 4 punti presa, 1 punto luce e 1 presa TV.

Il bagno con attacco per la lavatrice richiede 2 punti presa e 2 punti luce. Il corridoio lungo 6 m supera 5 m: servono 2 punti presa e 2 punti luce.

In totale si hanno almeno 19 punti presa e 8 punti luce. La superficie di 68 m² è compresa tra 50 e 75 m²: al Livello 1 servono almeno 3 circuiti, esclusi quelli dedicati agli apparecchi oltre 1000 W. Servono inoltre 2 prese dati, 1 apparecchio di illuminazione di sicurezza e almeno 2 differenziali.

## Esercizio 7.2 – Potenza convenzionale e contratto

La potenza convenzionale è la somma dei prodotti \(K_{c,i} \cdot P_i\):

\[ P_c = 0{,}5 \cdot 0{,}7 + 2{,}5 \cdot 0{,}2 + 2{,}0 \cdot 0{,}3 + 2{,}2 \cdot 0{,}3 + 1{,}2 \cdot 0{,}5 \]

\[ P_c = 0{,}35 + 0{,}50 + 0{,}60 + 0{,}66 + 0{,}60 = 2{,}71\,\mathrm{kW} \]

Un contratto da 3 kW ha una potenza disponibile di \(1{,}1 \cdot 3 = 3{,}3\,\mathrm{kW}\), superiore a 2,71 kW: in base al calcolo è sufficiente.

Il calcolo, però, è una media. Se forno e lavatrice funzionano insieme alla massima potenza si arriva a \(2{,}0 + 2{,}2 = 4{,}2\,\mathrm{kW}\), oltre la soglia di 4 kW di e-distribuzione: il contatore stacca entro circa 2 minuti (tabella 2.2). Le soluzioni sono due: un contratto da 4,5 kW, con 4,95 kW disponibili, oppure il contratto da 3 kW con un relè di controllo dei carichi che stacca la lavatrice quando il forno è acceso.

## Esercizio 7.3 – Caduta di tensione complessiva

La caduta si calcola con \(\Delta V = k \cdot I \cdot L / 1000\), con \(k\) in mV/(A·m). Sul montante:

\[ \Delta V_{mont} = \frac{7{,}10 \cdot 25 \cdot 20}{1000} = 3{,}55\,\mathrm{V} \quad \Rightarrow \quad \frac{3{,}55}{230} \cdot 100 = 1{,}54\,\% \]

Sulla linea prese in 2,5 mm²:

\[ \Delta V_{2,5} = \frac{17{,}04 \cdot 16 \cdot 22}{1000} = 6{,}00\,\mathrm{V} \quad \Rightarrow \quad 2{,}61\,\% \]

Il totale è \(1{,}54 + 2{,}61 = 4{,}15\,\%\), oltre il 4 % raccomandato dalla norma degli impianti. Con la linea in 4 mm²:

\[ \Delta V_{4} = \frac{10{,}65 \cdot 16 \cdot 22}{1000} = 3{,}75\,\mathrm{V} \quad \Rightarrow \quad 1{,}63\,\% \]

Il totale scende a \(1{,}54 + 1{,}63 = 3{,}17\,\%\), entro il limite. La linea si realizza quindi in 4 mm², almeno nella dorsale.

## Esercizio 7.4 – Le zone del bagno

Le distanze si confrontano con i confini delle zone, che arrivano tutte a 2,25 m di altezza. La zona 2 si estende fino a 0,60 m dal bordo della vasca, la zona 3 da 0,60 m fino a \(0{,}60 + 2{,}40 = 3{,}00\,\mathrm{m}\).

Elemento a). La presa a 0,40 m dal bordo e a 1,20 m da terra è in zona 2. Le prese ordinarie non sono ammesse: va spostata oltre 0,60 m dal bordo. L'altezza non conta.

Elemento b). La scatola di derivazione a 1,50 m dal bordo è in zona 3, dove le scatole sono ammesse. Il circuito deve essere protetto da un differenziale con \(I_{\Delta n} \le 30\,\mathrm{mA}\).

Elemento c). La presa per rasoio a 0,50 m dal bordo è in zona 2. È ammessa, perché ha il trasformatore di isolamento incorporato.

Elemento d). Lo scaldacqua sopra la vasca, a 2,0 m da terra, è sotto la quota di 2,25 m e quindi in zona 1. Lo scaldacqua elettrico fisso, collegato in modo permanente e con grado almeno IPX4, è tra gli apparecchi ammessi in zona 1.

## Esercizio 7.5 – Differenziali non selettivi

Il generale e i due differenziali a valle hanno la stessa corrente differenziale di 30 mA e nessun ritardo. Per un guasto verso terra su un circuito la corrente di dispersione attraversa entrambi i differenziali in serie, e può far intervenire il generale insieme a quello del gruppo, o prima. Si spegne così tutta la casa e si perde il frazionamento chiesto dal capitolo 37. Il tipo AC, inoltre, non è adatto ai carichi elettronici di oggi, come spiega la sezione 6.5.6.

Una composizione corretta prevede un generale che apre fase e neutro, senza funzione differenziale: magnetotermico da 32 A, oppure interruttore di manovra-sezionatore se il montante è già protetto dal DG nel quadro contatore. Sotto il generale si installano almeno due differenziali da 30 mA di tipo A, ciascuno con i magnetotermici del proprio gruppo; per lavatrice e climatizzatori si preferisce il tipo F. Se serve una protezione differenziale a monte, per esempio per il montante, si installa un differenziale di tipo S con corrente differenziale più alta, per esempio 300 mA.

## Esercizio 7.6 – Riserva di spazio nel quadro

La norma chiede il 30 % di moduli in più rispetto a quelli installati, con un minimo di 2:

\[ 18 \cdot 0{,}3 = 5{,}4 \quad \Rightarrow \quad 6\,\text{moduli liberi} \]

Il quadro deve quindi avere almeno \(18 + 6 = 24\) moduli. La taglia da 24 moduli rispetta il minimo; quella da 36 moduli lascia spazio anche a futuri apparecchi su guida DIN, per esempio per la domotica.

## Esercizio 7.7 – Alimentatore e cavo di una striscia LED

La potenza e la corrente della striscia sono:

\[ P = 9{,}6 \cdot 6 = 57{,}6\,\mathrm{W} \qquad I = \frac{57{,}6}{24} = 2{,}4\,\mathrm{A} \]

Con il margine del 20 % l'alimentatore deve avere almeno \(1{,}2 \cdot 57{,}6 = 69{,}1\,\mathrm{W}\). La taglia da 60 W non basta; si sceglie quella da 100 W, che lavora al 58 % del carico.

La caduta nel cavo lungo 8 m vale:

\[ \Delta V_{0,75} = \frac{2 \cdot 0{,}0213 \cdot 8 \cdot 2{,}4}{0{,}75} = 1{,}09\,\mathrm{V} \quad (4{,}5\,\%) \]

\[ \Delta V_{1,5} = \frac{2 \cdot 0{,}0213 \cdot 8 \cdot 2{,}4}{1{,}5} = 0{,}55\,\mathrm{V} \quad (2{,}3\,\%) \]

Con 0,75 mm² si supera il 3 %; si sceglie quindi il cavo da 1,5 mm².

Lungo la striscia la caduta cresce circa con il quadrato della lunghezza. Alimentata da un capo:

\[ \Delta V_{6\,\mathrm{m}} = 1{,}4 \cdot \left(\frac{6}{5}\right)^2 = 2{,}02\,\mathrm{V} \quad (8{,}4\,\%) \]

È più della caduta di una bobina da 5 m. La corrente nel primo contatto, 2,4 A, resta invece sotto i 3 A consigliati. Con il cavo da 1,5 mm² ai LED più lontani arrivano \(24 - 0{,}55 - 2{,}02 = 21{,}4\,\mathrm{V}\).

Alimentandola dal centro si hanno due tratti da 3 m:

\[ \Delta V_{3\,\mathrm{m}} = 1{,}4 \cdot \left(\frac{3}{5}\right)^2 = 0{,}50\,\mathrm{V} \quad (2{,}1\,\%) \]

La caduta lungo la striscia diventa un quarto e ai LED più lontani arrivano \(24 - 0{,}55 - 0{,}50 = 22{,}95\,\mathrm{V}\). Conviene quindi portare il cavo al centro, se il percorso lo consente: la luce resta più uniforme senza aumentare la sezione.
