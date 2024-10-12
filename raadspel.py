import random

def start_spel():
    getal = random.randrange(1, 51)

    print('Welkom bij Raad het nummer!')
    print('Raad een nummer tussen 1 en 50. Je hebt 6 pogingen om het te raden.')
    print('\n')

    for poging in range(1, 7):
        try:
            gok = int(input(f'Poging {poging}: Raad het getal: '))
        except:
            print('Ongeldige invoer, voer een getal in!')
            continue

        if gok == getal:
            print('Gefeliciteerd! Je hebt het nummer geraden')
            print('Je hebt gewonnen!')
            break
        elif gok < getal:
            print('Te laag! Gok hoger!')
        elif gok > getal:
            print('Te hoog! Gok lager!')
    else:
        print(f'Helaas, je hebt het niet geraden. Het getal was {getal}.')
        print('Volgende keer beter!')


