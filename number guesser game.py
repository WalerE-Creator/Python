import random


difficulty = input('''Please select your difficulty,
            1) Easy 1-10
            2) Medium 1-20
            3) Hard 1-30''')

highnum = int(difficulty) * 10

while True:
    printrules = input("Do you want to read the rules? (y/n)")
    if printrules in ['y','n']:
        print("Great!")
        break
    else:
        print("Nope - gotta be y or n!. Try again...")

if printrules == 'y':

    print(f'''   The rules are:

        You have 10 guesses to guess a random number between 1 & {highnum} you choose,
        you want to guess the number correctly in as few guesses as possible.
        ''')

guessnum = input(f'Please guess a number between 1 and {highnum}.')

hiddennum = random.randint(1, highnum)

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

        guessnum = input(f'Please guess another number between 1 and {highnum}.')
#to make a hint system
