listcampur =  [20, 10, [50, 70, [60, 40]], 30, 90, [80], 100]
list1 =  listcampur[0:2] 
list1a = listcampur[3:5]
list1b = listcampur[6:7]
list2 = listcampur[2][0:2]
list3 = listcampur[2][2][0:2]
list4 = listcampur[5]

listsemuanya = list1+list1a+list1b+list2+list3+list4
# print(listsemuanya)

import os
os.system('cls')

def mergesort(arr):#bagi list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #variable mecah list
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = []#list kosong untuk nampung nilai

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

listsemuanya = list1+list1a+list1b+list2+list3+list4
hasil = mergesort(listsemuanya)

print(listcampur)
print (hasil)