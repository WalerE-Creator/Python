Name = input("what is your name?")

while True:
    Passw = input("Please make a password at least 8 letters long")
    
    if len(Passw) > 7:

        print("Nice password, thanks!")
        break

    else:

        print("your password isn't long enough, please try again")

while True:
    Usern = input("Please make a username at least 8 letters long")
    if len(Usern) > 7:
            User = "Name " , Name, "Username " , Usern, "Password " , Passw
            print("Your user id is " , User)
            break
    else:
        print("your username isn't long enough, please try again")
