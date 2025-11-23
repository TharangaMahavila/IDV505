def pascal_line(n):
    return ' '.join(str(x) for x in pascal_rec([], n))


def pascal_rec(lst, n):
    if len(lst) > n:
        return lst
    new_list = [1]
    if len(lst) > 1:
        new_list.extend(get_two_concecutive_sum(lst, [], 0))
    if n > 0:
        new_list.append(1)
    return pascal_rec(new_list, n)


def get_two_concecutive_sum(lst, new_list, index):
    if len(lst) > index+1:
        new_list.append(lst[index]+lst[index+1])
    else:
        return new_list
    return get_two_concecutive_sum(lst, new_list, index+1)


print(pascal_line(7))
