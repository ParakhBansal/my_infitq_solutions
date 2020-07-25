#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    delivery=0
    #write your logic here
    
    if(0<distance_in_kms<=3):
        delivery=0
    elif(3<distance_in_kms<=6):
        delivery=(distance_in_kms-3)*3
    elif(distance_in_kms>6):
        delivery=(distance_in_kms-6)*6+9
    else:
        bill_amount=-1
    if(bill_amount!=-1):    
        if(food_type=="V" and quantity_ordered>=1):
            bill_amount=120*quantity_ordered+delivery
        elif(food_type=="N" and quantity_ordered>=1):
            bill_amount=150*quantity_ordered+delivery
        else:
            bill_amount=-1
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,0)
print(bill_amount)
