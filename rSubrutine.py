#R subrutine //Oppgave 6

#Fjerner alle smitte objekter, og returner en liste av land med 0 saker.
def fjernSmitteObjekter(data):
    for land in data:
        if land.smitteStatus() == 0:
            data.remove(land)
    return data
