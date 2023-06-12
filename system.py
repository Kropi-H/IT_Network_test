class Pozdrav():

    _greet = "{0}\n{1}\n{0}".format("-" * 30, "Evidence pojistenych")

    _menu = "{0}\n{1}\n{2}\n{3}\n{4}".format("Vyberte si akci:",
                                             "1 - Přidat nového pojistníka",
                                             "2 - Vypsat všechny pojištěné",
                                             "3 - Vyhledat pojistného",
                                             "4 - Konec")

    _rozlouceni = "Přeji hezký zbytek dne."

    @staticmethod
    def get_greet():
        return Pozdrav._greet

    @staticmethod
    def get_menu():
        return Pozdrav._menu

    @staticmethod
    def get_rozlouceni():
        return Pozdrav._rozlouceni