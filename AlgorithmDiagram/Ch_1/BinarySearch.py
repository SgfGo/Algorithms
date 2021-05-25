# @Time    : 2021/5/21 下午11:08
# @Author  : SgfGo
# @FileName: BinarySearch.py
# @Software: PyCharm
# 二分查找

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return  None

myList = [1, 3, 5, 9, 11]
print(binary_search(myList, 9))