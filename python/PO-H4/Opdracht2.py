print("LET OP: Voer decimalen in als \"5.2\", niet als \"5,2\"") # Om fouten te voorkomen

def gemiddelde(cijfer1, weging1, cijfer2, weging2): # Maak de functie aan
    print("Cijfer 1: " + str(cijfer1)+", weging "+str(weging1)) # laat cijfer 1 en 2 nogmaals zien, met bijbehordende weging 
    print("Cijfer 2: " + str(cijfer2)+", weging "+str(weging2))

    gemiddeld = round(((cijfer1 * weging1 + cijfer2* weging2)/(weging1+weging2)), 1) # Afronden naar 1 decimaal 

    print("Jouw gemiddelde is een " + str(gemiddeld)) # Stuur het gemiddelde terug naar de gebruiker
    print("\n") # Maak een lege lijn
    return gemiddeld # Stuur het gemiddelde terug en beëindig de functie

    
# Deze variabelen hebben 'Inp' in hun naam, hiermee weet je dat het om de input gaat.\
cijfer1Inp = float(input("Voer cijfer 1 in:\t")) # Vraag om het cijfer
weging1Inp = float(input("Voer de weging voor cijfer 1 in:\t")) or 1 # Vraag om de weging, geen weging => weging = 1

cijfer2Inp= float(input("Voer cijfer 2 in:\t")) # Vraag om het cijfer
weging2Inp = float(input("Voer de weging voor cijfer 2 in:\t")) or 1 # Vraag om de weging, geen weging => weging = 1

gemiddelde(cijfer1Inp, weging1Inp,cijfer2Inp, weging2Inp) # Roep de functies aan met bijbehorende argumenten


print("\nVeel succes met je toetsen!\n\nGemaakt door [NAAM]")