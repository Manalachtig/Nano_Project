# random module wordt geimporteerd om willekeurig keuzes te kunnen maken
import random

#functie om een woord te kiezen
def kies_woord():
    with open('woordenlijst.txt', 'r') as file: #hier wordt het bestand woordenlijst geopend en lezen we alle woorden
        woorden = file.read().splitlines() #bestand wordt gelezen en gesplitst in afzonderlijke regels, die wordt opgeslagen in lijst woorden
    return random.choice(woorden) #een willekeurig woord wordt gekozen uit de lijst en geretouneerd

#begin van het spel
def play():
    print("Welkom bij galgje!")
    naam = input("Voer je naam in: ")
    woord = kies_woord() #een willekeurig woord wordt gekozen uit kies_woord functie
    woord_aanvullen = '_' * len(woord) #geeft een reeks underscores aan die even lang is als het woord
    poging = 10 #speler krijgt 10 pogingen om het woord te raden

    print(f"Hallo {naam}, je hebt 10 pogingen om het woord te raden\nSpel gaat nu van start!")
    print(woord_aanvullen)
    print("\n")

    while poging > 0 and '_' in woord_aanvullen: #while loop blijft draaien zolang speler nog pogingen over heeft en het woord nog niet volledig is geraden
        gok = input("Raad een letter: ").lower()
        if gok in woord:
            woord_aanvullen = ''.join([letter if letter == gok else wc for letter, wc in zip(woord, woord_aanvullen)]) #als de geraden letter in het woord zit, wordt woord_aanvullen bijgewerkt om de geraden letter op de juiste posities te tonen
            print(f"Goed gedaan, {gok} zit in het woord!")
        else:
            poging -= 1 #als de geraden letter niet in het woord zit, wordt het aantal pogingen met 1 verminderd
            print(f"{gok} zit niet in het woord.")

        print(woord_aanvullen) #de huidige van woorden_aanvullen wordt getoond
        print(f"Resterende pogingen: {poging}") #status van aantal pogingen wordt getoond
        print("\n")

    if '_' not in woord_aanvullen: #als het woord volledig is geraden, wordt je gefeliciteerd
        print(f"Gefeliciteerd {naam}, je hebt het woord geraden! Je hebt gewonnen!")
    else: #als je pogingen op zijn, wordt een bericht getoond met het juiste woord
        print(f"Sorry, je hebt geen pogingen meer. Het woord was '{woord}'. Volgende keer beter!")

#play()
















#bron:list comprehensions, zip function, join method (copilot)