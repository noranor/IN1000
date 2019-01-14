# Innkapsling er når man sorterer metoder tilhørende enkelte klasser, slik at objekter som ligger under den spesifike klassen KUN skal ha tilgang til den klassens metoder. De objektene som tilhører den spesifike klassen har da samme type oppførsel. Dette er nyttig for å få en mer systematisert systemutviklingsprosess. Man driver som oftest med systemutvikling i team. Gitt at du har ansvar for å lage klasser, og andre programmerere har ansvar for å bruke metodene i de diverse klassene, så kan du velge å gjøre enkelte deler av implementasjonen offentlig (public), samtidig som andre deler blir private. De andre i teamet har da kun tilgang på de metodene som ligger under samme klasse som objektet de jobber med.
#EKSEMPEL:
class Test1:

    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def printeSelf1(self):
        print("Navn: ", self._navn, "\n", "Alder: ", self._alder," år", sep="")

class Test2:

    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def printeSelf2(self):
        print("Navn: ", self._navn, "\n", "Alder: ", self._alder, " år", sep="")

objekt_test1 = Test1("Roger", "48") # Setter at objektet skal tilhøre class Test1.
objekt_test1.printeSelf1() # Fungerer fint
objekt_test1.printeSelf2() # Her kaller jeg på en tode som ligger under class Test2. Denne fungerer ikke ettersom metoden ikke hører hjemme under samme klasse som det objektet gjør.

# Grensesnittet til en klasse er de metodene, funkjsonene og dataene som er tilgjengelig for objekter tilhørende den klassen å bruke. Dette skiller seg fra implementasjonen av en klasse ved at du kun får med deg den klassen og dens metoder inn i programmet ditt.
# EKSEMPEL:
# "Lager en ny .py-fil og skriver.. "
from teori import Test1 # Her vil kun de metodene og den informasjonen som er i class Test1 bli tilgjengelig i den nye filen. class Test2 og dens grensesnitt vil ikke bli tilgjengelig ettersom den ikke blir implementert i det nye programmet.

# Instandsmetode er en metode som tilhører et objekt under en gitt klasse. For eksempelet nevnt ovenfor, så vil en instansmetode for et objekt i Test2 være objekt_i_Test2.printeSelf2(). Disse skiller seg fra prosedyrene og funksjonene vi hittil har møtt ved at instansmetodene kun vil fungere på objekter som er laget under samme klasse som dem selv. 
