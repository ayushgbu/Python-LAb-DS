import random
l=list()
for i in range (0,10):
    a=random.randint(15,45)
    l.append(a)
count=0
for i in range (len(l)):
    if (l[i]<30):
        count+=1
print ("No. of entries less than 30 are ", count)

for i in l:
    if (i>35):
        l.remove(i)
print ("list after deleting entries greater than 35 is ",l)