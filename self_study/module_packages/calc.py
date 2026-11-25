
#importing a module mycalc
import mycalc

print(mycalc.add(10,5))
print(mycalc.substract(10,5))
print(mycalc.multiplication(10,5))
print(mycalc.division(10,5))


#using  all four styles (whole module, specific function, alias, multiple functions), print the square root of 144 and the factorial of 4.
import math #whole module
print(math.sqrt(144))
 
from math import factorial #specific function
print(factorial(4))

from math import sqrt, factorial #multiple function
print(sqrt(144), factorial(4))

from math import * #imported all 
print(floor(144/4))

import math as m #alias
print(pow(3,8))