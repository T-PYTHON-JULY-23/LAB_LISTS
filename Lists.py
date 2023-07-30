# LAB_LISTS

## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

main_list=[2, 3, 4, 5, 15, 1, 43, 20]
def first_list(lst1:list):
    total=0
    for item in lst1:
        total+=item
    return total     
print(first_list(main_list))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

nums = [10, 20, 30, 40, 50, 60] 
def max_num(nums):
    max_num=0 
    for num in nums: 
        if num > max_num: 
            max_num=num
    return max_num            
print(max_num(nums))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].

odd_numbers= []
for numbers  in range (1200,2000 ,125):
        if numbers%2 != 0:
            print(numbers)
            
 ### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
                       
new_list= main_list[  : 5]
print(new_list[  : 5])

     





