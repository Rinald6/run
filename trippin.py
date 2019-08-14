import time
import webbrowser
import os
def main():
    command=input("Enter the url of  what you want to search : ")
    time.sleep(1)
    webbrowser.open_new(command)
    answer=input("Do you want to set a time limit? ")
    if answer=="yes".lower():
        time_limit=int(input("How many minutes do you want to search until browser closes: "))
        time.sleep(time_limit*60)
        os.system("taskkill /im chrome.exe /f")
    else:
      print("Ok, have fun!")

main()