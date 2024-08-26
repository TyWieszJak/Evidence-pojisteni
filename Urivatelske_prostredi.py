from re import match

from Sprava_pojistencu import Evidence_pojistenych

print("-" * 30)
print(f"{'Evidence pojistenych':>25}")
print("-"* 30)

class Urivatelske_prostredi():

    def __init__(self, evidence):
        self.evidence = evidence

    def nabidka_voleb(self):
        while True :
            print("Vyberte si akci:")
            print("1 - Pridat nového pojisteného")
            print("2 - Vypsat vsechny pojistené")
            print("3 - Vyhledat pojisteného")
            print("4 - Konec")
            try:
                volba = int(input())
                match volba:
                    case 1:
                        self.ziskat_platny_vstup()
                        print("Data byla uložena.")
                        self.vypis()
                    case 2:
                        pojistenci = self.evidence.vypsat_vsechny_pojistene()
                       # print(f"{"Jmeno":<10}  {"Prijmeni":<10} {"Telefonni_cislo":<10}  {"Vek":>3}\n")
                        for pojistenec in pojistenci:
                            print(pojistenec)
                        self.vypis()
                    case 3:
                        self.ziskani_vstupu_pro_vyhledavani()
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

    def ziskat_platny_vstup(self):
        while True:
            # Získává jednotlivé vstupy od uživatele
            jmeno = self.kontrola_delky_vstupu("jméno")
            prijmeni = self.kontrola_delky_vstupu("příjmení")
            telefonni_cislo = self.kontrola_delky_vstupu("telefonní číslo")
            vek = self.kontrola_delky_vstupu("věk")

            # Předává vstupy metodě pridani_pojisteneho
            for osoba in self.evidence.seznam:  # Kontroluje, zda jsou jméno a příjmení nebo telefonní číslo duplicitní.
                if (osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()) or \
                        osoba.telefonni_cislo == telefonni_cislo:
                    print (f"Osoba s tímto jménem a příjmením nebo telefonním číslem již existuje.")
            self.evidence.pridani_pojisteneho(jmeno, prijmeni, telefonni_cislo, vek)

            return

    def kontrola_delky_vstupu(self, vstupni_slovo):
        while True:
            vstup = input(f"Zadejte {vstupni_slovo}:\n").strip()   # Kontroluje délku vstupu
            if len(vstup) > 0:
                return vstup
            else:
                print(f"{vstupni_slovo} je příliš krátké. Zadejte prosím znovu.")

    def ziskani_vstupu_pro_vyhledavani(self):

        hledane_jmeno = input("Zadejte jméno osoby:\n").strip()
        hledane_prijmeni = input("Zadejte příjmení osoby:\n").strip()
        nalezena_osoba = self.evidence.vyhledani_pojisteneho(hledane_jmeno, hledane_prijmeni)
        if nalezena_osoba:
            print(f"Nalezena osoba: {nalezena_osoba}")

        else:
            print(f"Osoba: {hledane_jmeno} {hledane_prijmeni} nebyla nalezena.")
        self.vypis()

    def vypis(self):
        print()
        print()
        print("Pokračujte libovolnou klavesou")
        input()

