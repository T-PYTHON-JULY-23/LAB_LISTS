# a question number 1
def sum_list(items):
    """sum of the list"""
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(sum_list([2, 3, 4, 5, 15, 1, 43, 20]))


# a question number 2
def max_list(ele):
    """the max of the list"""
    max_num = max(ele)

    return max_num


print(max_list([2, 3, 4, 5, 15, 1, 43, 20]))


# a question number 3
def odd_numbers(y, n):
    """finding odd number from 1200 to 2000"""
    return [x for x in range(y, n + 1, 125) if x % 2 != 0]


print(odd_numbers(1200, 2000))

# a question number 4
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
"""use list slicing to get a new list from the previous list"""
new_list = my_list[:5]
print(new_list)
