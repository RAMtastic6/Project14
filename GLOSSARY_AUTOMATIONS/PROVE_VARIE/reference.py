import os

# string.replace()
# questo metodo consente anche di rimpiazzare solamente la prima delle occorrenze
# di una stringa all'interno di un'altra stringa.

f = open("uc1.tex", "r")
uc_text = f.read()

s = "utente"
s_replacement = "reference_to_glossary"

def is_in(input: str, s: str) -> bool:
    if s in input:
        return True
    else:
        return False

if is_in(uc_text, s):
    print("trovata occorrenza")
    uc_text = uc_text.replace(s, s_replacement, 1) #modo per rimpiazzare solo la prima occorrenza di una stringa 

print(uc_text)