list_of_numbers = [2, 3, 4, 5, 15, 1, 43, 20]
def number(list_of_numbers):
    num=0
    for sum in list_of_numbers:
        num += sum
    return num

print(number(list_of_numbers))
def larg_number(list_of_numbers):
    largest = max(list_of_numbers)
    return largest

print(larg_number(list_of_numbers))
new_list =[]
for value in range(1200 , 2000, 125):
    number = value
    new_list.append(number)
print(new_list)
list_slicing = list_of_numbers[:6]
print(list_slicing)