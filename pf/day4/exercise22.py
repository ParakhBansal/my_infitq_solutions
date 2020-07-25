#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    ticket=airline+":"
    src=source[:3]+":"
    dest=destination[:3]+":"
    k=0
    for i in range(101,101+no_of_passengers):
        k=0
        ticket=airline+":"+src+dest+str(i)
        ticket_number_list.append(ticket)
    if(no_of_passengers<=5):
        return ticket_number_list
    else:
        return ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
