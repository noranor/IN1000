from motorsykkel import Motorsykkel

def hovedprogram():
    obj1 = Motorsykkel("Toyota", "DK 4485", 5000)
    obj2 = Motorsykkel("Honda", "ZZ 3256", 8500)
    obj3 = Motorsykkel("Suzuki", "HB 9810", 100)
    liste_sykler = [obj1, obj2, obj3]
    for sykler in liste_sykler:
        sykler.skrivUt()
    print("\n")
    obj3.kjor(10) #Oppdaterer antall kilometer kjørt med 10
    print(obj3._merke,"'en kjører 10 km ekstra. Den nye kilometerstanden dens er på ", obj3.hentKilometerstand(), " kilometer.", sep="")

hovedprogram()
