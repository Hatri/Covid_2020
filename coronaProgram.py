#Importer subrutinene
from Dato import Dato
from Land import Land
from Smitte import Smitte
from Region import Region
from cSubrutine import skrivUtAntallSaker
from dSubrutine import saker
from gSubrutine import opprettRegion
from mSubrutine import hentMaks
from rSubrutine import fjernSmitteObjekter
from nSubrutine import hentData
from wSubrutine import datastruktTilFil


#Global variabler for lagring
landFraFil = []  
landFraBruker = []  
regioner = []  
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


#Funksjon som leser data fra fil og lagrer dem til landFraFil    
# #Datafil hentet fra IN1000 Var2020
def lesFil():
    with open("covid19kunland.csv", "r") as file:
        for line in file.readlines():
            data = line.strip().split(",")
            try:
                chunk = data[2].split(" ")
                date = Dato(int(chunk[1].replace(",", "")),
                            int(months.index(chunk[0].replace("\"", "")) + 1),
                            int(data[3].replace("\"", "")))
                if data[4] == "":
                    data[4] = 0
                landFraFil.append(Land(data[0], data[1], date, int(data[4])))
            except Exception:
                chunk = data[2].split(" ")
                date = Dato.getInstance(int(chunk[1].replace(",", "")),
                                         int(months.index(chunk[0].replace("\"", "")) + 1),
                                         int(data[3].replace("\"", "")))
                if data[4] == "":
                    data[4] = 0
                landFraFil.append(Land(data[0], data[1], date, int(data[4])))


#Menyvalg funksjon for bruker: C, D, G, R, M, Q, R, W
def menyValg():
    while True:
        print("(C) Skriver ut smittedata for et land.")
        print("(D) Skriver ut smittedata for alle land for en dato oppgitt.")
        print("(G) Oppretter en region med smittedata for en gruppe land.")
        print("(M) Finner hvilken dato smitten økte mest for en region.")
        print("(Q) Avslutter programmet")
        print("(N) Legg til ny infomasjon.")
        print("(R) Fjerner alle smitte objekter med smittetall = 0.")
        print("(W) Skriver datastrukturen med ny infomasjon(N) ut til fil.")
        valg = input("Velg: ")
        if valg.lower() != "c" and valg.lower() != "d" and valg.lower() != "g" and \
                valg.lower() != "m" and valg.lower() != "r" and valg.lower() != "w" and \
                valg.lower() != "n" and valg.lower() != "q":
            print("Prov igjen med et gyldig valg.")
        else:
            return valg.lower()



#Oppgave 1, Main-prosedyren

def main():
    global landFraBruker, landFraFil
    lesFil()
    valg = menyValg()
    while valg != "q":
        if valg == "c":
            skrivUtAntallSaker(landFraFil)
        elif valg == "d":
            saker(landFraFil)
        elif valg == "g":
            regioner.append(opprettRegion(landFraFil))
            print("Region laget.")
        elif valg == "m":
            date, region = hentMaks(regioner)
            if date is not None:
                print("De fleste tilfeller i " + region.hentNavn() + " er: " + str(date))
            else:
                print("Regionen finnes ikke")
        elif valg == "n":
            landFraBruker.append(hentData())
            print("Ny info lagret")
        elif valg == "r":
            data = fjernSmitteObjekter(landFraFil)
            landFraFil = data
            print("Fjerner alle smitteobjekter med smittetall = 0.")
        elif valg == "w":
            datastruktTilFil(landFraBruker)
            print("Skriver nye saker ut til mappen med filnavnet: Oppdatert-Covid-Liste.csv")
        valg = menyValg()



#Kjør
main()



