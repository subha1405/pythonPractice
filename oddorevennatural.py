#  n=int(input("Enter a number"))
# i=0
# print("Odd numbers")
# while (i<=n) :
#     if(i%2!=0):
#         print(i)
#     i=i+1
# i=0
# print("Even numbers")
# while(i<=n):
#     if(i%2==0):
#         print(i)
#     i=i+1
n=int(input("Enter a number"))
i=0
for i in range(n):
    if(i%2==0):
        print(i)
    i=i+1