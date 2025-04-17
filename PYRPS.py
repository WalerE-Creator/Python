import random

score = 0

cpu_input = random.randint(1, 3)

print("Welcome to PYRPS (rock, paper, scissors in python).")

while True:
    cpu_input = random.randint(1, 3)

    user_input = input(
        """Please choose:
                1) Rock
                2) Paper
                3) Scissors

                """
    )

    user_input = int(user_input)

    if user_input not in [1, 2, 3]:
        print("Invalid input! Please try again.")
        continue

    if user_input == 1:
        if cpu_input == 3:
            print("You won!")
            score += 1
            print("Score:", score)
        else:
            print("You lost :(")
            print("Score:", score)

    if user_input == 2:
        if cpu_input == 1:
            print("You won!")
            score += 1
            print("Score:", score)
        else:
            print("You lost :(")
            print("Score:", score)

    if user_input == 3:
        if cpu_input == 2:
            print("You won!")
            score += 1
            print("Score:", score)
        else:
            print("You lost :(")
            print("Score:", score)

    print("\nLet's play again!")
