# @Time    : 2021/6/7 下午11:25
# @Author  : SgfGo
# @FileName: QuickSort.py
# @Software: PyCharm
# 分而治之策略 （Divide and conquer,D&C）快速排序

def quickSort(array):
    if len(array) < 2:
        return  array;
    else:
        pivot = array[0] # 选择基准值
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return  quickSort(less) + [pivot] + quickSort(greater)

print (quickSort([1,5,324,243,5,2,4,2]))