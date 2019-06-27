#Use this script to test a list of URLs; pass the URLs via a CSV file.
#If you are using an Excelsheet to capture the list of URLs, export the data to
# a CSV file.

import sys
import os
import urllib
import urllib2
import re
import textwrap
import csv
import webbrowser

#function to check if file exists
def check_file_exists(filename):
    if os.path.isfile(filename):
        return
    else:
        print("I can't find the file you want to process in the same folder as this script. Try again")
        sys.exit()

#function to check if user input is an integer
def check_number(number):
    try:
        number = int(number)
        if number >= 0:
            return "Positive"
        else:
            return "Negative"
    except ValueError:
        return "No"

#function to check if number is positive
def notify_user_pnumber(uinput,iname):
    if check_number(uinput)=="Positive":
        return int(uinput)
    elif check_number(uinput)=="Negative":
        print("Sorry {} numbers cannot be negative. Try again".format(iname))
        sys.exit()
    else:
        print("That doesn't look like a number. Try again")
        sys.exit()

count=0
fdict={} #dict to hold line numbers and column values
data=""

print("Hi there!")
file_name = raw_input("Enter the file name (containing URLs) along with its extension:")
check_file_exists(file_name) #validate file name

#If you have used empty lines for formatting your Excel, include them in your count
user_header = raw_input("Type the number of header rows within your file:")
header = notify_user_pnumber(user_header,"header") #validate header value

if header > 20:
    print("Sorry, I can handle only up to 20 header rows. Modify your file and try again.")
    sys.exit()
else:
    count= count + header #increment count as header lines will be ignored

column = raw_input("At which column position does the file contain URLs?")
column = notify_user_pnumber(column,"column")  #validate column value
#can you access name of a variable? Nope

#Do you need to log in to your domain to test the URLs? If not, comment this
#portion of the script
uauthdone=""
while uauthdone == "":
    udomainauth = raw_input("If you need to log on to your domain to test the URLS, type Yes, else type No:")
    if udomainauth == "Yes":
        udomainlink = raw_input("Type your domain; for example, https://www.abc.com :")
        webbrowser.open(udomainlink)
        uauthdone = raw_input("Please log in to your domain and type Continue when done:")
    elif udomainauth == "No":
        break

with open(file_name) as f:
    #for below code to work, export your Excel to CSV format
    line = csv.reader(f,delimiter=',') #returns a csv reader object
    #need to check if '\t' can be used for tab delimited files
    #\n is stripped out of csv files but not out of text files
    for _ in range(header):
        next(f) #skip the header lines
    for x in line:
        #join method concatenates the objects of an iterable to a string or
        #separator
        #print(x)
        y = ','.join(x)
        #print(y)
        y = y.split(',') #separating the items into a list to work with
        #print(y)
        #z = ' '.join(y).strip() #to check for empty lines but not at this stage
        #print(z)
        count = count + 1
        fdict[count] = y

#print(fdict)

print("\n------------------------------")
print("Beginning script to check URLs")
print("------------------------------")

for line in fdict:
    #If entire line is empty, ignore the row
    if not ' '.join(fdict[line]).strip():
        continue
    else:
        #print(fdict[line][column-1])
        link = fdict[line][column-1]
        if not link: #if the column doesn't contain URL, skip line
            print("Line {}: Column value is emtpty".format(line))
            continue
        else:
            try:
                urllib2.urlopen(link)
        #        g = urllib2.urlopen(ChUrl)
        #        print(g.getcode())
            except urllib2.HTTPError as e:
        #        print(e.code) # can add counter or line number variable here
        #        print(e.reason)
                if e.code == 404 or 403:
                    print("Line {}: status code {} returned, check your hyperlink--> {}".format(line,e.code,link))
            except urllib2.URLError as f:
                print("Line {}: check your hyperlink: {}, {}".format(line,link,f.args))
            except ValueError, u:
                print("Line {}: this does not look like a URL--> {}".format(line,link))

print("------------------------------")
print("Finished script execution")
print("------------------------------")
