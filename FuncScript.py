#Script that shows you how to import standard libraries
#For this script to work, the file FuncFile.py is also required

import FuncFile
import math

#To experiment, change the number in the list
mynum=[4,5,10]

mynumsum=FuncFile.fn_add(mynum)

print("The sum of the numbers is {}".format(mynumsum))

num=5

print("The exponential value of 5 is {}".format(math.exp(num)))
