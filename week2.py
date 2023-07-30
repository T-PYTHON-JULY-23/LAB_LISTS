list =[2, 3, 4, 5, 15, 1, 43, 20]

#q1 and q2
def list_sum (list):
    sum:int=0
    for i in range(0, len(list)):
        sum=sum+list[i]
    print("The sum of all elements in list:", sum)

def largest_number(list):
    larger= list[0]
    for i in list:
        if i>larger:
            larger=i
    print("The largest number in this list:",larger)

#q3 and q4
def oddnumbers():
 oddNmbrs=[]
 for i in range(1200,2000,125):
    if i%2!=0:
        odd=[i]
        oddNmbrs.extend(odd)
 print("The odd number from 1200 to 2000 with steps of 125:",oddNmbrs)
 slicinglist=oddNmbrs[:4]
 print("Slicing list: ",slicinglist)



list_sum(list)
largest_number(list)
oddnumbers()