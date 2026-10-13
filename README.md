# Manuale di Elettricità e Smart Home – Soluzioni complete degli esercizi

Questo repository raccoglie il procedimento completo degli esercizi del libro *Manuale di Elettricità e Smart Home – Guida pratica dall'interruttore all'App*, di Leonardo Maria Fenu.

Nel libro l'Appendice D riporta solo i risultati finali. Qui si trovano, per ogni esercizio, i dati, le formule usate e tutti i passaggi di calcolo, così da poter confrontare anche il ragionamento e non solo il numero finale.

## Contenuto

| File | Che cosa contiene |
|:--|:--|
| `soluzioni-complete.pdf` | Tutte le soluzioni in un unico PDF, da scaricare e stampare |
| `capitolo-01.md` … `capitolo-12.md` | Le stesse soluzioni, un file per capitolo, leggibili direttamente su GitHub |
| `esempi/` | Il codice completo degli esempi dell'Appendice B (Shelly, Sonoff, Tuya, MQTT) |
| `genera_pdf.sh` | Comando che ricrea il PDF dai file Markdown (richiede pandoc e xelatex) |

I numeri degli esercizi seguono la forma «capitolo.esercizio»: l'esercizio 6.3 è il terzo esercizio del capitolo 6. I testi degli esercizi sono nel libro, nella sezione «Esercizi» alla fine di ogni capitolo; anche i rimandi a sezioni, tabelle e figure si riferiscono al libro.

## Come rigenerare il PDF

```sh
bash genera_pdf.sh
```

Servono pandoc (versione 2.11 o successiva) e una distribuzione TeX con xelatex. Se sono installati i caratteri Source Sans Pro, Source Code Pro e Fira Math, il PDF usa gli stessi caratteri del libro.

## Segnalare un errore

Le segnalazioni sono benvenute. Il modo più semplice è aprire una *issue* in questo repository, indicando:

- il numero dell'esercizio, per esempio 4.3;
- il passaggio o il valore che sembra errato;
- se possibile, il calcolo corretto o la fonte.

Chi usa GitHub può anche proporre la correzione direttamente con una *pull request* sul file del capitolo. Le correzioni accolte entrano nel PDF e, se riguardano un risultato, nelle ristampe successive dell'Appendice D.

## Licenza

Copyright © 2026 Leonardo Maria Fenu. Soluzioni e testi sono distribuiti con licenza [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it): si possono condividere citando l'autore, senza usi commerciali né modifiche. Il codice della cartella `esempi/` si può usare e adattare per uso personale e didattico, citando la fonte. Dettagli nel file `LICENSE`.
