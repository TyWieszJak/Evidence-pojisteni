
class Dane_pojistenca:
        """
        Třída slouží k ukládání informací o pojištěnci, jméno, příjmení,
        telefonní číslo a věk. Obsahuje metody pro získání těchto atributů a umožňuje
        vrátit informace o pojištěnci.
        """
        def __init__(self,jmeno,prijmeni,telefonni_cislo,vek):
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
            return f"{self.jmeno:<10}  {self.prijmeni:<10} {self.telefonni_cislo:<10}  {self.vek:>3}"

