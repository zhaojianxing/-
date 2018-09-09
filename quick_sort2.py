import random

"""
def quick_sorted2(array):
    if len(array) < 2:
        return array
    key = random.choice(array)
    left_list = []
    right_list = []
    for i in array:
        if i < key:
            left_list.append(i)
        else:
            right_list.append(i)
    return quick_sorted2(left_list)+quick_sorted2(right_list)
"""
def qsort(arr):
    if not len(arr):
        return []
    else:
    # 在这里以第一个元素为基准线
        pivot = arr[0]
        left = qsort([x for x in arr[1:] if x < pivot])
        right = qsort([x for x in arr[1:] if x >= pivot])
    return left+[pivot]+right
if __name__ == '__main__':
    arry = [49,38,65,97,76,13,27,38]
    a = qsort(arry)
    print(a)
