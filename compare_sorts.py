import random   #Import module for generating random numbers
import time     #Import module for getting the current time

maxvalue = 1000

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # to change direction of sort, change direction of comparison
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def insertion_sort(array):
    for slot in range(1, len(array)):
        value = array[slot]
        test_slot = slot - 1
        while test_slot > -1 and array[test_slot] > value:
            array[test_slot + 1] = array[test_slot]
            test_slot = test_slot - 1
        array[test_slot + 1] = value
    return array

def bubble_sort(array):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        index -= 1
    return array

def main():
    numba = random.sample(range(1, maxvalue), maxvalue - 1)
    start = time.time()
    merge_sort(numba)
    end = time.time()
    print(f'Merge sort time: ', end - start)

    numba = random.sample(range(1, maxvalue), maxvalue - 1)
    start = time.time()
    insertion_sort(numba)
    end = time.time()
    print(f'Insertion sort time: ', end - start)

    numba = random.sample(range(1, maxvalue), maxvalue - 1)
    start = time.time()
    bubble_sort(numba)
    end = time.time()
    print(f'Bubble sort time: ', end - start)


    maxvalues = [100, 1000, 10000, 100000]

    for bigmax in maxvalues:
        print(f'\nMax value of: {bigmax}')
        numba = random.sample(range(1, bigmax), bigmax - 1)
        start = time.time()
        merge_sort(numba)
        end = time.time()
        print(f'Merge sort time: ', end - start)

        numba = random.sample(range(1, bigmax), bigmax - 1)
        start = time.time()
        insertion_sort(numba)
        end = time.time()
        print(f'Insertion sort time: ', end - start)

        numba = random.sample(range(1, bigmax), bigmax - 1)
        start = time.time()
        bubble_sort(numba)
        end = time.time()
        print(f'Bubble sort time: ', end - start)
    #ADD CODE to compare the three list-sorting functions
    #  See Canvas assignment for details.

main()
