def innledning(filnavn):
    fil = open(filnavn)
    ordbok = {}
    for linje in fil:
        innhold = linje.strip().split(" ")
        if len(innhold) == 2:
            ordbok[innhold[0].strip()] = innhold[1].strip()
    #nokkel_innhold = str(innhold[0].strip())
    #verdi_innhold = int(innhold[1].strip())
    return ordbok

def maanedensSalgsperson(ordbok):
    forelobig = ""
    mest = 0
    for nokkel_innhold in ordbok:
        print(nokkel_innhold, ":", ordbok[nokkel_innhold])
        tall = int(ordbok[nokkel_innhold])
        if tall > mest:
            mest = tall
            forelobig = nokkel_innhold
    print("\nPersonen som har solgt mest denne måneden er ", forelobig, "med", mest, "salg")

def totaltAntallSalg(ordbok):
    totalt = 0
    for nokkel in ordbok:
        salg = int(ordbok[nokkel])
        totalt = totalt + salg
    print("Totalt salg denne måneden er", totalt,"\n")
    return totalt

def gjennomsnittSalg(ordbok):
    totalt = 0
    for nokkel in ordbok:
        salg = int(ordbok[nokkel])
        totalt = totalt + salg
    gjennomsnitt = totalt / len(ordbok)
    print("Gjennomsnittsalget er", gjennomsnitt, "\n")

def hovedprogram():
    fil = input("Filnavn: ")
    bok = innledning(fil)
    maanedensSalgsperson(bok)
    totaltAntallSalg(bok)
    gjennomsnittSalg(bok)
    antallSelgere = len(bok)
    print("Antall selgere i denne statistikken: ", antallSelgere)

print("\n")
hovedprogram()
print("\n")


#bok = innledning("telefonsalg.txt")
#print(bok)
#maanedensSalgsperson(bok)
#totaltAntallSalg(bok)
#gjennomsnittSalg(bok)
