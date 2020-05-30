import random

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

res = random.randint(1, 100)

print("This is an interactive guessing game! You have to enter a number between 1 and 99 to find out the secret number. Type 'exit' to end the game. Good luck!")
i = 1
while(True):
    guess = input("What's your guess between 1 and 99?\n")
    if (guess == 'exit'):
        print("Goodbye!")
        exit()
    elif is_integer(guess):
        guess = int(guess)
        if guess == res:
            print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(i))
            break
        elif guess > res :
            print("Too high")
            i = i + 1
            continue
        else : 
            print("Too low")
            i = i + 1
            continue
    else:
        print("That is not a num")


