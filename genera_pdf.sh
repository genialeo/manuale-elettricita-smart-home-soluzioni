#!/usr/bin/env bash
# Genera soluzioni-complete.pdf da capitolo-01.md ... capitolo-12.md (stessa cartella).
#
# Uso: bash genera_pdf.sh
# Richiede pandoc (>= 2.11) e xelatex (TeX Live con fontspec e unicode-math).
# Caratteri: Source Sans Pro e Fira Math se installati (come nel libro), altrimenti
# i caratteri predefiniti di LaTeX.
#
# I file capitolo-NN.md sono generati dai sorgenti del libro: le correzioni
# accolte vengono riportate lì, poi si rigenerano i file e si rilancia questo comando.
set -euo pipefail
QUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$QUI"
export LANG=C.UTF-8 LC_ALL=C.UTF-8
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

{
  echo '\usepackage{fontspec}'
  if fc-list 2>/dev/null | grep "Source Sans Pro" >/dev/null; then
    echo '\setmainfont{Source Sans Pro}'
  fi
  if fc-list 2>/dev/null | grep "Source Code Pro" >/dev/null; then
    echo '\setmonofont{Source Code Pro}[Scale=MatchLowercase]'
  fi
  echo '\usepackage{unicode-math}'
  if fc-list 2>/dev/null | grep "Fira Math" >/dev/null; then
    echo '\setmathfont{Fira Math}'
  fi
  echo '\usepackage{xurl}'
  echo '\setlength{\parindent}{0pt}\setlength{\parskip}{4pt plus 1pt}'
  echo '\usepackage{titlesec}\titleformat{\section}{\Large\bfseries}{}{0pt}{}'
  echo '\titlespacing*{\section}{0pt}{0pt}{10pt}'
  echo '\titleformat{\subsection}{\normalsize\bfseries}{}{0pt}{}'
  echo '\newcommand{\sectionbreak}{\clearpage}'
} > "$TMP/preambolo.tex"

pandoc capitolo-[0-9][0-9].md \
  -f markdown+tex_math_single_backslash+tex_math_dollars \
  --pdf-engine=xelatex \
  -V documentclass=article -V papersize=a4 -V geometry:margin=22mm -V fontsize=11pt \
  -V lang=it -V fontfamily=fontspec -V colorlinks=true -V linkcolor=black -V urlcolor=blue \
  -V title="Manuale di Elettricità e Smart Home" \
  -V subtitle="Soluzioni complete degli esercizi" \
  -V author="Leonardo Maria Fenu" \
  --toc -V toc-title="Indice" \
  -H "$TMP/preambolo.tex" \
  -o soluzioni-complete.pdf

echo "Creato: $QUI/soluzioni-complete.pdf ($(pdfinfo soluzioni-complete.pdf 2>/dev/null | awk '/^Pages/{print $2}') pagine)"
