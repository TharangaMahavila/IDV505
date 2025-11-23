import random


def threesum_brute(lst, sum=0):
    three_sum_set = set()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i]+lst[j]+lst[k] == sum:
                    three_sum_set.add(tuple(sorted([lst[i], lst[j], lst[k]])))
    return list(three_sum_set)


def threesum_pointers(lst, sum=0):
    lst = sorted(lst)
    n = len(lst)
    three_sum_set = set()

    fp1 = 0
    while fp1 < n-2:
        fp2, bp = fp1 + 1, n - 1
        while fp2 < bp:
            total = lst[fp1] + lst[fp2] + lst[bp]
            if total == sum:
                three_sum_set.add((lst[fp1], lst[fp2], lst[bp]))
                fp1 += 1
                bp -= 1
            elif total < sum:
                fp2 += 1
            else:
                bp -= 1
        fp1 += 1
    return list(three_sum_set)


def threesum_caching(lst, sum=0):
    lst = sorted(lst)
    three_sum_set = set()
    n = len(lst)

    for i in range(n):
        v1 = lst[i]
        cache = set()  # Cache for 2-sum on the remaining elements
        for j in range(i + 1, n):
            v2 = lst[j]
            v3 = sum - v1 - v2
            if v3 in cache:
                # Sort to avoid duplicates
                three_sum_set.add((v1, v3, v2))
            cache.add(v2)

    return list(three_sum_set)


def get_nsum_list(size, width):
    lst = []
    for i in range(size):
        lst.append(random.randint(-1*width*size, width*size))
    return lst
