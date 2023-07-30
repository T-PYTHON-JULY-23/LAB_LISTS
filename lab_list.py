## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
number_list = [2, 3, 4, 5, 15, 1, 43, 20]
def number(number_list):
    num=0
    for sum in number_list:
        num += sum
    return num

print(number(number_list))

### Q2: Write a function that takes a list as a parameter, and then rturns the largest number from a list of numbers.
def larg_number(number_list):
    largest = max(number_list)
    return largest

print(larg_number(number_list))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
new_list =[]
for value in range(1200 , 2000, 125):
    number = value
    new_list.append(number)
print(new_list)

### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
list_slicing = number_list[:5]
print(list_slicing)