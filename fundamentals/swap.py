# Swap Without Temporary Variable
# Given two integers a and b, swap their values without using a third temporary variable. 
# Return the swapped values as a list [a, b]
# (where the first element is the original b and the second element is the original a).

# a = int(input("a:"))
# b = int(input("b:"))

# print([b,a])
# #wrong logic 
#here we the number isnt swaping, i have printed swaped variables

a = int(input("a:"))
b = int(input("b:"))

a=a+b
b=a-b
a=a-b

print([a,b])