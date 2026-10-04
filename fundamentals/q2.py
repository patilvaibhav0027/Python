# WAP to find the greatest of 3 numbers entered by user
a = int(input("enter number1: "))
b = int(input("enter number2: "))
c = int(input("enter number3: "))

if (a>=b) and (b>=c):
    print(a, "is the greatest")
elif (b>=a) and (a>=c):
    print(b, "is the greatest")
else:
    print(c, "is the greatest")