print("LET OP: Voer decimalen in als \"5.2\", niet als \"5,2\"")

def gemiddelde(cijfer1, weging1, cijfer2, weging2):
    print("Cijfer 1: " + str(cijfer1)+", weging "+str(weging1))
    print("Cijfer 2: " + str(cijfer2)+", weging "+str(weging2))
    gemiddeld = round(((cijfer1 * weging1 + cijfer2* weging2)/(weging1+weging2)), 1)
    print("Jouw gemiddelde is een " + str(gemiddeld))
    totaleWeging = weging1 + weging2
    print("\n")
    return gemiddeld

    

cijfer1Inp = float(input("Voer cijfer 1 in:\t")) 
weging1Inp = float(input("Voer de weging voor cijfer 1 in:\t")) 

cijfer2Inp= float(input("Voer cijfer 2 in:\t")) or 8.9
weging2Inp = float(input("Voer de weging voor cijfer 2 in:\t")) 

gemiddelde(cijfer1Inp, weging1Inp,cijfer2Inp, weging2Inp,)

print("\nVeel succes met je toetsen!\n\nGemaakt door [NAAM]")