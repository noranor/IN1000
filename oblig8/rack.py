# Fil 2 av 4
# ---------------- Obligatorisk innlevering nr. 8 -----------------------

# Ettersom fremgangsmåten i denne innleveringen var betydelig mer abstrakt enn hva vi har pleid å hatt, har jeg valgt å ikke strukturere besvarelsen etter deloppgave.
# Kommentarer eller forklaringer til de enkelte kodene er å finne under koden.

from node import Node
# Importerer class Node fra node.py

class Rack:
    def __init__(self, maksNoder):
        self._rackListe = []
        self._maksNoder = maksNoder
        # Oppretter kontruktøren til class Rack, definerer racklisten som en liste og definerer maks antall noder racket kan ha som parameter.

    def ledig_plass(self):
        plass = self._maksNoder - len(self._rackListe)
        # "plass" forteller oss om man kan legge node inn i racket eller ikke. Returnerer en bolsk verdi
        if plass != 0:
            return True
            # Så lenge variabelen "plass" ikke er 0, så vil den returnere "True" som en indikasjon på at det er plass.
        else:
            return None
            # Dersom variabelen "plass" er 0, betyr det at all ledig plass er brukt opp og metoden vil ikke returnere noe.

    def sett_inn_node1(self, node):
        # NB! Forskjell på sett_inn_node1(node) som finnes i class Rack og sett_inn_node2(node) som finnes i class Regneklynge.
        self._rackListe.append(node)
        return self._rackListe
        # Setter noder inn i racklisten og returnerer racklisten.

    def prosessorer_pr_rack(self):
        pros_pr_rack = 0
        # Oppretter en tom variabel.
        for node in self._rackListe:
            pros_pr_rack = pros_pr_rack + node.antall_prosessorer()
            # For hver node i racklisten henvises det til metoden antall_prosessorer() i class Node som gjengir hvor mange prosessorer som er i hver node. Den tomme variabelen økes med hvor mange prosessorer som angis etter hver iterasjon.
        return pros_pr_rack
        # Returnerer variabelen med totalt antall prosessorer per rack.

    def noder_med_nok_minne(self, paakrevd_minne):
        nok_minne = 0
        # Oppretter en tom variabel.
        for node in self._rackListe:
            if node.sjekk_minne(paakrevd_minne):
                nok_minne = nok_minne + 1
            # For hver node i racklisten henvises det til metoden sjekk_minne(paakrevd_minne) i class Node som returnerer en bolsk verdi dersom noden oppfyller vilkårende for påkrevd minne. Den tomme variabelen økes med hvor mange True som returneres.
        return nok_minne
        # Returnerer variabelen med totalt antall noder med nok minne per rack.
