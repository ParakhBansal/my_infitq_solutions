#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    cc={}
    for key in medical_speciality:
        k=0
        if key in patient_medical_speciality_list:
            k=patient_medical_speciality_list.count(key)
            cc[k]=key
    maxx=0
    for key in cc:
        if(key>=maxx):
            maxx=key
    speciality=cc[maxx]
    
    return speciality
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
