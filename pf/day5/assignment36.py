#PF-Assgn-36
def create_largest_number(number_list):
    number_list.sort(reverse=True)
    jj=""
    for k in number_list:
        jj+=str(k)
    gh="".join(jj)
    return gh

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
