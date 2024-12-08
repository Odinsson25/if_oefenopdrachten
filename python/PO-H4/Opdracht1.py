import math

oppervlakte = float(input("Wat is de oppervlakte van de kamer in m²?"))

if not oppervlakte:
    print("geen geldige input!")

print("De kamer is "+ str(oppervlakte) +" m²")

oppervlakte *= 1.1
oppervlakte = round(oppervlakte,2)
print("Er is "+ str(oppervlakte) +" m² nodig.")

pakken = math.ceil(oppervlakte/2.47)
print("Je hebt "+str(pakken)+" pakken nodig.")

prijs = pakken * 29.62
print("Het kost je €" +str(prijs))

print("\nGemaakt door [NAAM]")