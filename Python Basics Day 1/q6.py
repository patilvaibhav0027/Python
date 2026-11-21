# 6	Calculate simple interest.	Easy
#Simple Interest (SI) =((Principle x Rate x \Time in year) / 100).

# • Simple Interest: ((10,000 x  5 x  3) / 100 = {₹1,500})
# • Total Amount (P + SI): (10,000 + 1,500 = {₹11,500})


P = int(input("enter prinicple amount: "))
R = int(input("enter rate of interest on the amount: "))
T = int(input("enter duration in years: "))

SI =(P * R * T) / 100
print("Interest : ", SI)

     

