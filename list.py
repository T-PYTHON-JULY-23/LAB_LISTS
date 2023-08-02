'''
Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]

Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.

Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].

Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.


'''
#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.

def sum (number):
    sumResult=0
    for x in number:
        sumResult+=x
       
        
    return sumResult

list_num=[2, 3, 4, 5, 15, 1, 43, 20]
print(f"sum of all the items in that list: {sum(list_num)}")


#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def largesst (number):
    max=number[0]
    for x in number:
        if x> max:
            max=x
        
    return max


print(f"the largest number from a list of numbers: {largesst(list_num)}")
        
 #Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
      
def odd_num (start,end,step):
    list_number=[]
    for num in range(start, end + 1,step):
    # checking condition
     if num % 2 != 0:
        list_number.append(num)
        
        

        
    return list_number


print(f"odd numbers list from the elements of a range from 1200 to 2000 with steps of 125:  {odd_num(1200,2000,125)}")

#Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.

new_list_odd_num=list_num[:5]
print(f"{list_num}from the start to the 5th element in the list: {new_list_odd_num}")

    
    