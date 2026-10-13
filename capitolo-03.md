# Capitolo 3 – Materiali e cavi

*Soluzioni complete del capitolo 3 del «Manuale di Elettricità e Smart Home» di Leonardo Maria Fenu. I rimandi a sezioni, tabelle e figure si riferiscono al libro.*

Le soluzioni seguono l'ordine degli esercizi della sezione 3.9. I risultati sono arrotondati; i passaggi intermedi sono stati calcolati senza arrotondamenti.

## Esercizio 3.1 – Conduttori, isolanti e semiconduttori

La classificazione si basa sulla resistività e sul comportamento dei materiali (sezione 3.1).

- Conduttori: rame, per cavi, morsetti e sbarre dei quadri; alluminio, per linee aeree e cavi di grande sezione.
- Isolanti: PVC, per isolanti e guaine dei cavi civili; porcellana, per gli isolatori delle linee aeree e per alcuni portafusibili; mica, per i nastri dei cavi resistenti al fuoco come l'`FTG18OM16`.
- Semiconduttori: silicio e germanio, con cui si costruiscono diodi, LED e transistor.

## Esercizio 3.2 – Resistenza di una linea in rame e in alluminio

La resistenza si ricava con la formula della sezione 1.5.1, su una lunghezza complessiva di conduttore di 50 m, andata e ritorno.

Dati: \(L = 50\,\mathrm{m}\); \(S = 2{,}5\,\mathrm{mm^2}\); \(\rho_{Cu} = 0{,}0178\) e \(\rho_{Al} = 0{,}028\,\Omega\cdot\mathrm{mm^2/m}\).

\[ R_{Cu} = \frac{0{,}0178 \cdot 50}{2{,}5} = 0{,}356\,\Omega \qquad R_{Al} = \frac{0{,}028 \cdot 50}{2{,}5} = 0{,}560\,\Omega \]

A parità di sezione la linea in alluminio ha una resistenza maggiore di circa il 57 %. La sezione di alluminio che dà la stessa resistenza del rame è:

\[ S_{Al} = S_{Cu} \cdot \frac{\rho_{Al}}{\rho_{Cu}} = 2{,}5 \cdot \frac{0{,}028}{0{,}0178} = 3{,}93\,\mathrm{mm^2} \]

La sezione commerciale immediatamente superiore è 4 mm². Il calcolo serve solo per il confronto: nelle sezioni piccole degli impianti domestici l'alluminio non si usa.

## Esercizio 3.3 – Lettura di tre sigle

Si applicano le regole delle sezioni 3.4.1, 3.4.2 e 3.4.3.

`H07V-K 1×2,5`: cavo armonizzato (H) da 450/750 V (07), isolante in PVC (V), senza guaina. Il conduttore è flessibile per posa fissa (K) e la formazione è un'anima da 2,5 mm². È una cordina per condutture fisse in tubo o canale.

`H05VV-F 3G1,5`: cavo armonizzato da 300/500 V (05), isolante in PVC e guaina in PVC (VV), conduttore flessibile per posa mobile (F). Ha tre anime da 1,5 mm², di cui una giallo-verde. È un cordone per un apparecchio monofase di classe I: fase, neutro e conduttore di protezione.

`FG16OR16 0,6/1 kV 5G6`: cavo nazionale con corda flessibile in rame (F), isolante in HEPR di qualità G16, anime riunite in un cavo rotondo (O) e guaina in PVC di qualità R16. La tensione nominale è 0,6/1 kV. Ha cinque anime da 6 mm², di cui una sola giallo-verde: le altre quattro sono le tre fasi e il neutro. Può alimentare un circuito trifase con neutro, per esempio la linea di un quadro esterno o di una pompa di calore trifase.

## Esercizio 3.4 – Margine di isolamento a 400 V

La tensione di perforazione si stima con la formula della sezione 3.3.1.

Dati: \(s = 0{,}7\,\mathrm{mm}\); \(E_d \approx 25\,\mathrm{kV/mm}\); tensione concatenata 400 V efficaci.

\[ V_p = E_d \cdot s = 25 \cdot 0{,}7 = 17{,}5\,\mathrm{kV} \]

Il valore di picco della tensione concatenata è:

\[ V_{max} = 400 \cdot \sqrt{2} = 566\,\mathrm{V} \]

Il rapporto è \(17\,500 / 566 \approx 31\). Tra due cordine a contatto gli strati di isolante sono due, quindi il margine reale è ancora più alto. Il margine non è uno spreco, perché il valore di rigidità dielettrica vale per un materiale nuovo e integro. In servizio l'isolante invecchia con il calore, può essere stato schiacciato o graffiato durante la posa e deve reggere le sovratensioni di qualche kilovolt che arrivano dalla rete.

## Esercizio 3.5 – Classi CPR

Si applicano la CEI 64-8 e la CEI UNEL 35016 (sezione 3.5.3 e tabella 3.6).

Caso a): un appartamento è un luogo ordinario. Il requisito minimo prescritto dalla CEI 64-8 è la classe Eca, e le condutture incassate in strutture non combustibili non richiedono precauzioni particolari. La tabella della CEI UNEL 35016 indica per gli edifici civili fino a 24 m la classe `Cca-s3,d1,a3` quando i cavi sono posati in fascio, per esempio nei montanti condominiali. Le cordine `FS17`, le più usate, sono già di classe `Cca-s3,d1,a3` e soddisfano entrambe le indicazioni.

Caso b): una scuola è un luogo a maggior rischio in caso di incendio per l'affollamento, e i corridoi sono vie di esodo. Se manca una valutazione del rischio, la CEI 64-8 chiede almeno la classe `Cca-s1b,d1,a1`; la tabella della CEI UNEL 35016 indica la stessa classe per le scuole. Vanno bene, per esempio, cavi `FG16OM16`.

Caso c): l'atrio di una stazione ferroviaria rientra tra le grandi infrastrutture, per le quali la CEI UNEL 35016 indica la classe `B2ca-s1a,d1,a1`.

Significato della sigla `Cca-s1b,d1,a1`:

- Cca: classe di reazione al fuoco C per i cavi, con propagazione della fiamma e rilascio di calore limitati;
- s1b: fumi poco opachi, al secondo livello della categoria s1;
- d1: gocciolamento di particelle incandescenti limitato;
- a1: fumi poco acidi e poco corrosivi.

## Esercizio 3.6 – Classi degli apparecchi in cucina

Si usano le definizioni della sezione 3.7.1.

Il forno ha una carcassa metallica e una spina con contatto di terra: è di classe I. Richiede il conduttore di protezione, che porta a terra la corrente in caso di guasto e permette l'intervento del differenziale.

Il frullatore con il simbolo del doppio quadrato è di classe II. Il doppio isolamento protegge anche dopo un primo guasto, quindi l'apparecchio non va collegato a terra.

La striscia LED a 24 V c.c. alimentata da una sorgente SELV è di classe III. La tensione resta sotto 120 V in corrente continua e non va collegata a terra. L'alimentatore SELV che la alimenta dalla rete è un apparecchio a sé: di solito è di classe II e allora non richiede il conduttore di protezione. Se fosse di classe I, andrebbe collegato a terra.
