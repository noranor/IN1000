# Fil 3 av 4
# ---------------- Obligatorisk innlevering nr. 8 -----------------------

# Ettersom fremgangsmåten i denne innleveringen var betydelig mer abstrakt enn hva vi har pleid å hatt, har jeg valgt å ikke strukturere besvarelsen etter deloppgave.
# Kommentarer eller forklaringer til de enkelte kodene er å finne under koden.

from node import Node
from rack import Rack
# Importerer class Node fra node.py og class Rack fra rack.py.

class Regneklynge:
    def __init__(self, noder_pr_rack):
        self._noderPerRack = int(noder_pr_rack)
        self._regneklynge = []
        # Oppretter konstruktøren og definerer maksimalt antall noder per rack som et parameter i konstrukøren. En liste for regneklyngen blir også opprettet.

        rack = Rack(self._noderPerRack)
        self._regneklynge.append(rack)
        # Oppretter et rack-objekt inne i Regneklynge sin konstruktør med parameteren som definerer "maksNoder" som parameter i objektet. Dette for at de andre metodene i regneklynge og rack skal ha et objekt å forholde seg til fra starten av.

    def finn_ledig_rack(self):
        for rack in self._regneklynge:
            if rack.ledig_plass():
                return rack
        # Går igjennom for hvert rack i regneklyngen og sjekker hvor mye plass racket har. Dersom det har ledig plass, jf. metoden i class Rack - ledig_plass(), vil finn_ledig_rack() returnere det racket.
        return None
        # Dersom metoden ikke klarer å finne noen ledig rack, så vil den ikke returnere noe.

    def sett_inn_node2(self, node):
        # NB! Forskjell på sett_inn_node1(node) som finnes i class Rack og sett_inn_node2(node) som finnes i class Regneklynge.
        rack = self.finn_ledig_rack()
        # Definerer først et rack etter forrige metode.
        if rack != None:
            rack.sett_inn_node1(node)
        # Dersom returverdien fra finn_ledig_rack() ikke er None(= at det er plass), så vil den bruke sett_inn_node1(node) til å legge til ny node i racket.
        elif rack == None:
            rack = Rack(self._noderPerRack)
            rack.sett_inn_node1(node)
            self._regneklynge.append(rack)
        # Dersom returverdien er None (= at det ikke er noen racks med ledig plass) så vil den først opprette et nytt rack, sette noden inn i dette nye racket, og tilslutt legge racket inn i regneklyngen sammen med alle andre racks.

    def antall_prosessorer(self):
        pros = 0
        # Oppretter en tom variabel.
        for rack in self._regneklynge:
            pros = pros + rack.prosessorer_pr_rack()
            # For hvert rack i regneklyngen henvises det til metoden prosessorer_pr_rack() i class Rack som gjengir hvor mange prosessorer som er i hvert rack. Den tomme variabelen økes med hvor mange prosessorer som programmet finner i hvert rack etter hver iterasjon.
        return pros
        # Returnerer variabelen med totalt antall prosessorer.

    def minne(self, paakrevd_minne):
        minnet = 0
        # Oppretter en tom vaiabel.
        for rack in self._regneklynge:
            minnet = minnet + rack.noder_med_nok_minne(paakrevd_minne)
            # For hvert rack i regneklyngen henvises det til metoden noder_med_nok_minne(paakrevd_minne) i class Rack som returnerer et antall noder med nok minne for hvert rack. Den tomme variabelen økes med hvor stort antall noder_med_nok_minne() returnerer.
        return minnet
        # Returnerer variabelen med totalt antall noder med nok minne.

    def antall_racks(self):
        return len(self._regneklynge)
        # Returnerer lengden av regneklyngen. I dette tilfellet vil det tilsvare hvor mange racks som regneklyngen inneholder.
