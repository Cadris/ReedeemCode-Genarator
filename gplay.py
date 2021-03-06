import random
import string

bigSet = set()
limit = 1000         #total number of genarations in a run

# num = "0123456789"
# alpha = "QWERTYUIOPASDFGHJKLZXCVBNM"
# print(getCode)

def getCode(length = 16, char = string.ascii_uppercase +
                          string.digits ):
    return ''.join(random.choice( char) for x in range(length))

def writeToFile():    
    file_object = open('codes.txt', 'a')    
    # file_object.write('hello')    
    for item in bigSet:
        item += "\n"
        file_object.write(item)

    file_object.close()

setLength_old = len(bigSet)

while setLength_old<=limit:
    bigSet.add(getCode())
    if(setLength_old<len(bigSet)):
        setLength_old += 1

print(bigSet)
writeToFile()
print("Print Job Done")