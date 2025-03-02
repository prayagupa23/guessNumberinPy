import random
#generate random numbers by importing the 'random' module in python.
num = random.randint(1,50)

print("-----Number Guessor-----")
print("Rules:\n")
print("1.User enters a number in a specified range.\n")
print("2.The number generated randomly is checked if it matches the user's input\n")
print("3.Gives hints to the user based on the guess by the user!\n")

while(1):
    #input from users to guess a number in the range 1-50
    guessNumber = int(input("Enter a number in range 1-50: "))
    if guessNumber==num:
        print("Yippee! Number Guessed correctly.\n")
        break
    elif guessNumber<num:
        print("Too Low! get up dawg, guess again.\n")
    elif guessNumber>num:
        print("Too high! take a slight dig dawg.\n")
    elif abs(num-guessNumber)<=5:
        print("You are close! Keep trying.\n")
print("End\n")