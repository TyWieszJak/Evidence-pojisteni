from Validace import Validator

print("-" * 30)
print(f"{'Evidence pojistenych':>25}")
print("-"* 30)

class Urivatelske_rozhrani:
    """
    Třída poskytuje uživatelské rozhraní pro správu pojištěnců. Umožňuje interakci
    s uživatelem prostřednictvím textového menu, kde může uživatel přidávat, vyhledávat,
    upravovat a odebírat pojištěnce, a také ukončit program.

    :param evidence: Instance třídy EvidencePojistenych, která obsahuje seznam pojištěnců a metody
                     pro manipulaci s nimi.
    """

    def __init__(self, evidence):
        """
        Inicializuje třídu UzivatelskeRozhrani s instancí evidence pojištěnců.

        :param evidence: Instance třídy EvidencePojistenych pro správu pojištěnců.

        """
        self.evidence = evidence


    def nabidka_voleb(self):
        """
        Zobrazuje hlavní menu programu, kde uživatel může vybrat různé akce:
        - Přidání nového pojištěnce
        - Vypsání všech pojištěnců
        - Vyhledání pojištěnce
        - Odebrání pojištěnce
        - Editace pojištěnce
        - Ukončení programu

        Metoda čeká na uživatelskou volbu a poté zavolá příslušnou akci.
        :return: None
        """

        while True :

            print("Vyberte si akci:")
            print("1 - Pridat nového pojisteného")
            print("2 - Vypsat vsechny pojistené")
            print("3 - Vyhledat pojisteného")
            print("4 - Odebrani pojisteného")
            print("5 - Editace pojisteného")
            print("6 - Konec")

            try:
                volba = int(input())

                match volba:
                    case 1:
                        self.pridat_pojistence()
                        self.vypis()
                    case 2:
                        self.vypsat_vsechny()
                        self.vypis()
                    case 3:
                        self.ziskani_vstupu_pro_vyhledavani()
                    case 4:
                        self.odstraneni_pojisteneho()
                    case 5:
                        self.editace_pojisteneho()
                    case 6:
                        self.ukonceni_programu()
                    case _:
                        print("Neplatná volba.")

            except ValueError:
                    print("Neplatná volba.")
            except KeyboardInterrupt:
                print("\nProgram byl přerušen. Ukončuji.")
                break


    def ziskat_platny_vstup(self, typ, vstupni_slovo):
        """
        Získává validovaný vstup od uživatele na základě zadaného typu (text nebo číslo).
        Vstup je kontrolován pomocí validátoru.

        :param typ: Typ vstupu, který uživatel zadává. Možnosti jsou 'text' (pro textové vstupy)
                    a 'cislo' (pro číselné vstupy).
        :param vstupni_slovo: Popis vstupu, který se zobrazí uživateli jako nápověda (např. 'jméno',
                              'telefonní číslo').
        :return: Validovaný uživatelský vstup, který prošel kontrolou délky a typu dat.
        :rtype: str
        """

        while True:
            hodnota = input(f"Zadejte {vstupni_slovo}: ").strip()
            if Validator.kontrola_delky_a_typu_dat(hodnota, pouze_text=(typ == 'text'), pouze_cisla=(typ == 'cislo')):
                return hodnota


    def pridat_pojistence(self):
        """
        Přidává nového pojištěnce po získání platných vstupů.
        Pokud pojištěnec se stejnými údaji již existuje, informuje uživatele
        a akce je zrušena.

        :return: None
        """
        jmeno = self.ziskat_platny_vstup('text', 'jméno')
        prijmeni = self.ziskat_platny_vstup('text', 'příjmení')
        telefonni_cislo = self.ziskat_platny_vstup('cislo', 'telefonní číslo')
        vek = self.ziskat_platny_vstup('cislo', 'věk')

        for osoba in self.evidence.seznam:
            if (osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()) or \
                    osoba.telefonni_cislo == telefonni_cislo:
                print(f"Osoba s tímto jménem a příjmením nebo telefonním číslem již existuje.")
                return

        # Voláme metodu třídy Evidence_pojistenych
        self.evidence.pridani_pojisteneho(jmeno, prijmeni, telefonni_cislo, vek)
        print("Data byla uložena.")


    def ziskani_vstupu_pro_vyhledavani(self):
        """
        Získává od uživatele vstup pro vyhledání pojištěnce na základě jeho jména a příjmení.
        Pokud je pojištěnec nalezen, zobrazí informace o něm.

        :return: tuple(str, str): Jméno a příjmení pojištěnce, pokud je osoba nalezena.
                 tuple(None, None): Pokud osoba nebyla nalezena.
        """

        hledane_jmeno = self.ziskat_platny_vstup('text', 'jméno')
        hledane_prijmeni = self.ziskat_platny_vstup('text', 'příjmení')
        nalezena_osoba = self.evidence.vyhledani_pojisteneho(hledane_jmeno, hledane_prijmeni)
        if nalezena_osoba:
            print(f"Nalezena osoba: {nalezena_osoba}")
            self.vypis()
            #return hledane_jmeno,hledane_prijmeni
        else:
            print(f"Osoba {hledane_jmeno} {hledane_prijmeni} nebyla nalezena.")
        self.vypis()
        return None,None

    def editace_pojisteneho(self):
        """
        Umožňuje editaci údajů pojištěného. Uživatel zadá jméno a příjmení pro vyhledání osoby,
        a pokud je nalezena, může upravit její údaje, jako je jméno, příjmení, telefonní číslo a věk.

        :return: None
        """

        jmeno,prijmeni = self.ziskani_vstupu_pro_vyhledavani()
        nalezena_osoba = self.evidence.vyhledani_pojisteneho(jmeno,prijmeni)

        if nalezena_osoba:
            while True:

                print("Co chcete upravit?")
                print("1 - Jméno")
                print("2 - Příjmení")
                print("3 - Telefonní číslo")
                print("4 - Věk")
                print("5 - Ukončit úpravy")

                try:
                    volba = int(input())

                    match volba:
                        case 1:
                            nove_jmeno = Validator.kontrola_delky_a_typu_dat("nové jméno", pouze_text=True)
                            nalezena_osoba.jmeno = nove_jmeno
                            print(f"Jméno bylo změněno na {nove_jmeno}.")
                        case 2:
                            nove_prijmeni = Validator.kontrola_delky_a_typu_dat("nové příjmení", pouze_text=True)
                            nalezena_osoba.prijmeni = nove_prijmeni
                            print(f"Příjmení bylo změněno na {nove_prijmeni}.")
                        case 3:
                            nove_tel_cislo = Validator.kontrola_delky_a_typu_dat("nové telefonní číslo", pouze_cisla=True)
                            nalezena_osoba.telefonni_cislo = nove_tel_cislo
                            print(f"Telefonní číslo bylo změněno na {nove_tel_cislo}.")
                        case 4:
                            novy_vek = Validator.kontrola_delky_a_typu_dat("nový věk", pouze_cisla=True)
                            nalezena_osoba.vek = novy_vek
                            print(f"Věk byl změněn na {novy_vek}.")
                        case 5:
                            print("Upravy byly ukončeny.\n")
                            break
                        case _:
                            print("Neplatná volba.")
                except ValueError:
                    print("Neplatná volba.")
                except KeyboardInterrupt:
                    print("\nProgram byl přerušen. Ukončuji.")
                    break

    def odstraneni_pojisteneho(self):
        """
        Umožňuje odebrání pojištěného na základě jeho jména a příjmení.
        Pokud je pojištěnec nalezen, je smazán z evidence.

        :return: None
        """
        jmeno, prijmeni = self.ziskani_vstupu_pro_vyhledavani()

        if jmeno and prijmeni:
            if self.potvrdit_akci(f"Opravdu chceš odebrat pojištěného {jmeno} {prijmeni}?"):
                odstranena_osoba = self.evidence.odebrani_pojisteneho(jmeno, prijmeni)
                if odstranena_osoba:
                    print(f"Osoba {jmeno} {prijmeni} byla úspěšně odstraněna.")
                else:
                    print(f"Osoba {jmeno} {prijmeni} nebyla nalezena.")
                self.vypis()

    def ukonceni_programu(self):
        if self.potvrdit_akci("Opravdu chceš ukončit program?"):
            print("Program byl úspěšně ukončen.")
            exit()

    def potvrdit_akci(self, zprava):
        """
        Zobrazuje uživateli zprávu a žádá o potvrzení akce ('ano' nebo 'ne').

        :param self: Instance třídy, která metodu volá.
        :param zprava: str: Zpráva, která se zobrazí uživateli jako výzva k potvrzení akce.

        :return: bool: Vrací True, pokud uživatel potvrdil akci, jinak False.

        """
        while True:
            odpoved = input(f"\n{zprava} ano / ne: ").lower()
            if odpoved == "ano":
                return True
            elif odpoved == "ne":
                return False
            else:
                print("Neplatný příkaz, musíte zadat ano / ne")

    def vypsat_vsechny(self):
        """
        Vypíše všechny pojištěnce, kteří jsou aktuálně uloženi v evidenci.

        :return: None
        """
        print("=" * 60)
        pojistenci = self.evidence.vypsat_vsechny_pojistene()
        for pojistenec in pojistenci:
            print(pojistenec)


    def vypis(self):
        print()
        print()
        print("Pokračujte libovolnou klavesou")
        input()