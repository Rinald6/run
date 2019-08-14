name=input("Please,enter your name :")
answer=input(name + " would you like to play ?")
if answer=="yes".lower():
    command=input("Would you like to turn left or right ?")
    if command=="right".lower():
        command2=input("You encountered a monster.Would you like to attack or go back?")
        if command2=="attack".lower():
            print("Well done!You defeated the monster.")
        elif command2=="go back".lower():
            print("You failed to go back as the monster killed you.")
        else:
            print("Invalid command.")
    elif command=="left".lower():
        a=input("You met a man.He requests you to cooperate with him.Would you like?")
        if a=="yes".lower():
            print("You killed a lot and won the game!")
        elif a=="no".lower():
            print("The man did not accept your choice,so he killed you.")
        else:
            print("Invalid command!")
    else:
        print("Invalid input!")
elif answer=="no".lower():
    print("That is too bad.Bye!")
else:
    print("Invalid input.")