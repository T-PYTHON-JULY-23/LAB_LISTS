#1
my_list =[2, 3, 4, 5, 15, 1, 43, 20]
print(my_list)
def returns_lis(list):
 if len(my_list)>0:
     return sum(my_list)

print(returns_lis(my_list))

#2
def largest_number(lists):
    largest = lists[0]

    for num in lists:
        if num > largest:
            largest = num

    return largest
print(largest_number(my_list))

#3
odd_num = [num for num in range(1200, 2001, 125) if num % 2 != 0]
print(odd_num)

#4
new_list = my_list[:5]
print(new_list)


