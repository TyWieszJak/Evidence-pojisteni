from Sprava_pojistencu import Evidence_pojistenych
from Urivatelske_prostredi import Urivatelske_prostredi

if __name__ == "__main__":
    seznam =  []
    evidence = Evidence_pojistenych(seznam)
    UI = Urivatelske_prostredi(evidence)
    UI.nabidka_voleb()

"""
26.08.24 - pridat dokumentaci
         - osetrit znaky + cisla v pridavani pojistence
         - prenest validaci a print z pridavani pojistence , nebo pouzit return a vypsat to jinde
         - podle moznosti zkusit pridat nejaky veci navic
"""