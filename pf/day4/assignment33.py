#PF-Assgn-33

def find_common_characters(msg1,msg2):
    ki=msg1.replace(" ","")
    kj=msg2.replace(" ","")
    set2=frozenset(kj)
    ll=[x for x in ki if x in set2]
    rr="".join(ll)
    if not rr:
        return -1
    else:
        return rr
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
