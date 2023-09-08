n=int(input("Enter a number"))
org=0
res=n
while (n!=0):
    rem=n%10
    org=org+rem*rem*rem
    n=n//10
print(org)
print(n)
if(org==res):
    print("Armstrong number")
else:
    print("Not armstrong")

