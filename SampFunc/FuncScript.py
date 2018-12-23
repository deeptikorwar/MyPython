#Script that shows you how to import standard libraries
#For this script to work, the file FuncFile.py is also required

import FuncFile
import math

#To experiment, change the numbers in the list
mynum=[4,5,10]

mynumsum=FuncFile.fn_add(mynum)

print("The sum of the numbers is {}".format(mynumsum))

num=5

print("The exponential value of {} is {}".format(num,math.exp(num)))
