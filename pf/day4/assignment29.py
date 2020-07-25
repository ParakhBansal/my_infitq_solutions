#PF-Assgn-29
def calculate(distance,no_of_passengers):
    rate=int(distance/10)*70
    income=80*no_of_passengers
    if(income>rate):
        return (income- rate)
    else:
        return -1
    


#Provide different values for distance, no_of_passenger and test your program
distance=2000
no_of_passengers=50
print(calculate(distance,no_of_passengers))
