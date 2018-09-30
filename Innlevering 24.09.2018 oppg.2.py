# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:22:43 2018

@author: Johanne
"""

print("Dette programmet finner den kinetiske energien til et legeme i bevegelse.")

import math  #henter inn mattebiblioteket fordi jeg må bruke kvadratrot senere i koden

variabel=input("Skal du finne E (energi i joule), m (masse i kg) eller v (fart i m/s)?")  #lar brukeren velge hvilken variabel som skal finnes og bruker betingelser i koden nedenfor

E=["E", "e", "energi", "Energi", "energien", "Energien"]   #lager flere muligheter brukeren kan skrive inn for E, m og v slik at koden ikke henger seg opp dersom brukeren skriver inn med eller uten stor bokstav eller bruker ord istedenfor variabel
v=["v", "V", "fart", "Fart", "farten", "Farten"]
m=["m", "M", "masse", "Masse", "massen", "Massen"]


if variabel in E:   #bruker en kommando som heter in for å hente inn E (og m og v under)
    m=(float(input("Skriv inn massen til legemet i kg. ")))  #bruker float for E, m og v slik at brukeren kan bruke desimaler
    v=(float(input("Skriv inn farten til legemet i m/s. ")))
    E=(float((1/2)*m*v**2))
    print("Energien til legemet er", E, "J.")
elif variabel in m:
    v=float(input("Skriv inn farten til legemet i m/s. "))
    E=float(input("Skriv inn energien til legemet i J. "))
    m=(float(2*E)/v**2)
    print("Massen til legemet er", m, "kg.")
elif variabel in v:
    m=float(input("Skriv inn massen til legemet i kg. "))
    E=float(input("Skriv inn energien til legemet i J. "))
    v=(float(math.sqrt((2*E)/m)))  #henter kvadratrot fra mattebiblioteket fordi formelen må omgjøres
    print("Farten til legemet er", v, "m/s.")
else:
    print("Feilmelding. Ukjent variabel. Prøv igjen.")  #lar alt som ikke oppfyller betingelsene gi feilmelding
    
