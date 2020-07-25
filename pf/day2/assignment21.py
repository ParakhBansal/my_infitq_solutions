#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
        if(1<=day<=30):
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1
            next_month=month+1
            next_year=year
    elif(month==4 or month==6 or month==9 or month==11):
        if(1<=day<=29):
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1
            next_month=month+1
            next_year=year
    elif(month==12):
        if(1<=day<=30):
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1
            next_month=1
            next_year=year+1
    if(month==2):
        if((year%4==0 and year%100!=0)or(year%100==0 and year%400==0)):
            if(1<=day<=28):
                next_day=day+1
                next_month=month
                next_year=year
            else:
                next_day=1
                next_month=3
                next_year=year
        else:
            if(1<=day<=27):
                next_day=day+1
                next_month=month
                next_year=year
            else:
                next_day=1
                next_month=3
                next_year=year
    
    
    
    
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(31,12,2005)
