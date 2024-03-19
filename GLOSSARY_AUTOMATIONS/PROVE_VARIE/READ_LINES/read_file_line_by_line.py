f = open("uc1_1.tex", "r")

# l'idea di leggere un file riga per riga puó permettere di saltare le righe contenenti titoli. 
# funzione che legge tutte le righe di un singolo file e
# le mette all'interno di una lista 
lines = f.readlines()

not_title_lines = []
titles = ["textbf", "section", "subsection", "subsubsection"]

def check_for_titles(titles: list[str], line: str) -> bool:
    for t in titles:
        if t in line:
            return True
    return False 

for l in lines:
    if not check_for_titles(titles, l):
        not_title_lines.append("{}".format(l.strip()))

print(not_title_lines)