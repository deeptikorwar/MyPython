#For this script to work, the file file.txt is required
#The first line defines the column names, and serves as a reference for file format
#Output is stored in the file outputHTML.txt
"""
This script reads the tab limited file file.txt and creates HTML code, which can
be pasted into Remedy templates

Formatting text within Remedy fields takes a considerable amount of time; you can
instead create content in Excel, save the Excel data as a tab limited .txt file,
 and create HTML tags using this script

Below are the limitations of this script:
    1. Nested bullets are not supported
    2. Lines that start with - are not supported
    3. Strong tag is applied only at the paragraph level and not to parts of
     paragraph

Below is the list of supported tag types:
strong: Applies bold formatting for the entire paragraph
        p: Paragraph formatting is applied
        a: Creates a hyperlink
   bullet: Starts the code for unordered list
        b: Adds the code for a bulleted item
endbullet: Marks the end of unordered list
     step: Starts the code for ordered list
        n: Adds the code for a numbered item
  endstep: Marks the end of numbered list

The output is split into two parts based on the value in the "Type" column, TS
 or CS

Note:
    1. The tags for bulleted and numbered lists should be sequential; that is,
       they should startwith bullet or step, end with endbullet or endstep,
        and contain the individual b or n items in between
    2. The hyperlinks open in new tab and the hyperlink text is the same as the
       actual hyperlink
"""
import sys

def create_html(y,z):
        html_str=""
        for i,j in zip(y,z):
#Check for the tag type and create corresponding HTML tags
#If unrecognised tags are present in the file, exit the script
            if i=="strong":
                html_str = html_str + "<p><strong>" + j[1:-1] + "</strong></p>\n"
            elif i=="p":
                if j[1]=='"' and j[-1]=='"':
                    html_str = html_str + "<p>" + j[1:-1] + "</p>\n"
                elif j[1]=='"':
                    html_str = html_str + "<p>" + j[1:] + "</p>\n"
                elif j[-1]=='"':
                    html_str = html_str + "<p>" + j[:-1] + "</p>\n"
                else:
                    html_str = html_str + "<p>" + j + "</p>\n"
            elif i=="a":
                html_str = html_str + '<a target="_blank" isdialoglink="true" href="'+j+'"'+'>' + j + '</a>\n'
            elif i=="bullet":
                html_str = html_str + "<ul>"
            elif i=="step":
                html_str = html_str + "<ol>"
            elif i=="b" or i=="n":
                html_str = html_str + "<li>" + j + "</li>\n"
            elif i=="endbullet":
                html_str = html_str + "</ul>"
            elif i=="endstep":
                html_str = html_str + "</ol>"
            else:
                stoppgm=1
                html_str = "I can't recognise some of the tags you passed, please enlighten me!"
                break;
        return(html_str)

infoTSTag=[]
infoTSText=[]
infoCSTag=[]
infoCSText=[]

stoppgm=0


#Check for the tag type and create corresponding HTML tags
#If unrecognised tags are present in the file, exit the script
#Ignore blank lines and the lines that contain only the character '"'

with open("file.txt") as f:
    for y in range(1):
        next(f)
    for x in f:
        if x.isspace():
            continue
        elif x.split()[0] == '"':
#            print("In here")
            continue
        else:
            type=x.split()[0]
#            print(x)
            tag=[x.split()[1]]
            text=[" ".join(x.split()[2:])]
            #print(type)
            if type=="TS":
                infoTSTag.extend(tag)
                infoTSText.extend(text)
            elif type=="CS":
                infoCSTag.extend(tag)
                infoCSText.extend(text)
            elif type=='"':
                pass
            else:
                print("Type field missing data in some lines. Please correct file.")
                stoppgm=1
                break;

#print(infoTSTag)
#print(infoTSText)
#print(infoCSTag)
#print(infoCSText)

if stoppgm==1: #Exit program if data is not valid
    sys.exit()

TS_str=create_html(infoTSTag,infoTSText)
CS_str=create_html(infoCSTag,infoCSText)

#Write HTML code to the file
#Separate the code as per "Type" classification

f = open("outputHTML.txt", "w")
f.write("------Begin Technical Solution---------\n")
f.write(TS_str)
f.write("------End Technical Solution---------\n")
f.write("------Begin Customer Solution---------\n")
f.write(CS_str)
f.write("\n------End Customer Solution---------\n")
