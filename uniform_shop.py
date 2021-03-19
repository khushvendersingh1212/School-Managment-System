def limit2(num, minimum=1, maximum=5):
    return max(min(num, maximum), minimum)


while True:
    try:
        ad = int(input("Enter Admission Number - "))
        break
    except ValueError:
        print(" Please Enter Correct Admission Number...")

nam = input("Enter Name - ")
while True:
    try:
        cl = int(input("Enter Class - "))
        limit2(cl)
        break
    except ValueError:
        print(" Please Enter Correct Class...")

while True:
    try:
        ph = int(input("Enter Phone Number - "))
        break
    except ValueError:
        print(" Please Enter Correct Phone Number...")

file2 = open("receipt.txt", "a")
file2.write("School Uniform Receipt")


def tt():
    adst = str(ad)
    clst = str(cl)
    phst = str(ph)
    file2.write("Admission Number = "+adst+"\n")
    file2.write("Name = "+nam+"\n")
    file2.write("Class = " +clst+"\n")
    file2.write("Phone Number"+phst+"\n")

tt()

print("Do You Want Buy House T-Shirt?")
ts = input("Type 'y' If You Want To Buy Or Press Any Key To Jump Into Next Product - ")
if ts == "y":
    file2.write("Purchased House T-Shirt Price 250"+"\n")

print("Do You Want Buy House Trousers?")
ts1 = input("Type 'y' If You Want To Buy Or Press Any Key To Jump Into Next Product - ")
if ts1 == "y":
    file2.write("Purchased House Trousers Price 350"+"\n")

print("Do You Want Buy School Shirt?")
ts2 = input("Type 'y' If You Want To Buy Or Press Any Key To Jump Into Next Product - ")
if ts2 == "y":
    file2.write("Purchased School Shirt Price 300"+"\n")

print("Do You Want Buy School Trousers?")
ts3 = input("Type 'y' If You Want To Buy Or Press Any Key To Jump Into Next Product - ")
if ts3 == "y":
    file2.write("Purchased School Trousers Price 380"+"\n")

print("Do You Want Buy School Tie?")
ts4 = input("Type 'y' If You Want To Buy Or Press Any Key To Jump Into Next Product - ")
if ts4 == "y":
    file2.write("Purchased School Tie Price 100"+"\n")

print("Do You Want Buy School Belt?")
ts5 = input("Type 'y' If You Want To Buy Or Press Any Key To Jump Into Next Product - ")
if ts5 == "y":
    file2.write("Purchased School Belt Price 120"+"\n")
file2.close()