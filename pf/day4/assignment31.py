#PF-Assgn-31
def check_palindrome(word):
    pl=[]
    c=0
    for h in range(len(word)-1,-1,-1):
        pl.append(word[h])
    ki="".join(pl)
    if(ki==word):
        return True
    else:
        return False
        
    
    

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
