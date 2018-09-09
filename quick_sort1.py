def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low <high and array[high] >= key:
            high -= 1
        array[low] = array[high]

        while low < high and array[low] <= key:
            low += 1

        array[high] = array[low]

    array[low] = key

    return low

def quick_sorted(array,low,high):
    if low < high:
        pivoloc = sub_sort(array,low,high)

        quick_sorted(array,low,pivoloc-1)

        quick_sorted(array,pivoloc+1,high)

if __name__ == '__main__':
    array = [49,38,65,97,76,13,27,38]

    print(array)

    quick_sorted(array,0,len(array)-1)

    print(array)