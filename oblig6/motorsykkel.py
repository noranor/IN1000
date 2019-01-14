class Motorsykkel:
    def __init__(self, merke, regnr, km):
        self._km = km
        self._merke = merke
        self._regnr = regnr

    def kjor(self, antall):
        self._km = self._km + antall
        return self._km

    def hentKilometerstand(self):
        return self._km

    def skrivUt(self):
        print("Motorsykkelen er av merket '",self._merke,"', registreringsnummeret er ", self._regnr," og den har kjørt ", self._km," kilometer.", sep="")

#mot = Motorsykkel("Toyota", 3456, 200)
#mot.skrivUt()
