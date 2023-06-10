class Pojisteny():
    def __init__(self, jmeno, prijmeni, vek, telefon, id):
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        self.__vek = vek
        self.__tel_cislo = telefon
        self.__pojistenec_id = id

    def __str__(self):
        return f"{self.__jmeno} {self.__prijmeni} {self.__pojistenec_id}"
