from GLOSSARY_AUTOMATIONS.read_json import *
import os
# il path che corrisponde alla cartella del glossario

intestazione = r"""\documentclass[12pt, oneside]{article} 
\usepackage{amsmath, amsthm, amssymb, calrsfs, wasysym, verbatim, bbm, color, graphicx, geometry, fancyhdr, url, multirow, hyperref}
\usepackage[italian]{babel}

\geometry{tmargin=.75in, bmargin=.75in, lmargin=.75in, rmargin = .75in}


\author{RAMtastic6}

%Intestazione
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{Gruppo 14 RAMtastic6\\ramtastic6@gmail.com}
\fancyfoot[C]{\\thepage}

\renewcommand{\headrulewidth}{0pt} 

% Intestazione documento
\begin{document}
% Salta la prima pagina per l'intestazione
\thispagestyle{empty}
\title{Glossario}
\maketitle
\begin{figure}[h]
  \centering
  \includegraphics[scale=0.3]{logo.png}
\end{figure}
\begin{center}
    email: ramtastic6@gmail.com
\end{center}

% Informazioni sul documento
\section*{Informazioni sul documento}
\begin{tabular}{ll}
Versione: & 0.0.1 \\
Redattori:  & Michele Z.\\
Verificatori: & \\ 
Destinatari: & T. Vardanega, R. Cardin, Imola Informatica \\
Uso: & Esterno
\end{tabular}
\newpage

% Registro dei cambiamenti
\section*{Registro dei Cambiamenti - Changelog}
\begin{tabular}{|c|c|c|p{3cm}|p{6cm}|}
\hline
\textbf{Versione} & \textbf{Data} & \textbf{Autore} & \textbf{Verificatore} & \textbf{Dettaglio} \\
\hline
v.1.0.1 & 2024-03-22 & Brotto D. & N/A & Corrette le definizioni di PB e RTB \\
\hline
v.1.0.0 & 2024-03-20 & Brotto D. & N/A & Stilate le definizioni di tutti i termini, aggiunti alcuni termini ambigui come Prenotazione e Orinazione e rimosso Acquisizione \\
\hline
v.0.0.1 & 2024-01-19 & Michele Z. & Brotto D. & Creata struttura del glossario e aggiunti i termini \\
\hline
\end{tabular}
\newpage

% Sommario
\tableofcontents
\newpage
\section{Introduzione}
Il glossario ha lo scopo di raccogliere i termini tecnici usati nel corso del progetto, al fine di facilitare la comprensione della documentazione, sia per i membri del gruppo che per i lettori esterni.
\newpage
\input{Contents/A}
\input{Contents/B}
\input{Contents/C}
\input{Contents/D}
\input{Contents/E}
\input{Contents/F}
\input{Contents/G}
\input{Contents/H}
\input{Contents/I}
\input{Contents/J}
\input{Contents/K}
\input{Contents/L}
\input{Contents/M}
\input{Contents/N}
\input{Contents/O}
\input{Contents/P}
\input{Contents/Q}
\input{Contents/R}
\input{Contents/S}
\input{Contents/T}
\input{Contents/U}
\input{Contents/V}
\input{Contents/W}
\input{Contents/X}
\input{Contents/Y}
\input{Contents/Z}


\end{document}
"""

# ritorna la stringa della sezione del glossario
def compose_section(letter: str, json_array) -> str:
    section = ""
    section += "\\section{" + letter + "} \n"
    
    for d in json_array[letter]:
        section += "\\subsection{" + d["termine"] + "} \n"
        section += d["definizione"] + "\n"
    return section

def build_glossario(dir: str) -> None:
    f = open(dir + "glossary.tex", "w")
    f.write(intestazione)
    f.close()

    JSON_ARRAY = get_json_array_from_path(os.path.join(dir,"glossario.json"))

    for c in ALPHABET:
        section = compose_section(c, JSON_ARRAY)
        section_path = os.path.join(dir , "Contents" , (c + ".tex"))
        f = open(section_path, "w", encoding="utf8")
        f.write(section)
        f.close()
