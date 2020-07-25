#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    amount=0
    rate=0
    #Write your logic here
    rate=(no_of_adults*37550)+no_of_children*(37550/3)
    amount=rate+(rate*7)/100
    total_ticket_cost=amount-(amount*10)/100
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(2,3)
print("Total Ticket Cost:",total_ticket_cost)
