#Lab Lists
#Q1

myList = [2, 3, 4, 5, 15, 1, 43, 20]

def sumList(myList):
    Sum = sum(myList)
    print("the sum of the list is: ", Sum) 

sumList(myList)

#Q4
new_list= myList[0:5]
print(myList[:5])



#Q2
myList = [2, 3, 4, 5, 15, 1, 43, 20]

def largestNum(myList):

    print("The largest element is: ", max(myList))

largestNum(myList)




#q3
odd_list=[num for num in range(1200, 2000, 125) if num % 2 != 0]
print(odd_list)
  