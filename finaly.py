"""
import main
import trippin
import adv
import app
import gamee
import nowitness
"""
import subprocess
def execute():
    while True:
        num=int(input("Enter a number to access the file: "))
        if num==1:
            subprocess.call("python main.py")
        elif num==2:
            subprocess.call("python trippin.py")
        elif num==3:
            adv
            subprocess.call("python adv.py")
        elif num==4:
            subprocess.call("python app.py")
        elif num==5:
            subprocess.call("python gamee.py")
        elif num==6:
            subprocess.call("python nowitness.py")
        else:
            print("Invalid input!")

execute()
