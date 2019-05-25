#Use this script to insert a line (comment) into all files (ending with ".py")
#under the specified file path
#The script ignores empty files and files whose first line is similar to the
# one you are about to insert

#Sample search phrase: This script was created using
#Sample comment to insert: This script was created using Python 2.7
#Sample file path Documents/MyPythonFiles

import os
import sys
import textwrap

#To check whether the file is empty, use textwrap
#textwrap.wrap removes all empty spaces, tab stops, and new lines
#note that os.stat("test1.py").st_size and os.path.getsize("test1.py") return
#non-zero values for files that contain only new line characters or tab stops

def check_ifempty(file_name):
    with open(file_name) as my_file:
        file_text = my_file.read()
        text_list=textwrap.wrap(file_text)
        if len(text_list)==0:
            #print("Hey, there! You have an empty file.")
            return 1
        else:
            return 0
"""
To understand why the line is inserted in such a convoluted way, read the
answer that contains this line "The fundamental truth you are encountering
here is that you generally can't prepend data to an existing flat structure
#without rewriting the entire structure. " on stackoverflow
"""

def insertLine(file_name, line_text):
    with open(file_name) as my_file:
        my_file.seek(0)
        first_line = my_file.readline().strip() #remember to strip the new line character
#        print(first_line)
        my_file.close()
        print(file_name)
        if searchString in first_line:
            print("Yay! A line with similar pattern already exists in file: {}\n".format(file_name))
        else:
            print("Inserting line in file: {}\n".format(file_name))
            with file(file_name, 'r') as original:
                data = original.read()
            with file(file_name, 'w') as modified:
                modified.write(line_text + "\n" + data)
"""
#Below function does not do a recursive search
def getFiles(file_path):
    #get all files with .py extension under the given file path
    return os.listdir(file_path)
"""

#For recursive search use os.walk
def getFiles(file_path):
#get all files with .py extension under the given file path
#os.walk(path) yields directory path, directory names and file names
    files_list=[]
    for r, d, f in os.walk(file_path):
        for file in f:
            if '.py' in file:
                files_list.append(os.path.join(r, file))
    return(files_list)

searchString = raw_input("Enter the string you would like to search:\n")
insertString = raw_input("Enter the string you would like to insert:\n")
#If you wish to insert code instead of a comment, comment below line
insertString = "#" + insertString
file_path = raw_input("Enter the file path where you would like me to work:\n")

# If os.path.expanduser('~') is not added here, user has to input complete path
file_path = os.path.expanduser('~')+"/"+file_path
if os.path.exists(file_path) is False:
    print("The path you've supplied is not a valid directory.")
    sys.exit()
else:
    file_list = getFiles(file_path)
#print(file_list)

"""
for f in file_list:
    print(f)
"""

if not file_list: #checks if the list is non-zero
    print("No Files with '.py' extension in the supplied path")
    sys.exit()

for x in file_list:
    #Learning: Conversion to boolean is required in order to use True or False
    isempty=check_ifempty(x)
    if bool(isempty) is True:
        print("{} is empty..skipping file\n".format(x))
        continue
    else:
        insertLine(x, insertString)
