import random

plaintext = raw_input("Enter the plaintext: ")
key = raw_input("Enter the key: ")

splittedKey = list(key)
splittedPlaintext = list(plaintext)
listOfRows = []

for letter in splittedKey:
    row = []
    for i in range(len(splittedKey)):
        x = ord(letter)+i
        if x>122:
            x -= 26
        row.append(chr(x))
    listOfRows.append(row)
    
results = []
for letter in splittedPlaintext:
    resultByList = []
    for x in range(len(listOfRows)):
        row = listOfRows[x]
        for y in range(len(row)):
            if row[y] == letter:
                resultByList.append([x,y])
    results.append(resultByList)

result = ""
for i in results:
    choice = random.choice(i)
    result = result+str(choice[0])+","+str(choice[1])+" "
print(result)
