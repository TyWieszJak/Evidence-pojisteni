import re # import re pro regularni vyrazy


class Validace:
    """
        Utility třída pro validaci vstupních dat.

        Tato třída nabízí metody pro kontrolu délky a typu vstupních dat,
        jako jsou textové řetězce a číselné hodnoty. Používá regulární výrazy
        k ověření, zda vstup odpovídá požadovanému formátu.
    """
    @staticmethod
    def kontrola_delky_a_typu_dat(vstupni_slovo, pouze_text = False, pouze_cisla = False):
        """
        Kontroluje, zda vstupní data mají správnou délku a odpovídají požadovanému typu.

        :param vstupni_slovo: Vstupní řetězec, který se má validovat.
        :type vstupni_slovo: str
        :param pouze_text: Pokud je True, ověřuje, že vstup obsahuje pouze písmena a mezery.
        :type pouze_text: bool
        :param pouze_cisla: Pokud je True, ověřuje, že vstup obsahuje pouze číslice.
        :type pouze_cisla: bool

        :return: Vrací True, pokud vstup splňuje požadavky na typ a délku; jinak vrací False.
        :rtype: bool

        Kontrolní podmínky:

        - Pokud `pouze_text=True`, vstupní slovo musí obsahovat pouze písmena a mezery.
        - Pokud `pouze_cisla=True`, vstupní slovo musí obsahovat pouze číslice.
        - Pokud ani jeden parametr není True, vstup je považován za platný.
        0
        """

        if len(vstupni_slovo) > 0:
                if pouze_text:
                        # Kontrola, zda je vstup text
                    if re.fullmatch(r"[A-Za-z\s]+", vstupni_slovo):  # Povolit pouze písmena a mezery
                        return True
                    else:
                        print(f"Vstup musí obsahovat pouze písmena.")
                elif pouze_cisla:
                        # Kontrola, zda je vstup číslice nebo mezery
                    if re.fullmatch(r'^[0-9\s]+$', vstupni_slovo):  # Povolit pouze číslice a mezery nebo znaky
                        return True
                    else:
                        print(f"Vstup musí obsahovat pouze číslice, znaky (-, +, () )")
                else:
                    # Pokud nejsou specifikovány žádné typy, považujeme vstup za platný
                    return True
        else:
            print(f"Vstup je příliš krátký. Zadejte prosím znovu.")
        return False