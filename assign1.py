def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def area_c(rad1):
    return 3.142 * (rad1 * rad1)

def cmpd_int(p1,r1,t1):
    return p1 * (pow((1 + r1 / 100), t1))

def simp_int(p2,r2,t2):
    return (p2 * r2 * t2) / 100


print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      "5. Simple Intrest\n" \
      "6. Compound Interest\n" \
      "7. Area of Circle\n" \
      "8. Greatest of three number\n" \
      "9. ASCII representation Integer\n" \
      "10. ASCII represenation Character\n")


select = input("Select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 :")

if select == '1':
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == '2':
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == '3':
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif select == '4':
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))

elif select == '5':
    princ_1 = float(input("Enter principal amount: "))
    rate_1= float(input("Enter rate: "))
    time_1= float(input("Enter time: "))
    print("Simple Interest =", simp_int(princ_1,rate_1,time_1))

elif select == '6':
    princ_2 = float(input("Enter principal am of circle: "))
    rate_2 = float(input("Enter rate of circle: "))
    time_2 = float(input("Enter time of circle: "))
    print("Simple Interest =", cmpd_int(princ_2, rate_2, time_2))

elif select == '7':
    radius_1 = float(input("Enter radius of circle: "))
    print("Area of circle =", area_c(radius_1))

elif select == '8':
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    number_3 = int(input("Enter third number: "))

    if (number_1 > number_2) and (number_1 > number_3):
        largest = number_1
    elif (number_2 > number_1) and (number_2 > number_3):
        largest = number_2
    else:
        largest = number_3

    print("The largest number is", largest)

elif select == '9':
    number_1 = int(input("Enter the number: "))
    print("ASCII conversion from integer=",chr(number_1))

elif select == '10':
    number_1 = input("Enter the character: ")
    print("ASCII conversion from integer=",ord(number_1))


else:
    print("Invalid input")