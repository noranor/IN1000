# Fil 1 av 4
# ---------------- Obligatorisk innlevering nr. 8 -----------------------

# Ettersom fremgangsmåten i denne innleveringen var betydelig mer abstrakt enn hva vi har pleid å hatt, har jeg valgt å ikke strukturere besvarelsen etter deloppgave.
# Kommentarer eller forklaringer til de enkelte kodene er å finne under koden.

class Node:
    def __init__(self, minne, prosessor):
        self._minne = int(minne)
        self._prosessor = int(prosessor)
        # Oppretter konstruktøren og definerer minne og prosessor per Node.

    def antall_prosessorer(self):
        return self._prosessor
        # Returnerer objektets prosessor.

    def sjekk_minne(self, paakrevd_minne):
        if self._minne >= paakrevd_minne:
            return True
        else:
            return False
        # Sjekker hver node om de oppfyller kravet for påkrevd minne. Det returneres en bolsk verdi: True dersom noden oppfyller kravet og False dersom noden ikke gjør det.
