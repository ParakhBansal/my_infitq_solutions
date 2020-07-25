#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    t1=match_tuple.count("Team1")
    t2=match_tuple.count("Team2")
    if(t1>t2):
        return "Team1"
    elif(t2>t1):
        return "Team2"
    else:
        return Tie

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
