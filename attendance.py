import csv
from csv import writer
from csv import reader

print("""
█▄▀ █ █▀▄ █▀   █▀█ █░░ ▄▀█ █▄█   █▀ █▀▀ █░█ █▀█ █▀█ █░░
█░█ █ █▄▀ ▄█   █▀▀ █▄▄ █▀█ ░█░   ▄█ █▄▄ █▀█ █▄█ █▄█ █▄▄                                              

                                                                """)


def limit1(num, minimum=1, maximum=5):
    return max(min(num, maximum), minimum)


def limit2(num, minimum=1, maximum=31):
    return max(min(num, maximum), minimum)


def limit3(num, minimum=1, maximum=12):
    return max(min(num, maximum), minimum)


while True:
    try:
        cla1 = int(input("Enter Class "))
        cla = limit1(cla1)
        break
    except ValueError:
        print("Enter A Valid Class")

while True:
    try:
        day1 = int(input("Enter Today Day "))
        day = limit2(day1)
        break
    except ValueError:
        print("Enter A Valid Day")

while True:
    try:
        month1 = int(input("Enter Current Month "))
        month = limit3(month1)
        break
    except ValueError:
        print("Enter A Valid Month")

list_of_str = ["Attendance"]

opened_file = open('class-1.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
rowcount = len(apps_data)  # include header row


def cl2():
    opef = open("clas2.csv")
    redfil = reader(opef)
    apd = list(redfil)
    rowcount1 = len(apd)
    return rowcount1


def cl3():
    opef3 = open("clas3.csv")
    redfil3 = reader(opef3)
    apd3 = list(redfil3)
    rowcount3 = len(apd3)
    return rowcount3


def cl4():
    opef4 = open("clas4.csv")
    redfil4 = reader(opef4)
    apd4 = list(redfil4)
    rowcount4 = len(apd4)
    return rowcount4


def cl5():
    opef5 = open("clas5.csv")
    redfil5 = reader(opef5)
    apd5 = list(redfil5)
    rowcount5 = len(apd5)
    return rowcount5


def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


if cla == 1:
    for i in range(rowcount):
        a = 1 +i
        print(a ,end ="")
        inp = input(" Roll Number Present Or Not ")
        list_of_str.append(inp)
    add_column_in_csv('class-1.csv', 'attendance-class1.csv',
                      lambda row, line_num: row.append(list_of_str[line_num - 1]))

if cla == 2:
    for i2 in range(cl2()):
        a = 1 + i
        print(a, end="")
        inp3 = input(" Roll Number Present Or Not ")
        list_of_str.append(inp3)
    add_column_in_csv('clas2.csv', 'attendance-class2.csv', lambda row, line_num: row.append(list_of_str[line_num - 1]))

if cla == 3:
    for i3 in range(cl3()):
        a = 1 + i
        print(a, end="")
        inp3 = input(" Roll Number Present Or Not ")
        list_of_str.append(inp3)
    add_column_in_csv('clas3.csv', 'attendance-class3.csv', lambda row, line_num: row.append(list_of_str[line_num - 1]))

if cla == 4:
    for i4 in range(cl4()):
        a = 1 +i
        print(a ,end ="")
        inp4 = input(" Roll Number Present Or Not ")
        list_of_str.append(inp4)
    add_column_in_csv('clas4.csv', 'attendance-class4.csv', lambda row, line_num: row.append(list_of_str[line_num - 1]))

if cla == 5:
    for i5 in range(cl5()):
        a = 1 + i
        print(a, end="")
        inp5 = input(" Roll Number Present Or Not ")
        list_of_str.append(inp5)
    add_column_in_csv('clas5.csv', 'attendance-class5.csv', lambda row, line_num: row.append(list_of_str[line_num - 1]))
