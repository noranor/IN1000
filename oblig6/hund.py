class Hund:

    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt

    def metthet(self):
        self._mett = 10
        return self._mett

    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return self._vekt

    def spring(self):
        mett_spring = self.metthet()
        while mett_spring > 5:
            #mett_spring = self.metthet()
            mett_spring = mett_spring - 1
            if mett_spring <= 5:
                self._vekt -= 1
                print("Hundens vekt etter å ha sprunget er ", self._vekt, " kg.", sep="")
        return self._vekt

    def spis(self):
        tall = int(input("På en skala fra 0 til 10, hvor mett er hunden etter å ha spist?: "))
        mett_spis = self.metthet()
        mett_spis = mett_spis + tall
        print("Metthet etter å ha spist:", mett_spis)
        if mett_spis > 7:
            self._vekt += 1
        print("Hundens vekt er nå ", self._vekt, " kg.", sep="")
