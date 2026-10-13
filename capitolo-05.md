# Capitolo 5 – Comandi, relè e automazioni

*Soluzioni complete del capitolo 5 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 5.10. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 5.1 – Scelta dei comandi

Caso a). Tre punti di comando si realizzano con due deviatori, alle porte estreme, e un invertitore, alla porta intermedia. Tra un comando e l'altro corrono le due navette; la fase arriva al comune del primo deviatore e il ritorno di lampada parte dal comune del secondo.

Caso b). Con deviatori e invertitori il numero di invertitori è pari al numero di punti meno due:

\[ n_{inv} = n - 2 = 5 - 2 = 3 \]

Servono quindi due deviatori e tre invertitori, collegati in serie sulle navette. Con un relè passo-passo servono invece cinque pulsanti NA in parallelo e un relè; tra un pulsante e l'altro bastano due conduttori, la fase e il comando della bobina. Con cinque punti la soluzione con il passo-passo è di solito più semplice ed economica, come riassume la tabella 5.2.

Caso c). Serve un commutatore 1-0-2: le due uscite, collegate alle due velocità, non possono mai essere alimentate insieme, e la posizione 0 spegne l'aspiratore. Due interruttori indipendenti non andrebbero bene, perché permetterebbero di alimentare entrambi gli avvolgimenti.

## Esercizio 5.2 – Corrente delle bobine

La corrente si ricava dalla potenza nominale della bobina, \(I_{bob} = P_{bob}/V_{bob}\).

Dati: bobina a 12 V c.c. da 1 W; bobina a 230 V c.a. da 4,5 VA.

\[ I_{12} = \frac{1}{12} = 0{,}083\,\mathrm{A} = 83\,\mathrm{mA} \]

\[ I_{230} = \frac{4{,}5}{230} = 0{,}0196\,\mathrm{A} = 19{,}6\,\mathrm{mA} \]

Un'uscita da 20 mA non può comandare direttamente la bobina a 12 V, che ne richiede circa 83: serve un transistor o un modulo di interfaccia tra il microcontrollore e la bobina.

## Esercizio 5.3 – Corrente capacitiva su un ritorno di lampada

Si calcola la capacità totale tra fase e ritorno di lampada, poi la corrente capacitiva con \(I_C = 2\pi \cdot f \cdot C \cdot V\).

Dati: \(l = 40\,\mathrm{m}\); capacità per metro \(80\,\mathrm{pF/m}\); \(f = 50\,\mathrm{Hz}\); \(V = 230\,\mathrm{V}\).

\[ C = 40 \cdot 80 = 3200\,\mathrm{pF} = 3{,}2 \cdot 10^{-9}\,\mathrm{F} \]

\[ I_C = 2\pi \cdot 50 \cdot 3{,}2 \cdot 10^{-9} \cdot 230 = 2{,}31 \cdot 10^{-4}\,\mathrm{A} = 0{,}23\,\mathrm{mA} \]

La corrente è circa un quarto di quella di una spia di localizzazione (1 mA). È poca, ma può bastare a far lampeggiare una lampada LED di bassa potenza. Il rimedio più semplice è un carico di compensazione in parallelo alla lampada.

## Esercizio 5.4 – Contattore per una pompa

La corrente di impiego di un carico monofase con fattore di potenza si ricava da \(I_B = P/(V \cdot \cos\varphi)\).

Dati: \(P = 900\,\mathrm{W}\); \(V = 230\,\mathrm{V}\); \(\cos\varphi = 0{,}8\).

\[ I_B = \frac{900}{230 \cdot 0{,}8} = 4{,}89\,\mathrm{A} \]

La pompa è un motore per uso domestico: il contattore va scelto in categoria AC-7b, con una corrente nominale in quella categoria di almeno 4,9 A. Il dato da controllare è quello AC-7b, molto più basso del valore AC-7a: per un contattore modulare da 25 A in AC-7a si trovano per esempio 9 A in AC-7b (dati ABB ESB25). Il contatto del temporizzatore alimenta solo la bobina del contattore.

## Esercizio 5.5 – Generale del quadro d'appartamento

Nel sistema TT il generale deve sezionare anche il neutro: in un'abitazione monofase serve quindi un interruttore di manovra-sezionatore bipolare.

La corrente nominale si sceglie sulla protezione a monte, che è il magnetotermico da 32 A del quadro contatore:

\[ I_{n,sez} \ge 32\,\mathrm{A} \]

Va bene quindi un 32 A o un 40 A, coordinato con il magnetotermico a monte secondo le tabelle del costruttore. La somma delle correnti dei circuiti vale:

\[ 10 + 10 + 16 + 16 + 20 = 72\,\mathrm{A} \]

Non è un criterio corretto. La corrente che entra nel quadro non può superare a lungo i 32 A, perché il magnetotermico a monte interverrebbe; inoltre di solito i circuiti non assorbono insieme la loro corrente massima.

## Esercizio 5.6 – Ritorno della tensione: passo-passo e autoritenuta

Con il relè passo-passo, bistabile, i contatti restano nella posizione in cui si trovavano quando è mancata la tensione. Al ritorno della tensione la lampada si riaccende da sola.

Con l'autoritenuta la bobina si diseccita appena manca la tensione, e il contatto di autoritenuta K1\* si apre. Al ritorno della tensione il circuito resta aperto, perché né il pulsante di marcia né K1\* sono chiusi: la lampada rimane spenta finché qualcuno non preme di nuovo il pulsante di marcia.

Per un motore il cui riavvio spontaneo sarebbe pericoloso è adatto lo schema di autoritenuta. È la soluzione classica per il requisito, posto dalle norme per le macchine e per i motori, che vieta il riavviamento spontaneo quando può essere pericoloso (sezione 5.6.2).
