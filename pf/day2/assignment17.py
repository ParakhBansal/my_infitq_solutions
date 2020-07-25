#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    hike=0
    if(job_level==3):
        hike=(current_salary*15)/100
        new_salary=int(hike+current_salary)
    elif(job_level==4):
        hike=(current_salary*7)/100
        new_salary=int(hike+current_salary)
    elif(job_level==5):
        hike=(current_salary*5)/100
        new_salary=int(hike+current_salary)
    else:
        new_salary=int(current_salary)
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,7)
print(new_salary)
