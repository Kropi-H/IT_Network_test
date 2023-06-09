class Pojisteny():
    pojisteni_id = 0
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        self.__vek = vek
        self.__tel_cislo = telefon
        self.pojisteni_id += 1
        self.pojistenci = []

    def pridat_pojistence(self, pojistenec):
        self.pojistenci.append(pojistenec)
        print(self.pojistenci)

    def __str__(self):
        return f"{self.__jmeno} {self.__prijmeni} {self.pojisteni_id}"
