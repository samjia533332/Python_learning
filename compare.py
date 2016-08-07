import random
import time

list1 =[]

start = time.time()
count = 0
num = 0
while count<=1000 :
    num = random.random()
    list1.append(num)
    count = count + 1
    #print num
end = time.time()
print 'create list time'
print end-start

start = time.time()
# find the smallest number
small = list1[0]
for item in list1 : 
    if item <= small :
        small =item
print "O(n)"
print small
end = time.time()
print end - start

print "O(n^2)"
start = time.time()
small = list1[0]
isSmall = True

for item in list1 :
    for item2 in list1 :
        if item2 <= item :
            isSmall = False
        #print isSmall
    if isSmall == True :
        small = item
        break
print small
end = time.time()
print end - start
