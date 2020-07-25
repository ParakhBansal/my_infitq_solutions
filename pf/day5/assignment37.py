#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    tot=0
    for i in chocolates_received:
        tot+=i
    return tot

def reward_child(child_id_rewarded,extra_chocolates):
    if child_id_rewarded in child_id:
        if(extra_chocolates>=1):
            i=child_id.index(child_id_rewarded)
            global chocolates_received
            chocolates_received[i]+=extra_chocolates
            print(chocolates_received)
        else:
            print("Extra chocolates is less than 1")
    else:
        print("Child id is invalid")
    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
   


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)
