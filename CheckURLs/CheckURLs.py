"""Use this script to check the hyperlinks within a README.md GitHub file.
 Incorrect URLs and the corresponding line numbers are outputted. Note that the
 script does not take into account the empty lines within the .md file; hence,
  the outputted lines numbers may not match the line numbers of the .md file."""
import urllib
import urllib2
import re

def get_hlinks(source):
    """This function extracts the hyperlinks within the source line."""
    start_sep='href="'
    end_sep='"'
    result=[]
    tmp=source.split(start_sep)
    for par in tmp:
      if end_sep in par:
        result.append(par.split(end_sep)[0])
    return result

def check_URL(link, line):
    """This function attempts to open the URL and returns the error code
     (if any)."""
    try:
        urllib2.urlopen(link)
#        g = urllib2.urlopen(ChUrl)
#        print(g.getcode())
    except urllib2.HTTPError as e:
#        print(e.code) # can add counter or line number variable here
#        print(e.reason)
        if e.code == 404 or 403:
            print("Status code {} returned, check your hyperlink: {} at line {}".format(e.code, link, line))
    except urllib2.URLError as f:
        print("check your hyperlink: {} at line {}, {}".format(link,line,f.args))

#Get the link to the README file from the user
GitLink = raw_input("Type the GitHub README link. For example, https://github.com/deeptikorwar/MyTestRep/blob/master/README.md \n")

#write the source html to a file
#response = urllib2.urlopen('https://github.com/deeptikorwar/MyPython/blob/master/README.md')
#response = urllib2.urlopen('https://github.com/deeptikorwar/MyTestRep/blob/master/README.md')
response = urllib2.urlopen(GitLink)
with open('output.txt', 'w') as f:
    f.write(response.read())

fdict = {}

count = 0
getline = 0
endline = 0
check = 'div id="readme"'
#find the start and end line numbers of the readme.md content
with open("output.txt") as f:
    for x in f:
        count = count + 1
        fdict[count] = x
        if check in x:
            getline = count #set start of readme content
        if (count > getline) and '</article>' in x:
            endline = count #set end of readme content

#print(getline)
#print(endline)

newcount = 0
flinks = {}
s = ""

#add all the lines (within readme content) that contain hrefs to a dictionary
#read the lines from the readme div and add line numbers and href matches to
# a dictionary
for i in range(getline, endline):
    if "<a href=" in fdict[i]:
        flinks[newcount] = fdict[i]
    newcount = newcount + 1

#print(flinks)

#find the links within the lines and add them to a dictionary
flinks_final = {}
for key in flinks:
    hlinks = get_hlinks(flinks[key])
    flinks_final[key] = hlinks

#print(flinks_final)

#check the links
for x in sorted(flinks_final):
    url_lists = flinks_final[x]
    for i in url_lists:
        if 'https:' not in i:
            i = 'https://github.com' + i
#        print('Line' + str(x) + ': ' + i)
        #call the check urls function here
        #pass URL and the line number
        check_URL(i, x)
