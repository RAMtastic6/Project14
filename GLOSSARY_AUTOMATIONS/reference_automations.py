# file che contiene tutte e due le automazioni per i riferimenti

# 1. Automazione che rimpiazza tutte le parole nel glossario all'interno 
# di un file con un riferimento al glossario

# 2. Automazione che rimpiazza solo la prima occorrenza di una 
# parola all'interno del glossario 

from GLOSSARY_AUTOMATIONS.read_json import *
from GLOSSARY_AUTOMATIONS.read_all_files import * 


def check_for_titles(line: str) -> bool:
    """funzione che controlla se una stringa in latex abbia al suo interno un titolo"""
    titles = ["textbf", "section", "subsection", "subsubsection", "\\input", "title", "\\caption"]
    for t in titles:
        if t in line:
            return True
    return False 

def repl_all_occurrences(glossary_path: str, filename: str, content_folder: str = "") -> None:
    """rimpiazza tutte le occorrenze di parole contenute in un file
    chiamato filename che sono anche contenute all'interno del glossario"""
    # setup del dizionario e dei file
    JSON_ARRAY = get_json_array_from_path(glossary_path) 
    defs = get_termini_from_json(JSON_ARRAY)
    files = []
    files.append(filename)
    if content_folder != "":
        files += read_all_files(content_folder, "*.tex")


    for n in files: 
        # lettura del contenuto dal file 
        # il file deve essere scomposto riga per riga
        # in teoria basta splittare il contentuto del file
        # e salvarsi i singoli elementi all'interno 
        # di una lista (funzinoe list.split())
        f = open(n, "r")
        content = ""
        content = f.read()
        f.close()

        # splittare il contenuto delle righe
        lines = content.split("\n")
        new_content = ""

        # rimpiazzo di tutte le occorrenze di una definizione
        # presente nel glossario
        # problema: le entries della lista non sembrano modificarsi da sole.
        count_replaced_occurrences = 0 
        for d in defs:
            ref_string = "$\\textit{" + d + "}_G$"
            for index, item in enumerate(lines):
                if not check_for_titles(item) and ref_string not in item:
                    # ricercare la parola all'interno della riga, non la sottostringa
                    w = " " + d + " "
                    if w in item:
                        count_replaced_occurrences += 1 
                        lines[index] = item.replace(d, ref_string)
                    elif w.lower() in item:
                        count_replaced_occurrences += 1 
                        lines[index] = item.replace(d.lower(), "$\\textit{" + d.lower() + "}_G$")

        
        # ricomporre tutto contentuo all'interno di una 
        # singola stringa 
        for l in lines:
            new_content += l + "\n"
        new_content = new_content.rstrip("\n")

        # scrittura del contenuto all'interno del file
        f = open(n, "w")
        f.write(new_content)
        f.close()
        print("nel file {} sono stati rimpiazzati {} riferimenti".format(n, count_replaced_occurrences))



def repl_first_occurrence(glossary_path: str, filename: str, content_folder: str = "") -> None:
    """rimpiazza la prima occorrenza di parole contenute in un file
    chiamato filename che sono anche contenute all'interno del glossario"""

    # setup del dizionario e dei file
    JSON_ARRAY = get_json_array_from_path(glossary_path) 
    defs = get_termini_from_json(JSON_ARRAY) 
    done = {} 
    for d in defs:
        done[d] = False

    files = []
    files.append(filename)
    if content_folder != "":
        files += read_all_files(content_folder, "*.tex")

    # DEBUG
    # print(files)

    for n in files: 
        # lettura del contenuto dal file 
        f = open(n, "r")
        content = ""
        content = f.read()
        f.close()

        # splittare il contenuto delle righe
        lines = content.split("\n")
        new_content = ""

        # rimpiazzo di tutte le occorrenze di una definizione
        # presente nel glossario


        # il problema di questa automazione è il fatto che quando la si
        # esegue una seconda volta, la tabella done si svuota di tutti i suoi
        # valori. di conseguenza, non tiene traccia dei riferimenti già 
        # rimpiazzati all'interno del file.
        # servirebbe un modo per salvarli.
        # allo stato delle cose l'automazione funziona se la si esegue solamente una volta.
        # l'idea è quella di avere, per ogni sorgente, una mappa (dizionario in json) 
        # all'interno della quale una coppia chiave valore è definita nel seguente modo 
        # {'definizione', 'true'} => tiene solo le parole giá fatte.
        count_replaced_occurrences = 0 
        for d in defs:
            ref_string = "\\textit{" + d + "_G}"
            for index, item in enumerate(lines):
                if done[d] != True and (not check_for_titles(item)) and ref_string not in item:
                    # ricercare la parola all'interno della riga, non la sottostringa
                    w = " " + d + " "
                    if w in item:
                        count_replaced_occurrences += 1 
                        done[d] = True
                        lines[index] = item.replace(d, ref_string, 1)
                    elif w.lower() in item:
                        count_replaced_occurrences += 1 
                        done[d] = True
                        lines[index] = item.replace(d.lower(), ref_string, 1)                    

        # ricomporre tutto contentuo all'interno di una 
        # singola stringa 
        for l in lines:
            new_content += l + "\n"
        new_content = new_content.rstrip("\n")

        # scrittura del contenuto all'interno del file
        f = open(n, "w")
        f.write(new_content)
        f.close()
        print("nel file {} sono stati rimpiazzati {} riferimenti".format(n, count_replaced_occurrences))
