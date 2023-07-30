"""# LAB_LISTS



## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
### Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.

"""

def sum_of_list(arr:list) -> list:
    return sum(arr)

def max_elemnt(arr:list) -> int:
    return max(arr)

given_list=[2, 3, 4, 5, 15, 1, 43, 20]
print(sum_of_list(given_list))
print(max_elemnt(given_list))

oddlist=[number for number in range (1200,2000,125) if number%2!=0 ]
print(oddlist)
new_odd_list=oddlist[:5] #### its only 3 items 