"""
Budeme vytvaret pojisteneho, ktery bude obsahovat:
jmeno
vek
telefonni cislo
Ma to umiet vypsat vsechny pojistene.
A aby se dalo vyhledat podle jmena.
Dane entity jsou ulozeny  kolekci v pameti
Validace prazdneho jmena ( len() )
12.8.2024 - pridat inputy a vstupy k UI
          - dane pojistencu prejmenovat na pojistenec
          - vypisovat prez str a udelat instanci k tomu
          - predelat spravu pojistencu kde bude v init pouze seznam , seznam pojistencu smazat zeznam a pidat str
"""
from Seznam_pojistencu import Dane_pojistenca
class Evidence_pojistenych():
    def __init__(self):
            self.seznam = []
    def pridani_pojisteneho(self, jmeno, prijmeni, telefonni_cislo, vek):

        novy_pojistenec = Dane_pojistenca(jmeno, prijmeni, telefonni_cislo, vek)

        # Kontroluje, zda jsou jméno a příjmení nebo telefonní číslo duplicitní.
        for osoba in self.seznam:
            if (osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()) or \
                    osoba.telefonni_cislo == telefonni_cislo:
                print(f"Osoba s tímto jménem a příjmením nebo telefonním číslem již existuje.")
                self.vypis()
                return

        # Uklada vstup do seznamu.
        self.seznam.append(novy_pojistenec)
        print("Data byla uložena.")

        self.vypis()

    def vypsat_vsechny_pojistene(self):
        for pojistenec in self.seznam:
            # Vypíše všechny položky v seznamu a text zarovná.
            print(pojistenec)
        self.vypis()



    def vyhledani_pojisteneho(self):
        hledane_jmeno = input("Zadejte jméno osoby:\n")
        hledane_prijmeni = input("Zadejte příjmení osoby:\n")

        for osoba in self.seznam:
            # Program zkontroluje, zda má aktuální osoba vyplněné jméno a příjmení. Pokud ano, pokračuje dál.
            if osoba.jmeno and osoba.prijmeni:
                # Porovnání jména a příjmení.
                if osoba.jmeno.lower() == hledane_jmeno.lower() and osoba.prijmeni.lower() == hledane_prijmeni.lower():
                    # Zobrazení nalezené osoby a text zarovna.
                    print(f"Nalezena osoba: {osoba}")
                    self.vypis()
                    return #osoba
        print(f"Osoba: {hledane_jmeno} {hledane_prijmeni} nebyla nalezena.")
        print()
        return #None

    def vypis(self):
        print()
        print()
        print("Pokračujte libovolnou klavesou")
        input()
