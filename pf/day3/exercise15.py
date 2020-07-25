#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    a=0
    b=0
    while(number!=0):
        a=number%10
        if(number<10):
            sum_of_digits=sum_of_digits+number
        else:
            sum_of_digits=sum_of_digits+a
        number=int(number/10)    
        
        
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
