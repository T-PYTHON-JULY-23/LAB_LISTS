# Q1: Write a function that takes a list as a parameter,
# and then returns  the sum  of all the items in that list.
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
def sum_mylist (my_list):
    return sum(my_list) 

# Q2: Write a function that takes a list as a parameter,
#  and then returns the largest number from a list of numbers.
def max_mylist(my_list):
    return max(my_list)

# Q3: Create an odd numbers list from the elements of a range 
# from 1200 to 2000 with steps of 125, using [ List Comprehension ].

odd_numbers = [num for num in range (1200, 2000, 125) if num %2 != 0]

# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting 
# from the start to the 5th element in the list.

new_list = my_list [:5]

print(sum_mylist(my_list))
print(max_mylist(my_list))
print(odd_numbers)
print(new_list)



