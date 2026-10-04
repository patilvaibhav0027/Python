#arithmetic operators

a = 2
b = 5
print(a+b) #addition
print(a-b) #substraction
print(b-a) 
print(a*b) #multiply
print(a/b) #division
print(a % b) #modular
print(a ** b) #power a^b , 2^5: 32


#relational operator

a = 10
b = 20

print( a == b ) 
print (a != b )
print (a >= b ) #true
print (a <= b )
print (a > b)


#assignment operator

num = 10

num += 10
print(num)
num -= 10
print(num)
num /= 10
print(num)
num %= 10
print(num)
num *= 10
print(num)
num **= 10
print(num)


#logical operator

a = 50
b = 30

print (not ( a > b))
print ((a<b) and (a==10))
print((a>b) or (a<=b))