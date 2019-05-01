def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def print_armstrong(lower,upper):
    for num in range(lower, upper + 1):
        len_1 = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** len_1
            temp //= 10
        if num == sum:
            print(num)

def find_fact(num):
    fact_1 = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fact_1 = fact_1 * i
        print("The factorial of", num, "is", fact_1)

def check_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

def print_prime(lower,upper):
    for num in range(lower, upper + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

def digit_sum(num_1):
    tot = 0
    while (num > 0):
        dig = num % 10
        tot = tot + dig
        num = num // 10
    print("The total sum of digits is:", tot)

print("Please select operation -\n" \
      "1. Fibbonaci Series\n" \
      "2. Factorial\n" \
      "3. Print all Armstrong Number\n" \
      "4. Check whether Armstrong Number or not\n" \
      "5. Print all prime number\n" \
      "6. Check whether number is prime or not\n" \
      "7. Sum of digits")

select = input("Select operations form 1, 2, 3, 4, 5, 6: ")

if select == '1':
    num_1 = int(input("Enter the number of terms:"))
    if num_1 <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(num_1):
            print(recur_fibo(i))

elif select == '2':
    num_1 = int(input("Enter the number to find factorial:"))
    find_fact(num_1)

elif select == '3':
    low_1 = int(input("Enter a lower case value:"))
    upp_1 = int(input("Enter a upper case value:"))
    print_armstrong(low_1,upp_1)

elif select == '4':
    num_1 = int(input("Enter a  number:"))
    check_armstrong(num_1)

elif select == '5':
    low_1 = int(input("Enter a lower case value:"))
    upp_1 = int(input("Enter a upper case value:"))
    print_prime(low_1,upp_1)

elif select == '6':
    num_1 = int(input("Enter a number:"))
    check_prime(num_1)

elif select == '7':
    num_1 = int(input("Enter the number:"))
    digit_sum(num_1)

else:
    print("Invalid input specified\n")