from systemevidence import SystemEvidence

evidencnisystem = SystemEvidence()

greet = "{0}\n{1}\n{0}".format("-"*30,"Evidence pojistenych",)
menu = "{0}\n{1}\n{2}\n{3}\n{4}".format("Vyberte si akci:",
                      "1 - Přidat nového pojistníka",
                      "2 - Vypsat všechny pojištěné",
                      "3 - Vyhledat pojistného",
                      "4 - Konec")

while True:
    print(greet)
    print(menu)
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
        vek = int(input("Zadejte věk:\n"))
        try:
            vek = int(vek)
        except ValueError:
            print("Věk musí být číslo!")
            pokracovat = input("Pokracovat? Y/N: ")
            if pokracovat != "Y":
                break
        evidencnisystem.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
        input("Data byla uložena, pokračujte libovolnou klávesou...")

    elif vyber == 2:
        evidencnisystem.vypis_pojistencu()
        input("Pokračujte libovolnou klávesou...")
        break
    elif vyber == 3:
        jmeno = input("Zadejte jmeno pojištěného:\n").strip()
        prijmeni = input("Zadejte příjmení pojištěného:\n").strip()
        print(evidencnisystem.vrat_pojistence(jmeno, prijmeni))
        input("Pokračujte libovolnou klávesou...")
        break

    elif vyber == 4:
        break
"""jmeno = "Petr"
prijmeni = "Vácha"
vek = 13
tel_cislo = "123456789"


evidencnisystem.vytvor_pojisteneho("Marcel", "Vylulánek", 13, "333555777")


print(evidencnisystem.vrat_posledni_id_uzivatele())

print(evidencnisystem.vrat_pojistence("Marcel","Vypatlánek"))"""