#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    ls=[]
    while(len(ls)<15):
        
        if(given_year%4==0):
            if(given_year%100==0 and given_year%400==0):
                flag=1
            elif(given_year%100 and given_year%400!=0):
                flag=0
            elif(given_year%100!=0):
                flag=1
        else:
            flag=0
        if(flag==1):
            ls.append(given_year)
            given_year+=1
        elif(flag==0):
            given_year+=1

    return ls

list_of_leap_years=find_leap_years(2008)
print(list_of_leap_years)

import pytest

def test_find_leap_years_1():
    result=find_leap_years(2002)
    assert result==[2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]
    result=find_leap_years(2008)
    assert result==[2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800, 7200, 7600, 8000]
