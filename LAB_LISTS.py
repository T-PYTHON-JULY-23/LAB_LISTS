list = [2, 3, 4, 5, 15, 1, 43, 20]



def list_largest_num (list):
    list.sort()
    print("largest number in list is:",list[-1])

def list_sum(list):
    sum = 0
    for i in list:
     sum += i
    print(f"The sum of all the tems in the list: {sum}")



odd_list=[]

for i in range(1200,2000,125):
   odd_list.append(i)
print(odd_list)


list_largest_num (list)
list_sum (list)

new_list = list[:5]
print(new_list)