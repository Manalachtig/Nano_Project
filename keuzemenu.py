# importeert 2 files
import galgjespel
import raadspel

#print welkoms bericht en menu met 3 keuzes
def keuze_menu():
    print("Welkom bij Discovery App!\n")
    print("Maak een keuze")
    print("1. Galgje spel")
    print("2. Raad het nummer spel")
    print("3. Afsluiten")

def keuze():
    while True: #deze functie draait oneindig door, herhaalt het keuze menu en die de gebruiker vraagt om een keuze te maken
        keuze_menu() #afspelen van keuze menu
        keuze = input("Maak een keuze: ") #invoer van gebruiker wordt opgeslagen in variable keuze
        try: #try blok om fouten op af te handelen
            if keuze == '1':
                galgjespel.play() #de play functie wordt aangeroepen uit file galgjespel
            elif keuze == '2':
                raadspel.start_spel() #de start_spel functie wordt aangeroepen uit file raadspel
            elif keuze == '3':
                print("Tot ziens!")
                break #programma stopt met runnen
            else:
                print("\nOngeldige keuze, probeer opnieuw.") #als de gebruiker een ongeldig keuze invoert, wordt een foutmelding weergeven
        except:
            print("Er is een fout opgetreden.") #als er een fout optreedt tijdens de uitvoering van het gekozen spel, wordt een foutmelding afgedrukt


if __name__ == "__main__":
    keuze()

