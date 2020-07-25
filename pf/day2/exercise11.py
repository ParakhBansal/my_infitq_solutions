#PF-Exer-11

def display(num):
    message=" "
    if(num%3==0):
          if(num%5==0):
            message="zoom"
          else:
            message="zip"
    elif(num%5==0):
          if(num%3==0):
            message="zoom"
          else:
            message="zap"
    else:
         message="invalid"
    #write your logic here
    return message

#Provide different values for num and test your program
message=display(9)
print(message)
