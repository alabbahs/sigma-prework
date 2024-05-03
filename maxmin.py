def min_max(list):
    smallest = list[0]
    largest = list[0]
    for i in list:
        if smallest > i:
            smallest = i
        if largest < i:
            largest = i

    return [smallest, largest]


print(min_max([2, 4, 1, 0, 2, -1]))
print(min_max([20, 50, 12, 6, 14, 8]))
print(min_max([100, -100]))
