#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    suum=0
    for i in list_of_marks:
        suum=i+suum
    avg=suum/10
    count=0
    for k in list_of_marks:
        if(k>avg):
            count+=1
    nimi=(count/10)*100
    return nimi

def sort_marks():
    return sorted(list_of_marks)
    
def generate_frequency():
    lk=[0]*26
    for j in list_of_marks:
        for k in range(0,26):
            if(j==k):
                lk[k]+=1
    return lk
    
    
    
    

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
