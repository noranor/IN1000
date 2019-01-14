# Fil 3 av 3
# ---------------- Obligatorisk innlevering nr. 7 -----------------------
# ------------------------- HOVEDPROGRAM --------------------------------

print("\n")
print("---------------------- Velkommen til ---------------------")
print("---------------------- CELLESPILLET ----------------------")
print("\n")
print("Dette spillet fungerer som en simulering. Den viser \ncellers livsløp. En celles videre utvikling bestemmes av \nfølgende faktorer:\n\nDersom hovedcellen lever og har færre enn to levende naboceller, \nså vil den dø. Dette er en følge av underpopulasjon. Det samme \ngjelder hvis hovedcellen har mer enn tre levende naboceller, men \nda er det snakk om overpopulasjon. Dersom hovedcellen har enten \nto eller tre levende naboer, vil den kunne overleve.\n\nDersom hovedcellen er død, men har nøyaktig tre levende naboer, \nså vil dette forårsake at cellen vil gjenopplives.")
print("\n")
print("Anbefalt størrelse på brettet er mellom 10 og 40")
storrelse = int(input("\nAngi størrelse på brettet: "))
print("\n")

from spillebrett import Spillebrett
objekt = Spillebrett(storrelse, storrelse)

def main():
    generasjon = 0
    valg = 0

    while valg != "q":
        objekt.tegnBrett()
        print("Nåværende generasjon: ", generasjon)
        print("Antall levende celler: ", objekt.finnAntallLevende())
        print("\n")
        valg = input("Press ENTER for å fortsette. Skriv inn q og trykk ENTER for å avslutte.\n>>> ")
        valg.lower()
        generasjon = generasjon + 1
        #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # ***
        objekt.oppdatering()


    print("Spillet er avsluttet.")
    print("Antall generasjoner vært igjennom:", generasjon - 1)
    print("\n")

main()
