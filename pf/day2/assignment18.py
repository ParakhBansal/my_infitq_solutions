#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    #write your logic here
    if(current_currency_name=="Euro"):
        current_currency_amount=0.01417*amount_needed_inr
    elif(current_currency_name=="British Pound"):
        current_currency_amount=0.01*amount_needed_inr
    elif(current_currency_name=="Australian Dollar"):
        current_currency_amount=0.02140*amount_needed_inr
    elif(current_currency_name=="Canadian Dollar"):
        current_currency_amount=0.02027*amount_needed_inr
    else:
        current_currency_amount=-1
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"Euro")

print(currency_needed )
