#For this script to work, the file flower.txt is required
"""The script matches a flower (from the flower.txt file) that begins with the
 same letter as your first name."""

def open_flowers():
    """This function returns a dictionary containing:
       key - first letter of the flower name
       value - the name of the flower """
    fdict = {}
    with open("flower.txt") as f:
        for x in f:
            fdict[x[0]] = x.strip() #strips the new line characters
    return fdict

print("Hello there! Wat's your name?")

name = raw_input("Type you first name followed by a space and then your last name\n")
namecl = name[0].lower()
namecu = name[0].upper()

fdict = open_flowers()

#print("Your name is {}".format(name))
#print("The first character in your name is {} {}".format(namecl,namecu))

if fdict.get(namecl) is None and fdict.get(namecu) is None:
    print("Sorry! There is no flower with your name")
else:
    x = fdict.get(namecl) or fdict.get(namecu)
    print("Hey {}!! Here is a flower in your name: {}".format(name,x))
