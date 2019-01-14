# Fil 2 av 3
# ---------------- Obligatorisk innlevering nr. 7 -----------------------

# Besvarelsen er strukturert ved at oppgavenummer (evt. deloppgavenummer) er skrevet lengst til venstre, og da er det koden under den som tilhører deloppgaven.
# Kommentar til den enkelte kode er rett under koden.

from random import randint
from celle import Celle

class Spillebrett:

# Oppgave 1
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner

# Oppgave 1 a)
        self._rutenett = []
        for x in range(self._rader):
            self._rutenett.append([])
            for y in range(self._kolonner):
                self._rutenett[x].append(Celle())
        # Først er rutenettet en tom liste. Deretter legges til en ny tom liste for hver rad. Dette gjør at vi får kolonner. Så legges det til celle-objekter for hver plass i rutenettet som eksisterer.

# Oppgave 1 b)
        self._generasjon = 0

# Oppgave 2
        self.generer()

    def generer(self):
        for x in range(self._rader):
            for y in range(self._kolonner):
                rand = randint(0,3)
                if rand == 3:
                    self._rutenett[x][y].settLevende()
        # Gjør at brettet genererer tilfeldig om celle er levende eller død.

# Oppgave 3
    def tegnBrett(self): # Fungerer
        for x in range(self._rader):
            for y in range(self._kolonner):

# Oppgave 3 a)
                print(self._rutenett[x][y].tegn(),end=" ")
            print()

# Oppgave 3 b) - tømming av terminalvinduet - finner man i main.py. Merker dette med "# ***" i main.py.

# Oppgave 4
    def finnNabo(self, rad, kolonne):
        naboliste = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                naboRad = rad + x
                naboKolonne = kolonne + y
                if (naboRad == rad and naboKolonne == kolonne) != True:
                    if (naboRad < 0 or naboKolonne < 0 or naboRad > self._rader - 1 or naboKolonne > self._kolonner - 1) != True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste

# Oppgave 5
    def oppdatering(self):
        self._generasjon = 0

# Oppgave 5 a)
        celler_som_maa_do = []
        celler_som_maa_leve = []
        # celler_som_maa_do skal endre cellens status til "død" og celler_som_maa_leve skal endre cellens status til "levende".

# Oppgave 5 b)
        rad = 0
        kolonne = 0

        for section in self._rutenett:
            for cell in section:
                naboliste = self.finnNabo(rad, kolonne)
        # Går igjennom for hver del av rutenettet, finner celler og deres tilhørende naber. Setter dette så i en naboliste. Har samme navn her som i metoden finnNabo() for simpelhetens skyld.

                antall_levende = 0
                for nabo in naboliste:
                    if nabo.erLevende() == True:
                        antall_levende = antall_levende + 1
                # Oppretter først en variabel. Går igjennom en celles naboer og sjekker om de er levende. For hver levende nabocelle som finnes, så vil variabelen oppdateres  med + 1.

# ------------> Spillets regler er lagt til som kommentar til hver del av koden;

                if cell.erLevende() == True: # "Dersom cellens nåværende status er 'levende':"
                    if antall_levende > 3 or antall_levende < 2: # "Ved færre en to levende naboceller..." / " Hvis cellen har mer enn tre levende naboceller... "
                        celler_som_maa_do.append(cell) # "... dør cellen" / "... vil den dø."

                    elif antall_levende == 3 or antall_levende == 2: # "Ved to eller tre levende naboceller ..."
                        celler_som_maa_leve.append(cell) # "... vil cellen leve videre."

                elif cell.erLevende() == False: # "Dersom cellen er 'død':"
                    if antall_levende == 3:
                        celler_som_maa_leve.append(cell)
                    # "Cellens status blir 'levende' dersom den har nøyaktig tre levende naboer"

                kolonne = kolonne + 1
            rad = rad + 1
            # For å gå videre til neste kolonne og så videre til neste rad, må ført kolonnene oppdateres med + 1. Når Den har vært igjennom alle kolonnene, så går den igjennom alle radene og oppdaterer variabelen med + 1.
            kolonne = 0
            # Nullstiller "kolonne" før den går videre i programmet.

# Oppgave 5 c)
        for objekt in celler_som_maa_do:
            objekt.settDoed()
        for objekt in celler_som_maa_leve:
            objekt.settLevende()
        # Endrer statusen på de cellene som er plassert i de forskjellige listene.

# Oppgave 5 d)
        self._generasjon =  self._generasjon + 1
        # Oppdaterer generasjonen for hver iterasjon.

# Oppgave 6
    def finnAntallLevende(self):
        totalt_levende = 0
        for x in range(self._rader):
            for y in range(self._kolonner):
                if self._rutenett[x][y].erLevende() == True:
                        totalt_levende = totalt_levende + 1
        return totalt_levende
        # Oppretter først en variabel. Deretter går man igjennom rutenettet, og for hver levende celle man finner, så legger man til + 1 på variabelen.
