#For this script to work, the file varFile.txt is required
"""Use this script to check if the short description of a Django variable is
 being introduced to the reader before the corresponding long description
within a file. Instead of manually checking for such occurrences, technical
 writers can run this script on their files and review the flags rasied by this
 script. To use this script, place the file you want to review within the same
 folder as this script and replace varFile.txt with the file you want to review.
Note that for the script to work, the short and long Django variables should
start with "{short_" and "{long_", and the suffix of a short variable should
 match the suffix of the corresponding long variable. For example, if the short
 variable is {short_blah_name}, the long variable should be {long_blah_name}.
"""
#Improvement to script, read path location from user and run the script for all
#html files within that location

import os
import sys

def open_file():
    """This function returns a dictionary containing:
       lineNum - the line number; the line numbers start from 1
       line - the line content from the file"""
#check if file is empty and return message that file is empty
    if os.stat("varFile.txt").st_size==0:
        print("The file you want to review is empty")
        sys.exit()
    else:
        i=1
        fdict = {}
        with open("varFile.txt") as f:
            for x in f:
                fdict[i] = x.strip() #strips the new line characters
                i=i+1
        return fdict

shortVar="{short_";longVar="{long_"
listShort=[];listLong=[]
dictShortLong={}
setLong=""
position=0

fdict = open_file()
#print(fdict)

#get list of short and long variable names
for lineNum, line in fdict.items():
    if (longVar in line or shortVar in line):
        lineList=line.split()
        for x in lineList:
            if x[0:7]==shortVar and x not in listShort:
                listShort.append(x)
            elif x[0:6]==longVar and x not in listLong:
                listLong.append(x)

if len(listShort)==0:
   print("The file does not have any short Django variables")
   sys.exit()

#create a dictionary of short and long variable names as keys and the line
# number and position within line of their first occurrence within the file

for varname in listShort:
    for lineNum, line in fdict.items():
        if varname in line and varname not in dictShortLong:
            lineList=line.split()
            position=lineList.index(varname)
            dictShortLong[varname]=(lineNum,position)
            setLong=longVar+varname[7:] #construct corresponding longVar using shortVar
#            print(setLong)
            if setLong in line:
                position=lineList.index(setLong)
                dictShortLong[setLong]=(lineNum,position)

#print(dictShortLong)

for varname in listShort:
    setLong=longVar+varname[7:]
    if setLong not in dictShortLong:
        print("The long description of {} is not found in the file".format(varname))
    else:
        lineNumShort,lineSPosition=dictShortLong[varname] #unpack the tuple
        lineNumLong,lineLPosition=dictShortLong[setLong]
        if lineNumShort==lineNumLong and lineSPosition < lineLPosition:
            print("The short description of {} occurs before the long description at line {}".format(varname,lineNumShort))
        elif lineNumShort<lineNumLong:
            print("The short description of {} occurs before the long description at line {}".format(varname,lineNumShort))

print("-----------------")
print("Script complete")
