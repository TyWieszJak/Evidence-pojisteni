"""
Budeme vytvaret pojisteneho, ktery bude obsahovat:
jmeno
vek
telefonni cislo
Ma to umiet vypsat vsechny pojistene.
A aby se dalo vyhledat podle jmena.
Dane entity jsou ulozeny  kolekci v pameti
Validace prazdneho jmena ( len() )
"""
from Seznam_pojistencu import Dane_pojistencu
class Evidence_pojistenych(Dane_pojistencu):
    def pridani_pojisteneho(self):
        def ziskat_platny_vstup(potrebny_vstup):
            while True:
                # Kontroluje delku vstupu.
                vstup = input(f"Zadejte {potrebny_vstup}:\n").strip()
                if len(vstup) > 0:
                    return vstup
                else:
                    print(f"{potrebny_vstup} je příliš krátké. Zadejte prosím znovu.")

        # Získání a validace všech vstupů
        self._jmeno = ziskat_platny_vstup("jméno")
        self._prijmeni = ziskat_platny_vstup("příjmení")
        self._telefonni_cislo = ziskat_platny_vstup("telefonní číslo")
        self._vek = ziskat_platny_vstup("věk")


        # Kontroluje, zda jsou jméno a příjmení nebo telefonní číslo duplicitní.
        for osoba in self.seznam:
            if (osoba['jmeno'].lower() == self._jmeno.lower() and osoba['prijmeni'].lower() == self._prijmeni.lower()) or \
                    osoba['telefonni_cislo'] == self._telefonni_cislo:
                print(f"Osoba s tímto jménem a příjmením nebo telefonním číslem již existuje.")
                self.vypis()
                return


        # Uklada vstup do seznamu.
        Evidence_pojistenych.seznam.append({
            'jmeno': self._jmeno,
            'prijmeni': self._prijmeni,
            'telefonni_cislo': self._telefonni_cislo,
            'vek': self._vek
        })
        print("Data byla uložena.")

        self.vypis()

    def vypsat_vsechny_pojistene(self):
        for pojistency in Evidence_pojistenych.seznam:
            # Vypiše všechny položky v seznamu a text zarovna.
            print(f"{pojistency['jmeno']:<10}  {pojistency['prijmeni']:<10} {pojistency['telefonni_cislo']:<10}  {pojistency['vek']:>3}")
        self.vypis()


    def vyhledani_pojisteneho(self):
        hledane_jmeno = input("Zadejte jméno osoby:\n")
        hledane_prijmeni = input("Zadejte příjmení osoby:\n")

        for osoba in self.seznam:
            # Program zkontroluje, zda má aktuální osoba vyplněné jméno a příjmení. Pokud ano, pokračuje dál.
            if osoba['jmeno'] and osoba['prijmeni']:
                # Porovnání jména a příjmení.
                if osoba['jmeno'].lower() == hledane_jmeno.lower() and osoba['prijmeni'].lower() == hledane_prijmeni.lower():
                    # Zobrazení nalezené osoby a text zarovna.
                    print(f"Nalezena osoba:   {osoba['jmeno']:<10}  {osoba['prijmeni']:<10} {osoba['telefonni_cislo']:<10}  {osoba['vek']:>3}")
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
