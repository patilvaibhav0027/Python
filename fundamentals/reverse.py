#take a number from the user and print it in reverse order 

n=int(input("enter a number to count digits:"))

res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)
    
   



