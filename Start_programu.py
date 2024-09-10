from Sprava_pojistencu import Evidence_pojistenych
from Urivatelske_prostredi import Urivatelske_rozhrani

if __name__ == "__main__":
    seznam =  []
    evidence = Evidence_pojistenych(seznam)
    Urivatelske_rozhrani = Urivatelske_rozhrani(evidence)
    Urivatelske_rozhrani.nabidka_voleb()

