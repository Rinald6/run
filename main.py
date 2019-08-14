import os
def main():
    answer=input("Enter the file you want to check:")
    answer2=print(os.path.isfile(answer))
    if answer2==True:
        print("The file exists")
    else:
        print("The file doesn't exist.")
main()