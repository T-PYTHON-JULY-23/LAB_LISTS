
Qlist =  [2, 3, 4, 5, 15, 1, 43, 20]

#Q1
def sumOfAll(list):
    sumlist=0
    for val in list:
       sumlist+= val

    return sumlist

#Q2
def largest_number (list):
    larg_num = 0
    for val in list:
        if larg_num > val:
            continue
        elif larg_num < val:
            larg_num = val

    return larg_num    

#Q3
def odd_number_list():

    oddList= [val for val in range(1200,2001,125) if val %2 != 0  ] 

    return oddList



# Q1 test 
the_sum = sumOfAll(Qlist)
print(the_sum)

# Q2 test 
print(largest_number(Qlist))

# Q3 test
odd_n_list= odd_number_list()
print(odd_n_list)

#Q4
list_slic= Qlist[:5]
print(list_slic)
