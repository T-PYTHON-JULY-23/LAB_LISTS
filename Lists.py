# LAB_LISTS

## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

main_list=[2, 3, 4, 5, 15, 1, 43, 20]
def sum_list(main_list:list):
    total=0
    for item in main_list:
        total+=item
    return total     
print("sum List = " , sum_list(main_list))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def max_num(item):
    max_num=0 
    for item in main_list: 
        if item > max_num: 
            max_num=item
    return max_num            
print("max Number : " , max_num(main_list))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
numbers= []
for check_numbers  in range (1200,2000 ,125):
        if check_numbers%2 != 0:
            print("odd_number:" , check_numbers)

 ### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.

new_list= main_list[  : 5]
print("New List : " , new_list)