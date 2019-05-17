
def sort_words(my_str):
    words = my_str.split()
    words.sort()
    print("The sorted words are:")
    for word in words:
        print(word)

def compare_str(str1,str2):
    if(str1 > str2):
        print(str1, ' is grater than', str2)
    elif(str2 > str1):
        print(str2, ' is grater than', str1)
    else:
        print('strings are equal')

def check_palindrome(str1):
    str2 = reversed(str1)
    print(str2)
    if(list(str1) == list(str2)):
        print('Palindrome String')
    else:
        print('Not palindrome')

print("Please select operation -\n" \
      "1. Sort Words in the string \n" \
      "2. Comparing two strings\n" \
      "3. Check whether string is palindrome or not"
      )

select = input('Enter the number 1,2,3')

if(select=='1'):
    str1 = input('Enter the string to be sorted:')
    sort_words(str1)

if(select=='2'):
    str2 = input('Enter the first string: ')
    str3 = input('Enter the second string: ')
    compare_str(str2, str3)

if(select=='3'):
    str1 = input('Enter the string to check is palindrome or not: ')
    check_palindrome(str1)
