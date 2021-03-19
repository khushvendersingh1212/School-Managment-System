print("""
𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙎𝘾𝙃𝙊𝙊𝙇 𝙈𝘼𝙉𝘼𝙂𝙀𝙈𝙀𝙉𝙏 𝙎𝙔𝙎𝙏𝙀𝙈""")
print("""
Total Available Modules Are -
1 New Admission (Principal Login only)
2 Attendance (Teacher Login)
3 Uniform Shopping (Student Login)
4 Word Problem Solver (Student Login)
""")

print(""" Login Modes Are -
1 Principal
2 Student
3 Teacher
""")


def limit1(num, minimum=1, maximum=5):
    return max(min(num, maximum), minimum)


def limit2(num, minimum=1, maximum=3):
    return max(min(num, maximum), minimum)


while True:
    try:
        userau = int(input("Chose any of these Login Modes - "))
        useraut = limit2(userau)
        break
    except ValueError:
        print("No Valid Login Mode Selected! Please Try Again (Integer Values Allowed Only) ...")
if useraut == 1:
    while True:
        usr = input("Enter User Name: ")
        if usr == "Principal":
            password = input("Enter Password To Login Into Principal Account: ")
            if password == "STPAUL":
                import new_admission
                break
            else:
                print("Wrong Password")
        else:
            print("Wrong Username")

if useraut == 3:
    while True:
        usr3 = input("Enter User Name: ")
        if usr3 == "Teacher":
            password3 = input(" Enter Password To Login Into Teacher Account: ")
            if password3 == "STPAUL":
                import attendance
            else:
                print("Wrong Password")
        else:
            print("Wrong Username")

if useraut == 2:
    while True:
        usr2 = input("Enter User Name: ")
        if usr2 == "Student":
            password2 = input("Enter Password To Login Into Student Account: ")
            if password2 == "STPAUL":
                print("""
                    1 Uniform Shop
                    2 Word Problem Solver
                    """)
                while True:
                    try:
                        stuin = int(input("Choose Any Of These Option "))
                        stuinp = limit2(stuin)
                        if stuinp == 1:
                            import uniform_shop
                        if stuinp == 2:
                            import word_problem_solver
                    except ValueError:
                        print("No Valid Option Selected! Please Try Again ...")

            else:
                print("Wrong Password")
        else:
            print("Wrong Username")
