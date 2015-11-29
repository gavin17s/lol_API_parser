#A simple Rock Papers Scissors game vs a RNG computer
#Gavin Su
#http://gavin.su

import random

print("Rock Paper Scissors v0.1 by Gavin Su, http://gavin.su")

def winner(cpuChoice, playerChoice):
	if cpuChoice == "Rock" and playerChoice == "Scissors":
		return 0
	elif cpuChoice == "Rock" and playerChoice == "Paper":
		return 1
	elif cpuChoice == "Paper" and playerChoice == "Rock":
		return 0
	elif cpuChoice == "Paper" and playerChoice == "Scissors":
		return 1
	elif cpuChoice == "Scissors" and playerChoice == "Rock":
		return 1
	elif cpuChoice == "Scissors" and playerChoice == "Paper":
		return 0
	else:
		return 2

rounds = int(input("How many rounds would you like to play? ")) + 1
currentRound = 1
handsDict = {1:"Rock",2:"Paper",3:"Scissors"}
playerHand = ""
playerWins = 0
cpuHand = 0
cpuWins = 0
whoWon = 0

while currentRound != rounds:
	print("Round", currentRound)
	cpuHand = handsDict[random.randrange(1,4)]
	playerHand = handsDict[int(input("The computer has chosen its hand, what would you like to pick?\nEnter 1 for Rock, 2 for Paper, or 3 for Scissors. "))]
	print("...")

	whoWon = winner(cpuHand, playerHand)

	if whoWon == 0:
		print("You chose", playerHand, "and the CPU chose", cpuHand)
		print("The CPU wins this round!")
		cpuWins += 1
	elif whoWon == 1:
		print("You chose", playerHand, "and the CPU chose", cpuHand)
		print("You have won this round!")
		playerWins += 1
	else:
		print("You chose", playerHand, "and the CPU also chose", cpuHand)
		print("You both tied this round!")

	currentRound += 1

if cpuWins > playerWins:
	print("The CPU has won the game with {} win(s) out of {} Round(s).".format(cpuWins, rounds - 1))
elif playerWins > cpuWins:
	print("You have won the game with {} win(s) out of {} Round(s).".format(playerWins, rounds - 1))
else:
	print("The game has ended in a draw!")
