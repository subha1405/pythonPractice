a=input("Enter your name")
b=input("Do you have a criminal background ,Reply Y for yes,N for no")
if(b=='N'or b=='n'):
    c=int(input("Enter your age"))
    if(c>18):
        print("You are Eligible")
    else:
        print("You are not eligible")
elif(b=='Y'or b=='y'):
    print("GOOD")
else:
    print("Invalid Input")
