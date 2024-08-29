import re # import re pro regularni vyrazy

print("-" * 30)
print(f"{'Evidence pojistenych':>25}")
print("-"* 30)

class Urivatelske_prostredi():
    """
    Tato třída poskytuje uživatelské rozhraní pro správu pojištěnců. Umožňuje zobrazení menu s různými možnostmi.
    Třída zajišťuje, že uživatel zadá platná data.
    """

    def __init__(self, evidence):
        self.evidence = evidence

    def nabidka_voleb(self):
        """
        Tato metoda zobrazuje uživateli menu a na základě jeho volby provádí příslušnou akci.
        :return:
        """
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


    def ziskat_platny_vstup(self):
        """
        Získává jednotlivé vstupy od uživatele.
        Předává vstupy metodě pridani_pojisteneho
        :return:
        """
        while True:
            jmeno = self.kontrola_delky_a_typu_dat("jméno", pouze_text= True)
            prijmeni = self.kontrola_delky_a_typu_dat("příjmení", pouze_text= True)
            telefonni_cislo = self.kontrola_delky_a_typu_dat("telefonní číslo", pouze_cisla= True)
            vek = self.kontrola_delky_a_typu_dat("věk", pouze_cisla= True)

            self.evidence.pridani_pojisteneho(jmeno, prijmeni, telefonni_cislo, vek)

            return

    def kontrola_delky_a_typu_dat(self, vstupni_slovo, pouze_text = False, pouze_cisla = False):
        """
        Kontroluje délku vstupu. Kontroluje, zda je vstup text nebo cislo nebo mezery.
        Povoluje pouze písmena a mezery nebo cisla a mezery.
        :param vstupni_slovo:
        :param pouze_text:
        :param pouze_cisla:
        :return:
        """
        while True:
            vstup = input(f"Zadejte {vstupni_slovo}:\n").strip()   # Kontroluje délku vstupu
            if pouze_text:
                # Kontrola, zda je vstup text
                if re.fullmatch(r"[A-Za-z\s]+", vstup):  # Povolit pouze písmena a mezery
                    return vstup
                else:
                    print(f"{vstupni_slovo} musí obsahovat pouze písmena.")
            elif pouze_cisla:
                # Kontrola, zda je vstup číslice nebo mezery
                if re.fullmatch(r"[0-9\s]+", vstup):  # Povolit pouze číslice a mezery
                    return vstup
                else:
                    print(f"{vstupni_slovo} musí obsahovat pouze číslice nebo mezery.")
            else:
                if len(vstup) > 0:
                    return vstup
                else:
                    print(f"{vstupni_slovo} je příliš krátké. Zadejte prosím znovu.")

    def ziskani_vstupu_pro_vyhledavani(self):
        """
        Získává vstup pro metodu vyhledání pojištěného.
        :return:
        """

        hledane_jmeno = input("Zadejte jméno osoby:\n").strip()
        hledane_prijmeni = input("Zadejte příjmení osoby:\n").strip()
        nalezena_osoba = self.evidence.vyhledani_pojisteneho(hledane_jmeno, hledane_prijmeni)
        if nalezena_osoba:
            print(f"Nalezena osoba: {nalezena_osoba}")

        else:
            print(f"Osoba: {hledane_jmeno} {hledane_prijmeni} nebyla nalezena.")
        self.vypis()

    def ukonceni_programu(self):
        while True:
            odpoved = input("\nOpravdu chceš ukončit program ? ano / ne: ").lower()
            if odpoved == "ano":
                exit()
            elif odpoved == "ne":
                break
            else:
                print("Neplatny přikaz, musite zadat ano / ne")

    def vypis(self):
        print()
        print()
        print("Pokračujte libovolnou klavesou")
        input()

