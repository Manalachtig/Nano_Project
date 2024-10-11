#Dit zorgt ervoor dat je de functies van de random module kunt gebruiken, zoals het genereren van willekeurige getallen.
import random

#Dit kiest een willekeurig getal tussen 1 en 50 (inclusief 1, maar exclusief 51).
getal = random.randrange(1,51)

#Dit print een welkomsbericht en legt de regels van het spel uit.
print('Welkom bij Raad het nummer!')
print('Raad een nummer tussen 1 en 50. Je hebt 6 pogingen om het te raden.')
print('\n')

#Dit betekent dat de speler maximaal 6 keer mag raden.
for poging in range(1,7):

#Proberen om een geldige invoer te krijgen: Als de invoer ongeldig is (bijvoorbeeld een letter), wordt een melding weergegeven.
    try:
        gok = int(input(f'Poging {poging}: Raad het getal: '))
    except:
        print("Ongeldig invoer")

    if gok == getal:
        print('Gefeliciteerd! Je hebt het nummer geraden')
        print('Je hebt gewonnen!')
        break
    elif gok < getal:
        print('Te laag! gok hoger')
    if gok > getal:
        print('Te hoog! gok lager')
else:
    print('Helaas, je hebt het niet geraden.')
    print('Volgende keer beter!')
#Als de speler na 6 pogingen het getal nog steeds niet heeft geraden, wordt een bericht weergegeven dat het spel voorbij is.

#bron try/except: YT Giraffe Academy
