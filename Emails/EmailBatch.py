#For this script to work, the file test1.txt is required
"""This script reads the tab delimited file, test1.txt, and creates strings of
email addresses based on the specified batchsize."""

emails=[]
batchsize=3 #the number of email addresses per batch

#test1.txt contains tab limited columns. The email addresses are in the second
# column
with open("test1.txt") as f:
    for x in f:
        verse=[x.split()[1]] #Note you need to use [] to create a list
        #print(verse)
        emails.extend(verse)

print("\n")
print("There are {} email addresses in the file\n".format(len(emails)))
print("The addresses are:")
print(emails)

#Here are some values for a sample test case
#If 305 emails are to be split into 3 batches, each batch will contain 100
# emails. That is, the batches are 100 + 100 + 100 emails, and then 5 in the
# last batch
batch = len(emails)//batchsize #find the number of batches required
rem = len(emails)%batchsize    #the remaining emails after the last batch
final = batch * batchsize      #variable to hold the last index of the final batch

#initialise loop index numbers for the first batch
batchstart = 0
batchend = batchsize

print("\nWe need {} batches of emails".format(batch))

for y in range(batch):
    str=""
    print("\nHere is my {} batch".format(y+1))
#    print("My batchstart is {}".format(batchstart))
#    print("My batchend is {}".format(batchend))
#loop through email addresses of the batch
    for i in range(batchstart,batchend):
#        print(emails[i])
        if i == batchend-1:
            str = str+emails[i]
        else:
            str = str+emails[i]+";"
    print(str)
    batchstart = batchstart + batchsize #set loop start for next batch
    batchend = batchend + batchsize #set loop end for next batch

#loop for the remaining email addresses
str=""
print("\nThe remaining email addresses are:")
for i in range(final, final+rem):
    if i == (final+rem)-1:
        str=str+emails[i]
    else:
        str=str+emails[i]+";"
#    print(emails[i])
print(str)
