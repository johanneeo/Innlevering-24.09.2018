# Innlevering-24.09.2018
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:13:18 2018

@author: Johanne
"""

#pH kalkulator

import math   #henter inn mattebiblioteket ettersom vi må bruke logaritme i koden

print("Dette programmet regner ut pH-verdien i løsningen din.")

ioner=(float(input("Skriv inn antall H+-ioner i mol/L. ")))  #bruker float i tilfelle brukeren vil skrive inn desimaler

pH=-(math.log10(ioner))  #henter logaritme funksjonen fra mattebiblioteket

if 0<=pH<7:  #bruker betingelser for å bestemme om løsningen er sur, basisk eller nøytral
    print("pH-verdien er ", pH)
    print("Løsningen er sur.")
elif pH==7:
    print("pH-verdien er ", pH)
    print("Løsningen er nøytral.")
elif 7<pH<=14:
    print("pH-verdien er ", pH)
    print("Løsningen er basisk.")
else:
    print("Verdien din er ikke på pH-skalaen. Regnet feil?")  #lar alt annet gi feilmelding
