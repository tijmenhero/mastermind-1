import random
import os

def clear():
    os.system("clear")


# Function om het Mastermind bord te printen
def print_mastermind_board(passcode, guess_codes, guess_flags):

    print("-----------------------------------------")
    print("\t      MASTERMIND")
    print("-----------------------------------------")

    print("    |", end="")
    for x in passcode:
        print("\t" + x[:3], end="")
    print()

    for i in reversed(range(len(guess_codes))):
        print("-----------------------------------------")
        print(guess_flags[i][0], guess_flags[i][1], "|")

        print(guess_flags[i][2], guess_flags[i][3], end=" |")
        for x in guess_codes[i]:
            print("\t" + x[:3], end="")

        print()
    print("-----------------------------------------")


# De algemene functie 
if __name__ == '__main__':

    # Lijst van kleuren
    kleuren = ["ROOD", "GROEN", "GEEL", "BLAUW", "ZWART", "ORANJE"]

    # In kaart brengen van kleuren naar nummers
    kleuren_map = {
        1: "ROOD",
        2: "GROEN",
        3: "GEEL",
        4: "BLAUW",
        5: "ZWART",
        6: "ORANJE"
    }

    # Random een code kiezen
    random.shuffle(kleuren)
    passcode = kleuren[:4]

    # Aantal kansen voor de speler
    chances = 10

    # De code die er voor de speler staat
    show_passcode = ['UNK', 'UNK', 'UNK', 'UNK']

    # De code die de speler elke beurt ingevuld heeft
    guess_codes = [['-', '-', '-', '-'] for x in range(chances)]

    # D hints gegeven per beurt
    guess_flags = [['-', '-', '-', '-'] for x in range(chances)]

    clear()

    # De huidige beurt
    turn = 0

    # De Gameloop
    while turn < chances:

        print("-----------------------------------------")
        print(
            "de bedoeling van het spel is om te raden wat de kleuren code is hier voor krijg je hints na maten je een code hebt ingevuld:  z beteknt dat de kleur goed is en op de goede plek staat.       w is dat de kleur klopt maar niet op de goede plek staat      als er niks komt te staan betekent het kleur en plek fout "
        )
        print("-----------------------------------------")
        print("Vul de code in met nummers.")
        print(
            "1 - ROOD, 2 - GROEN, 3 - GEEL, 4 - BLAUW, 5 - ZWART, 6 - ORANJE")
        print("Bijvoorbeeld: ROOD GEEL ORANJE ZWART ---> 1 3 6 5")
        print("-----------------------------------------")
        print_mastermind_board(show_passcode, guess_codes, guess_flags)

        # De input van de speler accepteren
        try:
            code = list(map(int, input("Voer hier je code in = ").split()))
        except ValueError:
            clear()
            print("\tFoute Code! probeer opnieuw!")
            continue

        # Controleren of er 4 cijfers voor de kleuren zijn ingevoerd
        if len(code) != 4:
            clear()
            print("\tFoute Code! probeer opnieuw!")
            continue

        # Controleren of de cijfers ingevoerd overeenkomen met de cijfers van de kleuren
        flag = 0
        for x in code:
            if x > 6 or x < 1:
                flag = 1

        if flag == 1:
            clear()
            print("\tFoute Code! probeer opnieuw!")
            continue

        # Input opslaan
        for i in range(4):
            guess_codes[turn][i] = kleuren_map[code[i]]

        # Proces om hints te geven aanvankelijk van de spelers input
        dummy_passcode = [x for x in passcode]

        pos = 0

        # Loop om de hints te geven aan de speler
        for x in code:
            if kleuren_map[x] in dummy_passcode:
                if code.index(x) == passcode.index(kleuren_map[x]):
                    guess_flags[turn][pos] = 'Z'
                else:
                    guess_flags[turn][pos] = 'W'
                pos += 1
                dummy_passcode.remove(kleuren_map[x])

        random.shuffle(guess_flags[turn])

        # Controleren of je de code geraden hebt
        if guess_codes[turn] == passcode:
            clear()
            print_mastermind_board(passcode, guess_codes, guess_flags)
            print("Gefeliciteerd! Je hebt gewonnen!")
            again = input("wil je nog een keer spelen? (j/n)")
            # als je wil, nog een keer spelen
            if again == "j":
              print_mastermind_board(passcode, guess_codes, guess_flags)
            else:
              print("THE END")
            break

        # Update beurt
        turn += 1
        clear()

# Controleren of je verloren hebt
if turn == chances:
    clear()
    print_mastermind_board(passcode, guess_codes, guess_flags)
    print("Je hebt verloren! Volgende keer beter!")
    again = input("wil je nog een keer spelen? (j/n)")
    # als je wil, nog een keer spelen
    if again == "j":
      print_mastermind_board(passcode, guess_codes, guess_flags)
    else:
      print("THE END")