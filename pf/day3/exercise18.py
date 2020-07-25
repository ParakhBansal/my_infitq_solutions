#PF-Exer-18

def get_count(num_list):
    count=0
    x=0
    for num in num_list:
        if x==num:
            count+=1
        x=num
    
            # TODO: write code...
        # TODO: write code...
    # Write your logic here

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
