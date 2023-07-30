# Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
def my_list(Emplyees:int):
    print(sum(Emplyees))
ourlist = [2, 3, 4, 5, 15, 1, 43, 20]

my_list(ourlist)
# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers
print("-" * 15)

def num_list(Numbers:int):
    for n in Numbers:
        if n == max(Numbers):
            print(n)
Num = [2, 3, 4, 5, 15, 1, 43, 20]
num_list(Num)
# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
print("-" * 15)
lst = [n for n in (range(1200,2000,125)) if (n % 2) != 0]
print(lst)
# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
new_list = lst
print(new_list[:5])