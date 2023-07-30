def fun_list_num(list_num):
    items_sum = (sum(list_num))
    print(f"The sum of all item in list is : {items_sum}  &  {list_num}")
    print()
    max_item = max(list_num)
    print(f"The max number in the list is : {max_item}")

    print(f"The slice from 1 to 5 index : is {list_num[:5]}")

fun_list_num([2,3,4,5,15,1,43,20])



def fun_odd_num(num1,num2):
    odd_list = [num for num in range(num1, num2+1, 125) if num%2!=0] 
    return odd_list


print(fun_odd_num(1200,2000))
