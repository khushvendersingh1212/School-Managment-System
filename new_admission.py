import csv

print("""
█▄▀ █ █▀▄ █▀   █▀█ █░░ ▄▀█ █▄█   █▀ █▀▀ █░█ █▀█ █▀█ █░░
█░█ █ █▄▀ ▄█   █▀▀ █▄▄ █▀█ ░█░   ▄█ █▄▄ █▀█ █▄█ █▄█ █▄▄                                              

                                                                """)
print("        𝗡𝗲𝘄 A𝗱𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗙𝗼𝗿 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝟮𝟬𝟮𝟭        ")

f = open("stu.csv", "a+", newline="")
Smain = csv.writer(f)
f.seek(0)
if len(f.read()) == 0:
    Smain.writerow(["Name", "Father Name", "Mother Name", "Class", "Admission Number", "Phone Number", "D.O.B."])

mainrec = []
increas = 1

class1 = open("class-1.csv", "a+", newline="")
stuclas1 = csv.writer(class1)
class1.seek(0)
if len(class1.read()) == 0:
    stuclas1.writerow(["Roll Number", "Name", "Admission Number", "Phone Number"])

file2 = open('clas2.csv', 'a+', newline="")
stuclas2 = csv.writer(file2)
file2.seek(0)
if len(file2.read()) == 0:
    stuclas2.writerow(["Roll Number", "Name", "Admission Number", "Phone Number"])

file3 = open('clas3.csv', 'a+', newline="")
stuclas3 = csv.writer(file3)
file3.seek(0)
if len(file3.read()) == 0:
    stuclas3.writerow(["Roll Number", "Name", "Admission Number", "Phone Number"])

file4 = open('clas4.csv', 'a+', newline="")
stuclas4 = csv.writer(file4)
file4.seek(0)
if len(file4.read()) == 0:
    stuclas4.writerow(["Roll Number", "Name", "Admission Number", "Phone Number"])

file5 = open('clas5.csv', 'a+', newline="")
stuclas5 = csv.writer(file5)
file5.seek(0)
if len(file5.read()) == 0:
    stuclas5.writerow(["Roll Number", "Name", "Admission Number", "Phone Number"])

def limit1(num, minimum=1, maximum=5):
    return max(min(num, maximum), minimum)

while True:
    nam = input("Enter Student Name - ")
    while True:
        try:
            Clas1 = int(input("Enter Class - "))
            Clas = limit1(Clas1)
            break
        except ValueError:
            print("Enter A Valid Class")

    Fname = input("Enter Father Name - ")
    Mname = input("Enter Mother Name - ")
    adm = 100 + increas
    while True:
        try:
            phnumb = int(input("Enter Phone Number - "))
            #phnumb = limit1(phnum)
            break
        except ValueError:
            print("Enter A Valid Class")

    dob = input("Enter Date of Birth - ")
    lst = [nam, Fname, Mname, Clas, adm, phnumb, dob]
    mainrec.append(lst)

    if Clas == 1:
        stucls1list = []
        a1 = 0
        rollnum_cla1 = 0 + increas + a1
        a1 = 0 + rollnum_cla1
        lst1 = [rollnum_cla1, nam, adm, phnumb]
        stucls1list.append(lst1)
        for i1 in stucls1list:
            stuclas1.writerow(i1)
    if Clas == 2:
        # using with statement
        stucls2list = []
        b2 = 0
        rollnum_cla2 = 0 + increas + b2
        b2 = 0 + rollnum_cla2
        lst2 = [rollnum_cla2, nam, adm, phnumb]
        stucls2list.append(lst2)
        for i2 in stucls2list:
            stuclas2.writerow(i2)

    if Clas == 3:
        # using with statement
        stucls3list = []
        rollnum_cla3 = 0 + increas
        lst3 = [rollnum_cla3, nam, adm, phnumb]
        stucls3list.append(lst3)
        for i3 in stucls3list:
            stuclas3.writerow(i3)

    if Clas == 4:
        # using with statement
            stucls4list = []
            rollnum_cla4 = 0 + increas
            lst4 = [rollnum_cla4, nam, adm, phnumb]
            stucls4list.append(lst4)
            for i4 in stucls4list:
                stuclas4.writerow(i4)

    if Clas == 5:
        # using with statement
            stucls5list = []
            rollnum_cla5 = 0 + increas
            lst5 = [rollnum_cla5, nam, adm, phnumb]
            stucls5list.append(lst5)
            for i5 in stucls5list:
                stuclas5.writerow(i5)
    increas += 1

    c = input("Input 'Y' If You Want To Record More, Otherwise Press 'N' - ")
    if c == "N":
        break
    if c == "n":
        break
for i in mainrec:
    Smain.writerow(i)
f.close()
class1.close()
file2.close()
file3.close()
file4.close()
file5.close()