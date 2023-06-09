from pojisteny import Pojisteny
from systemevidence import SystemEvidence

evidencnisystem = SystemEvidence()

karel = evidencnisystem.vytvor_pojisteneho("Karel", "Vácha", 13, 123456789)
evidencnisystem.vytvor_pojisteneho("Petr", "Nezbeda", 69, 987654321)


print(f"{evidencnisystem.customer_count}")