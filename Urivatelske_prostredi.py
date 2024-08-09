
from Sprava_pojistencu import Evidence_pojistenych

print("-" * 30)
print(f"{"Evidence pojistenych":>25}")
print("-"* 30)

class Urivatelske_prostredi():

    def nabidka_voleb(self):
        while True:
            print("Vyberte si akci:")
            print("1 - Pridat nového pojisteného")
            print("2 - Vypsat vsechny pojistené")
            print("3 - Vyhledat pojisteného")
            print("4 - Konec")
            prehod = Evidence_pojistenych(None,None,None,None)
            try:
                volba = int(input())
                match volba:
                    case 1:
                        prehod.pridani_pojisteneho()
                    case 2:
                        prehod.vypsat_vsechny_pojistene()
                    case 3:
                        prehod.vyhledani_pojisteneho()
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

    #def __str__(self):
    #    return f"{self.nabidka_voleb()}"




