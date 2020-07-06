# C subrutine
#Skrev denne selv om den ikke var obligatorisk for å teste programmet tidlig.
#Skriver ut smittedata for et land som brukeren oppgir
def lesLand():
    navn = ""
    while True:
        print("Skriv inn navnet på landet(Engelsk).")
        navn = input()
        if navn != "":
            break
        else:
            print("Prov igjen.")
    return navn


# Skriver ut statusen til landet som er lest fra filen

def skrivUtAntallSaker(data):
    navn = lesLand()
    for land in data:
        if land.hentNavn().lower() == navn.lower():
            print(land.hentNavn() + " hadde " + str(land.smitteStatus()) + " saker i "
                  + str(land.hentDato()))