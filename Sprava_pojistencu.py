
from Seznam_pojistencu import Dane_pojistenca

class Evidence_pojistenych():
    """
    Třída obsahuje metody používané pro práci s evidencí (přidání, odebirani, vyhledávání, vypsání všech).
    """
    def __init__(self,seznam):

            self.seznam = seznam

    def pridani_pojisteneho(self, jmeno, prijmeni, telefonni_cislo, vek):
        """
        Metoda získává data z uživatelského rozhraní a kontroluje.
        Přidává záznam do seznamu.
        :param jmeno:
        :param prijmeni:
        :param telefonni_cislo:
        :param vek:
        :return:
        """

        novy_pojistenec = Dane_pojistenca(jmeno, prijmeni, telefonni_cislo, vek)
        self.seznam.append(novy_pojistenec)  # Uklada vstup do seznamu.

    def odebrani_pojisteneho(self,jmeno,prijmeni):
        """
        Odebírá pojištěného podle zadaných parametrů.
        """
        for osoba in self.seznam:
            if osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower():
                self.seznam.remove(osoba)
                return osoba

    def vypsat_vsechny_pojistene(self):
            """
             Vypíše všechny položky v seznamu
            """
            return  [str(pojistenec) for pojistenec in self.seznam]


    def vyhledani_pojisteneho(self,hledane_jmeno,hledane_prijmeni):
        """
        Kontrola jmena  a příjmení. A vyhledani v seznamu.
        :param hledane_jmeno:
        :param hledane_prijmeni:
        :return:
        """
        for osoba in self.seznam: # Program zkontroluje, zda má aktuální osoba vyplněné jméno a příjmení. Pokud ano, pokračuje dál.
            if osoba.jmeno and osoba.prijmeni:
                if osoba.jmeno.lower() == hledane_jmeno.lower() and osoba.prijmeni.lower() == hledane_prijmeni.lower():
                    return osoba
        return None



