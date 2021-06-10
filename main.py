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
    kleuren_map = {1:"ROOD", 2:"GROEN", 3:"GEEL", 4:"BLAUW", 5:"ZWART", 6:"ORANJE"}
 
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
 
    # The current turn
    turn = 0