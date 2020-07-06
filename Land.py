#Oppgave 3
class Land:

    # Konstrucktør
    def __init__(self, navn, kode, date, infection_status):
        self.__navn = navn
        self.__date = date
        self.__infection = infection_status
        self.__kode = kode

    def hentNavn(self):
        return self.__navn

    def hentKode(self):
        return self.__kode

    def hentDato(self):
        return self.__date
        
    def smitteStatus(self):
        return self.__infection
