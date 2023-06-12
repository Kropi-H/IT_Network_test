from system import Pozdrav
import time
class SystemEvidence():
    """
    Třída reprezentuje vytváření a evidování pojištěnců
    """

    #Fake list pojistenců. Jen aby tam nějaký na začátku byl ...
    pojistenci = [
        ["Marcel","Malý",68,"666333111",15]
    ]

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        """
        Vytvoření pojistného vložením (jmeno, prijmeni,vek, telefon)
        :param: jmeno
        :param: prijmeni
        :param: vek
        :param: telefon
        Navýšíme poslední číslo id z pojistenci (zavoláním metody vrat_posledni_id_uzivatele) a navýšíme o jedna
        :return: Vytvoření pojisteného a jeho přidání do listu pojistenci
        """
        pojisteny = [jmeno, prijmeni, vek, telefon, self.vrat_posledni_id_uzivatele() + 1]
        SystemEvidence.pojistenci.append(pojisteny)
        self.__plnoletost = (vek>=18)

    def vrat_posledni_id_uzivatele(self):
        """
        Není to nezbytné, jenom mě zajímala implementace - (databáze by se o to postarala sama)
        :return:Vrací poslední id uživatele.
        """
        pojistenec_id = SystemEvidence.pojistenci[-1][-1]
        return pojistenec_id

    def vypis_pojistencu(self):
        """
        :return:Vypisuje pojištěnce z listu pojistenci do zarovnané tabulky
        """
        column_widths = [max(len(str(item)) for item in column) for column in zip(*SystemEvidence.pojistenci)]
        for jmeno in SystemEvidence.pojistenci:
            for i, width in zip(jmeno, column_widths[:-1]):
                print("{:<{}}".format(i, width), end='\t')
            print()

    def vyhledej_pojistence(self,jmeno,prijmeni):
        """
        Vrací uzivatele, kterého hledáme v listu pojistenci podle jmena a prijmeni nebo string o nenalezeni
        Hledáni jsou podle indexů pojistenec[0] a pojistenec[1]
        :param jmeno:
        :param prijmeni:
        :return: __result jako uživatele nebo string o neúspěšném hledání
        """
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        self.__result = str()
        for pojistenec in SystemEvidence.pojistenci:
            if self.__jmeno == pojistenec[0] and self.__prijmeni == pojistenec[1]:
                self.__result = f"{pojistenec[0]}\t{pojistenec[1]}\t{pojistenec[2]}\t{pojistenec[3]}"
        if self.__result:
            return self.__result
        else:
            return f"Pojistenec {self.__jmeno} {self.__prijmeni} u nás není evidovaný!"

    def vrat_pojistence(self, jmeno, prijmeni):
        return self.vyhledej_pojistence(jmeno, prijmeni)

class Programrun():
    evidencnisystem = SystemEvidence()

    while True:
        print(Pozdrav.get_greet())
        print(Pozdrav.get_menu())
        vyber = input()
        try:
            vyber = int(vyber)
        except ValueError:
            print("Výběr musí být číslo")
            pokracovat = input("Pokracovat? Y/N: ")
            if pokracovat != "Y":
                break

        if vyber == 1:
            jmeno = input("Zadejte jméno pojištěného:\n").strip()
            prijmeni = input("Zadejte příjmení pojištěného:\n").strip()
            telefon = input("Zadejte telefonní číslo:\n").strip()
            vek = input("Zadejte věk:\n")
            try:
                vek = int(vek)
                evidencnisystem.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
                input("Data byla uložena, pokračujte libovolnou klávesou...")
            except ValueError:
                print("Věk musí být číslo!")
                pokracovat = input("Pokracovat? Y/N: ")
                if pokracovat != "Y":
                    break

        elif vyber == 2:
            evidencnisystem.vypis_pojistencu()
            input("Pokračujte libovolnou klávesou...")


        elif vyber == 3:
            jmeno = input("Zadejte jmeno pojištěného:\n").strip()
            prijmeni = input("Zadejte příjmení pojištěného:\n").strip()
            print(evidencnisystem.vrat_pojistence(jmeno, prijmeni))
            input("Pokračujte libovolnou klávesou...")


        elif vyber == 4:
            print(Pozdrav.get_rozlouceni())
            time.sleep(1)
            break