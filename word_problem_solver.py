print("""
█▄▀ █ █▀▄ █▀   █▀█ █░░ ▄▀█ █▄█   █▀ █▀▀ █░█ █▀█ █▀█ █░░
█░█ █ █▄▀ ▄█   █▀▀ █▄▄ █▀█ ░█░   ▄█ █▄▄ █▀█ █▄█ █▄█ █▄▄                                              

                                                                """)

print("Welcome To Word Problem Solver")

str1 = input("Enter A Question  ")
st1 = str1

def findSum(str1):
    # A temporary str1ing
    temp = "0"
    # holds sum of all numbers in string
    Sum = 0
    # read each character in input string
    for ch in str1:
        # if current character is a digit
        if ch.isdigit():
            temp += ch
        # if current character is an alphabet
        else:
            # increment Sum by number found
            Sum += int(temp)
            # reset temporary str1ing to empty
            temp = "0"
    return Sum + int(temp)

def sub():
    st = str1
    digits = [
        int(each)
        for each in st.split()
        if each.isdigit()]
    result = digits[0] - digits[1]
    #return result
    print(result)

test1 = 0

a1 = str1.find("left")
b1 = str1.find("lost")
c1 = str1.find("gave")
d1 = str1.find("give")
if a1 >= 0:
    test1 += 1
if b1 >= 0:
    test1 += 1
if c1 >= 0:
    test1 += 1
if d1 >= 0:
    test1 += 1

#monu have 900 l milk and give to tonu 100 l milk

#sub1 = "left" or "have" or "less" or "more"
# or ("how many" and "more") or ("have" or "than")

if test1 >=1:
   sub()
elif test1 <= 0:
    print(findSum(str1))