# 4. Определить, какое число в массиве встречается чаще всего.

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_freq = List.count(i)
        if (curr_freq > counter):
            counter = curr_freq
            num = i

    return num


List = [2, 1, 2, 2, 1, 3, 3, 4, 3, 4, 3]
print(most_frequent(List))