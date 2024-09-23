
from dane_pojistenca import Dane_pojistenca

class Evidence_pojistenych:
    """
    Třída obsahuje metody používané pro práci s evidencí (přidání, odebirani, vyhledávání, vypsání všech).
    """
    def __init__(self, seznam=None):
        """
        Inicializuje třídu Evidence_pojistenych se seznamem pojištěnců.

        :param self: Odkaz na instanci objektu.
        :param seznam: Seznam pojištěnců, který může být prázdný nebo obsahovat existující záznamy (výchozí hodnota je prázdný seznam).
        """
        if seznam is None:
            seznam = []
        self.seznam = seznam

    def pridani_pojisteneho(self, jmeno, prijmeni, telefonni_cislo, vek):
        """
        Přidává nového pojištěnce do evidence.

        :param self: Odkaz na instanci objektu.
        :param jmeno: Jméno pojištěnce (str).
        :param prijmeni: Příjmení pojištěnce (str).
        :param telefonni_cislo: Telefonní číslo pojištěnce (str).
        :param vek: Věk pojištěnce (int).
        :return: None
        """

        novy_pojistenec = Dane_pojistenca(jmeno, prijmeni, telefonni_cislo, vek)
        self.seznam.append(novy_pojistenec)

    def odebrani_pojisteneho(self,jmeno,prijmeni):
        """
        Odebírá pojištěnce z evidence podle jména a příjmení.

        :param self: Odkaz na instanci objektu.
        :param jmeno: Jméno pojištěnce, který má být odebrán (str).
        :param prijmeni: Příjmení pojištěnce, který má být odebrán (str).
        :return: Odebraný pojištěnec jako objekt Dane_pojistenca, nebo None, pokud pojištěnec nebyl nalezen.
        """

        osoba = self.najdi_pojistence(jmeno,prijmeni)
        if osoba:
            self.seznam.remove(osoba)
            return osoba

    def vypsat_vsechny_pojistene(self):
        """
        Vypíše všechny pojištěnce z evidence.

        :param self: Odkaz na instanci objektu.
        :return: Seznam řetězcových reprezentací všech pojištěnců (list).
        """
        return  [str(pojistenec) for pojistenec in self.seznam]


    def vyhledani_pojisteneho(self,hledane_jmeno,hledane_prijmeni):
        """
        Vyhledá pojištěnce podle zadaného jména a příjmení.

        :param self: Odkaz na instanci objektu.
        :param hledane_jmeno: Jméno pojištěnce, který má být vyhledán (str).
        :param hledane_prijmeni: Příjmení pojištěnce, který má být vyhledán (str).
        :return: Nalezený pojištěnec jako objekt Dane_pojistenca, nebo None, pokud pojištěnec nebyl nalezen.
        """
        return self.najdi_pojistence (hledane_jmeno, hledane_prijmeni)

    def najdi_pojistence(self,jmeno,prijmeni):
        """
        Vyhledá pojištěnce podle zadaného jména a příjmení v evidenci.

        :param self: Odkaz na instanci objektu.
        :param jmeno: Jméno pojištěnce, který má být nalezen (str).
        :param prijmeni: Příjmení pojištěnce, který má být nalezen (str).
        :return: Nalezený pojištěnec jako objekt Dane_pojistenca, nebo None, pokud pojištěnec nebyl nalezen.
        """
        for osoba in self.seznam:
            if osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower():
                return osoba
        return None