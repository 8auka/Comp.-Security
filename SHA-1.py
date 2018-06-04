st=input("Enter Text: ")
result=""
key="1001011110010111000101110101000101010100"
for x in st:
    c =format(ord(x),'b')
    if len(c) >= 8:
        result=result + str(c)
    else:
        block1 = str(("0"*(8-len(c)) + c))
        result=result + block1
result=result + format(len(st)*8,'b')
len_of_input = '0'*((int(len(result)/128)+1)*128 - len(result))
result = result + len_of_input 
blocks = []
block = ""
for i in range(128,len(block),128):
    for y in range(i-128,i):
        block = block+result[y]
    blocks.append(block)
    block = ""
def hash_func(block="", key=""):
    final = ""
    subBlock=""
    newFinal = ""
    subBlocks = []
    last = True
    for i in range(32,len(block)+1,32):
        for y in range(i-32,i):
            subBlock=subBlock+block[y]
        subBlocks.append(subBlock)
        subBlock = ""
    for sb in subBlocks:
        xored = ""
        
        for i in range(len(sb)):
            xored = xored+str((int(sb[i])^int(key[-i])))
        newFinal = newFinal + xored[::2]
        final = final + newFinal[:5] + newfinal[-5:]
        newFinal = ""
        xored = ""
    return final

for block in blocks:
    key = hash_func(block,key)

resultA = ""
binary = ""
for i in range(8,len(key)+1,8):
    for y in range(i-8,i):
        binary = binary+key[y]
    if int(binary,2) <= 33:
        resultA = resultA+chr(int(binary,2)+33)
    else:
        resultA = resultA+chr(int(binary,2))
    binary = ""
print("SHA-1 value is: ",hex(int(key)))
