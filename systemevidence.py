from pojisteny import Pojisteny
class SystemEvidence():

    # Fake pocatecni stav uzivatelu
    pojistenci = [
        ["Marcel", "Malý", 68, "666333111", 15]
    ]

    def __init__(self):
        pass

    # Vytvoření pojisteného a připíchnutí do listu pojistenci
    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = [jmeno, prijmeni, vek, telefon, self.vrat_posledni_id_uzivatele() + 1]
        SystemEvidence.pojistenci.append(pojisteny)

    def vrat_posledni_id_uzivatele(self):
        pojistenec_id = SystemEvidence.pojistenci[-1][-1]
        return pojistenec_id


    def vypis_pojistencu(self):
        column_widths = [max(len(str(item)) for item in column) for column in zip(*SystemEvidence.pojistenci)]
        for jmeno in SystemEvidence.pojistenci:
            for i, width in zip(jmeno, column_widths[:-1]):
                print("{:<{}}".format(i, width), end='\t')
            print()

    def vrat_uzivatele_podle_jmena_prijmeni(self,jmeno,prijmeni):
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        for pojistenec in SystemEvidence.pojistenci:
            if self.__jmeno == pojistenec[0] and self.__prijmeni == pojistenec[1]:
                print(pojistenec)

        
