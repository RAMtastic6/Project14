# file che contiene tutte e due le automazioni per i riferimenti

# 1. Automazione che rimpiazza tutte le parole nel glossario all'interno 
# di un file con un riferimento al glossario

# 2. Automazione che rimpiazza solo la prima occorrenza di una 
# parola all'interno del glossario 

from GLOSSARY_AUTOMATIONS.read_json import *
from GLOSSARY_AUTOMATIONS.read_all_files import * 

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
        f = open(n, "r")
        content = ""
        content = f.read()
        f.close()

        # rimpiazzo di tutte le occorrenze di una definizione
        # presente nel glossario
        for d in defs:
            ref_string = "\\textit{" + d + "}_G"
            if (d in content or d.lower() in content) and ref_string not in content:
                content = content.replace(d, ref_string)

        # scrittura del contenuto all'interno del file
        f = open(n, "w")
        f.write(content)
        f.close()



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

        # rimpiazzo di tutte le occorrenze di una definizione
        # presente nel glossario
        for d in defs:
            ref_string = "\\textit{" + d + "}_G"
            if done[d] != True and ref_string not in content and (d in content or d.lower() in content):
                # debug
                # print(ref_string)
                content = content.replace(d, ref_string)
                done[d] = True

        # scrittura del contenuto all'interno del file
        f = open(n, "w")
        f.write(content)
        f.close()
