# Fil 1 av 3
# ---------------- Obligatorisk innlevering nr. 7 -----------------------

# Besvarelsen er strukturert ved at oppgavenummer (evt. deloppgavenummer) er skrevet lengst til venstre, og da er det koden under den som tilhører deloppgaven.
# Kommentar til den enkelte kode er rett under koden.

# Oppgave 1
class Celle:
    def __init__(self):
        self._status = "død"

# Oppgave 2
    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

# Oppgave 3
    def erLevende(self):
        if self._status == "levende":
            return True
        elif self._status == "død":
            return False
    # Gir levende/død verdiene True/False

    def tegn(self):
        if self.erLevende():
            return "O"
        else:
            return "."
        # Returnerer konkrete tegn avhengig om statusen er True eller False.
        # Det er dette som utgjør det visuelle som vi kommer til å få opp på terminalen.
