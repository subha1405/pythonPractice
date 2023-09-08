n=int(input("Enter a number"))
rev=0
org=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(rev==org):
    print("Palindrome")
else :
    print("Not Palindrome")
