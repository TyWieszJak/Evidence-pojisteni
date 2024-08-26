
from Seznam_pojistencu import Dane_pojistenca

class Evidence_pojistenych():
    def __init__(self,seznam):

            self.seznam = seznam

    def pridani_pojisteneho(self, jmeno, prijmeni, telefonni_cislo, vek):

        novy_pojistenec = Dane_pojistenca(jmeno, prijmeni, telefonni_cislo, vek)


        for osoba in self.seznam:  # Kontroluje, zda jsou jméno a příjmení nebo telefonní číslo duplicitní.
            if (osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()) or \
                    osoba.telefonni_cislo == telefonni_cislo:
                print(f"Osoba s tímto jménem a příjmením nebo telefonním číslem již existuje.")
                return


        self.seznam.append(novy_pojistenec)  # Uklada vstup do seznamu.


    def vypsat_vsechny_pojistene(self):

            return  [str(pojistenec) for pojistenec in self.seznam] # Vypíše všechny položky v seznamu


    def vyhledani_pojisteneho(self,hledane_jmeno,hledane_prijmeni):

        for osoba in self.seznam: # Program zkontroluje, zda má aktuální osoba vyplněné jméno a příjmení. Pokud ano, pokračuje dál.
            if osoba.jmeno and osoba.prijmeni: # Porovnání jména a příjmení.
                if osoba.jmeno.lower() == hledane_jmeno.lower() and osoba.prijmeni.lower() == hledane_prijmeni.lower():
                    return osoba
        return None



