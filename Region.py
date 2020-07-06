#Oppgave 7
class Region:

    # Konstrucktør
    def __init__(self, navn, kode, flereLand):
        self.__navn = navn
        self.__kode = kode
        self.__flereLand = flereLand
        sum = 0
        forrige = flereLand[0]
        for land in flereLand:
            if land.hentNavn() != forrige.hentNavn():
                sum += forrige.smitteStatus()
        self.__Smitte = sum

    def hentNavn(self):
        return self.__navn

    def hentKode(self):
        return self.__kode

    # Henter totallen antall smittende i regionen
    def get_sum(self):
        return self.__Smitte

    # Henter alle land i regionen
    def hentLand(self):
        return self.__flereLand