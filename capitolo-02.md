# Capitolo 2 – Dalla rete al quadro di casa

*Soluzioni complete del capitolo 2 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 2.9. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 2.1 – Condizione di protezione in un sistema TT

La condizione di protezione nel sistema TT è \(R_A \cdot I_{\Delta n} \le 50\,\mathrm{V}\).

Con il differenziale da 30 mA:

\[ R_A \cdot I_{\Delta n} = 120 \cdot 0{,}03 = 3{,}6\,\mathrm{V} \le 50\,\mathrm{V} \]

La condizione è rispettata con ampio margine.

Con il differenziale da 300 mA:

\[ R_A \cdot I_{\Delta n} = 120 \cdot 0{,}3 = 36\,\mathrm{V} \le 50\,\mathrm{V} \]

Anche in questo caso la condizione è rispettata, ma il margine è ridotto.

La tensione massima che una massa può assumere senza che il differenziale da 30 mA intervenga è quella prodotta dalla corrente di intervento. Si ottiene 3,6 V, un valore non pericoloso. In pratica, con 120 Ω di resistenza di terra entrambi i differenziali proteggono, ma quello da 30 mA offre anche la protezione addizionale contro i contatti diretti.

## Esercizio 2.2 – Resistenza di terra massima

La resistenza massima si ricava dalla condizione \(R_A \le U_L / I_{\Delta n}\), con \(U_L = 50\,\mathrm{V}\):

\[ I_{\Delta n} = 30\,\mathrm{mA}: \quad R_A \le \frac{50}{0{,}03} = 1667\,\Omega \]

\[ I_{\Delta n} = 100\,\mathrm{mA}: \quad R_A \le \frac{50}{0{,}1} = 500\,\Omega \]

\[ I_{\Delta n} = 500\,\mathrm{mA}: \quad R_A \le \frac{50}{0{,}5} = 100\,\Omega \]

Più la corrente di intervento è alta, più l'impianto di terra deve essere buono.

## Esercizio 2.3 – Comportamento del contatore 2G

Con 3 kW impegnati la potenza disponibile è \(1{,}1 \cdot 3 = 3{,}3\,\mathrm{kW}\). Per e-distribuzione la soglia superiore vale 4 kW (tabella 2.2).

Situazione a). Il carico di 3,1 kW è inferiore a 3,3 kW: il prelievo è ammesso senza limiti di tempo e il contatore non interviene.

Situazione b). Il forno e la lavatrice prelevano insieme \(2{,}2 + 1{,}7 = 3{,}9\,\mathrm{kW}\), un valore compreso tra 3,3 e 4 kW, quindi sotto la soglia superiore. Dopo circa 2 minuti il display mostra il primo avviso, «ridurre carico». Il carico dura 90 minuti: si spegne prima del 92° minuto, quindi il secondo avviso non compare e non si arriva al distacco.

Situazione c). Con l'asciugacapelli la potenza sale a \(2{,}2 + 1{,}7 + 1{,}2 = 5{,}1\,\mathrm{kW}\), oltre la soglia superiore di 4 kW. Il primo avviso compare quasi subito e il contatore apre il circuito entro circa 2 minuti, se nel frattempo il carico non viene ridotto.

## Esercizio 2.4 – Aumento della potenza impegnata

La nuova potenza disponibile è:

\[ P_{disp} = 1{,}1 \cdot 4{,}5 = 4{,}95\,\mathrm{kW} \]

La corrente corrispondente a 230 V, con carico resistivo, è:

\[ I = \frac{4950}{230} = 21{,}5\,\mathrm{A} \]

La quota potenza passa da \(3 \cdot 26 = 78\) euro/anno a \(4{,}5 \cdot 26 = 117\) euro/anno. La differenza è di 39 euro all'anno, a cui si aggiunge il contributo una tantum per l'aumento. La corrente di 21,5 A va confrontata con la portata del montante e con l'interruttore che lo protegge.

## Esercizio 2.5 – Sistemi di distribuzione

Caso a). L'appartamento è alimentato dalla rete pubblica in bassa tensione: il neutro è a terra in cabina e le masse sono collegate al dispersore dell'edificio. Il sistema è TT.

Caso b). Il centro commerciale ha una propria cabina MT/BT, quindi gestisce il trasformatore e un unico impianto di terra. Le masse si collegano, attraverso il conduttore di protezione, al centro stella del proprio trasformatore: il sistema è TN.

Caso c). L'impianto fotovoltaico non cambia il collegamento con la rete pubblica. La villetta resta in sistema TT, perché è alimentata in bassa tensione dal distributore.

## Esercizio 2.6 – Progetto e documenti secondo il DM 37/08

L'unità abitativa ha una superficie di 110 m², inferiore a 400 m². La potenza impegnata di 7 kW, però, supera i 6 kW. Secondo il DM 37/08 il progetto deve quindi essere redatto da un professionista iscritto all'albo professionale.

A fine lavori l'impresa installatrice abilitata deve rilasciare la Dichiarazione di conformità, con i relativi allegati obbligatori, tra cui il progetto.

## Esercizio 2.7 – Guasto verso terra sul montante

Il differenziale sorveglia solo ciò che sta dopo di lui, perché confronta le correnti che lo attraversano. Il differenziale del quadro d'appartamento si trova alla fine del montante, che per lui sta tutto a monte. Un guasto tra la fase del montante e una parte metallica non cambia le correnti che attraversano il differenziale, che quindi non interviene. Il magnetotermico del quadro contatore non interviene a sua volta, perché la corrente verso terra, nel sistema TT, è al più di pochi ampere.

Le soluzioni sono due. La prima è realizzare il montante in Classe II, per esempio con cavi in un tubo isolante di plastica e senza scatole o tubi metallici lungo il percorso. La seconda è installare un differenziale nel quadro contatore, all'inizio del montante, scelto in modo da non intervenire insieme a quelli di casa. La scelta spetta al progettista o all'impresa installatrice.
