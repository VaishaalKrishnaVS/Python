# print(max(3,4))
# print(min(3,4))
# print(len("hello"))
#
# r = range(3,20,2)
# for n in r:
#    print(n)
#
# print(round(7.8))
# print(chr(65))
# print(float(5))
# print(int(5.2))
# print(pow(3,5))
# print(type(5.3))
# print("good morning")
# t = tuple([1,2,3,5])
# print(t)
# input("enter your name")


# def add():
#    a = int(input("enter first value: "))
#    b = int(input("enter second value: "))
#    c= a+b
#    print(c)
#
# def sub():
#    a = int(input("enter first value: "))
#    b = int(input("enter second value: "))
#    c= a-b
#    return c
#
# def mul(a,b):
#
#    c= a*b
#    print(c)
#
# def div(a,b):
#
#    c= a/b
#    return c
#
# add()
# print(sub())
# a = int(input("enter first value: "))
# b = int(input("enter second value: "))
# mul(a,b)
# a = int(input("enter first value: "))
# b = int(input("enter second value: "))
# print(div(a,b))


# def my_details(name,age):
#    print("name :", name)
#    print("age :", age)
#    return
#
# my_details("vaishaal",  18)
#
# def my_details(name,age):
#    print("name :", name)
#    print("age :", age)
#    return
#
# my_details( age = 18,name="vaishaal")
#
# def my_details(name,age=40):
#    print("name :", name)
#    print("age :", age)
#    return
#
# my_details( "vaishaal")
#
# def my_details(*name):
#    print(*name)
#
# my_details("vsv", "vajhd", "iregndos")

# import math as m
# from math import sqrt
# import math
#
# print(math.ceil(3.14))
# print(math.floor(3.14))
# print(math.factorial(3))
# print(math.gcd(12, 15))
# print(math.sqrt(25))
# print(math.log(2))
# print(math.log10(2))
# print(math.log2(2))
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
# print(math.pi)
# print(math.e)
#
# print(sqrt(25))
#
# print(m.ceil(3.14))
# print(m.floor(3.14))
# print(m.factorial(3))
# print(m.gcd(12, 15))
# print(m.sqrt(25))
# print(m.log(2))
# print(m.log10(2))
# print(m.log2(2))
# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.pi)
# print(m.e)
# swapping
# a = int(input())
# b = int(input())
# print(a, b)
# c = a
# a = b
# b = c
# print(a, b)
# circulating
#
#


# def circulate(lis, n):
#    for i in range(1, n+1):
#        b = lis[i:]+lis[:i]
#        print("the circulated value", i, "=", b)
#        return
#
#
# lis = [10, 20, 30, 40, 50, 60]
# n = int(input("enter value: "))
# circulate(lis, n)

#
#
# distance between 2 points
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

# print(distance)

#
####################################### leap year #########################################

# year = int(input())
# if(year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("it is a leap year")
#        else:
#            print("it is not a leap year")
#    else:
#        print("it is a leap year")
# else:
#    print("it is not a leap year")
#############################################################################################

################################## Temprature in celsius degree #############################

# celsius = int(input())
# fahrenheit = (celsius * 1.8) + 32
# print(f"The ans is {fahrenheit}")

###############################################################################################

############################### squareroot ####################################################

# import math as m

# a = int(input("First no: "))
# b = int(input("Second no: "))

# print(m.sqrt(a))
# print(m.sqrt(b))

################################################################################################

# list1 = [1, "hi", "Python", 2]
# print(list1[0:2])
# print(list1 * 3)
# del list1[2]
# print(list1)

#################################################################################################

# a = input("Enter a word")
# b = input("Enter a char")
# c = int(input("Enter a number"))

# d = a[:c] + b + a[c:]

# print(d)

#################################################################################################

# a = int(input("Enter the no: "))
# b = int(input("Enter the divisor: "))
# c = divmod(a, b)
# print(c)

# a = float(input("Enter the first no: "))
# b = float(input("Enter the second no: "))
# print("press 1 for addition")
# print("press 2 for subtraction")
# print("press 3 for multiplication")
# print("press 4 for division")
# c = int(input("Your Option: "))

# if c == 1:
#    d = a+b
# if c == 2:
#    d = a-b
# if c == 3:
#    d = a*b
# if c == 4:
#    d = a/b

# print(d)

################################# Greatest of three ##############################################

# a = int(input("First number: "))
# b = int(input("Second number: "))
# c = int(input("Third number: "))

# if a > b:
#   if a > c:
#       print(f"{a} is the greatest")
# elif b > c:
#   print(f"{b} is the greatest")
# else:
#   print(f"{c} is the greatest")

#################################################################################################

# print(7/2)
# print(7//2)
# print(7**2)
# print(7 % 2)
# tup = ("hi", "Python", 2)
# t[2] = "hi"
# list1 = [1, "hi", "Python", 2]
# print(list1[0:2])
# print(list1 * 3)
# del list1[2]
# print(list1)
# hi = "Welcome to India"
# print(hi[3])
# print(hi[:6])
# print(hi[-3])
# print(hi[:])
# x = 12
# y = 15
# print(x and y)
# print(x | y)
# college = "Sri krishna"
# college[1] = college[5] = "K"
# college[12] = " * "
# print(college)

######################################### Boolean ##############################################

# a = True
# print(a)
# b = False
# print(b)
#
# print(2 == 5)
# print(5 == 5)
#
# print(a+b)
# print(a*b)
# print(a+a)

#################################################################################################

########################## positive or negative #################################################

# a = int(input())
# if a > 0:
#    print("it is positive")
# else:
#    print("it is negative")

#################################################################################################

############################# odd or even #######################################################

# a = int(input())
# if a % 2 == 0:
#    print("it is even")
# else:
#    print("it is odd")

#################################################################################################

########################### Student mark system #################################################

# a = int(input())
#
# if a >= 90:
#    print("grade s")
# elif a >= 80:
#    print("grade a")
# elif a >= 70:
#    print("grade b")
# elif a >= 60:
#    print("grade c")
# elif a >= 50:
#    print("grade d")
# else:
#    print("fail")

#################################################################################################

############################ Traffic system #####################################################

# a = input()
#
# if a = "green":
#    print("go")
# elif a = "yellow":
#    print("ready")
# else:
#    print("stop")

#################################################################################################

########################### Amstrong number #####################################################

# a = int(input())
# c = 0
# m = a
# while a > 0:
#    b = a % 10
#    a = a / 10
#    c += pow(b, 3)
#
# if (c == m):
#    print(" it is an amstromg no")
# else:
#    print("it is not an amstromg no")

##################################################################################################

################################ Palindrome ######################################################

# a = int(input())
# c = 0
# m = a
# while a > 0:
#    b = a % 10
#    a = a / 10
#    c = 10 * c + b
#
# if m == a:
#    print("it is palindrome")
# else:
#    print("it is not palindrome")

#####################################################################################################

########################### GCD #################################################

# a = int(input("enter first no"))
# b = int(input("enter second no"))
# m = a
# n = b
# while (a != b):
#    if a > b:
#        a = a-b
#    elif b > a:
#        b = b-a
#
# print(f"{a} is the GCD of {m} and {n}")

#######################################################################################

############################ fibonacci series #########################################

# a = int(input())
# m = 0
# n = 1
# print(m)
#
# for i in range(2, a+1):
#    b = m+n
#    m = n
#    n = b
#    print(m)

#########################################################################################

####################### loops #################################################

# a = int(input())
# a = 5
# for i in range(a+1):
#    for j in range(1, i+1):
#        print(j, end=" ")
#    print("")
#
# for i in range(a+1):
#    for j in range(1, i+1):
#        print("*", end=" ")
#    print("")

###################################################################################

################### office ##################################################################

# a = int(input())
#b = int(input())#

# c = 0
# d = 0
# for sal in range(b):
#    c = a + sal*200
#    print(c)
#    d += c#

# print(d)
# a = "Hello world"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.title())
# print(a.find("llo"))
# print(a.split(' '))
# print(a.count('Hello'))
# print(a.center(25, "*"))
# print(a.replace('Hello', 'happy'))
# print(a.join(" . "))
# print(a.isupper())
# print(a.islower())
# print(a.isalpha())
# print(a.isalnum())
# print(a.isdigit())
# print(a.isspace())
# print(a.istitle())
# print(a.startswith("h"))
# print(max(a))
# print(min(a))
# print(len(a))
# ths = {1, 2, 4, 5, 6, 3}
# print(ths)

################################################################################

############# Square root using newtons method #################################

# def mySqrt(x):
#
#    n = x
#    p = 10 ** (-10)
#
#    while abs(x - n * n) > p:
#        n = (n + x / n) / 2
#
#    return n
#
#
# a = int(input("Enter your no: "))
# ans = mySqrt(a)
# print(f"The square root of {a} is {ans}")

################################################################################

#################### stu  and  dep #############################################

# no_of_students = int(input())
# list_of_students = []
#
# for i in range(no_of_students):
#    list_of_students.append(input())
#
# branch_name = input()
#
# for i in range(no_of_students):
#    student_name, branch = list_of_students[i].split()
#    if branch_name == branch:
#        print(student_name)

###############################################################################

################ vowel replacer ##############################################

# given_string = list(input())
# new_list = []
#
# for i in range(len(given_string)):
#    if given_string[i] in 'aeiou':
#        new_list.append(i)
#
# reversed_string = given_string[::-1]
#
# new_list.sort(reverse=True)
#
# for i in range(len(new_list)):
#    reversed_string.pop(new_list[i])
#
# print("".join(reversed_string))

################ expo #########################

# ef expo(n, m):
#   a = n**m
#   return a
#
#
# = int(input())
# = int(input())
#
# = expo(z, x)
# rint(c)

################################################

########## 7 not 5 ############################

# c = 0
# for i in range(1000, 2000):
#    if i % 7 == 0 and i % 5 != 0:
#        print(i)
#        c += 1
# print(c)

################################################

############ max of a list #####################

# list = []
#
#
# num = int(input("Enter total elements: "))
#
#
# for i in range(1, num + 1):
#    number = int(input())
#    list.append(number)
#
#
# def myMax(list):
#
#    max = list[0]
#    for x in list:
#        if x > max:
#            max = x
#    return max
#
#
# c = myMax(list)
#
# print(f"Largest element is: {c}")

###########################################################

# def rev(lst):
#    new_list = list[::-1]
#    return new_list
#
#
# list = [10, 11, 12, 13, 14, 15]
# print(rev(list))

#############################################################

################## linear serch #############################

#list = [2, 5, 1, 4, 7, 8, 9, 6, 5, 85, 56, 101]
#random_no = int(input())
#is_present = False
#
# for middle in range(len(list)):
#    if random_no == list[middle]:
#        print("the number is positioned at ", middle)
#        is_present = True
#
# if not is_present:
#    print("The number is not present in the list")
#############################################################

################## binary serch #############################

#list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list = []
#num = int(input("Enter total elements: "))
# for i in range(1, num + 1):
#    number = int(input())
#    list.append(number)
# list.sort()
#lower = 0
#higher = len(list)
#random_no = int(input())
#
#
# while (lower <= higher):
#    middle = int((lower + higher) / 2)
#    if (random_no == list[middle]):
#        print("the number is positioned at ", middle)
#        break
#    elif (random_no > list[middle]):
#        lower = middle + 1
#
#    else:
#        higher = middle - 1

#############################################################
