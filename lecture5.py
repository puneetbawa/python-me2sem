str1 = input('Enter the first string:')

print('the value of the entered string' , str1)
print('the value of the first character of string' , str1[0])

#Concatenation of two strings

str2 = input('Enter the second string:')

print('The concatenation using + :', str1 + str2)

str3 = str1 *3 #Using str3 to use in the process of interation

print('The concatenation using * :', str3)

#Iterating in the string

count = 0
for letter in str3:
    if(letter == 't'):
        count+= 1
print('No of t in the string', str, ':', count)

#Membership Check in the string

if('ingte' in str3):
    print('ingte found in the string ' , str3)
else:
    print('Not found in the string')

#Inbuilt String Functions and String Formatting
print('The length of the entered string is: ', len(str3))

print('The enumerate function of the string: ', enumerate(str3))

str4 = str3.upper()
print('The uppercase value of the ', str3, ' is: ', str4)

str5 = str4.lower()
print('The lowercase value of the ', str4, ' is: ', str5)

str6 = str4.split(' ')
print('The string is spitted by space as: ', str6)

print('The position of "ing" is', str3.find('ing'))
print('Replacing "ing" with "puneet"' , str3.replace('ing', ' puneet'))






