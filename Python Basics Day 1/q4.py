# 4	Swap two variables without using a third variable.	Easy

a = (int(input("enter value for a: ")))
b = (int(input("enter value for b: ")))

a=a+b
b=a-b
a=a-b

print("swaped value of b to a", a)
print("swaped value of a to b", b)