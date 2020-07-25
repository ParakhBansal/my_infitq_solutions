#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    x=0
    y=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    z=rupees_to_make-(no_of_five*5)
    x=int(rupees_to_make/5)
    y=rupees_to_make%5
    if(no_of_five>0):    
       if(z>0):
           if(z>no_of_one):
               five_needed=0
               one_needed=0
           elif(z<=no_of_one):
               five_needed=no_of_five
               one_needed=z
       elif(z<0):
           if(y==0):
               if(rupees_to_make>5):
                  five_needed=x
                  one_needed=0
               else:
                  if(rupees_to_make>no_of_one):
                     no_of_five=0
                     no_of_one=0
                  else:
                     five_needed=0
                     one_needed=rupees_to_make
           else:
               if(y>no_of_one):
                  five_needed=0
                  one_needed=0
               elif(y<=no_of_one):
                  five_needed=x
                  one_needed=y
       elif(z==0):
           five_needed=no_of_five
           one_needed=0
    else:
       if(rupees_to_make>no_of_one):
           five_needed=0
           one_needed=0
       else:
           five_needed=0
           one_needed=rupees_to_make
        
   

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    if(five_needed!=0 or one_needed!=0):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
