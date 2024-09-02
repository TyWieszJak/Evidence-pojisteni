
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
        """

        novy_pojistenec = Dane_pojistenca(jmeno, prijmeni, telefonni_cislo, vek)
        self.seznam.append(novy_pojistenec)  # Uklada vstup do seznamu.

    def odebrani_pojisteneho(self,jmeno,prijmeni):
        """
        Odebírá pojištěného podle zadaných parametrů.
        """
        osoba = self.najdi_pojistence()
        for osoba in self.seznam:
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
        """
        if hledane_jmeno is not None and hledane_prijmeni is not None:
            return self.najdi_pojistence (hledane_jmeno, hledane_prijmeni)

        return None

    def najdi_pojistence(self,jmeno,prijmeni):
        for osoba in self.seznam:
            if osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower():
                return osoba
        return None
