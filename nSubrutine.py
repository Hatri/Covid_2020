from Dato import Dato
from Land import Land
from dSubrutine import hentDato

# Henter ny informasjon fra bruker

def hentData():
    navn = ""
    while True:
        print("Skriv inn navnet på landet(Engelsk).")
        navn = input()
        if navn != "":
            break
        else:
            print("Prov igjen.")
    kode = ""
    while True:
        print("SKriv koden til landet.(i.e NOR, SWE)")
        kode = input()
        if kode != "" and len(kode) == 3:
            break
        else:
            print("Prov igjen.")
    dato = hentDato()
    smittet = 0
    while True:
        print("Skriv antall smittet på gitt dato.")
        try:
            smittet = int(input())
            if 0 < smittet:
                break
            else:
                print("Skriv antall pasienter.")
        except ValueError:
            print("Prov igjen.")

    return Land(navn,kode,dato,smittet)