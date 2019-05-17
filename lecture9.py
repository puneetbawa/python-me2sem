def comp_num(list1):
    largest = list1[0]
    lowest = list1[0]
    largest2 = None
    lowest2 = None
    for item in list1[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or largest2 < item:
            largest2 = item
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 == None or lowest2 > item:
            lowest2 = item

    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", lowest2)

def evn_odd_lst(list):
    evn_list = []
    odd_list = []
    for i in list:
        if(i%2==0):
            evn_list.append(i)
        else:
            odd_list.append(i)
    print("Mixed list: ", list)
    print("Even numbers in the list: ", evn_list)
    print("Odd numbers in the list: ", odd_list)

def merg_srt(list,list1):
    list3 = []
    list3 = list + list1
    list3.sort()
    return list3

def srt_scnd_element(list):
    sub_list = list[1:]
    print(sub_list)
    for i in range(0,len(sub_list)):
        for j in range(0,len(sub_list)):
            if(sub_list[i]<sub_list[j]):
                temp = sub_list[j]
                sub_list[j] = sub_list[i]
                sub_list[i] = temp

    print("Original List: ", list)
    print("Sorted List according to second element: ", sub_list)

def un_int(list,list1):
    print("Intersection of the two lists: ", set(list).intersection(list1))
    list3 = merg_srt(list,list1)
    list4 = []
    for i in list3:
        if i not in list4:
            list4.append(i)
    print("Union of the list", list4)

def perf_sq(list2):
    print(list2)
    list1= []
    for i in list2:
        j=i*i
        list1.append(j)
    print("perfect square: ", list1)

print("Please select operation -\n"\
      "1. Greatest/Second Greatest/Lowest/Second Lowest number in the list \n" \
      "2. Even and odd into sub lists\n" \
      "3. To merge the list and sort\n" \
      "4. to sort the list according to the second element\n" \
      "5. TO find the union and intersection of the two list\n" \
      "6. To find the perfect square\n" \
      )

select = input('Enter the operation to be performed: ')
list1 = []
num = int(input('Enter the number of elements in the list'))
for i in range(0,num):
    ele = int(input('Enter the element no'))
    list1.append(ele)

if(select ==  '1'):
    print(comp_num(list1))

if(select == '2'):
    evn_odd_lst(list1)

if(select == '3'):
    list2 = []
    num1 = int(input('Enter the number of elements in the second list'))
    for i in range(0, num1):
        ele1 = int(input('Enter the element no'))
        list2.append(ele1)
    print(merg_srt(list1, list2))

if(select == '4'):
    srt_scnd_element(list1)

if(select == '5'):
    list2 = []
    num1 = int(input('Enter the number of elements in the second list'))
    for i in range(0, num1):
        ele1 = int(input('Enter the element no'))
        list2.append(ele1)
    un_int(list1,list2)

if(select == '6'):
    perf_sq(list1)