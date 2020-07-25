#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    for j in range(0,len(item_tuple),2):
        if item_tuple[j] in menu:
            ind=menu.index(item_tuple[j])
            if(check_quantity_available(ind,item_tuple[j+1])==1):
                print (item_tuple[j],"is available")
            else:
                print(item_tuple[j],"stock is over")
        else:
            print(item_tuple[j],"is not available")


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index]>=quantity_requested):
        return 1
    else:
        return 0


#Provide different values for items ordered and test your program
place_order("Fried Rice",2,"Soup",1)
