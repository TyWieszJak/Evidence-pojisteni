
class Dane_pojistenca:
        """
    Třída slouží k ukládání informací o pojištěnci, včetně jména, příjmení,
    telefonního čísla a věku. Obsahuje metody pro získání a nastavení těchto atributů
    a také pro vracení informací o pojištěnci ve formátu řetězce.

    Atributy:
    ----------
    _jmeno : str: Jméno pojištěnce.
    _prijmeni : str: Příjmení pojištěnce.
    _telefonni_cislo : str: Telefonní číslo pojištěnce.
    _vek : int: Věk pojištěnce.
    """
        def __init__(self,jmeno,prijmeni,telefonni_cislo,vek):
            """
            Inicializuje instanci třídy Dane_pojistenca s údaji o pojištěnci.

            :param self: Instance třídy Dane_pojistenca.
            :param jmeno: str : Jméno pojištěnce.
            :param prijmeni: str: Příjmení pojištěnce.
            :param telefonni_cislo: str: Telefonní číslo pojištěnce.
            :param vek: int: Věk pojištěnce.
            """

            self._jmeno = jmeno
            self._prijmeni = prijmeni
            self._telefonni_cislo = telefonni_cislo
            self._vek = vek

        @property
        def jmeno(self):
            return self._jmeno

        @jmeno.setter
        def jmeno(self, nove_jmeno):
            self._jmeno = nove_jmeno

        @property
        def prijmeni(self):
            return self._prijmeni

        @prijmeni.setter
        def prijmeni(self, nove_prijmeni):
            self._prijmeni = nove_prijmeni

        @property
        def telefonni_cislo(self):
            return self._telefonni_cislo

        @telefonni_cislo.setter
        def telefonni_cislo(self, nove_telefonni_cislo):
            self._telefonni_cislo = nove_telefonni_cislo

        @property
        def vek(self):
            return self._vek

        @vek.setter
        def vek(self, novy_vek):
            self._vek = novy_vek

        def __str__(self):
            """
            Vrátí informace o pojištěnci jako formátovaný řetězec.

            :return: str: Formátovaný řetězec s informacemi o pojištěnci.
            """

            return f"{self.jmeno:<10}  {self.prijmeni:<10} {self.telefonni_cislo:<20}  {self.vek:>3}"

