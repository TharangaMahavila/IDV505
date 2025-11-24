def selection_sort(array):
    result = array[:]
    n = len(result)
    for i in range(n):
        min_index = i  # Assume this position has the smallest element
        # Find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        # Swap only if the minimum is not already at position i
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]

    return result


def bubble_sort(array):
    result = array[:]
    n = len(result)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                # Swap
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def insertion_sort(array):
    result = array[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result
