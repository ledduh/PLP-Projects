# # print list in reverse order using while and for loop

mylist = ["bear", "been", "bought"]
i = len(mylist)-1
# While loop
while i >= 0:
    print(mylist[i])
    i = i - 1 
# for loop
for i in reversed(mylist):
    print(i)

for i in range(11,21):
    if (i%5==0):
        print(i)