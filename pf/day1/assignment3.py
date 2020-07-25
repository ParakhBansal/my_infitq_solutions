#PF-Assgn-3
#This verification is based on string match.

mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five="false"
total_cost=0

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
total_cost=((distance_one_way*2)/mileage)*amount_per_litre
per_head_cost=total_cost/4

#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
