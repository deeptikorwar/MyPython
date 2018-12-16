#For this script to work, the file test1.txt is required
emails=[]
batchsize=4 #modify this number to the batch size you require

#test1.txt contains tab limited columns. The email address is in the second
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

#Values for a sample test case
#305 should be split into batches of 100. First 100 should be outputted. Then
#then next 100, again next 100 and then the remaining 5
batch = len(emails)//batchsize
rem = len(emails)%batchsize
final = batch * batchsize

#initialise loop numbers
batchstart=0
batchend=batchsize


print("\nWe need {} batches of emails".format(batch))

for y in range(batch):
    str=""
    print("\nHere is my {} batch".format(y+1))
#    print("My batchstart is {}".format(batchstart))
#    print("My batchend is {}".format(batchend))
    for i in range(batchstart,batchend):
#        print(emails[i])
        if i == batchend-1:
            str=str+emails[i]
        else:
            str=str+emails[i]+";"
    batchstart = batchstart + batchsize #set counter to range for next loop
    batchend = batchend + batchsize #set loop end for next batch
    print(str)

str=""
print("\nThe remaining email addresses are:")
for i in range(final, final+rem):
    if i == (final+rem)-1:
        str=str+emails[i]
    else:
        str=str+emails[i]+";"
#    print(emails[i])
print(str)
