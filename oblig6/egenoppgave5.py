class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def leggTilHobbyer(self):
        hobbyer = []
        tekst = 0
        print("\nPress ENTER for å ikke legge til flere hobbyer.")
        while tekst != "":
            tekst = input("Hvilke hobbyer har personen?: ")
            hobbyer.append(tekst)
        if tekst == "":
            hobbyer.remove("")
            return hobbyer

    def skrivHobbyer(self):
        lista = self.leggTilHobbyer()
        print("\nDette er hobbyene til ", self._navn, ": ", sep="")
        for innhold in lista:
            print(innhold)
        print("\n")

    def skrivUt(self):
        print("\nNavn: ", self._navn)
        print("Alder: ", self._alder)
        objekt.skrivHobbyer()

navn = str(input("Hva heter personen?: "))
alder = int(input("Hvor gammel er personen?: "))
objekt = Person(navn, alder)
#objekt.leggTilHobbyer()
objekt.skrivUt()
