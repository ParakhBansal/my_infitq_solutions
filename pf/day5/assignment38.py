#PF-Assgn-38
def no_digit(numb):
    count=0
    while(numb>0):
        count+=1
        numb=int(numb/10)
    return count
    
def check_double(number):
    d1=no_digit(number)
    d2=no_digit(2*number)
    ll=2*number
    bh=0
    if(d1==d2):
        k=str(number)
        m=str(ll)
        if(number!=ll):
            for u in k:
                bh=0
                for g in m:
                    if(u==g):
                       bh+=1
                if(bh==0):
                    return False
            return True
        else:
            return False
        

    
    else:
        return False
    
    

#Provide different values for number and test your program
print(check_double(125874))
