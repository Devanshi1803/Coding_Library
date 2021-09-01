str = input()
list = str.split (",")
li = []
for i in list:
	li.append(int(i))
"""  
#using extra space
#print(li)
neg=[]
pos=[]
for i in li:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
neg.extend(pos)
print(neg)
"""
i=0
j=0
for j in range(len(li)):
    if li[j]<0:
        temp = li[i]
        li[i]=li[j]
        li[j] = temp
        i+=1
print(li)