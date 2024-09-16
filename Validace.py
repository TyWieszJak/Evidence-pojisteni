import re # import re pro regularni vyrazy


class Validator():
    """
    Utility třida, kontroluje delku a typ dat.
    """
    @staticmethod
    def kontrola_delky_a_typu_dat(vstupni_slovo, pouze_text = False, pouze_cisla = False):
            """
            Kontroluje délku vstupu a zda odpovídá požadovanému typu.
            vstup: str - vstup uživatele
            pouze_text: bool - True, pokud má být vstup text
            pouze_cisla: bool - True, pokud má být vstup číslo
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