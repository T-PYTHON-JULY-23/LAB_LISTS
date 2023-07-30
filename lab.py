def sum(my_list:list) -> int:
    '''this function will return the summation of the numbers in a list'''
    sum = 0
    for num in my_list:
        sum += num
    return sum

def max(my_list:list) -> int:
    '''this function will return the largest number in the list'''
    max = my_list[0]
    for num in my_list:
        if num > max:
            max = num
    return max


example_list = [2, 3, 4, 5, 15, 1, 43, 20]


print(sum(example_list))
print(max(example_list))

num_list = [num for num in range(1200, 2000, 125) if num % 2 != 0]
print(num_list)

sliced_list = example_list[:5]
print(sliced_list)