from evidence_pojistenych import Evidence_pojistenych
from uzivatelske_rozhrani import Uzivatelske_rozhrani

if __name__ == "__main__":
    seznam =  []
    evidence = Evidence_pojistenych(seznam)
    Uzivatelske_rozhrani = Uzivatelske_rozhrani(evidence)
    Uzivatelske_rozhrani.nabidka_voleb()

