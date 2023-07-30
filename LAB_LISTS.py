


main_list=[2,3,4,5,15,1,43,20]

def sumList (num:list):
  
  Sum = sum (num)

  return Sum
        
print(sumList(main_list))

#####################

def largestNum(num:list):
  

    return max(num)
    

print(largestNum(main_list))


####################


def oddNum():
   oddList=[]
   for i in range(1200,2000,125):
      if i %2 !=0:
       oddList.append(i)


   return oddList

print(oddNum())


##################


def slicingList(num:list):
   
 newList=[]
 for i in num:
   if i %2 !=0:
     newList.append(i)
     
  
 return newList[:5]

     

print(slicingList(main_list)) 









