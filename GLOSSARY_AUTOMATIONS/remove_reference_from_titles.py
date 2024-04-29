import os
import re

f = open("../sorgenti/Analisi dei Requisiti/uc/uc1_1.tex", "r")
s = f.read()

# questa funzione assume che il testo in latex sia formattato correttamente
def find_all_occurrences(string: str, sub: str):
    dump = string 
    i = string.find(sub) 
    count = 0
    while i != -1:
        # sicuro è stata trovata un'occorenza data la POST di find
        count += 1

        # trovare una parentesi chiusa
        j = string.find("}", i + 1)

        # estrarre la stringa che va da \textbf fino alla parentesi chiusa
        title_string = string[i:j+1]
        print(title_string)
        if "\\textit" in title_string:
            print("trovato riferimento nel titolo")
        i = string.find(sub, i + 1)
    return dump 


print(find_all_occurrences(s, r"\textbf"))