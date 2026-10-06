# solve factorial 
# factorial of 5 :-> 5! = 5x4x3x2x1

n=int(input("enter num: "))
fact=1
if n>0:
    for i in range( 1, n+1 ):
        fact=fact*i
print(fact)

