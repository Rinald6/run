import random
def welcome_screen():
    name=input("Enter your name : ")
    print(name + ", welcome to Hangman car game.")
welcome_screen()
possible_answers=["mercedes","audi","volkswagen","bmw","opel","porsche","fiat","lancia","lamborghini","maserati",]
secret_word=random.choice(possible_answers)
length=len(secret_word)
display="*" * length
count=0
def hangman(count,display,secret_word):
    limit=3
    guess=input("The word is : " + display + "." + "Enter a letter : ")
    if guess in secret_word:
        index=secret_word.find(guess)
        secret_word=secret_word[:index] + "*" + secret_word[index + 1:]
        display=display[:index] + guess + display[index + 1:]
    else:
        count+=1
        if count==1:
           print("Wrong input! " + " You got 2 attempts remaining!" )
        elif count==2:
           print("Wrong input! " + " You got 1 attempt remaining!")
        elif count==3:
            print("I'm sorry you lost!" )
    if secret_word=="*"*length:
        print("Congrats, you won!")
    elif count!=limit:
        hangman(count,display,secret_word)
hangman(count,display,secret_word)
print("The word was " + secret_word + ".")