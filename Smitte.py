#Oppgave 4
class Smitte:

    # Konstrucktør
    def __init__(self, smittet, testet, innlagt, respirator, dode, dato):
        self.__smittet = smittet
        self.__testet = testet
        self.__innlagt = innlagt
        self.__respirator = respirator
        self.__dode = dode
        self.__dato = dato

    # Antall smittede
    def get_infected(self):
        return self.__smittet

    # Antall testet
    def get_tested(self):
        return self.__testet

    # Antall innlagt
    def get_hospitalized(self):
        return self.__innlagt

    # Antall i respirator
    def get_in_icu(self):
        return self.__respirator

    # Antall dode
    def get_dead(self):
        return self.__dode

    def hentDato(self):
        return self.__dato