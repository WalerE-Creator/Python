import random

hiddennum = random.randint(1,11)



while True:
    printrules = input("Do you want to read the rules? (y/n)")
    if printrules in ['y','n']:
        print("Great!")
        break
    else:
        print("Nope - gotta be y or n!. Try again...")

        


if printrules == 'y':

    print('''   The rules are:

        You have 10 guesses to guess a random number between 1 & 10,
        you want to guess the number correctly in as few guesses as possible.
        ''')

guessnum = input("Please guess a number between 1 and 10.")

guesses = 1

while True:

    if int(guessnum) == int(hiddennum):

        if guesses < 2:

            print(f'Great job, you got it correct in 1 guess')

        else:
        
            print(f'Great job, you got it correct in {guesses} guesses.')

        break

    else:

        guesses += 1

        print("You got it wrong, please try again")

        guessnum = input("Please guess another number between 1 and 10.")
#to make a hint system


    
