import random


difficulty = input(
    """Please select your difficulty,
            1) Easy 1-10
            2) Medium 1-20
            3) Hard 1-30
            """
)

highnum = int(difficulty) * 10

while True:
    printrules = input(
        """Do you want to read the rules? (y/n)
"""
    )
    if printrules in ["y", "n"]:
        print("Great!")
        break
    else:
        print("Nope - gotta be y or n!. Try again...")

if printrules == "y":

    print(
        f"""   The rules are:

        You have unlimited guesses to guess a random number between 1 & {highnum} you choose,
        you want to guess the number correctly in as few guesses as possible.
        You can type 99 to get a hint, the limit of hints is three.
        The more guesses you've done the more accurate the hint will be.
        """
    )

guessnum = input(
    f"""Please guess a number between 1 and {highnum}.
                 """
)

hiddennum = random.randint(1, highnum)

guesses = 1

while True:

    if int(guessnum) == int(hiddennum):

        if guesses < 2:

            print(f"Great job, you got it correct in 1 guess")

        else:

            print(f"Great job, you got it correct in {guesses} guesses.")

        break

    else:

        if int(guessnum) == 99:

            if guesses < 2:

                if int(hiddennum) > (highnum / 4):

                    print(f"The number is bigger than {highnum / 4}")

                    guessnum = input(
                        f"""Please guess another number between 1 and {highnum}.
                        """
                    )

                if int(hiddennum) < (highnum / 4) + (2 * (highnum / 4)):

                    print(
                        f"The number is smaller than {(highnum / 4) + (2 * (highnum / 4))}"
                    )

                    guessnum = input(
                        f"""Please guess a number between 1 and {highnum}.
                                     """
                    )

        if int(guessnum) == 99:

            if guesses > 1:

                if guesses < 3:

                    if int(hiddennum) > (highnum / 2):

                        print(f"The number is bigger than {highnum / 2}")

                        guessnum = input(
                            f"""Please guess a number between 1 and {highnum}.
                            """
                        )

                    if int(hiddennum) < (highnum / 2):

                        print(f"The number is smaller than {highnum / 2}")

                        guessnum = input(
                            f"""Please guess a number between 1 and {highnum}.
                            """
                        )

                if guesses > 2:

                    if int(hiddennum) < (highnum / 2):

                        print(f"The number is smaller than {highnum / 4}")

                        guessnum = input(
                            f"""Please guess a number between 1 and {highnum}.
                            """
                        )

                    else:

                        print(f"The number is bigger than {(highnum / 4) * 3}")

                        guessnum = input(
                            f"""Please guess a number between 1 and {highnum}.
                            """
                        )

        else:

            guesses += 1

            print("You got it wrong, please try again")

            guessnum = input(f"Please guess another number between 1 and {highnum}.")
