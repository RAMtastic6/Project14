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
\fancyfoot[C]{\thepage}

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
Versione: & 1.1.0 \\
Redattori:  & Zambon M. Brotto D. Zaupa R. Basso L.\\
Verificatori: & Brotto D. Zaupa R. Zambon M.\\ 
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
v 1.1.1 & 2024-06-10 & Brotto D. & N/A & Aggiunti termini Backend, Frontend, WebSocket, Docker Compose, NPM, Endpoint, SSR (Server Side Rendering), manutenzione, gateway, RDBMS, JWT, HTTP, Multi-tier, Controller layer, Service Layer, Data Access Layer, TypeORM, React Architecture, CRUD, Facade, Layer di persistenza, Logica di business\\
\hline
v 1.1.0 & 2024-05-12 & Basso L. & Zambon M. & Inserimenti di nuovi termini e modifica della struttura del glossario; rimossi i numeri all'interno di sezioni e sotto-sezioni.\\
\hline
v 1.0.0 & 2024-04-06 & Zaupa R. & Zaupa R. & Approvazione e validazione del documento\\
\hline
v 0.3.0 & 2024-04-05 & Zambon M. & Zaupa R. & Cambiati i termini: "Caso d'Uso" in "Caso d'uso", "Diagramma dei Casi d'Uso" in "Diagramma dei casi d'uso", "Requisiti funzionali desiderabili" in "Requisiti desiderabili funzionali", "Requisiti funzionali obbligatori" in "Requisiti obbligatori funzionali"\\
\hline
v 0.2.0 & 2024-04-03 & Zambon M. & Zaupa R. & Cambiati i termini: "Latex" in "LaTeX", "Precondizione" in "Precondizioni", "Postcondizione" in "Postcondizioni", "Processo primario" in "Processi primari", "Processo di supporto" in "Processi di supporto", "Processo organizzativo" in "Processi organizzativi", "Riferimento" in "Riferimenti", "Rischio" in "Rischi", "Sottocaso d'uso" in "Sottocasi d'uso", "Tecnologia" in "Tecnologie", "Verbale esterno" in "Verbali esterni", "Verbale interno" in "Verbali interni"\\
\hline
v 0.1.1 & 2024-04-02 & Zambon M. & Zaupa R. & Aggiunti i termini: Best practices, Complessita' ciclomatica, Inspection, Modello a V, Pull request, Walkthrough e Way of Working, con le rispettive descrizioni\\
\hline
v 0.1.0 & 2024-03-22 & Brotto D. & Zaupa R. & Corrette le definizioni di PB,RTB e Fornitura. Aggiunto il termine Caption\\
\hline
v 0.0.2 & 2024-03-20 & Brotto D. & Zaupa R. & Stilate le definizioni di tutti i termini, aggiunti alcuni termini ambigui come Prenotazione e Ordinazione e rimosso Acquisizione \\
\hline
v 0.0.1 & 2024-01-19 & Zambon M. & Brotto D. & Creata struttura del glossario e aggiunti i termini \\
\hline
\end{tabular}
\newpage

% Sommario
\tableofcontents
\newpage
\section*{Introduzione}
\addcontentsline{toc}{section}{Introduzione}
Il glossario ha lo scopo di raccogliere i termini tecnici usati nel corso del progetto, al fine di facilitare la comprensione della documentazione, sia per i membri del gruppo che per i lettori esterni.
\newpage
\input{Contents/A}
\newpage
\input{Contents/B}
\newpage
\input{Contents/C}
\newpage
\input{Contents/D}
\newpage
\input{Contents/E}
\newpage
\input{Contents/F}
\newpage
\input{Contents/G}
\newpage
\input{Contents/H}
\newpage
\input{Contents/I}
\newpage
\input{Contents/J}
\newpage
\input{Contents/K}
\newpage
\input{Contents/L}
\newpage
\input{Contents/M}
\newpage
\input{Contents/N}
\newpage
\input{Contents/O}
\newpage
\input{Contents/P}
\newpage
\input{Contents/Q}
\newpage
\input{Contents/R}
\newpage
\input{Contents/S}
\newpage
\input{Contents/T}
\newpage
\input{Contents/U}
\newpage
\input{Contents/V}
\newpage
\input{Contents/W}
\newpage
\input{Contents/X}
\newpage
\input{Contents/Y}
\newpage
\input{Contents/Z}


\end{document}
"""

# ritorna la stringa della sezione del glossario
def compose_section(letter: str, json_array) -> str:
    section = ""
    section += "\\section*{" + letter + "} \n" +"\\addcontentsline{toc}{section}{"+letter+"}" + "\n"
    
    for d in json_array[letter]:
        section += "\\subsection*{" + d["termine"] + "} \n "+"\\addcontentsline{toc}{subsection}{"+d["termine"]+"}" + "\n"
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
