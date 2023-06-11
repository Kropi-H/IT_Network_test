from pojisteny import Pojisteny
class SystemEvidence():
    """
    Třída reprezentuje vytváření a evidování pojištěnců
    """

    #Fake list pojistenců. Jen aby tam nějaký na začátku byl ...
    pojistenci = [
        ["Marcel", "Malý", 68, "666333111", 15]
    ]

    def __init__(self):
        pass


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

    def vrat_uzivatele_podle_jmena_prijmeni(self,jmeno,prijmeni):
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
                self.__result = f"{pojistenec[0]} {pojistenec[1]}"
        if self.__result:
            return self.__result
        else:
            return f"Pojistenec {self.__jmeno} {self.__prijmeni} u nás není evidovaný!"


