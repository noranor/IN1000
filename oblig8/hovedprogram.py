# Fil 4 av 4
# ---------------- Obligatorisk innlevering nr. 8 -----------------------

# Ettersom fremgangsmåten i denne innleveringen var betydelig mer abstrakt enn hva vi har pleid å hatt, har jeg valgt å ikke strukturere besvarelsen etter deloppgave.
# Kommentarer eller forklaringer til de enkelte kodene er å finne under koden.

from node import Node
from rack import Rack
from regneklynge import Regneklynge
# Importerer class Node fra node.py, class Rack fra rack.py og class Regneklynge fra regneklynge.py.

def hovedprogram():
    abel = Regneklynge(12)
    # Oppretter et objekt "Abel" i Regneklynge med noder_pr_rack = 12.

    for i in range(650):
        sekstifire = Node(64, 1)
        abel.sett_inn_node2(sekstifire)
    # Oppretter 650 Node-objekter med 64 GB minne og 1 prosessor. Alle disse nodene settes inn i objekt Abel gjennom metoden sett_inn_noder2(node) i Regneklynge.

    for i in range(16):
        tusen = Node(1024, 2)
        abel.sett_inn_node2(tusen)
    # Oppretter 16 Node-objekter med 1024 GB minne og 2 prosessor. Alle disse nodene settes inn i objekt Abel gjennom metoden sett_inn_noder2(node) i Regneklynge.

    print("\nNoder med minst 32 GB:", abel.minne(32))
    print("Noder med minst 64 GB:", abel.minne(64))
    print("Noder med minst 128 GB:", abel.minne(128))
    # Kaller på metoden minne() i Regneklynge og setter objekt abels paakrevd_minne til henholdsvis 32, 64 og 128. Metoden går så igjennom alle rackene i regneklyngen og alle nodene i de gitte rackene , og gjengir antallet noder som oppfyller paakrevd_minne.
    print("\nAntall prosessorer:", abel.antall_prosessorer())
    # Kaller på metoden antall_prosessorer() i Regneklynge. Denne returnerer totalt antall prosessorer i regneklyngen.
    print("Antall rack:", abel.antall_racks(), "\n")
    # Kaller på metoden antall_racks() i Regneklynge. Denne returnerer lengden av regneklyngen - altså hvor mange racks som befinner seg i regneklynge abel.

hovedprogram()
# Kjører hovedprogrammet.
