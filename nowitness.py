print("Welcome to our application.")
command=input("Type sign up in order to sign up:")
while command:
    if command=="sign up".lower():
       name=input("Enter your name :")
       surname=input("Enter your surname : ")
       birthyear=input("Enter your birthyear :")
       email=input("Create your email :")
       password=input("Enter a password :")
       print("User created")
    else:
     print("Wrong command!")
    break
command2=input("Type login in order to log in with the acount you created :")
while command2:
     if command2=="login".lower():
         for  i in range(3):
             email2=input("Enter email:")
             password2=input("Enter password :")
             if email==email2 and password==password2:
               break
             else:
               print("Incorrect")
         if i==2:
           print("You have been denied access!")
           break
         else:
           print("Correct log in")
           break
