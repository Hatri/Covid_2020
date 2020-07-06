#G Subrutine
#Oppretter en region med smittedata for en gruppe land
from Region import Region

def opprettRegion(data):
    navn = ""
    while True:
        print("Skriv inn region navnet.")
        navn = input().lower()
        if navn != "":
            break
        else:
            print("Navnet kan ikke være tomt, prov igjen.")
    kode = ""
    while True:
        print("Skriv kode for regionen")
        kode = input()
        if kode != "":
            break
        else:
            print("Region koden kan ikke være tomt, prov igjen.")
    leggTilLand = []
    while True:
        print("Skriv landene som skal legges til regionen. Separer med komma.(i.e Norway,Sweden)")
        leggTilLand = input().split(",")
        if len(leggTilLand) != 0:
            break
        else:
            print("Skriv minst et land.")
    flereLand = []
    for i in range(1, len(data)):
        if data[i].hentNavn() in leggTilLand:
            flereLand.append(data[i])

    return Region(navn, kode, flereLand)