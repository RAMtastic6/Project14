# importare le automazioni
import os
from GLOSSARY_AUTOMATIONS.build_glossary import build_glossario
from GLOSSARY_AUTOMATIONS.reference_automations import * 

# definizione di tutti i path
PATH_TO_GLOSSARY_FOLDER = os.path.join(os.getcwd(), "sorgenti", "Glossario/")
PATH_TO_GLOSSARY_JSON = os.path.join(os.getcwd(), "sorgenti", "Glossario/glossario.json")
PATH_TO_AR_FOLDER = os.path.join(os.getcwd(), "sorgenti", "Analisi dei Requisiti/")
PATH_TO_PDP_FOLDER = os.path.join(os.getcwd(), "sorgenti", "Piano_Di_Progetto/")
PATH_TO_WOW_FOLDER = os.path.join(os.getcwd(), "sorgenti", "Norme di Progetto/")
PATH_TO_PDW_FOLDER = os.path.join(os.getcwd(), "sorgenti", "Piano_Di_Qualifica/")

# eseguire automazioni
# 1. build del glossario
build_glossario(PATH_TO_GLOSSARY_FOLDER)
#repl_all_occurrences(PATH_TO_GLOSSARY_JSON, "sorgenti/Analisi dei Requisiti/main.tex", "sorgenti/Analisi dei Requisiti/uc/")
#repl_all_occurrences(PATH_TO_GLOSSARY_JSON, "sorgenti/Piano_Di_Progetto/main.tex", "sorgenti/Piano_Di_Progetto/sections/", "sorgenti/Piano_Di_Progetto/periodi/")
#repl_all_occurrences(PATH_TO_GLOSSARY_JSON, "sorgenti/Piano_Di_Qualifica/main.tex", "sorgenti/Piano_Di_Qualifica/sections/")
repl_all_occurrences(PATH_TO_GLOSSARY_JSON, "sorgenti/Norme di Progetto/main.tex", "sorgenti/Norme di Progetto/Contents/")
