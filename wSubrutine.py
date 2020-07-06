#W subrutine // Oppgave 9
#Skriver datastruckturen laget av nSubrutinen til fil.

def datastruktTilFil(data):
    with open("Oppdatert-Covid-Liste.csv", "w") as file:
        for land in data:
            file.write(land.hentNavn() + "," + land.hentKode() + "," + str(land.hentDato()) + "," +
                       str(land.smitteStatus()) + ",")