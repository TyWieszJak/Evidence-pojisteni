
from Sprava_pojistencu import Evidence_pojistenych
from Urivatelske_prostredi import Urivatelske_prostredi

if __name__ == "__main__":
    evidence = Evidence_pojistenych()
    UI = Urivatelske_prostredi(evidence)
    UI.nabidka_voleb()