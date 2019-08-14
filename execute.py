import os
import time
def main():
    while True:
        try:
            command=input("What app do you want to open? ")
            time.sleep(1)
            os.startfile(command)
        except:
            print("You entered the app's name incorrectly.")
            break
        answer = input("Do you want to set a time limit? ")
        if answer=="yes".lower():
            time_limit=int(input("How many minutes do you want to spend on your app? "))
            time.sleep(time_limit*60)
            os.system("taskkill/im "+command+ ".exe")
            break
        elif answer=="no".lower():
            print("Have fun!")
            break
        else:
            print("Wrong input!")
            break
main()
