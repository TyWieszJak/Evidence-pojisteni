import re # import re pro regularni vyrazy


class Validator():
    """
    Utility třida, kontroluje delku a typ dat.
    """
    @staticmethod
    def kontrola_delky_a_typu_dat(vstupni_slovo, pouze_text = False, pouze_cisla = False):
        """
        Kontroluje délku vstupu. Kontroluje, zda je vstup text nebo cislo nebo mezery.
        Povoluje pouze písmena a mezery nebo cisla a mezery.
        """
        while True:
            vstup = input(f"Zadejte {vstupni_slovo}:\n").strip()  # Kontroluje délku vstupu
            if len(vstup) > 0:
                if pouze_text:
                    # Kontrola, zda je vstup text
                    if re.fullmatch(r"[A-Za-z\s]+", vstup):  # Povolit pouze písmena a mezery
                        return vstup
                    else:
                        print(f"{vstupni_slovo} musí obsahovat pouze písmena.")
                elif pouze_cisla:
                    # Kontrola, zda je vstup číslice nebo mezery
                    if re.fullmatch(r'^[0-9\s\-()+]+$', vstup):  # Povolit pouze číslice a mezery nebo znaky
                        return vstup
                    else:
                        print(f"{vstupni_slovo} musí obsahovat pouze číslice, znaky (-, +, () ) nebo mezery.")
                else:
                    # Pokud nejsou specifikovány žádné typy, považujeme vstup za platný
                    return vstup
            else:
                print(f"{vstupni_slovo} je příliš krátké. Zadejte prosím znovu.")