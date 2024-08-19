
class Dane_pojistenca:
        def __init__(self,jmeno,prijmeni,telefonni_cislo,vek):
            self._jmeno = jmeno
            self._prijmeni = prijmeni
            self._telefonni_cislo = telefonni_cislo
            self._vek = vek

        @property
        def jmeno(self):
            return self._jmeno

        @property
        def prijmeni(self):
            return self._prijmeni

        @property
        def telefonni_cislo(self):
            return self._telefonni_cislo

        @property
        def vek(self):
            return self._vek

        def __str__(self):
            return f"{self.jmeno:<10}  {self.prijmeni:<10} {self.telefonni_cislo:<10}  {self.vek:>3}"