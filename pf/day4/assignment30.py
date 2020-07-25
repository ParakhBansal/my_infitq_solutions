#PF-Assgn-30

def encode(message):
    enc=[]
    k=message[0]
    count=0
    for j in range(0,len(message)):
        if message[j]==k:
            count+=1
        else:
            str(enc.append(str(count)+k))
            k=message[j]
            count=1
            if(j==len(message)-1):
                str(enc.append(str(count)+k))
    if(len(message)==1):
        count=1
        str(enc.append(str(count)+k))
    pp="".join(enc)
    return pp
            

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
