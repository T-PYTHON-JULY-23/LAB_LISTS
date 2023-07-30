numList = [2, 3, 4, 5, 15, 1, 43, 20]
#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
print('-------Q1-------')
def numberSum(numList:list):
    sumNum =0
    for num in numList:
        sumNum += num
    return sumNum
print(numberSum(numList))
print('-------Q2-------')
# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largeNumber(numList:list):
    max = numList[0]
    for num in numList:
        if num > max:
            max = num
    return max
print(largeNumber(numList))
print('-------Q3-------')
# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125
def oddNumber(list):
    newList =[]
    for num in list:
        if num %2 ==1:
            newList.append(num)
    return newList
print(oddNumber(range(1200,2000,125)))
print('-------Q4-------')
# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
sliceList = numList[:5]
print(sliceList)
