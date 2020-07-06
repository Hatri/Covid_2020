# Liste av mnd for å konvertere dataene som er lest fra filen til riktig månednummer.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


#Oppgave2
class Dato:
    instanceList = []

    # statisk metode for å hente et objekt fra listen hvis objektet allerede eksisterer
    @staticmethod
    def getInstance(dag, month, year):
        for instance in Dato.instanceList:
            if instance.getDay() == dag and instance.getMonth() == month and instance.getYear() == year:
                return instance
        return Dato(dag, month, year)

    def getDay(self):
        return self.__day

    def getMonth(self):
        return self.__month

    def getYear(self):
        return self.__year

    # Konstruktør oppretter bare objektet hvis det er ikke allerede er opptrett.
    def __init__(self, dag, month, year):
        for instance in Dato.instanceList:
            if instance.getDay() == dag and instance.getMonth() == month and instance.getYear() == year:
                raise Exception("Dato objektet eksisterer allerede.")
        else:
            self.__day = dag
            self.__month = month
            self.__year = year
            self.instanceList.append(self)

    # Sjekker likhet mellom to datoer
    def __eq__(self, other):
        if self.__year == other.getYear() and self.__day == other.getDay() and self.__month == other.getMonth():
            return True
        return False

    # representasjon av dataobjekt
    def __str__(self):
        return str(months[self.__month - 1]) + " " + str(self.__day) + ", " + str(self.__year)
