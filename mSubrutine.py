#M subrutine // Oppgave 8
#Henter region navn fra input og returnerer
def hentRegion(regioner):
    navn = ""
    while True:
        print("Skriv inn region navnet.")
        navn = input()
        if navn != "":
            break
    for region in regioner:
        if region.hentNavn() == navn.strip():
            return region


# Funskjonen får datoen da infeksjonen spredte seg mest i et gitt område
# Og returnerer navnet til region med datoen med flest smittende. 


def hentMaks(regioner):
    region = hentRegion(regioner)
    if region is not None:
        max = region.hentLand()[0].smitteStatus()
        forrige = region.hentLand()[0].smitteStatus()
        maksLand = region.hentLand()[0]
        for land in region.hentLand():
            if (land.smitteStatus() - forrige) > max:
                max = land.smitteStatus()
                maksLand = land
            forrige = land.smitteStatus()
        return [maksLand.hentDato(), region]
    else:
        return [None, None]
