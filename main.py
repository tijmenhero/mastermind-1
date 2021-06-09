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
