def list_sum(numbers_list: list) -> int:
    s = 0
    for num in numbers_list:
        if type(num) is list:
            s += list_sum(num)
        else:
            s += num
    return s


num_list = [1, 2, [3, 4], [5, 6, [7, 8, 9, 10]]]

print(list_sum(num_list))
