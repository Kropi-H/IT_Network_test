from pojisteny import Pojisteny
class SystemEvidence():
    def __init__(self):
        self.pojisteni = []
        self.customer_count = 0

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        self.customer_count += 1