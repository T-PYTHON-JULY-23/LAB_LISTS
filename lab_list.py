###Q1:
#creat a new list
my_list = [2,3,4,5,15,1,43,20] 

#defined a function that returns  the sum  of all the items in that list
def total_numbers (my_list):
    sum = 0
    for numbers in my_list :
        sum+= numbers
    return sum 

print (f"the total numbers is : {total_numbers(my_list)}")

#-----------------------------------------------------------------------------------------------

###Q2 :
#creat a function that print the largest number in a list ...
def largest_number(my_list):
    print (f"the largest number in the list is : {max(my_list)}")  # we use max fun to find the largest number 

largest_number(my_list)

#-------------------------------------------------------------------------------------------------

###Q3

odd_number_list = [numbers  for numbers in range(1200,2000,125) if numbers %2 != 0 ]
print(odd_number_list) 

#-------------------------------------------------------------------------------------------------

###Q4 : 
new_list = my_list[0:5]  #creat a new list by using list slicing
print(new_list)