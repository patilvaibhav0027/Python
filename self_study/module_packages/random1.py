# 4. Random Module
# Function	Purpose
# randint(a,b)	Random integer
# random()	Float between 0 and 1
# choice(seq)	Random element
# shuffle(list)	Shuffle a list

import random #module 
# Simulate rolling two dice and print each value and the total.
d1 = random.randint(1,6)
d2 = random.randint(1,6)
print("dice:", d1, d2, "total:", d1+d2 )

# Generate a random 4-digit OTP.
password=random.randint(1000,9999)
print("otp", password)

# Pick a random winner from ["Amit", "Raj", "Neha", "Jay"], then shuffle the list.
student = ["Amit", "Raj", "Neha", "Jay"]
winner= random.choice(student)
print("winners: ", winner)
print("shuffled:", random.shuffle(student))