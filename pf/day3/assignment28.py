#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    x=0
    sum=0
    rem=0
    liste=[]
    count=0
    # Write your logic here
    for i in range(num1,num2+1):
        x=i
        sum=0
        count=0
        if(x>9):
            while(x>0):
                rem=x%10
                count+=1
                sum+=rem
                x=int(x/10)
        else:
            count==1
            sum=i
        if(sum%3==0 and count==2 and i%5==0):
            liste.append(i)
    if(num2>num1):
        for j in range(0,len(liste)):
            for k in range(j,len(liste)):
                if(liste[j]>=liste[k]):
                    max_num=liste[j]
                else:
                    max_num=liste[k]
    else:
        max_num=-1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,30)
print(max_num)
