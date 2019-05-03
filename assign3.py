import math

print("Some constants in the math library of python\n")

print("The value of the inbuilt math variable[math.pi]:", math.pi)
print("The value of the inbuilt math variable[math.e]:", math.e)
print("The value of the inbuilt math variable[math.tau]:", math.tau)
print("The value of the inbuilt math variable[math.inf]:", math.inf)
print("The value of the inbuilt math variable[math.nan]:", math.nan)


print("The input that needs to be applied for the  following functions is single, and also returning the single value\n")

x = float(input("Enter number for single input math functions:"))

print("Square Root value of the number[math.sqrt(x)]:",math.sqrt(x))
print("Ceiling value of the number[math.ceil(x)]:",math.ceil(x))
print("Flooring value of the number[math.floor(x)]:",math.floor(x))
print("Absolute value of the number[math.fabs(x)]:",math.fabs(x))
print("Factorial of the number[math.factorial(x)]:",math.factorial(x))
print("Exponential of the number[math.exp(x)]:",math.exp(x))
print("Log value[Base 10] of the number[math.log10(x)]:",math.log10(x))
print("Log value[Base 2] of the number[math.log2(x)]:",math.log2(x))

print("TRIGNOMETRIC FUNCTIONS\n")
print("The input that needs to be applied for the  following functions is angle, and also returning the single value\n")

a = float(input("Enter the number for single trignometric math fucntion:"))

print("Sine value of the entered number is[math.sin(a)]:", math.sin(a))
print("Cosine value of the entered number is[math.cos(a))]:", math.cos(a))
print("Tan value of the entered number is[math.tan(a)]:", math.tan(a))
print("Arc Sine value of the entered number is[math.asin(a)]:", math.asin(a))
print("Arc Cosine value of the entered number is[math.acos(a)]:", math.acos(a))
print("Arc Tangent value of the entered number is[math.atan(a)]:", math.atan(a))

print("The input that needs to be applied for the  following functions are now multiple, though returning the single value\n")

y = float(input("Enter the first number for mutiple input math functions:"))
y = float(input("Enter the second number for mutiple input math functions:"))

print("GCD value for the input numbers[math.gcd(y,z)]:", math.gcd(y,z))
print("Remainder value for the input numbers[math.remainder(y,z)]:", math.remainder(y,z))
print("Power value for the input numbers[math.pow(y,z)]:", math.pow(y,z))
print("Copysign value for the input numbers[math.copysign(y,z)]:", math.copysign(y,z))
print("Mod value for the input numbers[maths.fmod(y,z)]",math.fmod(y,z))