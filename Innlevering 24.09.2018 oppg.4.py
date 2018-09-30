# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:14:06 2018

@author: Johanne
"""
#program som sjekker om et tall n er et heltall større enn 0 og regner ut fakultet til n
print("Dette programmet sjekker om et tall n er et heltall større enn 0, for deretter å regne ut fakultetet til n dersom det oppfyller betingelsene.")

import math       #henter inn mattebiblioteket ettersom vi skal finne fakultetet til n

n=float(input("Skriv inn et vilkårlig tall."))   #bruker float slik at man kan skrive inn alle tall

if n%1==0 and n>=0:                           #programmet sjekker om n er et heltall større enn eller lik 0
    print(math.factorial(n))      #henter kommando for fakultet og får programmet til å regne ut fakultetet til n dersom n er heltall over 0
else:                             #tall som ikke passer med betingelsene i linje 13 får feilmelding
    print("Feilmelding. Tallet er ikke et heltall større enn 0")

