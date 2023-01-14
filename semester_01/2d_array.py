# idk whats wrong with my code sir, i give up..
# so this is what i have in the moment

students = [[1201, "Claudius", "Andrew", "07/02/2005"],
            [1202, "Dylan", "Gunawan", "21/03/2005"],
            [1203, "Wincent", "Tan", "27/02/2005"],
            [1204, "Bayu", "Arimbawa", "19/07/2005"],
            [1205, "Christoph", "Sim", "30/06/2005"],
            [1206, "Filbert", "Hermawan", "31/01/2006"]]

def valdate(dob):
    if (dob[2] == "/") or (dob[5] == "/"): # format check
        if (int(dob[0:2]) > 31) or (int(dob[0:2]) < 0) or (int(dob[3:5]) > 12) or (int(dob[3:5]) < 0) or (int(dob[6:]) < 1022) or ((int[6:]) > 2022): # date check
            if (len(dob)) == 10: # length check 
                dob=dob
            else:
                while (len(dob)) != 10: 
                    print("Please enter a valid date")
                    dob = input("Enter DD/MM/YYYY: ")
        else:
            while (int(dob[0:2]) > 31 or (int(dob[0:2])) < 0) or (int(dob[3:5]) > 12 or int(dob[6:]) >2022) or int(dob[6:]) < 0:
                print("Please enter a valid date")
                dob = input("Enter DD/MM/YYYY: ")
    else:
        while (dob[2] != "/") or (dob[5] != "/"):
            print("Please enter a valid date")
            dob = input("Enter DD/MM/YYYY: ")

for i in range(3):
    s_id = len(students) + 1201 
    print("Student ID:", s_id)
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    dob = input("Enter Date of Birth: ")
    valdate(dob)
    temp = [s_id, f_name, l_name, dob]
    students.append(temp)
    
for count in range(len(students)):
    print(students[count])
