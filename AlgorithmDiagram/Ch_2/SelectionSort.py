# @Time    : 2021/6/6 下午10:18
# @Author  : SgfGo
# @FileName: SelectionSort.py
# @Software: PyCharm
# 选择排序

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return  smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr;

arr = [3,5,6,7,8,2,4]
print (selectionSort(arr))
