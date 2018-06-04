a = input("Enter a message:")
blocks=[]
h=''
def div_block(a):
    numbers_str=""
    len_txt=""
    for i in a:
         numbers_str=numbers_str+str(format(ord(i),"08b"))
    zeros = "0"*(448-(len(numbers_str)))
    numbers_str = numbers_str+zeros
    txt = format(len(a),"08b")
    len_txt = "0"*(64-len(txt))
    numbers_str = numbers_str + len_txt + txt
    return (numbers_str)
for i in range(32,len(a),32):
    h=h+a[i]
print(h)
