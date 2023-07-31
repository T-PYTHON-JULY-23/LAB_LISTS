#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.

list1 = [2, 3, 4, 5, 15, 1, 43, 20]

def sum_oflist (list1):
    total = sum(list1)
    return total
print(f" sum of the element: {sum_oflist(list1)}")

 
#use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
nwe_list = list1[:6]
print(nwe_list)



#Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def max_list (list1):
    largest = max(list1)
    return largest 
print(f"the largest number: {max_list(list1)}")



# Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_number_list = [number for number in range(1200,2000,125) if number%2!=0]
print(odd_number_list)







