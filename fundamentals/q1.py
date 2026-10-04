#conditional statement 
#if elif else
#WAP ro check if a number entered by the user is odd or even

num = int(input("enter number: "))

if (num%2==0):
    print( f"{num} is a even number")
elif (num%2!=0):
    print(f"{num} is a odd number")
else:
    print(f"{num} is not a natural number " )