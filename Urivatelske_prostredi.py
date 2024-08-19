
from Sprava_pojistencu import Evidence_pojistenych

print("-" * 30)
print(f"{"Evidence pojistenych":>25}")
print("-"* 30)

class Urivatelske_prostredi():

    def __init__(self):
        self.evidence = Evidence_pojistenych()

    def nabidka_voleb(self):
        while True:
            print("Vyberte si akci:")
            print("1 - Pridat nového pojisteného")
            print("2 - Vypsat vsechny pojistené")
            print("3 - Vyhledat pojisteného")
            print("4 - Konec")
            #prehod = Evidence_pojistenych()
            try:
                volba = int(input())
                match volba:
                    case 1:
                        jmeno = self.ziskat_platny_vstup("jméno")
                        prijmeni = self.ziskat_platny_vstup("příjmení")
                        telefonni_cislo = self.ziskat_platny_vstup("telefonní číslo")
                        vek = self.ziskat_platny_vstup("věk")
                        self.evidence.pridani_pojisteneho(jmeno, prijmeni, telefonni_cislo, vek)
                    case 2:
                        self.evidence.vypsat_vsechny_pojistene()
                    case 3:
                        self.evidence.vyhledani_pojisteneho()
                    case 4:
                        self.ukonceni_programu()
                    case _:
                        print("Neplatná volba.")

            except ValueError:
                    print("Neplatná volba.")

    def ukonceni_programu(self):
        while True:
            odpoved = input("\nOpravdu chceš ukončit program ? ano / ne: ").lower()
            if odpoved == "ano":
                exit()
            elif odpoved == "ne":
                break
            else:
                print("Neplatny přikaz, musite zadat ano / ne")

    def ziskat_platny_vstup(self,potrebny_vstup):
        while True:
            # Kontroluje delku vstupu.
            vstup = input(f"Zadejte {potrebny_vstup}:\n").strip()
            if len(vstup) > 0:
                return vstup
            else:
                print(f"{potrebny_vstup} je příliš krátké. Zadejte prosím znovu.")





