# First iteration of guess game
import random
print("What is your name? ")
name = input()
print("Why hello " + name + ", I am thinking of a number between 1 and 20. You have 6 chances to guess the correct number.")
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print("Take a guess!")
    playerGuess = int(input())

    if playerGuess < secretNumber:
        print("Your guess is too low.")

    elif playerGuess > secretNumber:
        print("Your guess was too high.")

    else:
        break

if playerGuess == secretNumber:
    print("Congratulations " + name + "! your guess of " + str(playerGuess) + " was correct! And you did it in " + str(guessTaken) + " guesses!")
else:
    print("Sorry you ran out of guesses. The correct answer was " + str(secretNumber))
