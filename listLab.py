

list =[2, 3, 4, 5, 15, 1, 43, 20]

#Q1 
def list_sum (list):
    sum=0
    for i in range(0, len(list)):
        sum=sum+list[i]
    print("The sum of itmes is:", sum)
    return sum

list_sum(list)

#Q2
def largest_number(list):
    larger= list[0]
    for i in list:
        if i>larger:
            larger=i
    return f"The largest number in the list is :{larger}"

print(largest_number(list))

#Q3 on normal way
oddNumbers=[]
for i in range(1200,2000,125):
    if i%2!=0:
        odd=[i]
        oddNumbers.extend(odd)
print(f"The odd number from 1200 to 2000 with steps of 125 is:{oddNumbers}")

#soultion of qustion 3 by using list comprehension-->
add_odd_number=[number for number in range(1200,2000,125)if number%2!=0]
print(add_odd_number)

#Q4 
slicinglist=list[:4]
print(f"Slicing list: {slicinglist} ")