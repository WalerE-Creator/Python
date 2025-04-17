print("Welcome to the PYCalculator!")

num1 = input("Please enter your 1st number")

num2 = input("Please enter your 2nd number")

op = input("Please enter an operator, if you don't know the correct symbol, type ref.")

while True:

    if op == '*':

        print(f'The answer is: {int(num1) * int(num2)}')

        break

    if op == '+':

        print(f'The answer is: {int(num1) + int(num2)}')

        break

    if op == '-':

        print(f'The answer is: {int(num1) - int(num2)}')

        break

    if op == '/':

        print(f'The answer is: {int(num1) / int(num2)}')

        break

    if op == 'ref':

        print('''
                Type * for times
                Type / for divide by
                Type + for addition
                Type - for subtraction
                ''')

        op = input("Please enter an operator, if you don't know the correct symbol, type ref.")



    
