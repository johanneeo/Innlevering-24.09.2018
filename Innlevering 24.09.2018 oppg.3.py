# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:09:39 2018

@author: Johanne
"""

print("Dette programmet regner ut populasjonsendringer innenfor et habitat")

B_nåværende=int(input("Hvor mange dyr er det i dyrepopulasjonen nå?"))  #bruker int her fordi det bare er hele antall dyr i populasjonen

while True:
    t=float(input("Skriv inn antall år som passerer."))  #bruker float for tiden i tilfelle det ikke er hele år som passerer
    a=input("Stiger eller synker populasjonen?")        #spør brukeren om populasjonen stiger eller synker slik at jeg kan bruke betingelser
    if a=="stiger":
        p=float(input("Skriv inn antall prosent dyrepopulasjonen stiger med."))   #bruker float i tilfelle brukeren vil skrive inn desimaler
        B_ny=int(B_nåværende*(1+p/100)**t)
        print("Dyrepopulasjonen er nå på",B_ny,"dyr.")
        break       #legger inn break for at koden skal stoppe
    elif a=="synker":
        p=float(input("Skriv inn antall prosent dyrepopulasjonen synker med."))
        B_ny=int(B_nåværende*(1-p/100)**t)
        print("Dyrepopulasjonen er nå på",B_ny,"dyr.")
        break
    elif a=="ingen av delene":        #kunne ha lagt inn flere alternativer brukeren kunne skrive inn, men programmet hang seg opp
        B_ny=B_nåværende              #uendret antall dyr i populasjonen  
        print("Dyrepopulasjonen er nå på", B_ny, "dyr.")
        break

#har ikke med else fordi koden hang seg opp. Det hadde i så fall meldt om en feilmelding og ledet brukeren tilbake til første spørsmål.