#PF-Exer-26

def factorial(number):
    fact=1
    while(number!=0):
        fact=fact*number 
        number-=1
    return fact


def find_strong_numbers(num_list):
    str_lt=[]
    for i in range(0,len(num_list)):
        temp=num_list[i]
        ssum=0
        if(temp==0):
            continue
        while(temp>0):
            if(temp>=10):
                rem=temp%10
                ssum=ssum+factorial(rem)
            else:
                ssum=ssum+factorial(temp)
                break
            temp=int(temp/10)
        if(ssum==num_list[i]):
            str_lt.append(num_list[i])
        
    return str_lt

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
