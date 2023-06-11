
from systemevidence import SystemEvidence

evidencnisystem = SystemEvidence()

jmeno = "Petr"
prijmeni = "Vácha"
vek = 13
tel_cislo = "123456789"

evidencnisystem.vytvor_pojisteneho(jmeno, prijmeni, vek, tel_cislo)
evidencnisystem.vytvor_pojisteneho("Marcel", "Vylulánek", 13, "333555777")
evidencnisystem.vypis_pojistencu()

print(evidencnisystem.vrat_posledni_id_uzivatele())

print(evidencnisystem.vrat_uzivatele_podle_jmena_prijmeni("Marcel","Vylulánek"))