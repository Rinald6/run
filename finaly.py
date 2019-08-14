import main
import trippin
import adv
import app
import gamee
import nowitness
def execute():
    num=(input("Enter a number to access the file: "))
    if num==1:
        main
    elif num==2:
        trippin
    elif num==3:
        adv
    elif num==4:
        app
    elif num==5:
        gamee
    elif num==6:
        nowitness
    else:
        print("Invalid input!")

execute()