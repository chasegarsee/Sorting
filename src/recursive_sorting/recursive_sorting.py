# TO-DO: complete the helper function below to merge 2 sorted arrays


def devider(array):  # devides the given array into 3 sections LEFT MIDDLE and RIGHT
    left = []
    pivot = array[0]
    right = []

    for j in array[1:]:  # iterating thru starting at the beginning
        if j <= pivot:  # if the iteration is less or equal to the before it
            left.append(j)  # put it at the beginning
        else:  # otherwise
            right.append(j)  # put it at the end

    return left, pivot, right


def quicksort(array):
    if array == []:  # if the array is empty
        return array  # return the array

    # Assigns left, pivot, right the to devider function
    left, pivot, right = devider(array)
    print(left + [pivot] + right)  # prints it

    # makes it so that the quick sort actually sortys them in order.
    return quicksort(left) + [pivot] + quicksort(right)


def merge(arrA, arrB):
    # assigns elements to equal the length of arrA + the length of arrB
    elements = len(arrA) + len(arrB)
    # assigns merged_arr to the first position of the array multiplied by the newly assigned elements
    merged_arr = [0] * elements
    # TO-DO

# starting values
    a = 0
    b = 0
    middle = 0

    # while a is less than the length of arrA and b is less than the length of arrB
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:  # if arrA at the 1st position is less than arrB at the 0 position
            merged_arr[middle] = arrA[a]  # add that number merged_arr
            a += 1  # increment a by 1
        else:  # otherwise
            # if arrA is greater than arrB at the 0 position add the number in arrB to merged_arr
            merged_arr[middle] = arrB[b]
            b += 1  # increment b by 1
        middle += 1  # increment middle by 1
        print(merged_arr)  # print that merged_arr bro

    while a < len(arrA):  # while a is less than the length of arrA
        merged_arr[middle] = arrA[a]
        a += 1
        middle += 1

    while b < len(arrB):  # while b is less than the length of arrB
        merged_arr[middle] = arrB[b]
        b += 1
        middle += 1

    print(merged_arr)

    return merged_arr


merge([1, 3], [2, 4])

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    if len(arr) > 1:  # if the length of the array is greater than 1
        # the middle is the length of the array divided by 2
        middle = len(arr) // 2
        # arrA is assigned to merge_sort sorting the array from the left
        arrA = merge_sort(arr[:middle])
        # arrB is assigned to merge_sort sorting the array from the right
        arrB = merge_sort(arr[middle:])
        arr = merge(arrA, arrB)  # arr is merging arrA and arrB into one

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
