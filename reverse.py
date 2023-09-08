# n=int(input("Enter a number"))
n=123
rev=0
while n!=0:
    rem=n%10
    print(rem)
    rev=rev*10+rem
    print(rev)
    n=n//10
    print(n)
print(rev)