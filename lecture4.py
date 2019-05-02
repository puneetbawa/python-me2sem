#Leap Year or not
#Convert height of a person from cm into inch and feet
#Temprature conversion from c to f and vice versa
#Printing tabe of a given number
#Least Significant of the entered integer at unit's place
#Divisible by 7 and multiple of 5 in given number
#gcd

import math

def check_lp_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

def cm_conversion(num):
    inch = 0.3937 * num
    feet = 0.0328 * num
    print("Inches is:", inch)
    print("Feet is:", feet)

def temp_conversion(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))

def print_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

def leas_sign(num):
    count = 0
    while (num > 0):
        count = count + 1
        num = num // 10
    return count

def div_fiv_sev(lower,upper):
    lower = int(input("Enter the lower range:"))
    upper = int(input("Enter the upper range:"))
    for i in range(lower, upper + 1):
        if (i % 7 == 0 and i % 5 == 0):
            print(i)

def compute_gcd(num, num1):
    print("The gcd of", num , "and", num1 , "is", math.gcd(num , num1))

print("Please select operation -\n" \
      "1. Check Leap Year or not \n" \
      "2. Conversion of height(from cm to feet and inches)\n" 
      "3. Conversion of temprature(from c to f)\n" \
      "4. Print the table of a given number\n" \
      "5. Least Significant of the entered integer at unit's place\n" \
      "6. Divisible by 7 and multiple of 5 in given number \n" \
      "7. GCD of number")

select = input("Select operations form 1, 2, 3, 4, 5, 6, 7: ")

if select == '1':
    num1 = int(input("Enter the year:"))
    check_lp_year(num1)

elif select == '2':
    num1 = float(input("Enter the height in centimeters:"))
    cm_conversion(num1)

elif select == '3':
    num1 = float(input("Enter the number in celsius:"))
    temp_conversion(num1)

elif select == '4':
    num1 = int(input("Enter the number for table:"))
    print_table(num1)

elif select == '5':
    num1 = int(input("Enter the number:"))
    print("The evaluated output is", str(num1) + str(leas_sign(num1)))

elif select == '6':
    low1 = int(input("Enter the lower range:"))
    upp1 = int(input("Enter the upper range:"))
    div_fiv_sev(low1,upp1)

elif select == '7':
    num = int(input("Enter the first number:"))
    num1 = int(input("Enter the second number:"))
    compute_gcd(num,num1)

else:
    print("Invalid input\n")
