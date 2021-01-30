############################################# odd or even

#a = int(input())
# if a % 2 == 0:
#    print(f"{a} is even")
# else:
#    print(f"{a} is odd")

# global and local variable

#a = 25
#
#
# def loc():
#    a = 10
#    print(f"this is local variable {a}")
#
#
# loc()
#print(f"this is global variable {a}")

# my_len

#str = input()
#
#
# def my_len():
#    a = len(str)
#    return a
#
#
#length = my_len()
#print(f"the length of the string {str} is {length}")

# str split

#s = "sri krishna arts kollege"
# print(s.split('k'))
# print(s.split('r'))

# output

#values = [1, 2, 3, 4]
#numbers = set(values)
#
#
# def checknums(num):
#    if num in numbers:
#        return True
#    else:
#        return False
#
#
# for i in filter(checknums, values):
#    print(i)

# 12 to 24

# def convert24(str1):
#    if str1[-2:] == "AM" and str1[:2] == "12":
#        return "00" + str1[2:-2]
#
#    elif str1[-2:] == "AM":
#        return str1[:-2]
#
#    elif str1[-2:] == "PM" and str1[:2] == "12":
#        return str1[:-2]
#
#    else:
#        return str(int(str1[:2]) + 12) + str1[2:8]
#
#
#print(convert24("06:35:40 PM"))

# for num in range(512):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# for num in range(2, 10):
#    if num % 2 == 0:
#        print("Found an even number", num)
#        continue
#    print("Found a number", num)


#a = int(input("enter first no"))
#b = int(input("enter second no"))
#m = a
#n = b
# while (a != b):
#   if a > b:
#       a = a-b
#   elif b > a:
#       b = b-a

#print(f"{a} is the GCD of {m} and {n}")

s = input()
a = s.lower()


vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
digits = "1234567890"
space = " "

con = 0
vow = 0
dig = 0
sp = 0

for i in a:
    if i in vowels:
        vow += 1
    elif i in consonants:
        con += 1
    elif i in digits:
        dig += 1
    elif i in space:
        sp += 1

print(f"There are {con} consonants")
print(f"There are {vow} vowels")
print(f"There are {dig} digits")
print(f"There are {sp} spaces")
