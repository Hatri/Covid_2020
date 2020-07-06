# D subrutine // Oppgave 5
#Skriver ut smittedata for alle land for en dato oppgitt av brukern
from Dato import Dato

def hentDato():
    day = 0
    while True:
        print("Skriv datoen(DD/Format).")
        try:
            day = int(input())
            if 0 < day <= 31:
                break
            else:
                print("Ikke gyldig, prov igjen. ")
        except ValueError:
            print("Ikke gyldig, prov igjen. ")
    month = 0
    while True:
        print("Skriv maanden. (MM/Format)")
        try:
            month = int(input())
            if 0 < month <= 12:
                break
            else:
                print("Ikke gyldig, prov igjen. ")
        except ValueError:
            print("Ikke gyldig, prov igjen. ")
    year = 0
    while True:
        print("Skriv aaret. (YYYY/Format)")
        try:
            year = int(input())
            if year == 2019 or year == 2020:
                break
            else:
                print("Ikke gyldig, prov igjen. ")
        except ValueError:
            print("Ikke gyldig, prov igjen. ")
    try:
        return Dato(day, month, year)
    except Exception:
        return Dato.getInstance(day, month, year)

# Skriver ut data basertt på datoen gitt av brukeren


def saker(data):
    date = hentDato()
    for land in data:
        if land.hentDato() == date:
            print(land.hentNavn() + " hadde " + str(land.smitteStatus()) + " saker i " + str(date))