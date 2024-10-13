#Dit zorgt ervoor dat we de functies uit random module kunnen gebruiken, zoals randrange om willekeurige getallen te kiezen
import random

def start_spel(): #functie start_spel die het spel begint
    getal = random.randrange(1, 51) #Dit kiest een willekeurige getal

    print('Welkom bij Raad het nummer!')
    print('Raad een nummer tussen 1 en 50. Je hebt 6 pogingen om het te raden.')
    print('\n')

    for poging in range(1, 7): #Dit zorgt ervoor dat de speler maximaal 6 pogingen krijgt om het getal te raden
        try: #Als het geen geldig getal is, krijgt speler een foutmelding en mag opnieuw proberen
            gok = int(input(f'Poging {poging}: Raad het getal: '))
        except:
            print('Ongeldige invoer, voer een getal in!')
            continue
# Als de gok gelijk is aan het getal, wint de speler en eindigt de loop
        if gok == getal:
            print('Gefeliciteerd! Je hebt het nummer geraden')
            print('Je hebt gewonnen!')
            break
        elif gok < getal:
            print('Te laag! Gok hoger!')
        elif gok > getal:
            print('Te hoog! Gok lager!')
    else: #Als de speler het getal niet heeft geraden binnen 6 pogingen
        print(f'Helaas, je hebt het niet geraden. Het getal was {getal}.')
        print('Volgende keer beter!')

#start_spel()